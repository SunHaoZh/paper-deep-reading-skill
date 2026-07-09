#!/usr/bin/env python3
"""Portable validation for a Codex skill package."""

from __future__ import annotations

import argparse
import re
from pathlib import Path


NAME_RE = re.compile(r"^[a-z0-9-]{1,63}$")


def parse_frontmatter(text: str) -> tuple[dict[str, str], list[str]]:
    errors: list[str] = []
    if not text.startswith("---\n"):
        return {}, ["SKILL.md must start with YAML frontmatter."]
    end = text.find("\n---", 4)
    if end == -1:
        return {}, ["SKILL.md frontmatter must end with ---."]
    raw = text[4:end].strip().splitlines()
    data: dict[str, str] = {}
    for line in raw:
        if ":" not in line:
            errors.append(f"Invalid frontmatter line: {line}")
            continue
        key, value = line.split(":", 1)
        value = value.strip().strip('"').strip("'")
        data[key.strip()] = value
    return data, errors


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("skill_dir", type=Path)
    args = parser.parse_args()

    skill_dir = args.skill_dir.resolve()
    skill_md = skill_dir / "SKILL.md"
    errors: list[str] = []

    if not skill_md.exists():
        errors.append("Missing SKILL.md.")
    else:
        text = skill_md.read_text(encoding="utf-8")
        frontmatter, fm_errors = parse_frontmatter(text)
        errors.extend(fm_errors)
        name = frontmatter.get("name", "")
        description = frontmatter.get("description", "")
        if not name:
            errors.append("Missing frontmatter field: name.")
        elif not NAME_RE.match(name):
            errors.append("Skill name must use lowercase letters, digits, and hyphens only.")
        if skill_dir.name != name:
            errors.append(f"Skill directory name '{skill_dir.name}' must match frontmatter name '{name}'.")
        if not description:
            errors.append("Missing frontmatter field: description.")
        elif len(description) < 80:
            errors.append("Description should clearly explain what the skill does and when to use it.")

    openai_yaml = skill_dir / "agents" / "openai.yaml"
    if not openai_yaml.exists():
        errors.append("Missing agents/openai.yaml.")

    for resource in ["references", "scripts", "assets"]:
        if not (skill_dir / resource).exists():
            errors.append(f"Missing resource directory: {resource}/")

    for error in errors:
        print(f"ERROR: {error}")
    if errors:
        return 1
    print("OK: skill package validation completed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
