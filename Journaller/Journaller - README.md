# Journaller

A Simple, HTML Based, Journal Entry Generator/Editor - designed to be fully featured in a single page.

## Background
I wanted to start journaling, but I didn't want to use a physical journal. I wanted to be able to export my entries to a format that I could use in other applications. I also wanted to be able to use it on any computer, even from a USB Drive.

## Usage
1. Download the latest release.
2. Open `Journaller.html` in your browser of choice.
3. Fill out the form.
4. Choose your export option.
5. Enjoy your exported file(s)!

## Features
- Date/Titles/Tags
- Various Export Options
- Dark/Light Mode
- Journal Prompts
- Clean Design
- 45+ Prompts

### Export Options
- CSV
- JSON
- Markdown
- Zip Folder (All of the above)
- Clipboard (In Markdown)

## Roadmap

### v5.0
- [ ] Daily Gratitude Section
- [ ] HTML Export
- [ ] Removal of FileSaver.js as dependency
- [ ] Removal of JSZip.js as dependency
- [ ] JSON Tags saved in array
- [ ] Image Attacher
- [ ] Cleaner Aesthetics
- [ ] Save As Fix?
- [ ] Fonts as Variable
- [ ] Themes

### Planned Functionality
- Themes
- Fonts
- Dynamically Generated Form
    - Not really sure how this would work realistically
    - Headers?
    - Benefit would be to me not typing out the titles and where they go later on
- Image Attacher
- Mood Option
    - With Tags?
- Separate Prompt section in main form with extra section exported?
- More Prompts
- Easily Configurable Default Theme
- PDF Export
- Word Counter

## Dependencies
I try to reduce the dependencies as much as possible, but some are necessary for the functionality of the application.

Should I find a way to remove them, I will, but for development speed they may be required in the interim.

### Current Dependencies
- FileSaver.js
- JSZip.js

## Contributing
If you have any ideas for features, or find any bugs, please open an issue or a pull request. I will try to respond as soon as possible.

Should you want to donate, you can do so [here](https://www.buymeacoffee.com/caddickbrown).

Thank you!

## License
This project is licensed under the MIT License.

## Change Log
### [4.0.0] - 2023-10-30

#### Added 

- More Prompts

#### Changed

- Aligned with SAppTemplate v2.1.1

#### Removed

- Material Icons as dependency
- Playfair Display Font as dependency


### [3.0.1] - 2023-10-29

#### Changed

- Updated Folder Names to fall in line with SAppTemplate

### [3.0.0]
- [x] Fixed Dark Mode button hover behavior
- [x] Added Export to Zip
- [x] Tags Field
- [x] CSS Tidy up
- [x] Better Colours (Kind of)
- [x] Dynamic Resize Textbox
- [x] Widened Form
- [x] Added Version Number
- [x] Added GitHub Link
- [x] Added Beginner "Journaller" Logo
- [x] Adjusted Export Button Placement
- [x] Adjusted Textbox Size

### [2.0.0]
- [x] Journal Prompts
- [x] More Colour
- [x] Colours as Variables
- [x] Comments Cleanup
- [x] Current Time included in export name
- [x] Textbox Font updated
- [x] Footer Added
- [x] Textbox Border Added
- [x] Spaced out Markdown Export

### [1.0.0]
- [x] Date/Titles
- [x] Export to Markdown
- [x] Export to CSV
- [x] Export to JSON
- [x] Export to Clipboard
- [x] Dark/Light Mode