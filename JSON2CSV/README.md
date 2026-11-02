# JSON2CSV
Convert JSON to CSV in your browser. Nothing is uploaded.

## Background
This began as a 30-line Python script (`ExApps/JSON2CSV/json2csv.py`) that needed a desktop file picker and broke on anything but a flat list of identical objects. As a single page it handles real-world JSON and works anywhere.

## Usage
1. Open `JSON2CSV.html` in your browser of choice.
2. Paste JSON, drop a `.json` file onto the left box, or press **Try a sample**.
3. Adjust the options. The CSV and a preview table update as you go.
4. **Download .csv** or **Copy**.

## Features
- Arrays of objects, a single object, an object of objects (`{"id1": {...}}`, the key becomes a `_key` column), arrays of plain values, and **JSON Lines**
- Wrapper objects such as `{"data": [...]}`: the array is found for you, with a picker if there are several
- Columns are the union of every key, in first-seen order; missing values stay empty
- **Flatten nested objects** to `address.city`; arrays can be joined with "; ", kept as JSON, or split into `tags[0]`, `tags[1]`
- Delimiter: comma, semicolon, tab or pipe; optional header, optional quote-everything
- Excel-friendly UTF-8 BOM; spreadsheet-formula defuse (cells starting `=`, `+`, `-`, `@`)
- Errors report line and column
- Light / Dark / Sepia / Terminal themes

## Behavior
- Only your option choices are remembered (`sapps.json2csv.options`). Your data never is.
- Line breaks inside values are preserved inside quoted cells; rows end with CRLF.

## Roadmap
### Planned Functionality
- CSV → JSON
- Column picker, rename and reorder
- Convert large files without freezing the page

## Change Log
### [1.0.0]
#### Added
- Browser version of `ExApps/JSON2CSV` with the features above

## Dependencies
None. One self-contained HTML file: no frameworks, no libraries, no fonts or scripts loaded from the network.

## Contributing
If you have any ideas for features, or find any bugs, please open an issue or a pull request. I will try to respond as soon as possible.

Should you want to donate, you can do so [here](https://www.buymeacoffee.com/caddickbrown).

Thank you!

## License
This project is licensed under the MIT License. See the [LICENSE](../LICENSE) file for details.

