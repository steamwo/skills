---
name: ecommerce-visual-qa
description: Run evidence-backed QA for input integrity, preflight readiness, product identity, source-pixel provenance, dimensions, scale, prompt traceability, person interaction, surface profiles, detail modules, cross-image consistency, delivery completeness, and marketplace readiness.
---

# Ecommerce Visual QA

## Objective

Evaluate each asset and the complete production system.

Do not collapse visual quality, product truth, operational readiness, profile validity, and delivery completeness into one score.

## QA states

- \`PASS\`
- \`REVIEW\`
- \`FAIL\`
- \`NOT_CHECKED\`

## Gate A — Input-source integrity

Check:
- user-intent fields came from explicit user input;
- product evidence derived from attachments is labeled as evidence;
- optional unspecified fields were omitted or handled through explicit legal policy.

## Gate B — Execution preflight

Check:
- source assets usable;
- required tools available;
- originals preserved;
- preprocessing traceable;
- output destination valid;
- blocked requirements identified before expensive work.

## Gate C — Product identity

Check silhouette, components, hardware, joints, supports, logos, texture, and other identity-critical details against authoritative references.

Identity drift = \`FAIL\`.

## Gate D — Product pixel provenance

Record source product asset, mask, transformations, authorized edits, and provenance class.

A generated lookalike replacing an available authoritative source is \`FAIL\`.

## Gate E — Dimensions / specifications

Check values, units, axes, evidence, product-vs-packaging, and dimension-line endpoints.

Unknown / estimated values MUST NOT appear as verified specs.

## Gate F — Scale / perspective

Check scale-calibration records, contact plane, camera assumptions, reference objects, uniform product scaling, and absence of geometry warp.

## Gate G — Prompt traceability

For generated assets verify:
- template version;
- rendered prompt;
- required placeholders resolved;
- fixed product-exclusion clauses preserved;
- no unsupported facts introduced.

## Gate H — Person interaction

Check anatomy, grip/contact points, occlusion, gravity, and unchanged product geometry.

## Gate I — Detail module integrity

Check:
- each module has one clear semantic purpose;
- claims inherit evidence;
- different profile renders preserve semantic priority;
- mobile / web variants are redesigned when needed rather than blindly squeezed;
- stitched long image, if present, is traceable to independent modules.

## Gate J — Output profile validity

Check:
- marketplace;
- surface;
- slot;
- device;
- design preset;
- dimensions;
- rule source;
- verification date;
- compliance status.

A \`DESIGN_ONLY\` preset MUST NOT be described as verified platform compliance.

## Gate K — Material / composite

Check source-aligned material appearance, mask correctness, fringe, shadows, and product RGB preservation.

## Gate L — Copy / graphics

Check language, spelling, numbers, units, claims, packaging quantities, certifications, logos, and readability.

## Gate M — Execution state / retry integrity

Read \`execution-state.json\`.

Check:
- stable asset IDs;
- checkpoints;
- input revision;
- retries recorded;
- completed valid artifacts reused;
- no duplicate expensive generation caused solely by interrupted monitoring.

## Gate N — Cross-image consistency

Check same SKU / variant, structure, verified dimensions, appearance, copy, provenance, and requested person consistency.

## Gate O — Delivery completeness

Read \`delivery-manifest.json\`.

Check planned, blocked, expected, produced, QA-completed, delivered counts and accessible references.

## Gate P — Marketplace export

Check current rule source, verification date, format, dimensions, file size, naming, and slot-specific constraints.

## Critical distinction

Report separately:
- \`visual_plausibility\`
- \`input_source_integrity\`
- \`preflight_readiness\`
- \`product_pixel_provenance\`
- \`metric_grounding\`
- \`output_profile_validity\`
- \`execution_integrity\`
- \`delivery_completeness\`

One cannot substitute for another.