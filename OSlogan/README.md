# OSlogan
A single-page slogan generator for the office-weary: every slogan is a reason plus a demand.

> "It's a Monday. Find me in the stationery cupboard… sleeping."

## Background
Started as a joke about what I'd put on a t-shirt on a bad day. It turned into a useful tiny template for a "mixable parts" generator: two lists, one random pick from each.

## Usage
1. Open `OSlogan.html` in your browser of choice.
2. Press **New slogan** (or the Space bar).
3. Press **Copy** to put it on the clipboard. Click any slogan in the history to copy that one instead.

## Features
- 25 reasons × 19 demands = 475 slogans
- Copy to Clipboard
- Recent slogans (last 8, remembered between visits)
- Keyboard: Space generates
- Light/Dark mode (remembered)

## Customising
The two lists, `reasons` and `demands`, are at the top of the script. Add lines to either; the count shown under the button updates itself.

## Roadmap
### Planned Functionality
- [ ] Download as PNG
- [ ] Third mixable part (a sign-off)

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
### [2.0.0]
#### Added
- Copy to Clipboard button (the v1 button referenced elements that did not exist and never worked)
- 25 reasons and 19 demands (was 9 and 3) and a second line for the demand
- History, Space-bar shortcut, remembered theme

#### Fixed
- Button label said "Get Random Journal Prompt"; v1 called a function that did not exist, so nothing was displayed

### [1.0.0]
- [x] Initial Release (now in `Archive/`, it was a broken copy of JPrompt)

