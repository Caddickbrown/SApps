# HTMLToDo
A simple, markdown-based ToDo App contained in a single HTML File.

## Background
I wanted a simple kanban app that I didn't need to install. This also brought up the question of "can I make a ToDo App in a similar format?"" I also wanted to be able to use it on any computer, even from a USB Drive. Additionally being able to export and import a standardised file was useful so I added that in.

## Usage
1. Download the latest release.
2. Open `HTMLToDo vx.x.x.html` in your browser of choice.
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

### [2.1.0] - 2024-12-

#### Changed

- [x] Import via File Section Prettied up
- [ ] Tab Title changes on Title Update
- [ ] Edit To Do

### Planned Functionality
- More Themes

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

### [2.0.0] - 2024-12-13

#### Added

- [x] Drag and drop reordering
- [x] "Copy to Clipboard" functionality
- [x] File upload option for imports
- [x] Editable list title
- [x] Theme settings to import/export
- [x] Notification system

#### Changed

- [x] Theme/Font Buttons instead of Drop Downs

#### Fixed

- [x] Font Selection

### [1.0.0] - 2024-12-10

#### Added

- [x] Initial Release
- [x] Add ToDos
- [x] Complete ToDos
- [x] Filtering ToDos
- [x] Flag ToDos
- [x] Delete ToDos
- [x] Export ToDos
- [x] Import ToDos
- [x] Themes

