---
name: ecommerce-visual-qa
description: Run evidence-backed QA for product identity, source-pixel provenance, dimensions, scale, perspective, person interaction, material fidelity, copy truth, cross-image consistency, marketplace readiness, and final delivery accounting.
---

# Ecommerce Visual QA

## Objective

Evaluate each asset and the complete image set. Do not collapse visual quality, product truth, scale accuracy, and delivery completeness into one score.

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

## Gate C — Input-source integrity

Check:
- user-intent fields came from explicit user input;
- attachment content was not used to invent platform, language, ratio, market, style, or extra requirements;
- product-evidence fields derived from attachments are labeled as evidence rather than user intent;
- optional unspecified fields were omitted or handled by an explicit legal \`auto\` option.

## Gate D — Dimensions and specifications

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

## Gate E — Scale and perspective

Check:
- \`scale-calibration.json\`;
- contact plane;
- product anchor;
- camera / projection assumptions;
- reference objects;
- depth relationships;
- uniform product scaling;
- absence of geometry warping.

## Gate F — Person interaction

Check:
- hand / finger anatomy;
- grip points;
- body support;
- foot / body placement;
- foreground / background occlusion;
- gravity;
- product geometry unchanged;
- no implied unverified performance.

## Gate G — Material / color

Check source-aligned material appearance and ensure brand grading does not recolor the product body.

## Gate H — Cutout and composite

Check:
- holes / gaps preserved;
- no fringe;
- no mask-eaten structure;
- contact / cast shadow direction;
- shadow does not overwrite product RGB;
- no confusing duplicate target product in background.

## Gate I — Copy and graphics

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

## Gate J — Prompt traceability

For generated backgrounds / people, verify:
- template version recorded;
- rendered prompt saved;
- required placeholders resolved;
- fixed product-exclusion clause present;
- no unsupported facts added.

## Gate K — Cross-image consistency

Check same SKU / variant, structure, verified dimensions, appearance, copy, and person consistency when required.

## Gate L — Marketplace export

Check marketplace, category, slot, rule source, verification date, dimensions / format / file size / naming.

## Gate M — Delivery completeness

Read \`delivery-manifest.json\`.

Check:
- planned count;
- blocked count;
- expected deliverable count;
- produced count;
- QA-completed count;
- delivered count;
- accessible delivery references.

Do not set project completion to \`COMPLETE\` unless the Delivery Gate passes.

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
- \`prompt_trace_status\`
- \`overall_status\`
- \`evidence\`
- \`issues\`
- \`severity\`
- \`remediation\`
- \`reviewer\`

## Critical distinction

These are independent:
- \`visual_plausibility\`
- \`metric_grounding\`
- \`product_pixel_provenance\`
- \`delivery_completeness\`

One cannot substitute for another.