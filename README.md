# SApps

A collection of lightweight, portable, single-page HTML applications designed for simplicity and offline use.

## Table of Contents
- [Overview](#overview)
- [Quick Start](#quick-start)
- [Features](#features)
- [Applications](#applications)
- [Technical Details](#technical-details)
- [Development](#development)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)
- [Changelog](#changelog)

## Overview
SApps is a suite of standalone HTML applications that can perform various tasks without external dependencies. Each app is designed to be portable, offline-friendly, and usable directly from a USB drive.

## No Frameworks, No Libraries, No Dependencies, No Problem
These applications are designed to be as lightweight as possible. They do not use any frameworks, libraries, or dependencies. They are designed to be entirely self-contained and portable. They should be able to be used on any computer, from a USB drive, and should not require any installation or configuration.

There is some customisation that can be done - but this should be a one time thing and should not require any further configuration.

## Quick Start
1. Download the latest release
2. Open `index.html` in your browser
3. Pick an app

Every app also works on its own: each lives at `<App>/<App>.html`.

## Features
### Core Features
- 🚀 No installation required
- 💻 Cross-platform compatibility
- 🔌 USB drive portable
- 🌐 Offline-first: no fonts, CDNs or network calls
- 🎨 Light/dark mode, with themes in the larger apps
- 💾 Local storage for data persistence, keys namespaced `sapps.<app>.*`
- 📱 Responsive design
- 🔒 Privacy-focused (all data stays in the browser)

## Applications

| Section | App | What it does | Status |
|---|---|---|---|
| Writing | [HTMLWriter](HTMLWriter/README.md) | Distraction-free writing, nine themes | Stable |
| | [Postage](Postage/README.md) | Markdown to HTML, live preview | Stable |
| | [HTML2MD](HTML2MD/README.md) | HTML to Markdown | Stable |
| | [Glossar](Glossar/README.md) | JSON glossary editor and reader | Stable |
| | [Journl](Journl/README.md) | Encrypted offline journal | Stable |
| Productivity | [HTMLToDo](HTMLToDo/README.md) | Task management | Stable |
| | [HTMLKanban](HTMLKanban/README.md) | Kanban board | Beta |
| | [Scopr](Scopr/README.md) | Scope a project from a checklist template | Stable |
| | [Formr](Formr/README.md) | Form data to CSV (formerly WT) | Stable |
| | [Wrkot](Wrkot/README.md) | Workout log | Stable |
| | [CounTally](CounTally/README.md) | Tally counter | Stable |
| Creative | [JPrompt](JPrompt/README.md) | Journalling prompts | Stable |
| | [Algorithmix](Algorithmix/README.md) | Creative challenge generator | Stable |
| | [OSlogan](OSlogan/README.md) | Slogan generator | Stable |
| | [HTMLPicker](HTMLPicker/README.md) | Spinning-wheel picker | Stable |
| Utilities | [TabLite](TabLite/README.md) | CSV viewer and editor | Stable |
| | [JSON2CSV](JSON2CSV/README.md) | JSON to CSV | Stable |
| | [JSONGenerator](JSONGenerator/README.md) | JSON record builder | Stable |
| | [B64](B64/README.md) | Image to Base64 | Stable |
| | [Galleria](Galleria/README.md) | Base64 image gallery | Stable |
| | [Recordr](Recordr/README.md) | Microphone recorder | Stable |

Also in the repo but not on the home page: [Journaller](Journaller/README.md)
(uses CDN libraries, so not offline) and [ExApps](ExApps/README.md) (Python
scripts that need a filesystem; see [REVIEW](ExApps/REVIEW.md)).

## Technical Details

### Architecture
- Single HTML file per application, named after its folder (`Folder/Folder.html`)
- Old versions in `Archive/`, experiments in `R&D/`; the version lives in the file, not the filename
- Inline CSS and JavaScript
- LocalStorage for data persistence
- Standardized theme system across apps

### Template System
The [SAppTemplate](SAppTemplate/SAppTemplate - README.md) provides the foundation for all apps, ensuring consistency in:
- Basic structure
- Theme implementation
- Common utilities
- Error handling
- Data persistence

## Development

### Setting Up Development Environment
1. Clone the repository
```bash
git clone https://github.com/Caddickbrown/SApps.git
```
2. Choose a template
```bash
cp -r SAppTemplate/ MyNewApp/
```
3. Start developing!

### Guidelines
- Follow the single-file philosophy
- Maintain offline functionality
- Implement the standard theme system
- Include proper error handling
- Add appropriate documentation

## Contributing
Contributions are welcome! Please:
1. Fork the repository
2. Create a feature branch
3. Submit a pull request

For bugs or feature requests, please open an issue.

Support the project: [Buy Me a Coffee](https://www.buymeacoffee.com/caddickbrown)

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contact
- Website: [caddickbrown.com](https://caddickbrown.com)

## Changelog

### [4.0.0] - 2026-11
#### Added
- `index.html` home page (replaces SApp Home): search, light/dark, links to every app
- HTMLPicker (merged with Batboard), Glossar, Wrkot, Journl, JSON2CSV, CounTally, Algorithmix web app
- JSONGenerator and TabLite documented and listed

#### Changed
- Standardised layout: `Folder/Folder.html`, `README.md` per app, `Archive/` for old versions
- HTMLWriter 4.0.0 merges the Acid themes (system fonts, no Google Fonts)
- Rewritten: HTML2MD, OSlogan, Postage, Recordr, Scopr, Formr (formerly WT), JPrompt
- localStorage keys namespaced `sapps.<app>.*`, with migration from the old keys
- HTMLKanban 3.1.0 (autosave, Enter-to-confirm bug fixed); HTMLToDo 5.7.1

#### Removed
- SApp Home iframe launcher

### [1.3.0] - 2023-11-17

#### Added
- SApp Home Page

### [1.2.0] - 2023-10-27

#### Added
- ExApps

### [1.1.0] - 2023-10-16

#### Added
- Changelog
- Contact Details

#### Changed
- Updated SApp READMEs to include SApp Names for clarity.

### [1.0.0]
- Initial Release

