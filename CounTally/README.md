# CounTally
A tally counter with a history, for phone or desktop. One HTML file.

## Background
I wanted a simple tally counter for my phone and computer without writing an iPhone app. The original version was a single counter and a Python script that generated report pages (kept in `ExApps/CounTally`). The planned features from that README (change by any amount, edit the count, several counters, daily to yearly totals, reports, themes) are now in one offline page.

## Usage
1. Open `CounTally.html` in your browser of choice. On a phone, add it to your home screen.
2. Press **+** and **−**, or tap the number to type one.
3. Switch the **Step** to count in 5s, 10s or any size.
4. Add more counters with **New counter**.

## Features
- Several named counters, each with its own daily history
- Count up or down by 1, 5, 10 or a custom step; type a value; reset today; **Undo**
- A note for each day
- Summary: this week, month, year, all time, average per active day, best day
- 14-day bar chart; totals by day, week (ISO), month or year
- **Export CSV** (`Date, Counter Name, Tally, Notes`) and **Import CSV**, which overwrites matching days
- Keys: `+` / `↑` / Space add, `-` / `↓` subtract, `z` undo
- Light / Dark / Sepia / Terminal themes

## Behavior
- Counts are stored in this browser (`sapps.countally.state`). The CSV is your backup and your way between devices.
- Days follow your local midnight; weeks start on Monday.

## Roadmap
### Planned Functionality
- Daily goals and streaks
- Counter colours
- Shared backup between devices

## Change Log
### [1.0.0]
#### Added
- Everything above. Replaces the single-counter page in `ExApps/CounTally`

## Dependencies
None. One self-contained HTML file: no frameworks, no libraries, no fonts or scripts loaded from the network.

## Contributing
If you have any ideas for features, or find any bugs, please open an issue or a pull request. I will try to respond as soon as possible.

Should you want to donate, you can do so [here](https://www.buymeacoffee.com/caddickbrown).

Thank you!

## License
This project is licensed under the MIT License. See the [LICENSE](../LICENSE) file for details.

