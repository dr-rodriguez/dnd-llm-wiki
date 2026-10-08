---
name: query
description: Answer questions about the D&D campaign (characters, NPCs, places, lore, quests, what happened when) from the wiki, citing the sessions the answer comes from, and save answers that pull many sources together as new wiki pages. Use when the user asks things like "who is Madasin", "what do we know about The Mountain", "what has Aolis done since Tesselia", or "when did we meet Sofia".
---

# Query

## 1. Search
- Start from the page that should own the answer: `wiki/index.md`, then the character, location, quest or lore page. Lore entries live in topic notes under `wiki/Lore/`.
- Use the frontmatter to narrow searches (properties are listed in `AGENTS.md`): `type: character` with `character-type: "PC"` for party questions, session `date:` for time spans.
- For "when" and "what happened" questions, follow the entity page's dated events and its Sources into the session notes.
- Optional: if the qmd MCP tools are available, the `dnd-wiki` collection supports keyword and semantic search, which helps with fuzzy questions ("the robot that wanted a body"). Grep and Glob work fine without it.
- Fall back to `raw/` only when the wiki is silent or looks wrong. If raw disagrees with the wiki, say so and suggest a lint.

## 2. Answer
- Use only what the wiki and raw notes say. If something is unknown or the notes conflict, say so.
- Cite the session dates the answer rests on (e.g. "(2026-09-24)").
- Write names as plain or bold text, not `[[wiki links]]`, since links don't render in chat.

## 3. Compound knowledge
If the answer pulls together several pages into something no single page holds (a timeline, a relationship history, a cross-cutting theme), it's worth saving:
- Create the page with the correct `type`, folder and frontmatter (`AGENTS.md`). A cross-cutting synthesis usually fits a new `lore` topic note (listed in `wiki/Lore/Lore.md`) or a `quest` page. Use normal wiki links and cite session notes.
- Add it to `wiki/index.md`.
- Append a row to `wiki/log.md` with the question and the page created (use the Edit tool so the file stays UTF-8).

Ordinary questions answered from existing pages need no log row.
