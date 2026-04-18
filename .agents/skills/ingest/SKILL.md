---
name: ingest
description: Use this skill when a new source document is added to the `raw/` folder, and you need to integrate its knowledge into the wiki.
---

# Ingest Skill

**Description:** Use this skill when a new source document is added to the `raw/` folder, and you need to integrate its knowledge into the wiki.

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
3. **Identify Key Information:** Extract the main entities, concepts, claims, and takeaways from the document.
4. **Plan Updates:** Identify which existing pages in the `wiki/` directory need to be updated with this new information. If new concepts are introduced, plan to create new pages for them.
5. **Execute Updates:** 
   - Update existing wiki pages to integrate the new knowledge.
   - Create new wiki pages as necessary.
   - **Internal Linking:** Ensure every major character, location, and lore concept is linked to its wiki page (e.g., `[[Characters#Soren|Soren]]`) the first time it is mentioned in a session note or update.
   - **Tagging:** Add a `tags` field to the YAML frontmatter. Tags should be character and location names mentioned in the document. Tags MUST be single words in PascalCase with no spaces or special characters (e.g., `MaggieNorth`, `LordlingsBordello`).
   - **Provenance:** Every update or new page MUST include a link back to the source document in `wiki/sources/`. For session notes, this can be a list at the bottom of the page; for entity pages, add to a "Sources" section.
   - Ensure all information is cross-referenced correctly.
6. **Archive Source:** Move the ingested files from `raw/` to `wiki/sources/`.
7. **Clean Up:** Ensure the `raw/` directory is empty.
8. **Update Index:** If you created new pages, add them to `wiki/index.md`.
9. **Log Activity:** Append a new row to the table in `wiki/log.md` detailing the file ingested, the date, and a brief summary of the changes made to the wiki. Use the `replace` tool to append the new row to ensure the table structure and UTF-8 encoding are maintained.
