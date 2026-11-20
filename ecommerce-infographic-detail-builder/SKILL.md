---
name: ecommerce-infographic-detail-builder
description: Build mobile-readable ecommerce selling-point graphics and semantic detail modules from approved visual masters and evidence-bound copy, using one dominant message per screen, explicit zones, deterministic final layout, platform style profiles, and responsive derivatives.
---

# Ecommerce Infographic & Detail Builder

## Objective

Turn verified product evidence into **conversion screens**, not poster clutter, while preserving product identity and exact copy.

## Required upstream inputs

Before building a factual infographic/detail board, require:
- approved semantic master(s);
- approved copy deck;
- dimension/variant source map when numbers are shown;
- product identity lock;
- critical geometry lock when activated;
- target output profile.

Do not use a generated final collage as the first place product geometry is evaluated.

## Semantic-master-first rule

For multi-panel boards:

```text
single-job visual masters
→ master QA
→ approved copy deck
→ deterministic layout
→ final layout QA
```

Do NOT default to one-shot generation of a six-grid/poster containing product redraws, text, dimensions and lifestyle imagery simultaneously.

If a cell fails, fix/replace that cell only.

## One-screen-one-job rule

A screen/module SHOULD have one dominant communication job:
- recognition;
- one selling point;
- one proof target;
- one dimension question;
- one material / structure proof;
- one variant choice;
- one package question.

Do not cram every benefit into one image.

## Copy hierarchy

Use only approved copy IDs.

For Chinese conversion graphics:
- main title: short enough to read at thumbnail size;
- supporting line: one or two concise lines;
- badge/corner label: very short;
- exact dimensions/numbers: only verified values.

Do not let a layout model improvise stronger claims.

## Zone layout

Explicitly define:
- product/image zone;
- copy zone;
- badge/value zone when needed;
- protected whitespace.

Do not place copy over identity-critical joints/hardware unless intentionally reviewed.

## Six-grid strategy

A 2×3 board may use six distinct buyer-decision jobs, for example:
1. product recognition / hero;
2. size or variant choice;
3. material / surface;
4. critical construction / joint;
5. contact/detail feature;
6. lifestyle / usage.

This is a planning heuristic, not a fixed marketplace rule.

Each cell MUST map to:
- one approved master ID;
- one or more approved copy IDs;
- one decision job.

## Thumbnail test

For gallery/search-card assets:
- review at small-card size;
- main product should remain obvious;
- headline should remain legible if used;
- remove copy before shrinking type below practical readability.

## Detail-page module strategy

Generate modules independently.

Typical sequence:
- recognition / brand promise;
- core benefit;
- lifestyle proof;
- material / structure;
- dimensions / variants;
- package / usage notes.

Independent modules are preferred masters; stitch only as a derivative.

## Text rendering strategy

Final exact Chinese, SKU labels, numbers, dimensions and repeated copy SHOULD be deterministic.

Preferred:
- Pillow / SVG / HTML/CSS;
- Adobe/Figma/other design tool;
- `ecommerce-product-image-studio/scripts/render_infographic_grid.py` as a baseline.

If image-model text is unavoidable:
- quote exact approved copy;
- use minimal text;
- QA every character/number/unit;
- after repeated failure, stop regenerating and switch to deterministic typography.

## MUST NOT

- invent claims to fill a screen;
- mix promotional benefit and product function without hierarchy;
- use long copy at thumbnail scale;
- present unknown dimensions;
- allow platform style to override evidence;
- redraw an approved product master during final layout;
- regenerate all six panels because one panel failed.

## Outputs

Create:
- module manifest;
- approved copy deck reference;
- dimension source map;
- approved semantic master references;
- deterministic layout manifest;
- profile derivatives;
- thumbnail-readability QA;
- optional long-image derivative.
