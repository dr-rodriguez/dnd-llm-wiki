---
name: ingest
description: Turn new D&D session notes in `raw/` into wiki pages. Writes the session note, updates the character, quest, lore and location pages it touches, then the index and log. Use when the user says "ingest", "ingest 2026-10-08", "add/process the new session notes", or mentions a new file in `raw/`, or when raw session files have no wiki note yet.
---

# Ingest

Follow `AGENTS.md` for note types, frontmatter properties, link format and provenance. This skill covers the workflow only.

## 1. Find what to ingest
- If the user names a date or file, use that.
- Otherwise, list raw session files with no wiki note: run `python3 .agents/skills/lint/lint_wiki.py` and look for `not ingested` errors.
- Several new files: ingest them oldest first, one at a time, so each session note can link the previous one.

## 2. Read the source
- Read the raw file in full. If an image is embedded (`![[file.png]]`), make sure the file is in `wiki/Images/` and keep the embed where it matters.
- Read the previous session note, so the lead paragraph picks up where it left off and names stay consistent.
- Fix any encoding mojibake in what you write (`â€™` → `'`, `â€œ`/`â€` → `"`, `â€”` → `—`, `â€“` → `–`, `â€¦` → `...`). Never edit `raw/`.
- If the notes correct an earlier session (e.g. "it wasn't a bomb"), fix that session note too and mention the correction (see the template).

## 3. Write the session note
Create `wiki/Sessions/YYYY/YYYY-MM-DD.md` from [session-template.md](session-template.md). Tags are the PascalCase names of the characters and locations in the session.

## 4. Update the pages the session touches
Go through every character, location, lore topic and quest the session mentions. For each:

- **Characters** (`wiki/Characters/PC/`, `wiki/Characters/NPC/`): add a dated bullet to the page's events list (under `Backstory / Events` or `Key Events`, whichever the page uses), e.g. `- **October 1, 2026:** ...`, in date order. Add the session to `## Sources` in date order. If species, class or player changed, update both the attribute table and the frontmatter.
  - New notable NPC: create a page in `wiki/Characters/NPC/` and add a row to `wiki/Characters/Characters.md`. Minor NPCs get only a roster row.
- **Quests** (`wiki/Quests/`): record progress, new tasks or completion on the quest page and in `Quests.md`. New missions get a task in `Quests.md`; give one its own page only if it spans several sessions.
- **Locations** (`wiki/Locations/`): major locations have their own page (`Tesselia.md`, `Drakenweld.md`, ...); add what happened there. New major location: create a page and link it from `Locations.md`. Minor locations stay as rows in the `Locations.md` table.
- **Lore** (`wiki/Lore/`): add or extend the entry in the matching topic note (Technology, Bestiary, Factions and Organizations, ...). If no topic fits, create a topic note and list it in `Lore.md`.

Every addition cites the session note (`[[Sessions/YYYY/YYYY-MM-DD|Session: YYYY-MM-DD]]`), never `raw/`. Link major entities on first mention in each page you touch.

## 5. Index and log
- `wiki/index.md`: add each new page. The Session Logs list is newest first: insert the new session at the top and move the *(Latest Session)* marker to it.
- `wiki/log.md`: append one row to the table (date, file ingested, short summary of pages created and updated). Use the Edit tool, not shell redirection, so the file stays UTF-8.

## 6. Check
Run `python3 .agents/skills/lint/lint_wiki.py` and fix any errors or warnings your changes introduced (unresolved links, orphans, missing index entries, wrong properties). Pre-existing `INFO` items can be left alone.
