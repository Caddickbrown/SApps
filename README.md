# Postage
Postage is a Single-Page HTML App that generates an HTML page from a Markdown-based input form.

The user enters markdown text into an input box and the app generates an HTML page from the input.

The export uses a basic template, but this will be customisable in the future. The app is designed to be as lightweight as possible.

## Background
I wanted a quick way to create a simple HTML page from a template and markdown input. I couldn't find anything that fit my needs, so I made my own.

## Usage
1. Download the latest release.
2. Open `Postage_vx.x.html` in your browser of choice.
3. Fill out the form.
4. Click the export button.
5. Enjoy your exported file!

## Features
- Converts Headings (h1-h6)
- Converts **bold**
- Converts *italics* and _italics_ (Asterisk and Underscore)
- Converts lists
- Converts line breaks
- Export to HTML
- Variable App Name

### v2.0
- [ ] Default Theme Preparation
- [ ] Convert __bold__ (Underscore)
- [ ] Convert ~~strikethrough~~
- [ ] Convert [links]()
- [ ] Convert `code`

## Future
### Planned Functionality
- Cleaner Look
- Dark Mode
- Default Theme
- Custom Themes
- CSS as a Variable (Copies down to the export)

#### Planned Conversion Capabilities
- Convert ***bold and italic***
- Convert > blockquotes
- Convert images
- Convert horizontal rules
- Convert tables
- Convert inline HTML
- Convert paragraphs
- Convert code blocks
- Convert fenced code blocks
- Convert blockquotes
- Convert ordered lists
- Convert task lists and to-dos
- Convert footnotes
- Convert definition lists
- Convert abbreviations
- Convert citations
- Convert subscript
- Convert superscript

### Export Options
- HTML

## Dependencies
I try to reduce the dependencies as much as possible, but some may be necessary for the functionality of the application.

Should I find a way to remove them, I will, but for development speed they may be required in the interim.

### Current Dependencies
- None!

## Contributing
If you have any ideas for features, or find any bugs, please open an issue or a pull request. I will try to respond as soon as possible.

Should you want to donate, you can do so [here](https://www.buymeacoffee.com/caddickbrown).
Thank you!

## License
This project is licensed under the MIT License.

## Change Log
### v1.1
- [x] Adjusted Styling
- [x] Added Variable App Name

### v1.0
- [x] Converts Headings (h1-h6)
- [x] Converts **bold**
- [x] Converts *italics* and _italics_ (Asterisk and Underscore)
- [x] Converts unordered lists
- [x] Converts line breaks
- [x] Export to HTML
