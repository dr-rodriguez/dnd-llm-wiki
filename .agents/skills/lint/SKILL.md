---
name: lint
description: Health-check the D&D wiki and fix what it finds — broken or ambiguous links, orphan pages, missing index entries, wrong frontmatter types or properties, un-ingested raw notes, contradictions between pages and claims that drift from the raw notes. Use when the user says "lint", "check the wiki", "health check", "find broken links", or asks whether the wiki is consistent.
---

# Lint

The rules being checked live in `AGENTS.md` (note types, properties, linking, provenance). Lint has a mechanical pass (scripted) and a judgment pass (reading).

## 1. Mechanical pass
Run:

```bash
python3 .agents/skills/lint/lint_wiki.py
```

It checks, across all of `wiki/`:
- frontmatter: valid `type`, `type` first, type matches folder; session `year`/`date`/H1 match the file name; character properties present and `character-type` matches the PC/NPC folder; tags are PascalCase
- links: unresolved, ambiguous (same name in `raw/` and `wiki/`), `wiki/`-prefixed, mangled `]]]`; non-session pages citing dated `raw/` files instead of the session note
- coverage: orphan pages, pages missing from `wiki/index.md`, raw session files with no wiki note, wiki session notes with no raw file
- the four bases in `wiki/Tables/` exist and filter on valid types

`ERROR` lines must be fixed. `WARN` lines should be fixed unless there's a reason not to (say why in the log). `wiki/log.md` is skipped for link checks, since it quotes old and example links.

**Known `INFO`:** about 260 `#Section` links point at bullet or table entries in hub pages (Lore topics, `Locations.md`), not headings, so Obsidian opens the page top. This is accepted for now. Don't mass-convert entries to headings without asking. `--anchors` lists them.

## 2. Judgment pass
The script can't judge content. Pick a scope rather than reading the whole wiki: by default, the sessions ingested since the last lint row in `wiki/log.md`, plus the character, quest, location and lore pages they link to. Do a full sweep only when the user asks.
- **Accuracy:** spot-check claims in those pages against the matching `raw/` files.
- **Contradictions:** the same fact stated differently on two pages (species, who did what, dates, status like alive/dead).
- **Stale claims:** roster rows, quest status or location descriptions that later sessions have overtaken.
- **Structure drift:** events bullets out of date order, stray links in the middle of lists, unsorted `## Sources`.
- **Data gaps:** entities mentioned in several sessions with no page or roster row.

## 3. Fix and report
- Fix clear-cut issues directly. If a fix would touch many pages (more than about 10) or changes meaning, list the planned changes and ask first.
- Re-run the script until it reports 0 errors.
- Append one row to `wiki/log.md` (date, `(Lint)`, what was fixed and what was flagged but left). Use the Edit tool, not shell redirection, so the file stays UTF-8.
- Tell the user what you fixed, what you flagged, and any raw notes worth ingesting.
