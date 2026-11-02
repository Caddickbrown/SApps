# Wrkot
A daily workout log in a single HTML file.

## Background
Wrkot began as a form that could remember one workout and copy it out as a line of CSV. It now keeps a full history, with weekly stats and a proper CSV round trip, so the log can live in a spreadsheet when you want it to.

## Usage
1. Open `Wrkot.html` in your browser of choice.
2. Pick a date, enter the workout type, minutes and any notes, then **Save workout**.
3. Download or copy the CSV whenever you want a backup.

## Features
- Unlimited history, newest first; edit or delete any entry
- Summary: sessions and minutes in the last 7 days, current day streak, total sessions
- Minutes-by-type bars; search and date-range filters
- Workout types autocomplete from your history
- **Download CSV**, **Copy CSV**, **Copy without header**
- **Import CSV** (merges, skips duplicates). Reads the old 3-column Wrkot export too
- Light / Dark / Sepia / Terminal themes

## CSV format
`Date,Workout Type,Duration (minutes),Notes`. Fields containing commas, quotes or line breaks are quoted correctly. Notes that begin with `=`, `+`, `-` or `@` get a leading `'` so spreadsheets do not run them as formulas; the import removes it again.

## Behavior
- Data lives in this browser only (`sapps.wrkot.data`). Clearing site data erases it, so export now and then.
- A workout saved by v1 (`workoutData`) is migrated into the log automatically, once.

## Roadmap
### Planned Functionality
- Distance / weight fields
- Weekly goal
- Calendar view

## Change Log
### [2.0.0]
#### Added
- Full history, stats, edit/delete, filters, CSV import and download, themes
#### Fixed
- Saving threw an error (the page looked for an element that did not exist)
- Each save overwrote the previous workout
- CSV broke on notes containing commas or line breaks
- Imported and saved text was inserted as raw HTML
#### Changed
- localStorage key `workoutData` → `sapps.wrkot.data` (migrated)

## Dependencies
None. One self-contained HTML file: no frameworks, no libraries, no fonts or scripts loaded from the network.

## Contributing
If you have any ideas for features, or find any bugs, please open an issue or a pull request. I will try to respond as soon as possible.

Should you want to donate, you can do so [here](https://www.buymeacoffee.com/caddickbrown).

Thank you!

## License
This project is licensed under the MIT License. See the [LICENSE](../LICENSE) file for details.

