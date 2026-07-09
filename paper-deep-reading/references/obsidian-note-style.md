# Obsidian Note Style

## Layout

Prefer one main note:

```text
Paper Title Deep Reading.md
assets/figures/
exports/
Question Log.md
```

Use internal links for major repeated concepts, but keep the reading path in one document.

## Callouts

Use Obsidian callouts consistently:

```markdown
> [!info] Metadata
> Source, DOI, venue, local PDF path.

> [!help] Beginner note
> Explain the concept in plain language.

> [!note] Figure note
> Explain what the figure is doing and why it matters.

> [!summary] Mechanism chain
> Connect the key steps.

> [!question] Self-check
> Ask one useful recall or reasoning question.
```

## Figure Syntax

Use Markdown image syntax for portability:

```markdown
![Figure 1](assets/figures/fig-1-main-claim.png)
```

Obsidian embeds such as `![[figure.png|600]]` may be used in local vaults, but export scripts should support both forms.

## Styling

If the user asks for a beautiful vault, copy `assets/obsidian-css-snippet.css` into the vault's `.obsidian/snippets/` folder and tell the user to enable the snippet.

Keep style quiet and readable:

- Comfortable line height.
- Wide figures.
- Distinct callout borders.
- Avoid decorative layouts that interrupt long-form reading.
