#!/usr/bin/env python3
"""Lightweight checks for Paper Deep Reading Obsidian notes."""

from __future__ import annotations

import argparse
import re
from pathlib import Path


IMAGE_PATTERNS = [
    re.compile(r"!\[[^\]]*\]\(([^)]+)\)"),
    re.compile(r"!\[\[([^|\]]+)(?:\|[^\]]+)?\]\]"),
]


def iter_image_paths(text: str) -> list[str]:
    paths: list[str] = []
    for pattern in IMAGE_PATTERNS:
        for match in pattern.finditer(text):
            path = match.group(1).strip()
            if path and not path.startswith(("http://", "https://")):
                paths.append(path.split("|", 1)[0])
    return paths


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("note", type=Path, help="Markdown note to validate")
    args = parser.parse_args()

    note = args.note.resolve()
    text = note.read_text(encoding="utf-8")
    errors: list[str] = []
    warnings: list[str] = []

    required = ["# ", "## One-Sentence Conclusion", "## Paragraph-by-Paragraph"]
    for marker in required:
        if marker not in text:
            warnings.append(f"Missing expected marker: {marker}")

    if "> [!note]" not in text:
        warnings.append("No figure-note callouts found.")
    if "> [!help]" not in text:
        warnings.append("No beginner explanation callouts found.")

    qids = re.findall(r"^##\s+(Q\d+):", text, flags=re.MULTILINE)
    duplicates = sorted({qid for qid in qids if qids.count(qid) > 1})
    for qid in duplicates:
        errors.append(f"Duplicate question ID: {qid}")

    for raw in iter_image_paths(text):
        candidate = (note.parent / raw).resolve()
        if not candidate.exists():
            errors.append(f"Missing image: {raw}")

    for item in warnings:
        print(f"WARNING: {item}")
    for item in errors:
        print(f"ERROR: {item}")

    if errors:
        return 1
    print("OK: note structure validation completed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
