#!/usr/bin/env python3
"""Mechanical health checks for the D&D LLM Wiki.

Usage: python3 .agents/skills/lint/lint_wiki.py [--anchors]

Checks frontmatter types and properties, link resolution, orphans,
index coverage, raw/wiki session coverage, tags and the Obsidian bases.
Judgment checks (contradictions, stale claims, data gaps) stay manual.
Exits 1 if any ERROR is found.
"""
import re
import sys
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
WIKI = ROOT / "wiki"
RAW = ROOT / "raw"

VALID_TYPES = {"character", "location", "lore", "quest", "session-note", "reference"}
CHARACTER_PROPS = ["name", "species", "class", "character-type", "player", "link"]
BASES = ["Characters.base", "Quests.base", "Lore.base", "Sessions.base"]
EXEMPT = {"index.md", "log.md"}  # no frontmatter required

LINK_RE = re.compile(r"(!?)\[\[([^\[\]]+?)\]\]")
TAG_RE = re.compile(r"^[A-Z][A-Za-z0-9]*$")
DATE_RE = re.compile(r"^\d{4}-\d{2}-\d{2}$")

errors, warnings, infos = [], [], []


def rel(p):
    return p.relative_to(ROOT).as_posix()


def parse_frontmatter(text):
    """Minimal YAML reader: scalar keys and simple '- item' lists."""
    if not text.startswith("---"):
        return None
    end = text.find("\n---", 3)
    if end == -1:
        return None
    fm, key = {}, None
    for line in text[3:end].splitlines():
        if not line.strip():
            continue
        m = re.match(r"^([A-Za-z0-9_-]+):\s*(.*)$", line)
        if m:
            key, val = m.group(1), m.group(2).strip()
            if val.startswith("[") and val.endswith("]"):  # inline list
                fm[key] = [v.strip().strip('"').strip("'") for v in val[1:-1].split(",") if v.strip()]
            else:
                fm[key] = val.strip('"').strip("'")
        elif key and line.strip().startswith("- "):
            if not isinstance(fm.get(key), list):
                fm[key] = []
            fm[key].append(line.strip()[2:].strip().strip('"'))
    return fm


def expected_type(path):
    parts = path.relative_to(WIKI).parts
    top = parts[0]
    if top == "Characters":
        return "character"
    if top == "Locations":
        return "location"
    if top == "Lore":
        return "lore"
    if top == "Quests":
        return "quest"
    if top == "Sessions":
        return "session-note" if len(parts) == 3 else "reference"
    return None


def slug(heading):
    return heading.strip().lower()


# ---- collect files -------------------------------------------------------
vault_files = [p for p in ROOT.rglob("*")
               if p.is_file() and not any(s.startswith(".") for s in p.relative_to(ROOT).parts)]
wiki_notes = sorted(p for p in WIKI.rglob("*.md") if not any(s.startswith(".") for s in p.relative_to(WIKI).parts))

by_name = defaultdict(list)  # "basename" and "basename.ext" -> files
for f in vault_files:
    by_name[f.name.lower()].append(f)
    if f.suffix == ".md":
        by_name[f.stem.lower()].append(f)


def resolve(target):
    """Resolve an Obsidian link target the way Obsidian does (shortest path)."""
    t = target.strip().replace("\\", "/")
    name = t.rsplit("/", 1)[-1].lower()
    cands = by_name.get(name, [])
    if "/" in t:
        tl = t.lower()
        cands = [c for c in cands
                 if rel(c).lower().endswith(tl) or rel(c).lower().endswith(tl + ".md")]
        # wiki/ is the site root, so "Sessions/..." should resolve inside wiki/
        wiki_hits = [c for c in cands if rel(c).lower() in ("wiki/" + tl, "wiki/" + tl + ".md")]
        root_hits = [c for c in cands if rel(c).lower() in (tl, tl + ".md")]
        cands = wiki_hits or root_hits or cands
    return list(dict.fromkeys(cands))


headings_cache = {}


def headings(path):
    if path not in headings_cache:
        text = path.read_text(encoding="utf-8", errors="replace")
        headings_cache[path] = {slug(m.group(1)) for m in re.finditer(r"^#{1,6}\s+(.+?)\s*$", text, re.M)}
    return headings_cache[path]


# ---- per-note checks -----------------------------------------------------
incoming = defaultdict(set)
index_links = set()
bad_anchors = []

for note in wiki_notes:
    r = rel(note)
    text = note.read_text(encoding="utf-8", errors="replace")

    if "�" in text or re.search(r"â€|Ã¢", text):
        warnings.append(f"{r}: encoding mojibake")

    if note.name not in EXEMPT:
        fm = parse_frontmatter(text)
        if fm is None:
            errors.append(f"{r}: missing frontmatter")
            fm = {}
        t = fm.get("type")
        exp = expected_type(note)
        if not t:
            errors.append(f"{r}: missing `type`")
        elif t not in VALID_TYPES:
            errors.append(f"{r}: invalid type `{t}`")
        elif exp and t != exp:
            errors.append(f"{r}: type `{t}` but folder expects `{exp}`")
        elif list(fm)[0] != "type":
            warnings.append(f"{r}: `type` is not the first property")

        if t == "session-note":
            parts = note.relative_to(WIKI).parts
            if fm.get("date") != note.stem or not DATE_RE.match(note.stem):
                errors.append(f"{r}: date `{fm.get('date')}` does not match file name")
            if fm.get("year") != note.stem[:4] or parts[1] != note.stem[:4]:
                errors.append(f"{r}: year `{fm.get('year')}` / folder `{parts[1]}` do not match file name")
            if not re.search(rf"^# Session: {re.escape(note.stem)}\s*$", text, re.M):
                warnings.append(f"{r}: H1 is not `# Session: {note.stem}`")
            if not (RAW / note.stem[:4] / note.name).exists():
                errors.append(f"{r}: no matching raw/{note.stem[:4]}/{note.name}")

        if t == "character" and note.name != "Characters.md":
            missing = [k for k in CHARACTER_PROPS if k not in fm]
            if missing:
                errors.append(f"{r}: missing properties {missing}")
            ct = fm.get("character-type")
            folder = note.relative_to(WIKI).parts[1] if len(note.relative_to(WIKI).parts) > 2 else None
            if folder in ("PC", "NPC") and ct != folder:
                errors.append(f"{r}: character-type `{ct}` but in {folder}/ folder")
            if ct == "NPC" and fm.get("player"):
                warnings.append(f"{r}: NPC has a `player`")

        for tag in fm.get("tags") or []:
            if not TAG_RE.match(tag):
                warnings.append(f"{r}: tag `{tag}` is not PascalCase")

    if note.name == "log.md":  # history entries quote old and example links
        continue

    if "]]]" in text:
        errors.append(f"{r}: mangled link `]]]`")

    for m in LINK_RE.finditer(text):
        body = m.group(2).replace("\\|", "|")
        target = body.split("|", 1)[0]
        target, _, anchor = target.partition("#")
        if not target:  # same-page anchor
            continue
        if target.lower().startswith("wiki/"):
            errors.append(f"{r}: link starts with `wiki/`: [[{body}]]")
            continue
        hits = resolve(target)
        if not hits:
            errors.append(f"{r}: unresolved link [[{body}]]")
            continue
        if len(hits) > 1:
            errors.append(f"{r}: ambiguous link [[{body}]] -> {[rel(h) for h in hits]}")
        dest = hits[0]
        if dest != note:
            incoming[dest].add(note)
        if note.name == "index.md" and note.parent == WIKI:
            index_links.add(dest)
        if anchor and dest.suffix == ".md" and slug(anchor.split("#")[0]) not in headings(dest):
            bad_anchors.append(f"{r}: [[{body}]] -> no heading `{anchor}` in {rel(dest)}")
        # raw/ links: session notes and reference notes only, except CSVs / bios
        if rel(dest).startswith("raw/"):
            t = (parse_frontmatter(text) or {}).get("type")
            dated = re.match(r"raw/\d{4}/", rel(dest))
            if t not in ("session-note", "reference") and dated:
                warnings.append(f"{r}: links raw session [[{body}]]; cite the wiki session note")

# ---- vault-wide checks ---------------------------------------------------
for note in wiki_notes:
    r = rel(note)
    if note.name in EXEMPT:
        continue
    if not incoming[note]:
        errors.append(f"{r}: orphan (no incoming links)")
    if note not in index_links:
        warnings.append(f"{r}: not listed in wiki/index.md")

for raw_note in sorted(RAW.glob("[0-9][0-9][0-9][0-9]/*.md")):
    wiki_note = WIKI / "Sessions" / raw_note.parent.name / raw_note.name
    if not wiki_note.exists():
        errors.append(f"{rel(raw_note)}: not ingested (no {rel(wiki_note)})")

for base in BASES:
    p = WIKI / "Tables" / base
    if not p.exists():
        errors.append(f"wiki/Tables/{base}: missing")
        continue
    for t in re.findall(r'type\s*==\s*"([^"]+)"', p.read_text(encoding="utf-8")):
        if t not in VALID_TYPES:
            errors.append(f"wiki/Tables/{base}: filters on unknown type `{t}`")

if bad_anchors:
    infos.append(f"{len(bad_anchors)} links point at a #section that is not a heading "
                 "(list or table entries; Obsidian opens the page top). Run with --anchors to list.")

# ---- report --------------------------------------------------------------
print(f"Checked {len(wiki_notes)} wiki notes, {len(list(RAW.glob('[0-9]*/*.md')))} raw session files.\n")
for label, items in (("ERROR", errors), ("WARN", warnings), ("INFO", infos)):
    for item in items:
        print(f"{label}  {item}")
if "--anchors" in sys.argv:
    print()
    for item in bad_anchors:
        print(f"ANCHOR  {item}")
print(f"\n{len(errors)} errors, {len(warnings)} warnings, {len(infos)} info.")
sys.exit(1 if errors else 0)
