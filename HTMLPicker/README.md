# HTMLPicker
A spin-the-wheel random picker in a single HTML file.

## Background
Started as a quick "Decider" wheel. A later copy hard-coded a list of names; this version is a general wheel where the list is yours, and any list (a team, a menu, a game) can be saved and loaded by name. The original wheel is kept in `Archive/`.

## Usage
1. Open `HTMLPicker.html` in your browser of choice.
2. Add options (type and press Enter), import a list, or load a template.
3. Press **Spin** (or the Space bar).

## Features
- Labelled wheel; the result is chosen fairly (crypto-random) and the wheel lands on it
- Add, rename, recolour and remove options
- Import a list from pasted text, one per line; add a colour with a trailing hex code (`Pizza #ff8800`)
- Copy the list, or export it as a `.txt` file
- Save your own named lists; built-in templates: Yes/No, Coin flip, Dice, Dinner, Who goes first, Rock Paper Scissors
- "Remove the winner after each spin" for drawing without replacement
- Shuffle, clear, recent-results history
- Light / Dark / Sepia / Terminal themes
- Respects "reduce motion" (the wheel jumps rather than spins)

## Behavior
- Options are unique (case-insensitive). Names are plain text and are never interpreted as HTML.
- Everything is saved in this browser only (`sapps.htmlpicker.*`).

## Roadmap
### Planned Functionality
- Weighted options
- Shareable list links
- Sound toggle

## Change Log
### [2.0.0]
#### Added
- Labelled wheel, per-option colours, saved lists, templates, history, import/export, themes, keyboard support
#### Changed
- Merged HTMLPicker v1.0.0 and its list-based copy into one app; version removed from the filename
#### Fixed
- The announced winner did not match the slice under the pointer (wrong angle maths)
- Second and later spins started from the wrong position
- Option names were inserted as raw HTML

## Dependencies
None. One self-contained HTML file: no frameworks, no libraries, no fonts or scripts loaded from the network.

## Contributing
If you have any ideas for features, or find any bugs, please open an issue or a pull request. I will try to respond as soon as possible.

Should you want to donate, you can do so [here](https://www.buymeacoffee.com/caddickbrown).

Thank you!

## License
This project is licensed under the MIT License. See the [LICENSE](../LICENSE) file for details.

