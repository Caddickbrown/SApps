# Journl
A private, offline journal editor for [jrnl](https://jrnl.sh)-style text files, in a single HTML file.

## Background
Journl grew out of **Chronolog**, a small page for reading and writing jrnl.sh entries (kept in `Archive/`). Chronolog's to-do list is where most of Journl came from: tags and mentions, search, stats, starred entries, themes, editing, and, from the `Encryption` experiment, password-protected saves. That experiment is now the main app.

## Usage
1. Open `Journl.html` in your browser of choice.
2. Type an entry and press **Enter** (Shift+Enter for a new line). The first sentence becomes the title.
3. Use #tags and @mentions. Click one to filter by it.
4. **Import/Export** to save or load files.

## Features
- Entries are remembered in this browser between visits (switch this off from the menu)
- Add, edit, delete and ★ star entries; search; four sort orders
- #tags and @mentions highlighted and click-to-filter; stats view
- **Save (encrypted)** / **Load (encrypted)**: AES-GCM with a PBKDF2 key, in a `.ejrn` file
- Import jrnl-style text (`[2025-01-02 09:30:00] Title`), paste or file. Duplicates are skipped
- Export `.txt` (jrnl format) or Markdown; copy everything to the clipboard
- 30 themes, light/dark, three fonts. Remembered between visits
- Keys: `/` focuses search, `Esc` closes menus and dialogs

## Behavior
- A jrnl entry starts with `[YYYY-MM-DD HH:MM(:SS)]`, runs until the next timestamped line, and may contain blank lines. A leading `*` marks it starred.
- "Remembering" stores your entries **unencrypted** in this browser's local storage. If that is not what you want, turn it off and use the encrypted save instead.
- Encrypted files are only as strong as the password. There is no recovery if it is lost.

## Roadmap
Carried over from Chronolog's list; ticked items are done.

- [x] Basic entry creation with timestamps, import/export, copy, search, tags and mentions, statistics, highlighting, sorting
- [x] Dark mode and themes
- [x] Local storage persistence, saved preferences
- [x] Entry editing, multiple export formats (text, Markdown), tag filtering by click
- [x] Keyboard shortcuts
- [ ] Mobile-responsive layout pass
- [ ] Markdown rendering and preview
- [ ] Tag/mention autocomplete and statistics page
- [ ] Bulk operations; entry versioning
- [ ] Activity heatmap, tag cloud, writing-time patterns

## Change Log
### [2.1.0]
#### Added
- Persistence, plain-text and Markdown export, text import, tag click-to-filter, shortcuts, empty states
#### Changed
- Encrypted files now use a random salt per file (older files still open)
- Promoted from `R&D/Encryption.html`; Chronolog and Journl v2.0.0 moved to `Archive/`
#### Fixed
- Entry text was inserted as raw HTML (script injection from an imported file)
- Importing a file you had just exported duplicated every entry; blank lines inside an entry split it in two
- Saving a large journal could crash the encryptor
- Copy and export re-sorted the live entry list

### [2.0.0] and earlier
- Journl v2.0.0 (themes, tags, stats) and Chronolog v1.0.0

## Dependencies
None. One self-contained HTML file: no frameworks, no libraries, no fonts or scripts loaded from the network.

## Contributing
If you have any ideas for features, or find any bugs, please open an issue or a pull request. I will try to respond as soon as possible.

Should you want to donate, you can do so [here](https://www.buymeacoffee.com/caddickbrown).

Thank you!

## License
This project is licensed under the MIT License. See the [LICENSE](../LICENSE) file for details.

