---
name: ecommerce-product-image-studio
description: Orchestrate a fidelity-first e-commerce product visual workflow from real SKU references, explicit task intake, verified dimensions, deterministic prompt rendering, source-pixel compositing, QA, delivery accounting, and marketplace export preflight.
---

# Ecommerce Product Image Studio

## Objective

Produce a complete, traceable e-commerce visual set for a real SKU.

Priority order:

1. product identity and source-pixel fidelity;
2. verified product facts and dimensions;
3. explicit user intent;
4. scene/person scale and perspective;
5. current marketplace constraints;
6. brand styling and creative presentation.

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
- \`references/prompt-rendering.md\`
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

## Stage -1 — Intake contract

Create \`task-input.json\` from the machine-readable input schema.

### Intent fields

Marketplace, market, ratio, language, requested deliverables, style, and extra requirements MUST come from explicit user intent. Do not infer them from attachment appearance, filenames, product category, or marketplace habits.

### Evidence fields

Authoritative product images MUST be inspected for product evidence:
- visible geometry;
- components;
- hardware;
- texture / color;
- supported view;
- visible markings.

This is intentionally different from form-only pass-through skills. Product-image inspection is required because identity locking depends on it.

Do not promote visual evidence into unsupported business claims.

### Missing-field policy

Ask only for missing fields that block the next requested deliverable.

Examples:
- no platform → generic master is still possible;
- no dimensions → metric dimension graphics / metric scale claims are blocked;
- no sale quantity → package / included-item claims are blocked;
- no rear view → factual rear-view image is blocked.

## Stage 0 — Scope

MUST identify:
- SKU / variant when available;
- requested asset roles;
- target marketplace if explicitly provided;
- authoritative product references.

If marketplace rules are not verified, plan a generic master and do not claim platform compliance.

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

For scene or person images, run \`product-scale-calibration\` before compositing.

MUST define:
- contact plane;
- product anchor;
- camera / projection assumptions;
- reference objects, if any;
- person scale basis, if any;
- scale status.

If evidence is insufficient, set \`SCALE_UNVERIFIED\` and do not claim real-world scale accuracy.

## Stage 5 — Gallery plan

Run \`ecommerce-gallery-planner\`.

Each planned asset MUST have:
- role and buyer question;
- source references;
- product pixel policy;
- scale status;
- generation/compositing method;
- copy evidence;
- acceptance criteria.

Do not fill image slots by inventing views or facts.

## Stage 6 — Deterministic prompt rendering

Do not improvise generation prompts from scratch when a repository template exists.

Use:
- \`templates/empty-scene-prompt.md\`
- \`templates/person-layer-prompt.md\`

Rendering MUST follow \`references/prompt-rendering.md\`.

Required unresolved placeholders block the asset. Missing optional fields are omitted rather than guessed.

Fixed product-fidelity clauses MUST remain present.

## Stage 7 — Production

### Product body

Default route:

\`\`\`text
authoritative photo
→ alpha mask
→ ORIGINAL PRODUCT RGB cutout
→ composite
\`\`\`

Product RGB SHOULD be immutable except for explicitly authorized, non-identity corrections.

### Background

AI MAY generate:
- empty rooms;
- abstract backdrops;
- environmental surfaces;
- non-product props.

Background prompts MUST explicitly exclude the target product and confusing lookalikes.

### Person

People MUST be independent assets or layers. Do not generate the person and product as one fused image when source-pixel fidelity is required.

### Shadows

Create contact and cast shadows as independent layers. Shadows MUST NOT overwrite product RGB.

### Text / dimensions

Final Chinese copy, numbers, dimensions, arrows, logos, and tables SHOULD be added with layout/design tools, not trusted to an image model.

## Stage 8 — Product + person + scene

Run \`product-human-scene-integration\`.

MUST validate:
- hand / body contact points;
- occlusion order;
- ground/contact plane;
- product geometry unchanged;
- person action does not imply unverified performance.

If realistic interaction cannot be achieved without redrawing product geometry, the asset is \`BLOCKED\`.

## Stage 9 — Infographic and detail modules

Run \`ecommerce-infographic-detail-builder\`.

Use only verified dimensions and claims. Do not infer dimensions from the composite.

For Chinese e-commerce detail pages, independent vertical modules are preferred unless the user specifically requests a stitched long image.

## Stage 10 — QA

Run \`ecommerce-visual-qa\`.

The following are separate gates:
- identity fidelity;
- pixel provenance;
- dimension truth;
- scale grounding;
- person interaction;
- copy truth;
- cross-image consistency;
- export compliance.

A pretty image can still be \`FAIL\`.

## Stage 11 — Delivery gate

Create \`delivery-manifest.json\` using \`references/delivery-gate.md\`.

A run is not \`COMPLETE\` until:
- every non-blocked planned final asset exists;
- each final asset has QA status;
- each final asset has an accessible delivery reference;
- delivered asset count equals expected deliverable count.

Never claim “all images complete” when only some files were surfaced to the user.

## Stage 12 — Marketplace export

Run \`marketplace-export-preflight\`.

Marketplace requirements MUST be current and source-backed. Do not hard-code stale Taobao / Tmall / JD / PDD dimensions as permanent truths.

## Failure conditions

Set \`FAIL\` or \`BLOCKED\` when:
- generated product geometry differs from the authoritative SKU;
- product was regenerated instead of source-pixel composited without explicit creative-preview authorization;
- a required view is unsupported;
- a dimension is published without evidence;
- product scale is presented as accurate without grounding;
- a person interaction requires impossible product deformation;
- package contents or claims are invented;
- required prompt-template fields are unresolved;
- final delivery is claimed complete while the delivery manifest is incomplete.

## Outputs

A complete run SHOULD produce:
- \`task-input.json\`
- \`asset-audit.md\`
- \`evidence-matrix.json\`
- \`product-identity.json\`
- \`product-dimensions.json\`
- \`scale-calibration.json\` where applicable
- \`image-plan.json\`
- rendered prompt records
- product cutouts and masks
- generated empty backgrounds / person layers
- layered composites
- copy deck and dimension source map
- master exports
- per-image QA and cross-image QA
- \`delivery-manifest.json\`
- marketplace preflight records

Generated files are not complete until QA provenance, identity, and delivery gates are satisfied.