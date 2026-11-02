# Algorithmix
A deliberately slightly-odd creative-prompt generator.

> You have 9 seconds to film a painting. Your keywords are hot air balloon, mother figure and envy. Good luck!

## Background
Algorithmix gives you a small, strange brief to jump off from. "You have 9 seconds to film a painting…" could mean a 9-second film, 9 seconds to get everything set up, or something else entirely. That ambiguity is the point.

It began life as a C++ program (the first language I had to hand, and a candidate for embedding in a physical device), then Python, then JavaScript. `Algorithmix.html` is the finished, friendly version.

## Usage
1. Open `Algorithmix.html` in your browser of choice.
2. Press **Generate** (or the Space bar).
3. Click a highlighted word to re-roll just that word. **Shift-click** (or right-click) a word to lock it so Generate leaves it alone.
4. **Copy** the result, or click one in the history to copy it.

## Features
- ~1,500 nouns plus time units, verbs, items and emotions (from `List.json`, built into the page so it works offline)
- Re-roll or lock individual words
- Maximum time setting (remembered)
- Recent prompts (last 10)
- Light/Dark mode (remembered)

## Layout
| Path | What it is |
|------|------------|
| `Algorithmix.html` | The app |
| `List.json` | The word lists (source of the lists inlined in the app) |
| `Ports/` | The original C++, Python and JavaScript versions |
| `R&D/` | An early ChatGPT-assisted web attempt, kept for reference |

To change the words, edit `List.json` and paste it over the `WORDS` constant in the HTML file.

## The prompt template
`You have [number] [time unit] to [verb] [item]. Your keywords are [noun], [noun] and [emotion].`

## Roadmap
### Planned Functionality
- [ ] More templates (not just the "you have N seconds" one)
- [ ] Word list editor in the page

## Dependencies
I try to reduce the dependencies as much as possible. Everything is inline; the app works offline from a single file.

### Current Dependencies
- None

### Previous Dependencies
- None

## Contributing
If you have any ideas for features, or find any bugs, please open an issue or a pull request. I will try to respond as soon as possible.

Should you want to donate, you can do so [here](https://www.buymeacoffee.com/caddickbrown).

Thank you!

## License
This project is licensed under the MIT License.

## Change Log
### [1.0.0]
#### Added
- Single-file web app: generate, copy, re-roll or lock individual words, history, themes

#### Changed
- Python, C++ and JavaScript versions moved to `Ports/`; ChatGPT attempt moved to `R&D/`
- README rewritten (it previously contained scratch notes)

### [0.1.0]
- Command-line prototypes in C++, Python and JavaScript

