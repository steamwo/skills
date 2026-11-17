---
name: ecommerce-gallery-planner
description: Plan an evidence-backed e-commerce asset family with distinct buyer-decision roles, requested deliverables, semantic detail modules, surface profiles, provenance, scale status, production method, and acceptance criteria.
---

# Ecommerce Gallery Planner

## Objective

Plan a complete asset family where each image or module answers a distinct buyer question.

Do not create near-duplicate images just to fill slots.

## Required inputs

- \`task-input.json\`
- \`product.json\`
- \`product-identity.json\`
- \`product-dimensions.json\`
- reference audit outputs
- \`scale-calibration.json\` for scale-sensitive scenes
- brand system if available
- current marketplace / surface requirements if known

Read:
- \`ecommerce-product-image-studio/references/output-profile-contract.md\`
- \`ecommerce-product-image-studio/references/detail-module-contract.md\`

## Requested deliverables rule

If the user explicitly requested deliverable types, the plan MUST respect that request.

Do not infer unrequested deliverables from:
- product category;
- uploaded image style;
- marketplace convention;
- an old default gallery.

If the user requested a “complete image set”, the planner MAY propose a complete role set, but unsupported roles remain \`BLOCKED\` rather than invented.

## Asset families

Distinguish:
- semantic asset / module;
- one or more render profiles.

Example:

\`\`\`text
module: product dimensions
  ├── generic detail-page render
  ├── mobile render
  └── marketplace-specific render
\`\`\`

Do not duplicate evidence or rewrite claims independently per render.

## Recommended asset roles

Use only roles supported by evidence:
1. hero / primary product image;
2. additional verified product view;
3. verified feature / benefit image;
4. lifestyle scene;
5. person-use scene;
6. dimension / specification image;
7. material / structure detail;
8. packaging / included items;
9. semantic detail-page modules.

These are roles, not a mandatory fixed count.

## MUST

For every semantic asset record:
- \`id\`
- \`sku\` / variant
- \`role\`
- \`purpose\`
- \`buyer_question\`
- \`requested_by\` or planning rationale
- \`source_images\`
- \`supported_view\`
- \`product_pixel_policy\`
- \`scale_status\`
- \`dimension_source\`
- \`copy_evidence\`
- \`generation_method\`
- \`prompt_template\` where applicable
- \`output_profiles\`
- \`layer_plan\`
- \`acceptance_criteria\`
- \`risks\`
- \`status\`

## Product pixel policy

For authoritative product photos, default to \`SOURCE_PRODUCT_PIXEL\`.

Other allowed sources:
- \`VERIFIED_CAD_3D\`
- \`CONCEPT_ONLY\` with explicit non-factual labeling

## MUST NOT

- invent unsupported views;
- turn a generated lookalike into a SKU image;
- create dimension graphics from unknown values;
- infer packaging contents;
- imply unverified load / ergonomic benefits;
- treat a scene as metric when scale is unverified;
- claim a named output preset is platform-compliant without current verification;
- silently add deliverables unless the user asked for a complete set.

## Planning statuses

- \`READY\`
- \`REVIEW\`
- \`BLOCKED\`
- \`NOT_APPLICABLE\`

## Outputs

Create:
- \`image-plan.json\`
- \`plan-summary.md\`
- \`blocked-assets.md\`
- \`copy-deck.md\`

The plan is the source of truth for execution-state and Delivery Gate accounting.