# SAppTemplate
A Template Repo for Single Page Apps.

## Background
As I built more SApps, I found that I needed a template that gave me basic functionality to all of the different SApps. Dark Mode being a good example, where the code and functionality should be the same and standardised. I created this template repo to help me get started with new projects.

An SApp Template Update could be akin to an "OS" Update. It will bring new features and functionality to all SApps easily.

## Usage
This repo is a template repo, so you can use it to create a new repo with all of the files and folders in this repo. It can then be edited to create the actual SApp Page.

The SApp Template Version also tells me something about what functionality the SApp has and what needs patching in.

## Features
- Dark/Light Mode
- Colours as Variables
- Page Name as Variable
- Version Number as Variable
- Default Light/Dark Mode
- Standardised Footer

## Roadmap

### Planned Functionality
- Multiple Themes
- Simplification
- Bug Fixes

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

### [2.1.1] - 2023-10-30

#### Changed

- Version Number now only requires the number and not the "v" at the start.
- Moved Template Variable to Custom Section as is dependent on SApp Update version

#### Removed
- Extra Spacing in Notifications code

### [2.1.0] - 2023-10-29

#### Changed

- Changed Dark/Light Mode Toggle Button Text to Embedded Icons (Lucide Icons)
- Toggle Button CSS to account for Icon
- Archive Now contains latest version of the SApp Template - will be updated with each new version

#### Fixed

- Hidden Notification was blocking Dark Mode Toggle Button - Fixed by adding a changing z-index to the Notification

### [2.0.0] - 2023-10-29

#### Added

- Default Light/Dark Mode
- Template Version added
- Notification Pop Up Functionality
- Template Button
- Standardised "Default" CSS Sections/Functions
- Standardised "Custom" CSS Sections/Functions
- Standardised "Default" Script Sections/Functions
- Standardised "Custom" Script Sections/Functions

#### Changed

- Version Number now has 3 digits to account for Bug Fixes, Minor, and Major Updates
- Dark/Light Mode Variables Simplified
- Dark/Light Mode Toggle Hover Colours
- R&D Version now named with R&D in the name

#### Removed

- CSS Toggle Button Hover Colour Variables
- Version number in Main File Name - to allow for easier change reviewing

### [1.0.0]
- [x] Initial Release