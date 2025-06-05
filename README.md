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

There is some customisation that can be done - but this should be a one time think and should not require any further configuration.

## Quick Start
1. Download the latest release
2. Open `SApp Home/SApp Home.html` in your browser
3. Select any app from the launcher

## Features
### Core Features
- 🚀 No installation required
- 💻 Cross-platform compatibility
- 🔌 USB drive portable
- 🌐 Offline-first design
- 🎨 Unified theme system (Light/Dark/Sepia/Terminal)
- 💾 Local storage for data persistence
- 📱 Responsive design
- 🔒 Privacy-focused (all data stored locally)

### Browser Compatibility
- Chrome (Recommended)
- Firefox
- Edge
- Safari

## Applications

### Writing & Documentation
| App | Description | Status |
|-----|-------------|---------|
| [HTMLWriter](HTMLWriter/README.md) | Distraction-free writing environment | Stable |
| [Journaller](Journaller/README.md) | Journal entry management and export | Stable |
| [Postage](Postage/README.md) | Markdown to HTML converter | Stable |

### Productivity
| App | Description | Status |
|-----|-------------|---------|
| [HTMLToDo](HTMLToDo/README.md) | Task management system | Stable |
| [HTMLKanban](HTMLKanban/README.md) | Visual project management | Beta |
| [WT](WT/README.md) | Form data to CSV exporter | Stable |

### Creative Tools
| App | Description | Status |
|-----|-------------|---------|
| [JPrompt](JPrompt/README.md) | Journal prompt generator | Stable |
| [OSlogan](OSlogan/README.md) | Random slogan generator | Stable |
| [Algorithmix](Algorithmix/README.md) | Creative prompt generator | Beta |

### Utilities
| App | Description | Status |
|-----|-------------|---------|
| [HTML2MD](HTML2MD/README.md) | HTML to Markdown converter | Stable |
| [Galleria](Galleria/README.md) | Base64 image gallery | Stable |
| [Recordr](Recordr/README.md) | Simple audio recorder | Beta |

## Technical Details

### Architecture
- Single HTML file per application
- Inline CSS and JavaScript
- LocalStorage for data persistence
- PostMessage API for inter-app communication
- Standardized theme system across apps

### Template System
The [SAppTemplate](SAppTemplate/README.md) provides the foundation for all apps, ensuring consistency in:
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

