# Paper Deep Reading Skill

A Codex skill for turning journal paper PDFs into beginner-friendly Obsidian deep-reading notes.

It is designed for students, new researchers, and R&D teams who need to read one difficult paper carefully: paragraph translation, figure interpretation, beginner concept support, question logs, and shareable PDF exports.

## What It Produces

- One main Obsidian Markdown note.
- Paragraph-by-paragraph translation or explanation.
- Figures placed near the relevant discussion.
- Detailed figure notes: what the figure is, what each panel does, what it proves, and why the authors included it.
- Beginner callouts for difficult concepts and methods.
- A deduplicated learning question log.
- Optional PDF export.

## Quick Install

Clone this repository and copy the skill folder into your Codex skills directory:

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

## Repository Layout

```text
paper-deep-reading/
  SKILL.md
  agents/openai.yaml
  references/
  scripts/
  assets/
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

MIT
