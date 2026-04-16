# Query Skill

**Description:** Use this skill to answer user questions using the knowledge stored in the wiki.

## Workflow
1. **Search the Wiki:** Use search tools to find relevant information within the `wiki/` directory based on the user's question. `wiki/index.md` is a good starting point.
2. **Synthesize Answer:** Formulate a comprehensive answer using *only* the information found in the wiki. Cite the specific wiki pages used.
3. **Evaluate Answer Value:** Determine if the generated answer represents a new synthesis of information that isn't explicitly captured in a single existing page.
4. **Compound Knowledge:** If the answer is of high value or introduces a new conceptual grouping:
   - Create a new page in the `wiki/` directory containing this synthesized answer.
   - Update `wiki/index.md` with the new page.
5. **Log Activity:** Append an entry to `wiki/log.md` recording the query, the date, and whether a new page was generated from the answer.
