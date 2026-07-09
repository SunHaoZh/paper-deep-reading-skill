# Installation

## Download Options

- Git clone: `git clone https://github.com/SunHaoZh/paper-deep-reading-skill.git`
- ZIP download: `https://github.com/SunHaoZh/paper-deep-reading-skill/archive/refs/heads/main.zip`
- Releases: `https://github.com/SunHaoZh/paper-deep-reading-skill/releases`

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

## Install For Claude Code

Claude Code can use Agent Skills with `SKILL.md`.

User-level:

```bash
mkdir -p ~/.claude/skills
cp -r paper-deep-reading ~/.claude/skills/
```

Project-level:

```bash
mkdir -p .claude/skills
cp -r paper-deep-reading .claude/skills/
```

Fallback prompt:

```text
adapters/claude-code/commands/paper-deep-reading.md
```

## Install For General AI Tools

For tools that do not document a native skill folder, copy this universal adapter into the tool's prompt library or custom instructions:

```text
adapters/universal/paper-deep-reading-prompt.md
```

## Install For Marvis

Use the dedicated Marvis prompt adapter:

```text
adapters/marvis/paper-deep-reading-marvis-prompt.md
```

Copy the file content into Marvis custom instructions, prompt templates, project memory, or the closest reusable prompt area supported by your Marvis environment.

## Optional Dependencies

PDF rendering and extraction may use:

- Python 3.10+
- PyMuPDF: `python -m pip install pymupdf`
- Node.js
- Playwright and marked: `npm install`
