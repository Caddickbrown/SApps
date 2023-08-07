# WT
WT is a small HTML based project to create a form that can have it's data exported to CSV.

It can be configured by editing the variables at the start of the Javascript Section, and will expand to however many fields you require.

It is designed to be completely self-reliant and customisable. It does not require any external libraries or frameworks. It is also designed to be as lightweight as possible.

It currently only supports number fields, but I will be adding more field types in the future.

## v1.0 Functionality
- [x] Customisable number of fields from internal JS
- [x] Customisable Theme from internal CSS
- [x] Export to CSV


## Configuration
To configure the form, edit the variables at the start of the Javascript section.

- The "App Name" is defined in the `appName` variable. Functionally this doesn't do anything, but you can change it to suit your needs.
- The Exported File Name is defined in the `FileName` variable. This is the name of the file that will be downloaded when the user clicks the "Export" button.
- The form fields are defined in the `fields` array.

### Themeing
Should you want to change the theme, you can do so by editing the CSS variables in the `:root` section.

## Future
### Planned Functionality
- Customisable fields from within the page
- Field Types
- Remove Fields from within the page
- Dark Mode

## Contributing
If you have any suggestions or improvements, please feel free to submit a pull request. I will review it as soon as possible.

Should you wish to donate to the project, you can do so [here](https://www.buymeacoffee.com/caddickbrown).
Thank you!