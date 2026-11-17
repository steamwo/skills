---
name: ecommerce-product-image-studio
description: Orchestrate a fidelity-first e-commerce visual production system with explicit intake, execution preflight, buyer-decision planning, SKU/variant matrices, output profiles, deterministic prompts, source-pixel compositing, reusable derivatives, resumable execution, QA, delivery accounting, and marketplace export.
---

# Ecommerce Product Image Studio

## Objective

Produce a complete, traceable e-commerce visual asset family for a real product family and its SKUs.

The system optimizes for:
1. product identity and source-pixel fidelity;
2. verified product facts and dimensions;
3. explicit user intent;
4. buyer-decision coverage;
5. variant correctness;
6. reusable production masters;
7. operational readiness;
8. scene/person scale and perspective;
9. surface / marketplace requirements;
10. brand styling and creative presentation.

Creative quality MUST NOT override product truth.

## Required contracts

Read:
- \`references/task-input-schema.json\`
- \`references/intake-contract.md\`
- \`references/execution-preflight.md\`
- \`references/buyer-decision-framework.md\`
- \`references/variant-matrix-contract.md\`
- \`references/asset-reuse-contract.md\`
- \`references/output-profile-contract.md\`
- \`references/detail-module-contract.md\`
- \`references/prompt-rendering.md\`
- \`references/execution-state-contract.md\`
- \`references/delivery-gate.md\`

Use applicable sub-skills:
- \`product-reference-audit\`
- \`product-identity-lock\`
- \`product-dimension-lock\`
- \`product-scale-calibration\`
- \`ecommerce-gallery-planner\`
- \`product-cutout-composite\`
- \`lifestyle-scene-composite\`
- \`human-lifestyle-composite\`
- \`product-human-scene-integration\`
- \`ecommerce-infographic-detail-builder\`
- \`brand-visual-system\`
- \`ecommerce-visual-qa\`
- \`marketplace-export-preflight\`
- \`wood-product-fidelity\` when wood products are involved.

## Product pixel rule

If the user supplies an authoritative product photo, that photo is the default source of truth for the visible product body.

**MUST**
- preserve original product RGB whenever practical;
- create / review alpha separately;
- preserve source view, geometry, hardware, texture, color, logos, holes, seams, edge profiles, and component count;
- record product provenance for every final asset.

**MUST NOT**
- regenerate the product from text;
- replace the product with a visually similar model;
- use image-to-image product redraw as a normal production route;
- stretch, warp, liquify, or generatively modify product geometry;
- invent unseen sides, accessories, packaging, dimensions, or performance claims.

A generated lookalike product is an identity \`FAIL\`.

## Stage -3 — Task intake

Create \`task-input.json\`.

Intent fields such as marketplace, ratio, output profile, language, requested style, target market, and deliverables MUST come from explicit user intent.

Authoritative product images MUST be inspected for product evidence.

Do not infer business intent from product appearance.

## Stage -2 — Execution preflight

Create \`execution-preflight.json\`.

Validate source files, required tools, output paths, preprocessing, and requested profiles before expensive generation.

Do not silently fall back to product regeneration because a required fidelity tool is missing.

## Stage -1 — Product family / variant matrix

If the product has more than one SKU or variant, create \`variant-matrix.json\` before planning the image set.

MUST identify:
- family ID;
- variant axes;
- variant IDs / SKUs;
- variant-specific dimensions;
- variant-specific color / material / packaging / copy;
- facts verified to be family-shared;
- facts whose sharedness is unknown;
- variant-bound assets;
- family-shared assets.

Use sharedness states:
- \`SHARED_VERIFIED\`
- \`VARIANT_SPECIFIC\`
- \`UNKNOWN_SHAREDNESS\`
- \`NOT_APPLICABLE\`

Do not assume a fact or visual asset is shared across variants merely because only one variant was photographed.

## Stage 0 — Scope, stable IDs, and execution state

Create \`execution-state.json\`.

MUST identify:
- project / product family;
- SKU / variant scope;
- stable semantic asset IDs;
- output profile families;
- authoritative source assets.

Every durable stage SHOULD checkpoint its output.

## Stage 1 — Reference audit

Run \`product-reference-audit\`.

Create source inventory, view coverage, evidence matrix, missing-assets list, and usage map.

## Stage 2 — Product identity lock

Run \`product-identity-lock\`.

Identity MUST be recorded per relevant variant scope.

Family-shared identity features require verified invariance.

## Stage 3 — Dimension lock

Run \`product-dimension-lock\`.

Dimensions that differ by variant MUST remain at variant level.

A family-level dimension may be used only when verified identical across all applicable variants.

## Stage 4 — Buyer-decision map

Before deciding image count, create \`buyer-decision-map.json\`.

Plan around purchase questions such as:
- What is this?
- Is it relevant to my use?
- Why choose it?
- How is it used?
- Will it fit?
- Which variant should I choose?
- What materials / structure support trust?
- What are the verified specifications?
- What exactly is included?
- What usage / compatibility limits matter?

Each semantic asset SHOULD map to:
- \`decision_stage\`
- \`buyer_question\`
- \`decision_answer\`
- \`evidence_refs\`

Do not create decorative duplicates merely to increase image count.

## Stage 5 — Scale and perspective

For scale-sensitive scenes, run \`product-scale-calibration\`.

For variant families, scale assumptions MUST be checked per variant when geometry differs.

## Stage 6 — Semantic asset family plan

Run \`ecommerce-gallery-planner\`.

Plan semantic assets first, then output-profile renders.

Each semantic asset MUST declare:
- stable \`asset_id\`;
- buyer-decision stage;
- variant scope;
- reuse class;
- source assets;
- product provenance policy;
- dimensions / copy evidence;
- scale status;
- output profiles;
- dependencies;
- acceptance criteria.

Do not multiply every asset by every SKU by default.

## Stage 7 — Asset reuse / derivative graph

Create \`asset-derivation-map.json\`.

Classify assets by layer:
- authoritative source;
- reusable production master;
- composed semantic asset;
- surface / marketplace derivative.

Reuse valid upstream assets when their inputs and variant scope remain valid.

Examples:
- brand system → usually family-shared;
- empty background → may be reusable;
- product cutout → usually variant-bound;
- size-specific dimension graphic → variant-bound;
- translated copy → downstream derivative;
- mobile layout → derivative of semantic module.

When an upstream dependency changes, invalidate only dependent downstream assets.

## Stage 8 — Output profiles

Create output profiles per requested marketplace / surface / slot / device.

Distinguish:
- \`DESIGN_ONLY\`
- \`VERIFIED\`
- \`NEEDS_REVIEW\`
- \`BLOCKED\`

Named presets are not proof of current marketplace compliance.

## Stage 9 — Deterministic prompt rendering

Use repository templates.

Required unresolved placeholders block production.
Missing optional values are omitted.
Fixed product-fidelity constraints remain.

## Stage 10 — Production

### Product body

Default:

\`\`\`text
authoritative photo
→ alpha mask
→ ORIGINAL PRODUCT RGB cutout
→ semantic composite
\`\`\`

### Background / person / props

AI MAY generate independent, non-product layers.

### Text / dimensions

Use layout / design tooling for final copy, numbers, logos, dimension lines, and tables.

## Stage 11 — Product + person + scene

Run \`product-human-scene-integration\`.

A reusable person pose or background MAY be shared only when the target variant still fits the verified scale / contact geometry.

Do not deform a different variant to reuse an old composition.

## Stage 12 — Detail modules and responsive renders

Run \`ecommerce-infographic-detail-builder\`.

Build independent semantic modules as masters.

Render them into requested profiles.

A stitched long image is a derivative deliverable, not the only editable master.

## Stage 13 — QA

Run \`ecommerce-visual-qa\`.

Separate gates MUST cover:
- input-source integrity;
- preflight readiness;
- buyer-decision coverage;
- variant correctness;
- asset reuse / derivative integrity;
- identity fidelity;
- pixel provenance;
- dimension truth;
- scale grounding;
- prompt traceability;
- person interaction;
- copy truth;
- output-profile validity;
- cross-image / cross-variant consistency;
- execution integrity;
- delivery completeness.

## Stage 14 — Resume / targeted invalidation

Read \`execution-state.json\` and \`asset-derivation-map.json\`.

Reuse valid upstream assets.

Invalidate only the smallest dependent graph.

Examples:
- translation change → copy/layout/QA only;
- output profile change → profile render/export only;
- one variant dimension changes → affected variant's dimension and scale-dependent assets only;
- source product photo changes → variant cutout and all downstream dependent assets;
- family-shared brand style changes → layouts may rerender, product cutouts remain valid.

Blind duplicate expensive generation is prohibited.

## Stage 15 — Delivery gate

Create \`delivery-manifest.json\`.

Count deliverables by actual requested semantic asset × required variant scope × required output profiles, not by naive SKU multiplication.

A run is not \`COMPLETE\` until every expected, non-blocked final derivative has QA status and an accessible delivery reference.

## Stage 16 — Marketplace export

Run \`marketplace-export-preflight\`.

Marketplace requirements MUST be current and source-backed.

## Outputs

A complete production run SHOULD include:
- \`task-input.json\`
- \`execution-preflight.json\`
- \`execution-state.json\`
- \`variant-matrix.json\` when applicable
- \`buyer-decision-map.json\`
- reference audit outputs
- \`product-identity.json\`
- \`product-dimensions.json\`
- \`scale-calibration.json\` where applicable
- \`image-plan.json\`
- \`asset-derivation-map.json\`
- output-profile records
- rendered prompts
- masks / product cutouts
- generated empty backgrounds / people
- semantic composites
- detail modules
- profile / marketplace derivatives
- QA
- \`delivery-manifest.json\`

Generated files are not complete until product truth, variant scope, buyer-decision coverage, provenance, dependency state, QA, and delivery contracts are satisfied.