# JSONGenerator
A form that builds JSON records for a collection of quotes, excerpts, lessons, tips and insights, so they can be pasted into a larger JSON file.

## Background
I keep a growing JSON file of things worth remembering. Writing the records by hand meant typos, duplicate IDs and inconsistent fields, so this form does it for me.

## Usage
1. Open `JSONGenerator.html` in your browser of choice.
2. On **Add Content** choose the type (Quote, Lesson, Excerpt, Tip or Insight), set the ID number, pick (or add) an author and fill in the text, source, date and tags.
3. Click **Generate JSON**, then **Copy to Clipboard**.
4. On **Add Author**, enter an author ID and name (plus categories) to generate an author record.

## Features
- Five content types; Excerpt and Lesson show extra fields (work title/series/type/characters; source experience and applicability)
- IDs are prefixed by type and zero-padded (`Q0001`)
- Author dropdown with a built-in list, or add a new author inline
- Tag and category entry (type, press Enter)
- "Today" button for the date
- Works offline, no dependencies

## Notes
- The built-in author list lives in the `authorData` array near the top of the script. Edit it to match your own file.
- The page does not remember what you entered; copy the output as you go.

## Roadmap
### Planned Functionality
- [ ] Remember the last ID used
- [ ] Load an existing JSON file to pick authors and the next free ID
- [ ] Light/Dark mode

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
- Documented (the app has been in the repo without a README); version number added to the page footer

