# JPrompt vs ThoughtCrafter

Written while tidying SApps for import into cooperativesausage.com. Facts below come from reading `JPrompt/` (v3.0, v4.0 draft, `assets/List.json`) and the vendored copy at `cooperativesausage/public/thoughtcrafter/`.

## What each one is

| | JPrompt | ThoughtCrafter |
|---|---|---|
| Question it asks | A full reflective question: *"What did I learn today?"* | A topic: *"What do you think of **Aberdeen**?"* |
| Content | 566 unique prompts (567 in the old list; 1 duplicate removed) | 367,352 topics: places 148k, nouns 86k, words 49k, people 34k, movies 31k, books 8k, concepts 8k, plus brands, sayings, dilemmas, phobias… |
| Size and loading | One 72 KB file, works from `file://`, USB stick, any sub-path | 1.4 MB page + 22 MB of JSON fetched at runtime. Tier 1 (18k) is embedded; tiers 2 and 3 need http |
| Variety control | None in v3. **v4.0 adds** categories, no-repeat deck, favourites, own prompts | Everyday / Mixed / Deep Cuts rarity weighting |
| Output | Copy the prompt | Write box + tags + live **jrnl-format entry** (`[timestamp] Thoughts - Topic`, `@thoughts @tags`) |
| Online dependency | None | "Look it up" links to Wikipedia/Wiktionary (optional) |
| Source repo | In SApps | None. `projects.py` has `repo: None` and `PINS.json` has no entry, so the vendored copy is the only copy |

## What JPrompt has that ThoughtCrafter doesn't

- **Reflective, first-person prompts.** ThoughtCrafter gives you a *subject*; JPrompt gives you a *question about you* ("What would I tell my younger self?", "What am I grateful for?"). They produce different writing: opinion versus self-reflection.
- **A small, curated, portable list.** 566 prompts, ~50 KB, fully offline.
- **Categories** (new in 4.0, assigned by keyword rules and easy to correct): Reflection, Goals & growth, Feelings, Today, Relationships, Memories, Gratitude, Creative, Imagine. ThoughtCrafter's only axis is rarity.
- **Creative-writing prompts** ("Write a story…", ~22 of them) and "what if" scenarios.
- **Favourites and your own prompts**, plus a **prompt of the day**.

## What ThoughtCrafter has that JPrompt lacked

- The write-box → tags → journal-entry flow. **JPrompt 4.0 now has the same flow**, producing the same format (`[timestamp] Prompt text` / body / `@journal @tags`) so entries from either paste straight into Journl.
- Rarity tiers and a huge pool.
- A distinctive editorial design.

## What could be merged

| Idea | Verdict |
|---|---|
| Add JPrompt's 566 questions to ThoughtCrafter as a "Questions" tier | Technically easy (they fit its row format: `[text, "question", "", ""]`). But ThoughtCrafter's source repo is unknown, so edits would live only in the vendored copy and be lost on the next sync. Needs the upstream repo first |
| Add ThoughtCrafter's topic list to JPrompt | No. 22 MB breaks JPrompt's reason for existing (tiny, offline) |
| Share the entry format | **Done.** Both emit jrnl-format entries |
| Share rarity weighting | Not applicable: JPrompt's list is flat and small |

## Recommendation

**Keep JPrompt as its own app, and give the pair a shared "Journalling" grouping on the site.** They are siblings, not duplicates: ThoughtCrafter is *"what do you think of X?"*, JPrompt is *"look inward"*, and both now end in the same jrnl-format entry that Journl reads. Merging would trade a 72 KB offline page for a 22 MB one and edit a copy with no upstream.

On the hub that means one **Journalling** section containing ThoughtCrafter, JPrompt, and (if you want it public rather than just the private `/jnl`) Journl. If you later find or create ThoughtCrafter's repo, adding JPrompt's questions as a fourth "Questions" mode is a half-day job.

## Housekeeping done in JPrompt

- v4.0.0 promoted to `JPrompt.html` (rebuilt rather than taking the R&D v4 draft, which was v3 plus a default-theme tweak).
- The list is embedded in the page, so there is no `fetch` and it works from `file://` and from any URL path. `assets/List.json` stays as the editable source.
- `assets/fonts/` is no longer used by anything (the Merchant font was dropped in v3). It can be deleted.
- One duplicate prompt removed ("What did I learn today?").
