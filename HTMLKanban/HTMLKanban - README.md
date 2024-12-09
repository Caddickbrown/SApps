# HTMLKanban
A simple, markdown-based Kanban App contained in a single HTML File.

## Background
I wanted a simple kanban app that I didn't need to install. I also wanted to be able to use it on any computer, even from a USB Drive. Additionally being able to export and import a standardised file was useful so I added that in.

## Usage
1. Download the latest release.
2. Open `HTMLKanban.html` in your browser of choice.
3. Write.
4. Copy/Export as required.
5. Enjoy!

## Features

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

### Planned Functionality
- Cleaned Up Style Menu
- Easier Dragging
- Imported File Fixes?
- More Themes
- Change Theme with Imported File
- Change App Name with Imported File
- Change Settings with Imported File
- Auto Complete in Column
- Custom CSS

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

### [1.0.0] - 2024-12-09

#### Added

- [x] Initial Release
- [x] Drag-and-drop Cards
- [x] Drag-and-drop Columns
- [x] Notification Support
- [x] Basic Themes
- [x] Settings Pop-Up
- [x] Export to and import from Markdown
- [x] Default Cards (Change in File)