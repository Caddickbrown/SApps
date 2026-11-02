# Scopr
A scoping tool: tick the work that's in scope, get an estimate and a ready-made Markdown to-do list.

## Background
I created this to scope out projects. A tickbox template is a fast way to say "we're doing these things, not those", and the result should drop straight into a task list.

## Usage
1. Open `Scopr.html` in your browser of choice.
2. Give the project a name and tick the tasks that are in scope (tick a section heading to tick the whole section).
3. Watch the estimated total update. The list on the right is a Markdown checklist.
4. **Copy** it or **Download .md**.

### Making your own template
Click **Edit template**. The format is plain text:

```
# Section name
- Task name | 4
- Another task | 2.5
```

`#` starts a section, `-` adds a task, and the number after `|` is the estimate in hours (optional). **Apply** saves it; **Reset to default** restores the example.

## Features
- Editable template, saved in your browser
- Ticks, project name and open/closed sections are remembered
- Per-section and overall estimates
- Markdown checklist output (`- [ ] Task (4h)`), copy or download
- Light/Dark mode (remembered)

## Data
Stored in `localStorage` under `sapps.scopr.*`. Clearing site data resets it.

## Roadmap
### Planned Functionality
- [ ] Multiple saved templates
- [ ] Day-rate / cost totals
- [ ] CSV export

## Dependencies
I try to reduce the dependencies as much as possible. Everything is inline; the app works offline from a single file.

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
### [1.0.0]
#### Added
- Editable template with estimates, section totals, Markdown checklist output, copy and download
- Saved state, light/dark mode

#### Fixed
- v0.1 exported checkbox *input names* ("task1") instead of the task text
- Ticking a sub-task could tick the wrong parent; the parent-ticking logic was removed in favour of explicit section ticks

### [0.1.0] - 2023-11-22
- Initial Release (Proof of Concept, now in `Archive/`)

