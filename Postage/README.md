# Postage
Postage is a single-page HTML app that turns Markdown into a standalone HTML page, with a live preview.

## Background
I wanted a quick way to create a simple HTML page from Markdown without a build step or an install.

## Usage
1. Open `Postage.html` in your browser of choice.
2. Type or paste Markdown on the left, or click **Open .md file…**. The preview updates as you type.
3. Click **Export HTML** for a standalone `converted.html` (light/dark aware, no external files), or **Copy HTML** for just the body markup.

Try it with [`Examples/Sample.md`](Examples/Sample.md), a small file that exercises headings, bold and italics.

## Features
- Live preview, remembered draft
- Headings (h1-h6), paragraphs, **bold**, *italics* (`*` and `_`), ~~strikethrough~~, `inline code`
- Links and images
- Bulleted, numbered, nested and task lists (`- [x]`)
- Blockquotes, fenced code blocks (with language class), tables, horizontal rules
- Raw HTML in the input is escaped, and `javascript:` links are neutralised
- Light/Dark mode (remembered)

## Roadmap
### Planned Functionality
- [ ] Customisable export template/CSS
- [ ] Footnotes
- [ ] Reference-style links

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
#### Changed
- Rewritten with a proper block parser (v1 relied on line-by-line regular expressions, so every list item became its own list and every newline a `<br>`)
- Live preview alongside the editor

#### Added
- Blockquotes, code blocks, tables, ordered lists, task lists, nested lists, links, images, strikethrough, horizontal rules

### [1.1.1]
- Previous stable release (now in `Archive/`)

