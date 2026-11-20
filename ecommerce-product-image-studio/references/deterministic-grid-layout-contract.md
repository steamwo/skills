# Deterministic Grid Layout Contract

## Purpose

Make multi-panel ecommerce graphics reproducible and text-accurate after the visual masters have passed QA.

Image generation is for imagery. Final grid geometry, exact copy, dimensions, labels, and repeated typography SHOULD be handled by deterministic layout tooling.

## Inputs

A layout job consumes only:
- approved semantic masters;
- approved copy deck;
- output profile;
- campaign palette / typography direction;
- explicit cell order;
- optional icons with known provenance.

## MUST

- preserve source master aspect ratio by contain/crop, never non-uniform warp;
- render exact approved copy;
- keep numbers/units unchanged;
- keep text outside critical product regions unless intentionally designed otherwise;
- maintain consistent gutters, margins, hierarchy and cell boundaries;
- keep a source map from cell to master and copy IDs.

## MUST NOT

- ask an image model to redraw the product while adding layout;
- let a layout step invent selling points;
- mechanically shrink text below readable size;
- replace a failed cell by regenerating all six panels;
- use a one-shot AI poster as the only editable master for factual ecommerce content.

## Default 2×3 board

A 2×3 board is a common design pattern, not a platform rule.

Recommended behavior:
- one dominant title per cell;
- optional one-line subtitle;
- 65–85% of each cell reserved for visual evidence when possible;
- strong whitespace;
- consistent title baseline;
- no more than one decision job per cell.

## Chinese typography

Exact Chinese copy SHOULD be rendered by:
- Pillow / SVG / HTML/CSS;
- Adobe/Figma/other deterministic design tools;
- or another system that preserves exact characters.

A CJK-capable font must be explicitly available to the rendering environment. Do not silently substitute missing glyphs.

## Script

`scripts/render_infographic_grid.py` provides a deterministic 2×3-or-general-grid reference renderer.

It is intentionally simple:
- exact text;
- fixed cells;
- image contain/crop;
- no generative image modification.

Use it as a reliable baseline, not as the only possible art direction.
