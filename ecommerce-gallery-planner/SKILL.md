---
name: ecommerce-gallery-planner
description: Plan a complete evidence-backed e-commerce image set with distinct buyer-decision roles, explicit requested deliverables, source references, product-pixel policy, scale status, copy evidence, production method, and acceptance criteria.
---

# Ecommerce Gallery Planner

## Objective

Plan a complete image set where each asset answers a distinct buyer question. Do not create near-duplicate images just to fill slots.

## Required inputs

- \`task-input.json\`
- \`product.json\`
- \`product-identity.json\`
- \`product-dimensions.json\`
- reference audit outputs
- \`scale-calibration.json\` for any scale-sensitive scene
- brand system if available
- current marketplace / slot requirements if known

## Requested deliverables rule

If the user explicitly requested deliverable types, the plan MUST respect that request.

Do not infer unrequested deliverables from:
- product category;
- uploaded image style;
- marketplace convention;
- an old default gallery.

If the user requested a “complete image set”, the planner MAY propose a complete role set, but unsupported roles remain \`BLOCKED\` rather than invented.

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
9. detail-page modules.

These are roles, not a mandatory fixed count.

## MUST

For every planned image record:
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
- \`layer_plan\`
- \`acceptance_criteria\`
- \`risks\`
- \`status\`

## Product pixel policy

For authoritative product photos, default to \`SOURCE_PRODUCT_PIXEL\`.

Do not plan a generative redraw of the product body as a normal production route.

Other allowed sources:
- \`VERIFIED_CAD_3D\`
- \`CONCEPT_ONLY\` with explicit non-factual labeling

## MUST NOT

- invent an unsupported rear / side / bottom view;
- turn a visually similar generated product into a SKU image;
- create dimension graphics from unknown values;
- infer packaging contents from the hero photo;
- use a person scene to imply unverified load capacity or ergonomic benefit;
- treat a scene as metric when scale is unverified;
- silently add deliverables the user did not request unless the user asked for a complete set.

## Planning statuses

- \`READY\`
- \`REVIEW\`
- \`BLOCKED\`
- \`NOT_APPLICABLE\`

If an asset is blocked, record the missing source rather than filling it with invented content.

## Outputs

Create:
- \`image-plan.json\`
- \`plan-summary.md\`
- \`blocked-assets.md\`
- \`copy-deck.md\`

The image plan becomes the source of truth for the Delivery Gate counters.