---
name: world-anvil
description: Convert a wiki page or a single entry (session note, character, lore entry, quest, location, roster table) into World Anvil BBCode, printed in a code block ready to paste into a World Anvil article. Output only, never edits files. Use when the user says "World Anvil", "BBCode", "WA", or "convert/export <page> for World Anvil", e.g. "world anvil 2026-10-01" or "BBCode for Lore The Mountain".
---

# World Anvil

Output only; never edit wiki or raw files.

## Workflow
1. **Resolve the source** from the user's argument:
   - A date (`2026-10-01`) → `wiki/Sessions/<year>/<date>.md`. No argument → the session marked *(Latest Session)* in `wiki/index.md`.
   - A character name (`Maxim`, `Aolis`) → `wiki/Characters/PC/<Name>.md` or `wiki/Characters/NPC/<Name>.md`. Use Glob to match partial names.
   - A page name (`Lore`, `Quests`, `Locations`, `Characters`, `B-Team`, ...) → find the page with Glob (`wiki/**/<Page>.md`). Hubs live in their own folders: `wiki/Characters/Characters.md`, `wiki/Characters/B-Team.md`, `wiki/Quests/Quests.md`, `wiki/Locations/Locations.md`, `wiki/Lore/Lore.md`. Lore entries sit in topic notes under `wiki/Lore/` (Ancient History, Major Projects, Deities and Religions, Locations of Interest, Technology, Factions and Organizations, Bestiary).
   - Ignore `wiki/Tables/*.base` files; they are Obsidian views, not content.
   - A page plus an entry or section (`Lore The Mountain`, `Lore Overseer`, `Quests Scout The Mountain`, `Locations Tesselia`) → convert **only** that entry. Entries are a `##`/`###` section, a `* **Name**:` / `- **Name**:` list item, or a table row. Use Grep to find it.
   - If ambiguous or not found, say what you searched and ask; do not guess.
   Always read the file fresh from disk, since the user may have edited it.
2. **Convert** using the rules below.
3. **Print** the result in a single fenced code block tagged `bbcode`, so it can be copied in one click.
4. **Add a short note** after the block (two bullets max):
   - `[h1]` can be dropped if the article template already shows the title.
   - Cross-links to other World Anvil articles use `@[Article Name](article)`; names were left as plain text because the article titles are unknown.

## Conversion Rules (all page types)
- **Drop:** YAML frontmatter, `## Sources` / `## References` sections, and every provenance link, whether `[[raw/...]]` or a session citation like `[[Sessions/YYYY/YYYY-MM-DD|Session]]`, including `[Source]` labels. Leave no stray spaces before punctuation where a citation was removed.
- **Wiki links:** `[[target|Label]]` → `Label`; `[[target]]` → last path segment without `#anchor`. Remove parenthetical or sentence-level "See [[...]]" cross-references entirely.
- **Headings:** `#` → `[h1]`, `##` → `[h2]`, `###` → `[h3]`, `####` → `[h4]`. Close each tag.
- **Emphasis:** `**x**` → `[b]x[/b]`, `*x*` → `[i]x[/i]`. Preserve existing emphasis exactly; add none. If link removal leaves bold around plain text, result is `[b]Label[/b]`.
- **Bulleted lists** (`-` or `*`): wrap consecutive items in `[ul]...[/ul]`, each as `[li]...[/li]` on its own line. Nested items: put a nested `[ul]` inside the parent `[li]`.
- **Numbered lists:** `[ol]...[/ol]` with `[li]` items.
- **Checklists** (`- [ ]` / `- [x]`): use `[li]` and prefix the text with `☐ ` or `☑ `.
- **Tables:** `[table]`, header row as `[tr][th]..[/th][/tr]`, body rows as `[tr][td]..[/td][/tr]`, one row per line, `[/table]`. Unescape `\|` inside cells. Drop empty trailing columns. Skip the `---` separator row.
- **Paragraphs:** plain text separated by a blank line.
- **Long single-line entries** (Lore note style): keep the entry as one paragraph, even when it has dated sentences (`On 2026-09-03 ...`). Do not restructure or summarize.
- **Single entry output:** when converting one entry, use its name as `[h1]` (or `[h2]` if the user says it is part of a larger article) followed by its text.
- Do not change wording, add facts, reorder content, or escape quotes/apostrophes.
- One blank line between block elements; none inside lists.

## Page-Type Notes
Choose the rules below from the note's `type` frontmatter property: `session-note`, `character`, `lore`, `quest`, `location`, `reference`. Index pages are hubs of their type (e.g. `Characters.md`, `Lore.md`).
- **Character frontmatter:** the frontmatter is dropped. If the page has no attribute table but the frontmatter has `species`, `class`, `character-type` or `player`, emit a small `[table]` of those values (skip empty ones) right after `[h1]`.
- **Sessions:** intro paragraph, then `[h2]` sections, `[ul]`/`[ol]` lists. Title is `[h1]Session: YYYY-MM-DD[/h1]`.
- **Character pages:** keep the page's own section order (headings vary: `Backstory / Events`, `Backstory`, `Key Events`, `Appearance`, ...). Dated event bullets (`- **October 1, 2026:** ...`) stay as `[li]`. Drop trailing `[Session]` links and any stray session-link bullets inside the events list.
- **Lore / Quests / Locations / Characters index pages:** these are big; if the user gave no entry, ask which entry or section they want rather than converting the whole file. Convert the whole file only if they say so.

## Output Template
```bbcode
[h1]Title[/h1]

Intro paragraph.

[h2]Section[/h2]
[ul]
[li]Item with [b]bold[/b].[/li]
[/ul]

[h3]Sub-section[/h3]
[ol]
[li]Numbered item.[/li]
[/ol]

[table]
[tr][th]Name[/th][th]Race[/th][/tr]
[tr][td]Maxwella[/td][td]Elf[/td][/tr]
[/table]
```
