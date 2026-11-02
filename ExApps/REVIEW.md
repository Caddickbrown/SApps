# ExApps review

ExApps are the things that did not fit the single-page rule. Five were reviewed to see which still earn a place now that the browser can do more than it could in 2023.

| ExApp | Verdict | Why |
|---|---|---|
| **JSON2CSV** (`json2csv.py`, 1 KB) | **Promoted to SApp** → [`/JSON2CSV`](../JSON2CSV/) | Needs only a file in and a file out, which a page does better than a Tk dialog. The script also failed on anything but a flat list of identically-keyed objects, and built paths by splitting on `/`, which breaks on Windows |
| **CounTally** (`CounTally.py` + HTML templates) | **Promoted to SApp** → [`/CounTally`](../CounTally/) | A counter that needs a Python script to write its own report pages is the wrong way round; the planned features (multi-counter, history, reporting) are all easy in-page. `ExApps/CounTally/CounTally.html` was a one-counter template with no storage. README told you to open the `.py` "in your browser" |
| **Archivr** (`Archivr.py`) | **Keep as ExApp** | Its job is moving files between a USB stick and a folder and optionally deleting the originals. A page cannot do that without the File System Access API, which is Chromium-only and asks permission per folder; the point is a one-step habit |
| **CFiler** (`CFiler.py`) | **Keep as ExApp** | Writes a `Contents.html` that links to files beside it. A page could build the HTML, but the links only work if the result is saved into the same folder, which is again filesystem work. For a *contents page you maintain by hand*, [Glossar](../Glossar/) now covers the same need |
| **PostBuildr** (README + a Markdown template only) | **Drop** | The script was never committed, so there is nothing to run. Its stated job (Markdown with front matter → blog-post HTML) is what **Postage** already does in the browser. If front matter is the missing piece, add it to Postage |

## Things worth knowing before anyone runs these

- **Archivr deletes by default.** `DELETE_AFTER_COPY = True`, with no confirmation, and it copies *everything* in the source folder including sub-folders. `shutil.copy2` fails on a directory, the error is swallowed by a blanket `except`, and the delete step is skipped, so a second run (after the `Archive` folder exists) leaves things half-copied. With `False` it moves the `Archive` folder into itself. Fix before relying on it: skip directories, confirm before delete, copy-then-verify.
- **CFiler** builds `href`s and names without escaping, so a file name containing `<` or `&` produces broken HTML; `Library/` must exist or it raises `FileNotFoundError`; `Contents.html` in the repo is generated output.
- **CounTally.py** only runs from the folder holding `counter_data.csv`; the repo copy of that file is empty.
- Both Python tools still work as described in their READMEs. They were left exactly as they were.

## What changed in the repo

- Added top-level `JSON2CSV/` and `CounTally/` SApps.
- Left every file under `ExApps/` untouched, apart from this review and the ExApps README.
