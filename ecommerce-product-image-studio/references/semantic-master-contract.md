# Semantic Master Production Contract

## Purpose

Separate **product photography generation** from **infographic / collage layout**.

Weak image models often preserve product identity in a simple single-job image, then lose geometry when asked to simultaneously solve:
- multiple panels;
- Chinese text;
- dimensions;
- icons;
- lifestyle scenes;
- material close-ups;
- marketing hierarchy.

The workflow therefore approves visual masters first and composes them later.

## Core rule

For factual ecommerce production:

```text
authoritative references
→ identity + critical geometry locks
→ single-job semantic masters
→ QA approval
→ approved copy deck
→ deterministic layout / derivatives
```

Do NOT default to one-shot generative six-grid / poster / detail-board images.

## Semantic master

A semantic master is an independently QA-able visual asset with one dominant buyer-decision job.

Typical masters:
- clean hero;
- variant / size visual;
- material close-up;
- joint / construction close-up;
- anti-slip / hardware detail;
- person-use / lifestyle;
- packaging/included-items proof when verified.

A master SHOULD normally contain no final typography unless text is itself part of the photographed product.

## Identity-critical details

For joints, screws, holes, labels, end grain, ports, or other critical details:
- prefer authoritative real crops where possible;
- otherwise use the strictest route necessary to preserve the detail;
- never let a decorative collage generation become the factual source for that detail.

## Approval gate

A master cannot enter final layout until:
- product identity passes;
- critical geometry passes when activated;
- variant scope passes;
- dimensions/facts pass when present;
- person interaction passes when present;
- material fidelity passes;
- product provenance is recorded.

Status:
- `APPROVED`
- `REVIEW`
- `FAIL`
- `BLOCKED`

Only `APPROVED` masters may be used in a final deterministic information layout.

## Six-grid / multi-panel rule

For a 2×3 or other multi-panel ecommerce board:

- define six semantic jobs first;
- map each cell to one approved master;
- map each text block to approved copy;
- render the grid deterministically;
- crop approved masters as needed without changing product geometry;
- do not regenerate the entire board just to repair one cell.

If one cell fails, replace only that cell/master.

## Recommended six-grid decision coverage

Use only relevant stages, but a useful default for physical consumer products is:

1. recognition / hero;
2. variant choice / dimensions;
3. material / surface;
4. critical construction / joint;
5. comfort / visible detail / contact feature;
6. usage / lifestyle.

This is a planning heuristic, not a mandatory template.

## Provenance

The final board records:
- cell ID;
- source master ID;
- crop/transform;
- copy IDs;
- layout profile;
- QA status.

A final board MUST NOT silently contain a new AI-redrawn version of the product that bypassed master QA.
