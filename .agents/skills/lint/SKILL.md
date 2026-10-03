---
name: lint
description: Use this skill to perform periodic health checks on the wiki to maintain its consistency and quality.
---

# Lint Skill

**Description:** Use this skill to perform periodic health checks on the wiki to maintain its consistency and quality.

## Workflow
1. **Scan the Wiki:** Review the pages within the `wiki/` directory.
2. **Cross-Reference Sources:** Compare key claims in the wiki against the archived documents in `raw/` to ensure accuracy.
3. **Identify Issues:** Look for the following problems:
   - **Contradictions:** Information on one page that conflicts with another.
   - **Stale Claims:** Information that may be outdated or inconsistent with the source material.
   - **Orphan Pages:** Pages that are not linked to from `wiki/index.md` or any other pages.
   - **Missing Provenance:** Identify any pages that lack links back to their original source documents in `raw/`.
   - **Data Gaps:** Missing information that should be logically present based on existing context.
   - **Classification and Properties:** Check every note against the Note Types and Properties table in `AGENTS.md`:
     - Every note except `index.md` / `log.md` has frontmatter with a valid `type`: `character`, `location`, `lore`, `quest`, `session-note` or `reference`.
     - The type matches the note's folder. A note in the wrong folder should be moved, and its links fixed.
     - `session-note` pages have `year` and `date` that match the file name.
     - `character` pages have `name`, `species`, `class`, `character-type`, `player`, `link`. Values agree with the page's attribute table and the raw Characters CSV.
     - Quick check: `grep -L "^type:" -r wiki --include=*.md` lists notes missing a type (ignore `index.md` and `log.md`).
   - **Base Tables:** `wiki/Base Tables/` still holds `Characters.base`, `Quests.base`, `Lore.base` and `Sessions.base`, and their filters use the current type names.
   - **Mangled Links:** Search for `]]]`, which marks a link damaged by a bad link update; restore the eaten character before it.
4. **Resolve Issues:**
   - Fix broken links and integrate orphan pages.
   - Update or flag contradictory and stale information.
   - Suggest areas for future ingestion to fill data gaps.
5. **Log Activity:** Append a new row to the table in `wiki/log.md` recording the date of the linting operation and a summary of the issues fixed. Use the `replace` tool to append the new row to ensure the table structure and UTF-8 encoding are maintained.
