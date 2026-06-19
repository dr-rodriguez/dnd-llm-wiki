---
name: query
description: Use this skill to answer user questions using the knowledge stored in the wiki.
---

# Query Skill

**Description:** Use this skill to answer user questions using the knowledge stored in the wiki.

## Workflow
1. **Search the Wiki:** Use search tools to find relevant information within the `wiki/` directory based on the user's question. `wiki/index.md` is a good starting point. If the synthesized wiki pages are insufficient, consult the original documents in `wiki/sources/`.
2. **Synthesize Answer:** Formulate a comprehensive answer using *only* the information found in the wiki and its sources.
   - **Link Formatting:** When responding to the user, transform Obsidian-style links (e.g., `[[path/to/page#heading|Display Text]]` or `[[page]]`) into bold or italic text for clarity (e.g., **Display Text** or *page*).
   - **Internal Citations:** Ensure that any new wiki pages created during the 'Compound Knowledge' step still use standard Obsidian-style links for wiki-compatibility.
3. **Evaluate Answer Value:** Determine if the generated answer represents a new synthesis of information that isn't explicitly captured in a single existing page.
4. **Compound Knowledge:** If the answer is of high value or introduces a new conceptual grouping:
   - Create a new page in the `wiki/` directory containing this synthesized answer.
   - Update `wiki/index.md` with the new page.
5. **Log Activity:** Append a new row to the table in `wiki/log.md` recording the query, the date, and whether a new page was generated from the answer. Use the `replace` tool to append the new row to ensure the table structure and UTF-8 encoding are maintained.
