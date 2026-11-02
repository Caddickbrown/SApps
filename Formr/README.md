# Formr
*(Formerly WT.)* A small HTML app for building a quick data-entry form and exporting what you enter as CSV.

## Background
I wanted a fast way to make a simple form, fill it in over and over, and get a spreadsheet-ready file. I couldn't find anything that fit, so I made my own. Originally called WT.

## Usage
1. Open `Formr.html` in your browser of choice.
2. Under **Fields**, type a name, choose Number or Text, and press Enter / **Add field**. Remove a field with its ×.
3. Fill in the **Entry** form and press **Add entry**. Repeat.
4. **Export CSV** downloads every entry (`YYYY-MM-DD-<file name>.csv`). Change the file name next to the button.

## Features
- Fields are added in the page; no code editing needed
- Number and text fields
- Many entries per file, with a table to review and remove them
- Correct CSV quoting (commas and quotes in values are safe)
- Everything is remembered in your browser (`sapps.formr.*`)
- Light/Dark mode (remembered)

## Roadmap
### Planned Functionality
- [ ] Drag to reorder fields
- [ ] More field types (date, tick box, choice)
- [ ] Import an existing CSV

## Dependencies
I try to reduce the dependencies as much as possible. Everything is inline; the app works offline from a single file.

### Current Dependencies
- None

### Previous Dependencies
- Icon font reference in the v2.0 draft (never loaded)

## Contributing
If you have any ideas for features, or find any bugs, please open an issue or a pull request. I will try to respond as soon as possible.

Should you want to donate, you can do so [here](https://www.buymeacoffee.com/caddickbrown).

Thank you!

## License
This project is licensed under the MIT License.

## Change Log
### [3.0.0]
#### Changed
- Renamed from WT to Formr
- Fields are configured in the page rather than by editing the JavaScript
- Multiple entries per export (was a single row)

#### Fixed
- Empty fields were exported as 0
- Values containing commas or quotes broke the CSV
- The v2.0 draft referenced icon fonts that were never loaded and overwrote its own field-creation code

### [2.0.0] (draft)
- Tag-style field entry; never finished (now in `Archive/`)

### [1.0.0]
- Initial Release as WT (now in `Archive/`)

