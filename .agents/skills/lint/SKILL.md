---
name: lint
description: Use this skill to perform periodic health checks on the wiki to maintain its consistency and quality.
---

# Lint Skill

**Description:** Use this skill to perform periodic health checks on the wiki to maintain its consistency and quality.

## Workflow
1. **Scan the Wiki:** Review the pages within the `wiki/` directory.
2. **Cross-Reference Sources:** Compare key claims in the wiki against the archived documents in `wiki/sources/` to ensure accuracy.
3. **Identify Issues:** Look for the following problems:
   - **Contradictions:** Information on one page that conflicts with another.
   - **Stale Claims:** Information that may be outdated or inconsistent with the source material.
   - **Orphan Pages:** Pages that are not linked to from `wiki/index.md` or any other pages.
   - **Missing Provenance:** Identify any pages that lack links back to their original source documents in `wiki/sources/`.
   - **Data Gaps:** Missing information that should be logically present based on existing context.
4. **Resolve Issues:**
   - Fix broken links and integrate orphan pages.
   - Update or flag contradictory and stale information.
   - Suggest areas for future ingestion to fill data gaps.
5. **Log Activity:** Append an entry to `wiki/log.md` recording the date of the linting operation and a summary of the issues fixed.
