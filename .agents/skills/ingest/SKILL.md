---
name: ingest
description: Use this skill when a new source document is added to the `raw/` folder, and you need to integrate its knowledge into the wiki. `raw/` is the permanent, immutable source of truth for these documents.
---

# Ingest Skill

**Description:** Use this skill when a new source document is added to the `raw/` folder, and you need to integrate its knowledge into the wiki. `raw/` is the permanent, immutable source of truth for these documents.

## Workflow
1. **Read the Source:** Carefully read the new document in the `raw/` directory.
2. **Sanitize Content:** If the source document contains corrupted character sequences (often due to encoding issues), replace them with their correct equivalents:
   - `â€™` → `'`
   - `â€œ` → `"`
   - `â€` → `"`
   - `â€“` → `–`
   - `â€”` → `—`
   - `â€¦` → `...`
   - `â¡` → `!`
   - `Ã¢â‚¬â„¢` → `'`
   - `Ã¢â‚¬Å“` → `"`
   - `Ã¢â‚¬Â` → `"`
   - `Ã¢â‚¬â€œ` → `–`
   - `Ã¢â‚¬â€` → `—`
   - `Â¾` → `¾`
   - `Â½` → `½`
   - `Â¼` → `¼`
3. **Identify Key Information:** Extract the main entities, concepts, claims, and takeaways from the document.
4. **Plan Updates:** Identify which existing pages in the `wiki/` directory need to be updated with this new information. If new concepts are introduced, plan to create new pages for them.
5. **Execute Updates:** 
   - Update existing wiki pages to integrate the new knowledge.
   - Create new wiki pages as necessary. **Classify each new page first**: pick its `type` from the table in `AGENTS.md` (Note Types and Properties), then put it in that type's folder:
     - `session-note` → `wiki/Sessions/YYYY/YYYY-MM-DD.md` (link as `[[Sessions/YYYY/YYYY-MM-DD|YYYY-MM-DD]]`).
     - `character` → `wiki/Characters/<Name>.md`, with the attribute table (Type, Species, Class, Player). Also add a row to `wiki/Characters/Characters.md`.
     - `quest` → `wiki/Quests/`. Also update `wiki/Quests/Quests.md`.
     - `lore` → a new entry in the matching topic note under `wiki/Lore/`. If no topic fits, create a new topic note and list it in `wiki/Lore/Lore.md`.
     - `location` → a new row/entry in `wiki/Locations/Locations.md`.
     - `reference` → loose out-of-game notes in `wiki/Sessions/` (rare).
     - Images go in `wiki/Images/`.
   - **Properties:** Every new page starts with frontmatter: `type` first, then the type's extra properties, then `tags`.
     - Session notes: `year` (number) and `date` (`YYYY-MM-DD`, from the raw file name).
     - Character pages: `name`, `species`, `class`, `character-type` (`PC`/`NPC`), `player` (PCs only), `link` (leave empty).
     - When an ingest changes a character's species, class or player, update both the attribute table and the frontmatter.
     - Never remove `type` from an existing page. The Base tables in `wiki/Base Tables/` depend on it.
   - **Internal Linking:** Ensure every major character, location, and lore concept is linked to its wiki page (e.g., `[[Characters#Soren|Soren]]`) the first time it is mentioned in a session note or update.
   - **Tagging:** Add a `tags` field to the YAML frontmatter (after `type` and its properties). Tags should be character and location names mentioned in the document. Tags MUST be single words in PascalCase with no spaces or special characters (e.g., `MaggieNorth`, `LordlingsBordello`).
   - **Provenance:** Every update or new page MUST cite its source. Only session notes (and the loose reference notes in `wiki/Sessions/`) link to `raw/` (e.g., `[[raw/2024/2024-01-01.md|Source]]`). Every other page (characters, lore, quests, locations) cites the wiki session note instead (e.g., `[[Sessions/2024/2024-01-01|Session: 2024-01-01]]`), and links `raw/` only when no wiki page covers that source (e.g., the CSVs).
   - Ensure all information is cross-referenced correctly.
6. **Update Index:** If you created new pages, add them to `wiki/index.md`.
7. **Log Activity:** Append a new row to the table in `wiki/log.md` detailing the file ingested, the date, and a brief summary of the changes made to the wiki. Use the `replace` tool to append the new row to ensure the table structure and UTF-8 encoding are maintained.
