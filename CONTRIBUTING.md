# Contributing

Contributions are welcome.

Good contributions include:

- Better figure-note templates.
- Better beginner explanation patterns.
- Obsidian styling improvements.
- Export fixes for Markdown and Obsidian image syntax.
- Examples based on open-access papers.
- Validation rules that catch broken links or repeated question entries.

Please avoid submitting copyrighted full-text translations unless the source license allows redistribution.

Before opening a pull request:

```bash
python ~/.codex/skills/.system/skill-creator/scripts/quick_validate.py paper-deep-reading
python paper-deep-reading/scripts/validate_note_structure.py examples/example-output/example-paper-deep-reading.md
```
