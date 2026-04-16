# LLM Wiki Schema and Guidelines

This repository is maintained as an LLM Wiki, a persistent, compounding personal knowledge base.
As an AI agent, you are responsible for maintaining and updating the wiki based on these guidelines.

## Folder Structure
- `raw/`: Immutable source documents (articles, papers, logs). This is the source of truth. Do not modify files here.
- `wiki/`: LLM-generated markdown files (summaries, entity pages, concept maps). You own and update these files.
- `.agents/skills/`: Contains specific skill instructions for Ingesting, Querying, and Linting the wiki.

## Core Files
- `wiki/index.md`: A content-oriented catalog of every page in the wiki. Update this whenever a new page is created.
- `wiki/log.md`: A chronological, append-only record of all ingests, queries, and maintenance tasks.

## Core Workflows
1. **Ingest**: Read new sources in `raw/`, discuss takeaways, and update relevant `wiki/` pages.
2. **Query**: Answer questions by searching the wiki. File high-value answers back into the wiki as new pages.
3. **Lint**: Perform health checks to identify contradictions, stale claims, orphan pages, or data gaps.

Please refer to the specific skills in `.agents/skills/` for detailed instructions on performing these tasks.
