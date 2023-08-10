# WT
WT is a small HTML based project to create a form that can have it's data exported to CSV.

It can be configured by editing the variables at the start of the Javascript Section, and will expand to however many fields you require.

It is designed to be completely self-reliant and customisable. The app is designed to be as lightweight as possible.

It currently only supports number fields, but I will be adding more field types in the future.

## Background
I wanted a quick way to create a simple HTML form that could be exported to CSV. I couldn't find anything that fit my needs, so I made my own.

## Usage
1. Download the latest release.
2. Configure the form in the HTML in your text-editor of choice.
3. Open `WT_vx.x.html` in your browser of choice.
4. Fill out the form.
5. Click the export button.
6. Enjoy your exported file!

## Features
- Customisable Field Names
- Customisable number of fields from internal JS
- Customisable Theme from internal CSS
- Export to CSV
- Customisable Exported file name
- Customisable App Name

## Configuration
To configure the form, edit the variables at the start of the Javascript section.

- The "App Name" is defined in the `appName` variable. Functionally this doesn't do anything, but you can change it to suit your needs.
- The Exported File Name is defined in the `FileName` variable. This is the name of the file that will be downloaded when the user clicks the "Export" button.
- The form fields are defined in the `fields` array.

### Themeing
Should you want to change the theme, you can do so by editing the CSS variables in the `:root` section.

## Future
### v2.0
- [x] Dark Mode
- [ ] Customisable fields from within the page
- [ ] Standardised Theming
- [x] Default Theme Preparation

### v3.0
- [ ] Cleaner Aesthetics
- [ ] Field Types
- [ ] Remove Fields from within the page

### v4.0
- [ ] Themes
- [ ] Default Theming Options

### Planned Functionality
- TBC

## Dependencies
I try to reduce the dependencies as much as possible, but some may be necessary for the functionality of the application.

Should I find a way to remove them, I will, but for development speed they may be required in the interim.

### Current Dependencies
- None

## Contributing
If you have any ideas for features, or find any bugs, please open an issue or a pull request. I will try to respond as soon as possible.

Should you want to donate, you can do so [here](https://www.buymeacoffee.com/caddickbrown).
Thank you!

## License
This project is licensed under the MIT License.

## Change Log
## v1.0
- [x] Customisable Field Names
- [x] Customisable number of fields from internal JS
- [x] Customisable Theme from internal CSS
- [x] Export to CSV
- [x] Customisable Exported file name
- [x] Customisable App Name