---
name: ecommerce-product-image-studio
description: Orchestrate a fidelity-first e-commerce product visual workflow with explicit intake, execution preflight, verified product evidence, surface profiles, deterministic prompts, source-pixel compositing, resumable execution, QA, delivery accounting, and marketplace export.
---

# Ecommerce Product Image Studio

## Objective

Produce a complete, traceable e-commerce visual asset family for a real SKU.

Priority order:

1. product identity and source-pixel fidelity;
2. verified product facts and dimensions;
3. explicit user intent;
4. operational readiness;
5. scene/person scale and perspective;
6. surface / marketplace requirements;
7. brand styling and creative presentation.

Creative quality MUST NOT override product truth.

## Normative rule: source product pixels

If the user supplies an authoritative product photo, that photo is the default source of truth for the visible product body.

**MUST**
- preserve original product RGB whenever practical;
- obtain or create an alpha mask separately;
- preserve source view, geometry, visible hardware, texture, color, logos, holes, seams, edge profiles, and component count;
- record source asset provenance for every final image.

**MUST NOT**
- regenerate the product from a text prompt;
- use image-to-image generation that redraws the product body and then treat it as the original SKU;
- replace the product with a visually similar model;
- stretch, liquify, warp, or generatively modify product geometry to fit a scene;
- invent unseen sides, accessories, packaging, dimensions, or performance claims.

A generated lookalike product is an identity \`FAIL\`.

## Required contracts and sub-skills

Read:
- \`references/task-input-schema.json\`
- \`references/intake-contract.md\`
- \`references/execution-preflight.md\`
- \`references/output-profile-contract.md\`
- \`references/detail-module-contract.md\`
- \`references/prompt-rendering.md\`
- \`references/execution-state-contract.md\`
- \`references/delivery-gate.md\`

Use applicable modules:
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

## Stage -2 — Task intake

Create \`task-input.json\` from the machine-readable input schema.

### Intent fields

Marketplace, market, ratio, surface profile, language, requested deliverables, style, and extra requirements MUST come from explicit user intent.

Do not infer them from:
- attachment appearance;
- filenames;
- product category;
- previous defaults;
- common marketplace practice.

### Evidence fields

Authoritative product images MUST be inspected for:
- visible geometry;
- components;
- hardware;
- texture / color;
- supported view;
- visible markings.

Do not promote visual evidence into unsupported business claims.

### Missing-field policy

Ask only for missing fields that block the next requested deliverable.

Examples:
- no platform → generic master is possible;
- no full dimensions → metric dimension graphics / scale claims may be blocked;
- no sale quantity → package / included-item claims are blocked;
- no rear view → factual rear-view image is blocked.

## Stage -1 — Execution preflight

Before expensive generation, create \`execution-preflight.json\`.

Check:
- source files exist and are usable;
- source resolution is adequate for planned crop / output;
- required production tools are available;
- output destinations are writable and non-destructive;
- platform / surface profiles are identified when required;
- preprocessing is non-destructive and traceable.

Preflight statuses:
- \`READY\`
- \`READY_WITH_REVIEW\`
- \`BLOCKED\`

Do not silently fall back to product regeneration because a required fidelity tool is missing.

## Stage 0 — Scope and execution state

Create \`execution-state.json\`.

MUST identify:
- project / SKU / variant;
- stable planned asset IDs;
- requested asset roles;
- output profile families;
- authoritative product references.

Each durable stage SHOULD checkpoint its state.

Resume interrupted work from the first invalid / incomplete stage instead of recreating the entire project.

## Stage 1 — Reference audit

Run \`product-reference-audit\`.

MUST produce:
- source inventory;
- view coverage;
- evidence matrix;
- missing-asset list;
- source usage map.

One photo MUST NOT be treated as proof of unseen geometry or full 3D dimensions.

## Stage 2 — Product identity lock

Run \`product-identity-lock\`.

Create \`product-identity.json\` with:
- authoritative references;
- must-preserve geometry and details;
- must-not-invent facts;
- locked / editable / conditionally editable regions;
- provenance requirements.

## Stage 3 — Dimension lock

Run \`product-dimension-lock\`.

Create \`product-dimensions.json\`.

Every published number MUST have:
- value;
- unit;
- axis / measurement definition;
- evidence;
- status.

Unknown dimensions remain unknown.

## Stage 4 — Scale and perspective

For scene or person images, run \`product-scale-calibration\`.

MUST define:
- contact plane;
- product anchor;
- camera / projection assumptions;
- reference objects, if any;
- person scale basis, if any;
- scale status.

If evidence is insufficient, set \`SCALE_UNVERIFIED\`.

## Stage 5 — Asset family and detail-module plan

Run \`ecommerce-gallery-planner\`.

Plan semantic assets / modules first, then one or more output profiles.

Each semantic asset MUST have:
- stable \`asset_id\`;
- role and buyer question;
- source references;
- product pixel policy;
- scale status;
- output profiles;
- generation / compositing method;
- copy evidence;
- acceptance criteria.

Do not fill slots by inventing views or facts.

## Stage 6 — Output profiles

For each requested surface, create / verify output profiles.

Distinguish:
- \`DESIGN_ONLY\` preset;
- \`VERIFIED\` marketplace compliance profile.

Named presets such as Amazon A+ standard / premium web / premium mobile are useful planning labels, but their current dimensions MUST be verified before platform-compliance claims.

Desktop and mobile versions MAY require separate layout renders rather than simple resizing.

## Stage 7 — Deterministic prompt rendering

Use repository prompt templates when available:
- \`templates/empty-scene-prompt.md\`
- \`templates/person-layer-prompt.md\`

Required unresolved placeholders block the asset.
Missing optional fields are omitted.
Fixed product-fidelity clauses remain present.

Save rendered prompts and template versions.

## Stage 8 — Production

### Product body

Default route:

\`\`\`text
authoritative photo
→ alpha mask
→ ORIGINAL PRODUCT RGB cutout
→ composite
\`\`\`

### Background

AI MAY generate empty rooms, surfaces, props, and atmosphere.

Background prompts MUST exclude the target product and confusing lookalikes.

### Person

People MUST be independent assets / layers when source-pixel fidelity is required.

### Shadows

Create contact / cast shadows independently. Shadows MUST NOT overwrite product RGB.

### Text / dimensions

Final Chinese copy, numbers, dimensions, arrows, logos, and tables SHOULD use layout / design tools.

## Stage 9 — Product + person + scene

Run \`product-human-scene-integration\`.

If believable interaction requires product deformation or redraw, set \`BLOCKED\`.

## Stage 10 — Detail modules and responsive renders

Run \`ecommerce-infographic-detail-builder\`.

Build independent semantic modules as editable masters.

Render them into requested surface profiles.

A stitched long image is a derivative deliverable, not the only master, unless the user explicitly requires otherwise.

## Stage 11 — QA

Run \`ecommerce-visual-qa\`.

Separate gates:
- input-source integrity;
- preflight readiness;
- identity fidelity;
- pixel provenance;
- dimension truth;
- scale grounding;
- prompt traceability;
- person interaction;
- copy truth;
- surface-profile validity;
- cross-image consistency;
- delivery completeness.

## Stage 12 — Resume / retry

Read \`execution-state.json\` before rerunning interrupted work.

MUST:
- reuse valid durable outputs;
- retry only failed / invalidated stages;
- record retry reason;
- avoid duplicate expensive generation jobs with the same execution key.

Examples:
- copy-only change → rerun layout / QA, not background generation;
- platform profile change → rerun export / profile render, not product cutout;
- product source change → invalidate downstream cutout / composite / layout / QA.

## Stage 13 — Delivery gate

Create \`delivery-manifest.json\`.

A run is not \`COMPLETE\` until:
- every non-blocked expected final asset exists;
- every final asset has QA status;
- every final asset has an accessible delivery reference;
- delivered count equals expected count.

Never claim “all images complete” when only some assets were surfaced.

## Stage 14 — Marketplace export

Run \`marketplace-export-preflight\`.

Marketplace requirements MUST be current and source-backed.

Do not hard-code remembered dimensions as permanent truth.

## Failure conditions

Set \`FAIL\` or \`BLOCKED\` when:
- product geometry differs from the authoritative SKU;
- product was regenerated instead of source-pixel composited;
- required source view is unsupported;
- a number is published without evidence;
- metric scale is claimed without grounding;
- person interaction requires product deformation;
- package contents or claims are invented;
- required prompt fields are unresolved;
- required preflight capability is unavailable;
- a design preset is falsely presented as verified compliance;
- the same expensive generation task is blindly duplicated;
- final delivery is claimed complete while the manifest is incomplete.

## Outputs

A complete run SHOULD produce:
- \`task-input.json\`
- \`execution-preflight.json\`
- \`execution-state.json\`
- \`asset-audit.md\`
- \`evidence-matrix.json\`
- \`product-identity.json\`
- \`product-dimensions.json\`
- \`scale-calibration.json\` where applicable
- \`image-plan.json\`
- output-profile records
- rendered prompt records
- product cutouts / masks
- generated backgrounds / person layers
- layered composites
- independent detail modules
- responsive / platform renders
- copy / dimension source maps
- per-image and cross-image QA
- \`delivery-manifest.json\`
- marketplace preflight records

Generated files are not complete until identity, provenance, QA, execution-state, and delivery contracts are satisfied.