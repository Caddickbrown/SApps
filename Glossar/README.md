# Glossar
A JSON-driven guidebook: sections, subsections and searchable items, in a single HTML file.

## Background
Glossar started as a rough template for a glossary or "article index" page: headings, subheadings and a list of items from a bit of JSON. It is now a small editor and reader, useful for glossaries, FAQs, cheat sheets, reading lists and field guides.

## Usage
1. Open `Glossar.html` in your browser of choice. It opens on a short sample guidebook that explains itself.
2. Use **Edit data…** to replace the JSON with your own, then **Apply**.
3. Browse by section, or search everything from the box (press `/`).

## Data format
```json
{
  "title": "My guide",
  "sections": [
    { "heading": "Section", "subheadings": [
      { "subheading": "Subsection", "items": [
        "A plain item",
        { "title": "An item", "text": "Optional description.", "link": "https://example.com" }
      ]}
    ]}
  ]
}
```
Items may be strings or objects. Only `http(s)` links are shown.

## Features
- Sidebar tree, overview tiles, breadcrumbs, and shareable deep links (`#s=1&u=0`)
- Live search over every title and description, with highlighting
- In-page JSON editor with validation that says what is wrong and where
- Load and download JSON; export the whole guide as Markdown; print-friendly layout
- Light / Dark / Sepia / Terminal themes

## Behavior
- Data is saved in this browser only (`sapps.glossar.data`). Download the JSON to keep or move it.
- Content is always treated as text, never HTML.

## Roadmap
### Planned Functionality
- Form-based editing (no raw JSON)
- Tags on items
- Import from Markdown

## Change Log
### [1.0.0]
#### Added
- Search, editor, import/export, Markdown export, deep links, themes, sample guidebook
#### Changed
- Promoted from `R&D` (the rough template is kept in `Archive/`)

## Dependencies
None. One self-contained HTML file: no frameworks, no libraries, no fonts or scripts loaded from the network.

## Contributing
If you have any ideas for features, or find any bugs, please open an issue or a pull request. I will try to respond as soon as possible.

Should you want to donate, you can do so [here](https://www.buymeacoffee.com/caddickbrown).

Thank you!

## License
This project is licensed under the MIT License. See the [LICENSE](../LICENSE) file for details.

