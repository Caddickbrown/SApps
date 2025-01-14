# HTMLToDo
A simple, markdown-based ToDo App contained in a single HTML File.

## Background
I wanted a simple kanban app that I didn't need to install. This also brought up the question of "can I make a ToDo App in a similar format?"" I also wanted to be able to use it on any computer, even from a USB Drive. Additionally being able to export and import a standardised file was useful so I added that in.

## Usage
1. Download the latest release.
2. Open `HTMLToDo vx.x.x.html` in your browser of choice.
3. Add and use the todolist as required.
4. Copy/Export as required.
5. Enjoy!

## Features
- Add/Complete/Edit/Flag/Delete ToDos
- Export/Import ToDos/Themes/Settings
- Copy Remaining ToDos to Clipboard (With or without Completed Items)
- Edit the Title to personalise your ToDo List.
- Drag and drop reordering.
- Themes!
- Tag and Mentions highlighting.
- Search/Filters.

## Behavior
- ToDos can be edited by double clicking on them.
- To save the edit, press Enter.
- To cancel the edit, press Escape.

- Priority tasks are marked with a red flag and are always at the top of the list.
- Completed tasks are moved to the bottom of the list.

- Tags are created by using the `#` symbol. They highlight things for easier visibility/searching.
- Mentions are created by using the `@` symbol. They highlight things for easier visibility/searching.

- Search is case insensitive and searches through the entire list including tags and mentions.

- Themes are exportable/importable.

- To copy the remaining ToDos to the clipboard, click the "Copy to Clipboard" button. To only copy active tasks click the "Copy Remaining Tasks" button.
- The ToDos are copied in the order they are displayed (and the same way they are exported as a file).

- To export ToDos, click the "Export" button. The ToDos are exported in the order they are displayed.

- To reorder ToDos, click and drag the ToDo.

- To edit the list title, double click on the title.
- To save the edit, press Enter. To cancel the edit, press Escape.

- To import ToDos, click the "Import" button. You can either upload a previously exported file, or copy and paste in the text directly.

- To add a ToDo, type in the input box press Enter the ToDo is added to the bottom of the list.

### Complete
- To complete a ToDo, click the checkbox.

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

### [5.5.0] - 2025-01-

#### Changed

- [ ] Upgraded Markdown Mode so still have Menu Access
- [ ] Ticking a todo while filtered now doesn't reset the filter

### [6.0.0] - 2025-01-

#### Added

- [ ] Tips Animation
- [ ] Filter on Tags/Mentions
- [ ] Local Save (Shouldn't be relied on - but will save some data)
- [ ] Version info cards

#### Changed

- [ ] Import by File - Now a button in Menu
- [ ] UI Utilities now handled in one section
- [ ] Event Handlers now handled in one section

#### Fixed

- [ ] Version info pop up now Scrollable

#### Removed

- [ ] Import by Text - Replaced by Markdown Mode
- [ ] Import Modal

### Planned Functionality
- Favicon

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

### [5.0.0] - 2025-01-14

#### Added

- [x] Type ! at the start of ToDo to make it a Priority
- [x] Tips Cycle through in the Input Box background

#### Changed

- [x] Moved Markdown Mode button to Settings Menu

#### Removed

- [x] Number of pre-installed themes to reduce file size. (These can be re-added later on)

### [4.0.0] - 2025-01-10

#### Added

- [x] Markdown Mode (Review Current ToDos in Markdown)

#### Fixed

- [x] Editing Todo no longer resets Search

#### Removed

- [x] Excessive Comments

### [3.0.0] - 2025-01-08

#### Added

- [x] Tags
- [x] Mentions
- [x] Search
- [x] Galaxy Theme
- [x] Mint Theme

### [2.1.0] - 2025-01-07

#### Added

- [x] Tab Title changes on Title Update
- [x] Edit To Do with double click
- [x] Copy Remaining ToDos to Clipboard

#### Changed

- [x] Import via File Section Prettied up

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

