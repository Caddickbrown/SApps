# HTMLWriter
A simple, markdown-based Writer App contained in a single HTML File.

## Background
I wanted a simple writing app that I didn't need to install. I also wanted to be able to use it on any computer, even from a USB Drive.

## Usage
1. Download the latest release.
2. Open `HTMLWriter.html` in your browser of choice.
3. Write.
4. Copy/Export as required.
5. Enjoy!

## Features
- Themes!
- Insert Date Button
- Formatting Buttons (Bold, Italics, Underline)
- txt Export Button
- Copy Button
- Default Theme Options
- Multiple Fonts
- Line Numbers
- Word Counter

## Changing the Default Theme
To change the default theme you just need to "uncomment" out the theme you want and comment out any others within the HTML file.
- Open the HTML file in your text editor of choice.
- Hit Ctrl+F and Search for "Config"
- Find the section that lists the different options (such as "default" or "sepia")
- Comment out the themes that you don't want by putting "//" in front of them.
- Remove the "//" from the theme you would like to be your default.
- Save the file.
- Test
- Enjoy!

## Roadmap

### v4.0.0 - 

#### Added
- [ ] To Do Buttons
- [ ] Bullet Point Buttons

#### Changed

#### Fixed

- [ ] Javascript Cleanup

#### Removed

### Planned Functionality
- Focus Mode (Fading Sentences/Clear Away Options)
- SApp Standardisation
- Typewriter Mode
- Toolbar Orientation (Side/Top/Bottom)
- Mobile Optimisation
- More Themes
- Character/Sentence Counters
- Reading Time Estimate
- Word Goal
- Heading Increaser/Decreaser

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

### [3.0.0] - 2024-10-25

#### Added

- [x] Terminal Theme
- [x] Text File Upload (txt and md)
- [x] Button Border CSS Styling for all themes
- [x] Style Settings Popup Menu
- [x] Margin Width Options
- [x] Font Size Options
- [x] Version Info on Version Number click

#### Removed

- [x] Redundant Script Tags

### [2.1.0] - 2024-10-15

#### Added

- [x] Hoverable Footer
- [x] Version Number as Variable

#### Fixed

- [x] CSS Cleanup
- [x] Button Hover Colours

### [2.0.0] - 2024-10-15

#### Added

- [x] Notification Bubble Support
- [x] Line Numbers Mode
- [x] Multiple Themes
- [x] Multiple Fonts

#### Removed

- [x] Annoying Pop Up when Copying

#### Fixed

- [x] Formatting Selection Offset

### [1.1.0] - 2024-10-09

#### Added

- [x] Default Theme

### [1.0.0] - 2024-10-09

- [x] Initial Release