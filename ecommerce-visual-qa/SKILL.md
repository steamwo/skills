---
name: ecommerce-visual-qa
description: Run evidence-backed QA for input integrity, buyer-decision coverage, SKU/variant correctness, asset reuse, product identity, provenance, dimensions, scale, prompt traceability, surface profiles, execution state, delivery completeness, and marketplace readiness.
---

# Ecommerce Visual QA

## Objective

Evaluate individual assets, variant families, derivatives, and the complete production system.

## QA states

- \`PASS\`
- \`REVIEW\`
- \`FAIL\`
- \`NOT_CHECKED\`

## Gate A — Input-source integrity

Check explicit user intent vs extracted product evidence.

## Gate B — Execution preflight

Check source usability, tools, preprocessing, outputs, and blockers.

## Gate C — Buyer-decision coverage

Read \`buyer-decision-map.json\`.

Check:
- each planned semantic asset answers a buyer question;
- claimed answer has evidence;
- important unanswered questions are visible as blocked / partial;
- decorative duplicates did not replace needed decision coverage.

## Gate D — Variant matrix integrity

Read \`variant-matrix.json\`.

Check:
- correct family / variant ID;
- variant axis values;
- dimension scope;
- color / finish scope;
- packaging / included-item scope;
- copy scope;
- sharedness state.

Cross-SKU leakage is \`FAIL\`.

## Gate E — Product identity

Check geometry, components, hardware, supports, markings, texture, and variant-specific appearance against authoritative references.

## Gate F — Product pixel provenance

Record product-body source, mask, transformations, authorized edits, and provenance class.

A generated lookalike replacing an authoritative source is \`FAIL\`.

## Gate G — Dimensions / specifications

Check value, unit, axis, variant scope, evidence, packaging separation, and dimension-line endpoints.

## Gate H — Scale / perspective

Check calibration, contact plane, camera assumptions, variant geometry, uniform product scaling, and absence of warp.

## Gate I — Prompt traceability

Check template version, resolved placeholders, fixed product-exclusion clauses, and absence of unsupported facts.

## Gate J — Person interaction

Check anatomy, contact, occlusion, gravity, product geometry, and variant fit.

A person composition reused for a different variant must still fit the variant's verified geometry.

## Gate K — Detail module integrity

Check one semantic purpose, evidence inheritance, variant scope, responsive behavior, and long-image traceability.

## Gate L — Asset reuse / derivative integrity

Read \`asset-derivation-map.json\`.

Check:
- parent asset IDs;
- variant scope;
- reuse class;
- product provenance;
- output profile;
- invalidation inputs;
- stale derivatives.

A derivative whose upstream dependency changed but was not rebuilt / re-QA'd is \`FAIL\` or \`REVIEW\`.

## Gate M — Output profile validity

Check marketplace, surface, slot, device, preset, dimensions, rule source, verification date, and compliance status.

## Gate N — Material / composite

Check mask, texture/color fidelity, shadows, and product RGB preservation.

## Gate O — Copy / graphics

Check language, spelling, numbers, units, claims, certifications, quantity, and variant scope.

## Gate P — Execution state / retry integrity

Check stable IDs, checkpoints, targeted invalidation, retries, and absence of blind duplicate expensive generation.

## Gate Q — Cross-image / cross-variant consistency

Check:
- same variant within a variant-bound asset chain;
- family-shared facts truly shared;
- dimensions and copy do not leak across variants;
- comparison images preserve intended scale relationships;
- product appearance remains consistent with each source variant.

## Gate R — Delivery completeness

Count expected outputs by semantic asset × required variant scope × output profile.

Do not use naive “number of SKUs × number of images” when assets are legitimately shared.

## Gate S — Marketplace export

Check current platform rules and export constraints.

## Critical separation

Report separately:
- \`visual_plausibility\`
- \`buyer_decision_coverage\`
- \`variant_integrity\`
- \`product_pixel_provenance\`
- \`metric_grounding\`
- \`asset_reuse_integrity\`
- \`output_profile_validity\`
- \`execution_integrity\`
- \`delivery_completeness\`

One cannot substitute for another.