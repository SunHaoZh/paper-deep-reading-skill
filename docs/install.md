# Installation

## Install For Codex

Copy the `paper-deep-reading` folder into your Codex skills directory.

macOS/Linux:

```bash
cp -r paper-deep-reading ~/.codex/skills/
```

Windows PowerShell:

```powershell
Copy-Item -Recurse .\paper-deep-reading "$env:USERPROFILE\.codex\skills\"
```

Restart Codex if the skill does not appear immediately.

## Optional Dependencies

PDF rendering and extraction may use:

- Python 3.10+
- PyMuPDF: `python -m pip install pymupdf`
- Node.js
- Playwright and marked: `npm install`
