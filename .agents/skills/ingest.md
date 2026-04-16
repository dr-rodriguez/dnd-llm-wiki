# Ingest Skill

**Description:** Use this skill when a new source document is added to the `raw/` folder, and you need to integrate its knowledge into the wiki.

## Workflow
1. **Read the Source:** Carefully read the new document in the `raw/` directory.
2. **Identify Key Information:** Extract the main entities, concepts, claims, and takeaways from the document.
3. **Plan Updates:** Identify which existing pages in the `wiki/` directory need to be updated with this new information. If new concepts are introduced, plan to create new pages for them.
4. **Execute Updates:** 
   - Update existing wiki pages to integrate the new knowledge.
   - Create new wiki pages as necessary.
   - Ensure all information is cross-referenced correctly.
5. **Update Index:** If you created new pages, add them to `wiki/index.md`.
6. **Log Activity:** Append an entry to `wiki/log.md` detailing the file ingested, the date, and a brief summary of the changes made to the wiki.
