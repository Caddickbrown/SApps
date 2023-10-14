# SApps
SApps is a project of a collection of simple, lightweight Single-Page HTML Applications that can perform various tasks and functions. They are portable, do not use any dependencies (where possible), are offline-friendly, and are able to be stored and used from a USB Drive.

They have entirely inline CSS and Javascript, and are designed to be entirely self-reliant with no external requirements. They should be consistent in formatting and should not have "quirks" unique to an app. 

Each SApp should have its own README.md file that details the usage and features of the application. This README.md file is for the SApps project as a whole.

## Background
I started off experimenting in looking at a way to make a journalling app that was portable and could export to various formats. Soon realising that I could use a similar format for other applications that could be used for various tasks. From here I began standardising the format and creating a template that could be used for all of the applications.

## Usage
1. Download the latest release of the relevant application.
2. Open the HTML file in your browser of choice.
3. Use the application.

## Features
- No installation required
- Works on any computer
- Works from a USB Drive
- Offline Friendly
- Dark/Light Mode

## SAppTemplate
SApp Template is a template for creating new SApps. It contains the basic structure and functionality that I use for all of my SApps. It is designed to be a starting point for new SApps. It is not designed to be used as an application itself.

It is designed to be copied and renamed, and then modified to suit the needs of the new application.

Each SApp will be updated to the latest version of the template as and when I update them. This will bring in line default functionality and features (such as Dark Mode or formatting) to all SApps.

## Apps
### Journaller
Journaller allows you to write journal entries and export them to various formats.

### JPrompt
JPrompt generates a random journal prompt on command.

### WT
WT is a small HTML based project to create a form that can have its data exported to CSV.

It can be configured by editing the variables at the start of the Javascript Section, and will expand to however many fields you require.

### Postage
Postage allows you to write in Markdown and export to a standardised HTML format.

### OSlogan
OSlogan generates a random slogan on command. These were originally designed to be used as "Offensive" T-shirt slogans, but can be used for anything.

### HTML2MD
HTML2MD converts an HTML page to Markdown.

### Algorithmix
Algorithmix is slightly different to the other SApps. It was originally an idea to make a random creative prompt generator. Thiswas tightly crontrolled but vague enough for you to make it creative. It was designed to be used for writing, drawing, or any other creative endeavour. This project has been brought into the SApps project though as it would work well in this format.

It does contain the "App" in Python and C++ though as this was an older application prior to the SApp project.

## Dependencies
I try to reduce the dependencies as much as possible, but some may be necessary for the functionality of the application.

Should I find a way to remove them, I will, but for development speed they may be required in the interim.

## Contributing
If you have any ideas for features, or find any bugs, please open an issue or a pull request. I will try to respond as soon as possible.

Should you want to donate, you can do so [here](https://www.buymeacoffee.com/caddickbrown).

Thank you!

## License
This project is licensed under the MIT License.