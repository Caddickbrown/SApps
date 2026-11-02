# Recordr
A simple microphone recorder that runs in a web browser.

## Background
I wanted to make a quick voice recording on any computer without installing software, and then keep the file for use in other applications.

## Usage
1. Open `Recordr.html` in your browser of choice.
2. Click **Start recording** and allow microphone access when asked.
3. Click **Stop recording**.
4. Play it back in the preview player, then **Download** it, **Record again**, or **Discard** it.

Files are named `Recording_YYYY-MM-DD_HH-MM-SS.<ext>`.

## Features
- Live timer and level meter
- Playback preview before you save
- Picks the best format your browser records (WebM/Opus in Chrome, Edge and Firefox; MP4/M4A in Safari) and names the file to match
- Friendly messages if the microphone is blocked, missing or the browser can't record
- Warns before you close the tab mid-recording
- Light/Dark mode (remembered)

## Notes
- Browsers only allow microphone access on `https://`, `localhost` or (in most browsers) a local `file://` page.
- Recordings are **not** WAV. Browsers record compressed audio; v0.1 mislabelled WebM data as `.wav`, which most players refused to open. If you need WAV, open the file in any audio editor and export.
- Nothing is uploaded; recordings exist only in the page until you download them.

## Roadmap
### Planned Functionality
- [ ] Pause / resume
- [ ] Choose which microphone to use
- [ ] Optional WAV export

## Browser Support
Chrome, Edge, Firefox, Safari (14.1+): anything with `MediaRecorder`.

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
- Playback preview, timer display while recording, level meter, discard
- Dark/Light mode
- Error handling for denied or missing microphone and unsupported browsers

#### Fixed
- Downloads were labelled `.wav` but were WebM/Opus audio
- The timer kept running (and stacking up timeouts) after recording stopped
- `MediaRecorder` was given `timeslice` as a constructor option, which does nothing; the unused "2 minute maximum" variable was removed
- Microphone stayed on after recording stopped

### [0.1.0]
- Initial Project setup (now in `Archive/`)

