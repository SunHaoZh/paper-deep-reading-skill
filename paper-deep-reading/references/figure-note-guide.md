# Figure Note Guide

## Placement

Place a figure immediately after the paragraph where the paper first relies on it. If a caption spans pages or columns, crop the figure and caption separately only when this improves readability.

## Naming

Use stable lowercase filenames:

```text
assets/figures/fig-1-main-claim.png
assets/figures/fig-2-method-validation.png
assets/figures/fig-s1-control-experiment.png
```

## Required Figure Note Structure

For every main figure, include:

- What this figure is: microscopy, schematic, diffraction/FFT, spectrum, phase diagram, time trace, model, simulation, statistics, etc.
- What each panel does: explain panel A/B/C rather than only restating labels.
- How to read it: axes, colors, symbols, arrows, scale bars, and comparison groups.
- What it proves or supports: connect to the paper's claim.
- Why it matters: explain the role in the whole argument.
- Why the authors included it: motivation and persuasion strategy.
- Beginner warning: one sentence about a common misreading.

## Distinguish Evidence Types

Use precise verbs:

- "shows" for direct visual or measured evidence.
- "quantifies" for extracted numerical trends.
- "supports" for evidence that strengthens a claim.
- "suggests" for an inference.
- "models" or "calculates" for simulation and theory.

## Good Figure Note Pattern

```markdown
> [!note] Figure 1 note
> **What it is:** A combined microscopy and diffraction figure.
> **What each panel does:** Panel A establishes sample orientation; panel B maps local composition; panel C measures displacement.
> **How to read it:** First read the coordinate arrows, then compare bright/dark contrast, then connect the measured displacement to the structural model.
> **Meaning:** This figure turns the paper's central mechanism from a verbal claim into spatial evidence.
> **Author's purpose:** The authors place it early because later switching arguments depend on this structural baseline.
> **Beginner warning:** Bright contrast is not automatically "more polarization"; it may reflect atomic number, diffraction condition, detector geometry, or sample thickness.
```
