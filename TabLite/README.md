# TabLite
A lightweight CSV viewer and editor contained in a single HTML file.

## Background
I wanted to open, tidy and sanity-check a small CSV file without reaching for a spreadsheet application. TabLite loads a CSV, lets you edit it in place, checks each column against a simple schema, and exports it again.

## Usage
1. Download the latest release.
2. Open `TabLite.html` in your browser of choice.
3. Choose a CSV file, or press **Import** and paste CSV text.
4. Edit cells, sort by clicking a header, search with the search box.
5. (Optional) Press **Configure Schema** to set a type for each column. Cells that fail their type are outlined in red.
6. Export with **Export CSV**, **Export MD** or **Copy**.

## Features
- Open a CSV file or paste CSV text
- Edit cells in place; **Add Record** appends a blank row
- Click a column header to sort (ascending, then descending)
- Live search across every column
- Per-column schema validation: Text, Number, Currency, Email, Date (YYYY-MM-DD), Time (24hr), Required
- Export as CSV, as Markdown (CSV with a small front matter block holding the theme, mode and font), or copy to the clipboard
- Importing a Markdown export restores its theme settings
- Six themes (Default, Sepia, Cool, Terminal, GX, Honey Bee), each with light and dark mode, and three fonts
- Theme and font are remembered (`sapps.tablite.theme`, `sapps.tablite.font`)
- Table data is **not** stored: it lives in the page until you close or reload it

## Roadmap

### Planned Functionality
- Optional autosave of the table (local storage)
- Delete record and add/remove column
- Multi-line cells (needs a fuller CSV parser)
- Persist the schema alongside the data

## Dependencies
I try to reduce the dependencies as much as possible, but some may be necessary for the functionality of the application.

Should I find a way to remove them, I will, but for development speed they may be required in the interim.

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

- [x] Version number in the footer
- [x] Export CSV button
- [x] Importing a Markdown export restores its theme, mode and font
- [x] README

#### Changed

- [x] File renamed from `tablite-complete.html` to `TabLite.html`
- [x] Local storage keys renamed to `sapps.tablite.theme` and `sapps.tablite.font` (old keys migrate automatically)
- [x] Search runs on every input event, not just key presses
- [x] Edited cells keep what was typed and are flagged if invalid, instead of silently reverting in the data
- [x] Text sorting is case-insensitive; the sort arrow survives a re-render

#### Fixed

- [x] Unclosed `div` around the table
- [x] Exported CSV now quotes cells containing quotes or line breaks, not only commas
- [x] The font setting was written but never read back
- [x] Column names containing quotes or angle brackets no longer break the schema dialog
- [x] Short rows are padded so every row has a cell per header
