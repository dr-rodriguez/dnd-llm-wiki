---
name: query
description: Use this skill to answer user questions using the knowledge stored in the wiki.
---

# Query Skill

**Description:** Use this skill to answer user questions using the knowledge stored in the wiki.

## Workflow
1. **Search the Wiki:** Use search tools to find relevant information within the `wiki/` directory based on the user's question. `wiki/index.md` is a good starting point. Notes are classified by the `type` frontmatter property (see Note Types and Properties in `AGENTS.md`):
   - Use the type to narrow the search, e.g. `grep -l "^type: character" -r wiki` for characters.
   - Use `character-type: "PC"` / `player:` for questions about the party.
   - Use `year:` / `date:` for questions about a time span.
   - Folders follow the type: `wiki/Characters/`, `wiki/Locations/`, `wiki/Lore/` (topic notes), `wiki/Quests/`, `wiki/Sessions/YYYY/`.
   - If the synthesized wiki pages are insufficient, consult the original documents in `raw/`.
2. **Synthesize Answer:** Formulate a comprehensive answer using *only* the information found in the wiki and its sources.
   - **Link Formatting:** When responding to the user, transform Obsidian-style links (e.g., `[[path/to/page#heading|Display Text]]` or `[[page]]`) into bold or italic text for clarity (e.g., **Display Text** or *page*).
   - **Internal Citations:** Ensure that any new wiki pages created during the 'Compound Knowledge' step still use standard Obsidian-style links for wiki-compatibility.
3. **Evaluate Answer Value:** Determine if the generated answer represents a new synthesis of information that isn't explicitly captured in a single existing page.
4. **Compound Knowledge:** If the answer is of high value or introduces a new conceptual grouping:
   - Create a new page containing this synthesized answer. Classify it with a `type` and put it in that type's folder, with the required frontmatter properties. A cross-cutting synthesis usually fits `lore` (as a new topic note under `wiki/Lore/`, listed in `wiki/Lore/Lore.md`) or `quest`.
   - Update `wiki/index.md` with the new page.
5. **Log Activity (only if a page was created):** Do **not** log ordinary queries — a question answered from existing wiki content needs no row in `wiki/log.md`. Only if the previous step created a new wiki page, append a new row to the table in `wiki/log.md` recording the query, the date, and the page that was generated. Use the `replace` tool to append the new row to ensure the table structure and UTF-8 encoding are maintained.
