# LLM Wiki Schema and Guidelines

This repository is maintained as an LLM Wiki, a persistent, compounding personal knowledge base.
As an AI assistant, you are focused on navigating, maintaining, and updating this wiki of D&D session notes.

## Folder Structure
- `raw/`: Permanent, immutable source of truth for source documents (articles, papers, logs) provided by humans. Session notes are organized into year-based subdirectories (e.g., `raw/2024/`).
- `wiki/`: LLM-generated markdown files (summaries, entity pages, concept maps). You own and update these files.
- `.agents/skills/`: Contains specific skill instructions for Ingesting, Querying, and Linting the wiki.

## Core Files
- `wiki/index.md`: A content-oriented catalog of every page in the wiki (excluding `raw/`). Update this whenever a new page is created.
- `wiki/log.md`: A chronological, append-only record of all ingests, queries, and maintenance tasks.

## Provenance and Linking
To maintain the wiki as a reliable knowledge base, every claim or significant piece of information in the `wiki/` directory MUST be linked back to its original source in `raw/`.
- Use Obsidian-style links: `[[raw/2024/2024-01-01.md|Source]]`.
- For entity pages (e.g., a character or location), include a "Sources" section listing all relevant source documents.
- For specific claims or session summaries, provide inline citations or a list of references at the bottom of the page.

## Internal Linking
To create a densely interconnected knowledge base:
- Every time a major character, location, or lore concept is mentioned for the first time in a page, it MUST be linked to its corresponding wiki page.
- Use the format `[[EntityName]]` or `[[wiki/Sessions/YYYY-MM-DD|YYYY-MM-DD]]`.
- If an entity is in a subdirectory, use the full path: `[[wiki/Characters/Soren|Soren]]`.

## Core Workflows
1. **Ingest**: Read new sources in `raw/` and integrate their information into `wiki/`. Source documents remain in `raw/` as the permanent source of truth.
2. **Query**: Answer questions by searching the wiki. File high-value answers back into the wiki as new pages.
3. **Lint**: Perform health checks to identify contradictions, stale claims, orphan pages, or data gaps. Check `wiki/` against `raw/` to ensure accuracy.

Please refer to the specific skills in `.agents/skills/` for detailed instructions on performing these tasks.
