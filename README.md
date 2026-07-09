# Paper Deep Reading Skill

A portable agent skill for turning journal paper PDFs into beginner-friendly Obsidian deep-reading notes.

It is designed for students, new researchers, and R&D teams who need to read one difficult paper carefully: paragraph translation, figure interpretation, beginner concept support, question logs, and shareable PDF exports.

## What It Produces

- One main Obsidian Markdown note.
- Paragraph-by-paragraph translation or explanation.
- Figures placed near the relevant discussion.
- Detailed figure notes: what the figure is, what each panel does, what it proves, and why the authors included it.
- Beginner callouts for difficult concepts and methods.
- A deduplicated learning question log.
- Optional PDF export.

## Download And Install

Choose the entry that matches your tool.

### Option 1: Codex

```bash
git clone https://github.com/SunHaoZh/paper-deep-reading-skill.git
cp -r paper-deep-reading-skill/paper-deep-reading ~/.codex/skills/
```

On Windows PowerShell:

```powershell
git clone https://github.com/SunHaoZh/paper-deep-reading-skill.git
Copy-Item -Recurse .\paper-deep-reading-skill\paper-deep-reading "$env:USERPROFILE\.codex\skills\"
```

Then ask Codex:

```text
Use $paper-deep-reading to create an Obsidian deep-reading note from this journal paper PDF. Explain it for a beginner, place figures in context, maintain a question log, and export a PDF.
```

### Option 2: Claude Code

Claude Code supports Agent Skills with `SKILL.md`. Copy the same skill folder into one of these locations:

```bash
# User-level skill
cp -r paper-deep-reading-skill/paper-deep-reading ~/.claude/skills/

# Project-level skill
mkdir -p .claude/skills
cp -r paper-deep-reading-skill/paper-deep-reading .claude/skills/
```

See [`docs/adapters.md`](docs/adapters.md) for details and a fallback slash-command prompt.

### Option 3: Marvis

For Marvis-style tools, use the dedicated prompt adapter:

```text
adapters/marvis/paper-deep-reading-marvis-prompt.md
```

Copy it into Marvis custom instructions, prompt templates, project memory, or the closest reusable prompt area available in your Marvis environment.

### Option 4: General AI Tools

For tools without a native skill directory, copy [`adapters/universal/paper-deep-reading-prompt.md`](adapters/universal/paper-deep-reading-prompt.md) into the tool's custom instructions, prompt library, or project memory.

### Option 5: ZIP Or Release Download

- Repository ZIP: `https://github.com/SunHaoZh/paper-deep-reading-skill/archive/refs/heads/main.zip`
- Releases: `https://github.com/SunHaoZh/paper-deep-reading-skill/releases`
- Git clone: `https://github.com/SunHaoZh/paper-deep-reading-skill.git`

## Repository Layout

```text
paper-deep-reading/
  SKILL.md
  agents/openai.yaml
  references/
  scripts/
  assets/
adapters/
docs/
examples/
```

## Why This Is Different

Many academic AI tools focus on search, summarization, or writing. This skill focuses on learning one paper deeply. It treats figures as arguments, not decorations, and it keeps a question log so repeated concepts are merged into a growing study guide.

## Public Example Policy

Do not publish full-text translations of copyrighted papers unless the source license permits it. Use open-access papers, author-provided examples, or synthetic excerpts for public demos.

## Optional PDF Export

Install Node dependencies:

```bash
npm install
```

Export a note:

```bash
node paper-deep-reading/scripts/export_obsidian_note_pdf.js path/to/note.md path/to/output.pdf
```

## Validation

Validate the skill package:

```bash
python ~/.codex/skills/.system/skill-creator/scripts/quick_validate.py paper-deep-reading
```

Validate a note:

```bash
python paper-deep-reading/scripts/validate_note_structure.py examples/example-output/example-paper-deep-reading.md
```

## License

MIT. See [`docs/license.md`](docs/license.md) for a plain-language explanation.
