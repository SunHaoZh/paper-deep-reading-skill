# Tool Adapters

This repository is centered on the `paper-deep-reading/` folder. That folder follows the `SKILL.md` pattern used by agent-skill systems. Keep this folder as the source of truth.

## Codex

Copy the skill folder into the Codex skills directory:

```bash
cp -r paper-deep-reading ~/.codex/skills/
```

Windows PowerShell:

```powershell
Copy-Item -Recurse .\paper-deep-reading "$env:USERPROFILE\.codex\skills\"
```

Invoke it with:

```text
Use $paper-deep-reading to create an Obsidian deep-reading note from this journal paper PDF.
```

## Claude Code

Claude Code supports Agent Skills with a `SKILL.md` file. Use the same source folder:

```bash
# User-level skill
mkdir -p ~/.claude/skills
cp -r paper-deep-reading ~/.claude/skills/

# Project-level skill
mkdir -p .claude/skills
cp -r paper-deep-reading .claude/skills/
```

If a Claude Code environment does not load skills automatically, use the fallback command prompt in:

```text
adapters/claude-code/commands/paper-deep-reading.md
```

## Marvis

At this time, this repository treats Marvis as a prompt-adapter target, not as a confirmed native `SKILL.md` runtime. Use the Marvis adapter:

```text
adapters/marvis/paper-deep-reading-marvis-prompt.md
```

Copy it into the Marvis custom instructions, prompt template, project memory, or equivalent reusable instruction area available in your environment.

## Marvin And Other AI Workbenches

Tool names and extension systems change, and not every tool has a public skill-folder standard. For Marvin-like or generic AI workbenches, use the universal prompt adapter unless the tool documents native `SKILL.md` support:

```text
adapters/universal/paper-deep-reading-prompt.md
```

Copy that file into the tool's custom instructions, project memory, prompt library, or reusable command area.

## Compatibility Policy

- Mark an adapter as "native" only when the target tool publicly documents the required folder or file format.
- Use "universal prompt" for tools that accept reusable instructions but do not document a skill package format.
- Keep `paper-deep-reading/SKILL.md` as the canonical implementation.
- Do not duplicate long workflow text across adapters; adapters should point back to the canonical skill and references.
