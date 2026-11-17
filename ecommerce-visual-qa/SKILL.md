---
name: ecommerce-visual-qa
description: Run evidence-backed QA for product identity, source-pixel provenance, dimensions, scale, perspective, person interaction, material fidelity, copy truth, cross-image consistency, and marketplace export readiness.
---

# Ecommerce Visual QA

## Objective

Evaluate each asset and the complete image set. Do not collapse visual quality, product truth, and scale accuracy into one score.

## QA states

- \`PASS\`
- \`REVIEW\`
- \`FAIL\`
- \`NOT_CHECKED\`

## Gate A — Product identity

Check against authoritative references:
- silhouette;
- component count;
- relative positions;
- hardware locations;
- holes / seams / joints;
- handles / supports / edge profiles;
- logo / markings;
- visible texture / grain / color.

Any identity-critical drift is \`FAIL\`.

## Gate B — Product pixel provenance

Record:
- source product asset;
- whether final product pixels are \`SOURCE_PRODUCT_PIXEL\`, \`VERIFIED_CAD_3D\`, or generated;
- masks and transformations;
- any authorized edits.

If an authoritative source photo existed but the product was regenerated as a lookalike without explicit creative-preview authorization, set \`FAIL\`.

Prompt similarity does not pass provenance.

## Gate C — Dimensions and specifications

Check:
- values;
- units;
- axis definitions;
- measurement state;
- evidence;
- product vs packaging;
- net vs gross weight;
- dimension-line endpoints.

Unknown / estimated values MUST NOT appear as verified customer-facing specifications.

## Gate D — Scale and perspective

Check:
- \`scale-calibration.json\`;
- contact plane;
- product anchor;
- camera / projection assumptions;
- reference objects;
- depth relationships;
- uniform product scaling;
- absence of geometry warping.

Do not mark metric scale \`PASS\` when the scene is only visually plausible.

## Gate E — Person interaction

Check:
- hand / finger anatomy;
- grip points;
- body support;
- foot / body placement;
- foreground / background occlusion;
- gravity;
- product geometry unchanged;
- no implied unverified performance.

## Gate F — Material / color

Check:
- visible texture direction;
- wood grain / knots where applicable;
- finish appearance;
- real color;
- metal / fabric / surface characteristics.

Brand color grading MUST NOT recolor the product body.

## Gate G — Cutout and composite

Check:
- holes / gaps preserved;
- no white / dark fringe;
- no mask-eaten structure;
- contact / cast shadow direction;
- shadow does not overwrite product RGB;
- no confusing duplicate target product in background.

## Gate H — Copy and graphics

Check:
- Chinese spelling;
- numbers;
- units;
- punctuation;
- claim evidence;
- packaging quantities;
- certifications;
- logos;
- readability.

## Gate I — Cross-image consistency

Check:
- same SKU / variant;
- same product structure;
- consistent dimensions;
- consistent color / material;
- consistent copy;
- person consistency when required;
- no contradictory packaging / quantity.

## Gate J — Marketplace export

Check:
- marketplace;
- category;
- slot;
- rule source;
- verification date;
- dimensions / format / file size / naming.

## Report schema

Each image SHOULD include:
- \`asset\`
- \`sku\`
- \`role\`
- \`source_images\`
- \`product_provenance\`
- \`identity_status\`
- \`dimension_status\`
- \`scale_status\`
- \`interaction_status\`
- \`copy_status\`
- \`overall_status\`
- \`evidence\`
- \`issues\`
- \`severity\`
- \`remediation\`
- \`reviewer\`

## Critical distinction

These three are independent:
- \`visual_plausibility\`
- \`metric_grounding\`
- \`product_pixel_provenance\`

One cannot substitute for another.