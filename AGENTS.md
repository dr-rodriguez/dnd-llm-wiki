# LLM Wiki Schema and Guidelines

This repository is maintained as an LLM Wiki, a persistent, compounding personal knowledge base.
As an AI assistant, you are focused on navigating, maintaining, and updating this wiki of D&D session notes.

## Folder Structure
- `raw/`: Permanent, immutable source of truth for source documents (articles, papers, logs) provided by humans. Session notes are organized into year-based subdirectories (e.g., `raw/2024/`).
- `wiki/`: LLM-generated markdown files (summaries, entity pages, concept maps). You own and update these files.
  - `wiki/Sessions/YYYY/`: Session summaries, organized into year-based subdirectories mirroring `raw/` (e.g., `wiki/Sessions/2024/2024-01-04.md`).
  - `wiki/Quests/`: Quest overview (`Quests.md`) and detailed quest/mission pages.
  - `wiki/Locations/`: Locations hub (`Locations.md`).
  - `wiki/Lore/`: Lore hub (`Lore.md`) plus one note per topic (Ancient History, Major Projects, Deities and Religions, Locations of Interest, Technology, Factions and Organizations, Bestiary). Link entries as `[[wiki/Lore/Technology#Slave Drives|Slave Drives]]`.
  - `wiki/Characters/`: One page per character, plus the `Characters.md` roster table and `B-Team.md` (group page).
  - `wiki/Sessions/`: Year subfolders hold session notes; loose files here (`Extra Notes.md`, `Level Up Notes-Ideas.md`) are out-of-game reference notes.
  - `wiki/Images/`: Images embedded in wiki pages (and referenced by raw notes via `![[file.png]]`).
  - `wiki/Base Tables/`: Obsidian Bases (`Characters.base`, `Quests.base`, `Lore.base`, `Sessions.base`) that list notes by their `type` property. They are driven by frontmatter, so keep properties correct rather than editing the bases.
- `.agents/skills/`: Contains specific skill instructions for Ingesting, Querying, and Linting the wiki.

## Note Types and Properties
Every note in `wiki/` (except `index.md` and `log.md`) MUST start with YAML frontmatter that has a `type` property. The type follows the folder:

| `type` | Folder | Extra properties |
| --- | --- | --- |
| `character` | `wiki/Characters/` | `name`, `species`, `class`, `character-type` (`PC` or `NPC`), `player` (PCs only), `link` (external sheet URL; leave empty if unknown) |
| `location` | `wiki/Locations/` | none |
| `lore` | `wiki/Lore/` | none |
| `quest` | `wiki/Quests/` | none |
| `session-note` | `wiki/Sessions/YYYY/` | `year` (number, e.g. `2026`), `date` (`YYYY-MM-DD`) |
| `reference` | `wiki/Sessions/` (loose files) | none |

- Put `type` first, then the type's extra properties, then `tags` / `aliases`.
- Character property values come from the page's attribute table (Type, Species, Class, Player) and the raw Characters CSV. Quote string values. Leave a property empty rather than guessing.
- Hub/roster pages (`Characters.md`, `Quests.md`, `Lore.md`, `Locations.md`) carry their folder's `type` with no extra properties. `Characters.base` leaves out `Characters.md` by name.
- Example (character):
  ```yaml
  ---
  type: character
  name: "Aolis"
  species: "Drow"
  class: "Shadow Sorcerer"
  character-type: "PC"
  player: "Koi/Altair"
  link:
  tags:
    - Aolis
  ---
  ```
- Example (session note):
  ```yaml
  ---
  type: session-note
  year: 2026
  date: 2026-10-01
  tags:
    - Aolis
  ---
  ```

## Core Files
- `wiki/index.md`: A content-oriented catalog of every page in the wiki (excluding `raw/`). Update this whenever a new page is created. Has no `type`.
- `wiki/log.md`: A chronological, append-only record of all ingests, queries, and maintenance tasks. Has no `type`.

## Provenance and Linking
To maintain the wiki as a reliable knowledge base, every claim or significant piece of information in the `wiki/` directory MUST be linked back to its original source in `raw/`.
- Use Obsidian-style links: `[[raw/2024/2024-01-01.md|Source]]`.
- For entity pages (e.g., a character or location), include a "Sources" section listing all relevant source documents.
- For specific claims or session summaries, provide inline citations or a list of references at the bottom of the page.

## Internal Linking
To create a densely interconnected knowledge base:
- Every time a major character, location, or lore concept is mentioned for the first time in a page, it MUST be linked to its corresponding wiki page.
- Use the format `[[EntityName]]` or `[[wiki/Sessions/YYYY/YYYY-MM-DD|YYYY-MM-DD]]`.
- If an entity is in a subdirectory, use the full path: `[[wiki/Characters/Soren|Soren]]`.

## Core Workflows
1. **Ingest**: Read new sources in `raw/` and integrate their information into `wiki/`. Source documents remain in `raw/` as the permanent source of truth.
2. **Query**: Answer questions by searching the wiki. File high-value answers back into the wiki as new pages.
3. **Lint**: Perform health checks to identify contradictions, stale claims, orphan pages, or data gaps. Check `wiki/` against `raw/` to ensure accuracy.

Please refer to the specific skills in `.agents/skills/` for detailed instructions on performing these tasks.
