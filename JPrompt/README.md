# JPrompt
Random journalling prompts, with categories, favourites and a jrnl-format entry builder. One HTML file.

## Background
I wanted a quick journal prompt on command, from a file that needs no installation and works on any computer, even from a USB drive. Version 4 keeps that and adds what a prompt tool needs once you actually use it: no repeats, categories, saving the good ones, and somewhere to write.

JPrompt asks *about you*. Its sibling on the website, ThoughtCrafter, picks a *topic*. See [COMPARISON-ThoughtCrafter.md](COMPARISON-ThoughtCrafter.md).

## Usage
1. Open `JPrompt.html` in your browser of choice.
2. Press **New prompt** (or Space).
3. Optionally pick a category first.
4. Write underneath, add tags, and **Copy journal entry**. Paste it into Journl or any jrnl file.

## Features
- 566 prompts in 9 categories: Reflection, Goals & growth, Feelings, Today, Relationships, Memories, Gratitude, Creative, Imagine (plus **Mine**)
- A shuffled deck: no prompt repeats until you have seen them all; **Back** steps through what you saw
- **Prompt of the day**: the same prompt all day for everyone
- ★ Save prompts you like; export them as `.txt`
- Add your own prompts (one per line); they join the deck
- Write box with tags. The entry copies as `[2025-01-02 09:30:00] Prompt text`, your text, then `@journal @your @tags`
- Light / Dark / Sepia / Terminal themes

## Behavior
- Saved and custom prompts live in this browser (`sapps.jprompt.favs`, `sapps.jprompt.custom`). What you write in the box is **not** saved.
- Categories are assigned automatically from keywords, so a few prompts will sit in a surprising place. The category is the first element of each row in the embedded data.
- `assets/List.json` is the editable source list; the page embeds a copy, so it works without a server.

## Roadmap
### Planned Functionality
- Questions mode inside ThoughtCrafter (blocked on finding its source repo)
- Hand-corrected categories
- A "write now" mode that saves a draft

## Change Log
### [4.0.0]
#### Added
- Categories, shuffled no-repeat deck, Back, prompt of the day, favourites, custom prompts, write box, jrnl-format entry copy, Sepia/Terminal themes
#### Changed
- Filename is `JPrompt.html` (no version); old versions in `Archive/`
- Prompt list embedded, duplicate removed (566)

### [3.0]
- Aesthetic standardisation, dark/light mode, colours/page name/version as variables, font dependency removed

### [2.0]
- Visual changes, bigger buttons, copy button appears on generation

### [1.0]
- Initial release: random prompt, copy to clipboard, 550+ prompts

## Dependencies
None. One self-contained HTML file: no frameworks, no libraries, no fonts or scripts loaded from the network.

## Contributing
If you have any ideas for features, or find any bugs, please open an issue or a pull request. I will try to respond as soon as possible.

Should you want to donate, you can do so [here](https://www.buymeacoffee.com/caddickbrown).

Thank you!

## License
This project is licensed under the MIT License. See the [LICENSE](../LICENSE) file for details.
