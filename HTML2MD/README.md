# HTML2MD
A single-page HTML app that converts HTML into Markdown, entirely in your browser.

## Background
I wanted a quick way to turn saved web pages and snippets into Markdown for notes without installing anything or sending content to a website. It's the reverse of [Postage](../Postage/README.md).

## Usage
1. Open `HTML2MD.html` in your browser of choice.
2. Paste HTML into the left box, or click **Open HTML file…**.
3. The Markdown appears on the right as you type.
4. Click **Copy Markdown** or **Download .md** (the file takes the name of the uploaded file).

## Features
- Live conversion (paste or open a file)
- Uses the browser's own HTML parser, so messy or partial HTML is fine
- Converts: headings, paragraphs, **bold**, *italic*, ~~strikethrough~~, links, images, inline code, code blocks (with language hint), nested bullet and numbered lists, blockquotes, horizontal rules, line breaks and tables
- Drops `<script>`, `<style>`, `<head>` and other non-content
- Copy to clipboard and download as `.md`
- Light/Dark mode (remembered)

## Known Limits
- Tables with merged cells (`colspan`/`rowspan`) are flattened
- Inline `style` and CSS classes are ignored, as Markdown has no equivalent
- Raw HTML with no Markdown equivalent is reduced to its text

## Roadmap
### Planned Functionality
- [ ] Option to keep unsupported tags as raw HTML
- [ ] Fetch-free "clean up a whole page" mode (strip nav/footer)

## Dependencies
I try to reduce the dependencies as much as possible. Everything is inline; the app works offline from a single file.

### Current Dependencies
- None

### Previous Dependencies
- Regex-only converter

## Contributing
If you have any ideas for features, or find any bugs, please open an issue or a pull request. I will try to respond as soon as possible.

Should you want to donate, you can do so [here](https://www.buymeacoffee.com/caddickbrown).

Thank you!

## License
This project is licensed under the MIT License.

## Change Log
### [2.0.0]
#### Changed
- Rewritten around the browser's HTML parser (v1 used regular expressions and only handled a handful of tags)
- Paste input as well as file upload; conversion is live (the artificial 2-second delay is gone)
- Light/Dark mode, SApps house style

#### Added
- Ordered and nested lists, tables, code blocks, blockquotes, images, horizontal rules, strikethrough

#### Fixed
- Files whose `<body>` tag carried attributes, or with no `<body>`, were not converted

### [1.0.0]
- Initial Release (now in `Archive/`)

