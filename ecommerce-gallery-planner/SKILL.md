---
name: ecommerce-gallery-planner
description: Plan a buyer-decision-driven e-commerce asset family across SKU variants, semantic modules, reusable masters, output profiles, provenance, scale status, dependencies, and acceptance criteria.
---

# Ecommerce Gallery Planner

## Objective

Plan the **minimum truthful asset family that resolves the important purchase questions**.

Do not optimize for raw image count.

Read:
- \`ecommerce-product-image-studio/references/buyer-decision-framework.md\`
- \`ecommerce-product-image-studio/references/variant-matrix-contract.md\`
- \`ecommerce-product-image-studio/references/asset-reuse-contract.md\`
- \`ecommerce-product-image-studio/references/output-profile-contract.md\`
- \`ecommerce-product-image-studio/references/detail-module-contract.md\`

## Required inputs

- \`task-input.json\`
- \`product.json\`
- \`product-identity.json\`
- \`product-dimensions.json\`
- \`variant-matrix.json\` when applicable
- \`buyer-decision-map.json\`
- reference audit outputs
- scale calibration for scale-sensitive scenes
- brand system if available
- output profile requirements

## Buyer-decision coverage

Every semantic asset SHOULD declare:
- \`decision_stage\`
- \`buyer_question\`
- \`decision_answer\`
- \`evidence_refs\`

Typical stages:
- recognition;
- relevance;
- value;
- usage;
- fit / scale;
- trust;
- specification;
- variant choice;
- included items;
- risk reduction.

Do not create near-duplicate assets that answer the same question unless they serve a distinct variant / profile / evidence need.

## Variant scope

Every semantic asset MUST declare one of:
- \`family\`
- one or more explicit \`variant_id\`
- \`bundle\`
- market-specific scope when needed.

Reuse requires verified sharedness.

Examples:
- brand typography module → often family-shared;
- 25cm dimension graphic → variant-specific;
- empty gym background → potentially reusable;
- 25cm product cutout → variant-specific;
- package contents → variant-specific unless verified shared.

## Asset reuse class

Every semantic asset SHOULD declare:
- \`reuse_class\`: \`FAMILY_SHARED\`, \`VARIANT_BOUND\`, or \`CONDITIONAL\`;
- \`parent_asset_ids\`;
- \`invalidation_inputs\`.

This allows the execution engine to reuse upstream masters without losing SKU correctness.

## Asset families

Distinguish:
- semantic asset / module;
- variant binding;
- output-profile renders.

Example:

\`\`\`text
semantic asset: "size selection"
  scope: family
  evidence: variant-matrix.json
  ├── zh-CN mobile render
  └── Amazon web render
\`\`\`

Do not duplicate evidence independently per render.

## Recommended roles

Use only when supported:
1. hero / primary product;
2. additional verified product view;
3. verified feature / benefit;
4. lifestyle scene;
5. person-use scene;
6. dimension / specification;
7. material / structure detail;
8. variant comparison;
9. packaging / included items;
10. usage / compatibility note;
11. semantic detail-page module.

These are roles, not a fixed mandatory count.

## Required record

For every semantic asset:
- \`asset_id\`
- \`role\`
- \`decision_stage\`
- \`buyer_question\`
- \`decision_answer\`
- \`variant_scope\`
- \`reuse_class\`
- \`requested_by\` or planning rationale
- \`source_images\`
- \`supported_view\`
- \`product_pixel_policy\`
- \`scale_status\`
- \`dimension_source\`
- \`copy_evidence\`
- \`generation_method\`
- \`prompt_template\`
- \`output_profiles\`
- \`parent_asset_ids\`
- \`invalidation_inputs\`
- \`acceptance_criteria\`
- \`risks\`
- \`status\`

## MUST NOT

- multiply all image roles by all SKUs automatically;
- reuse a product asset across variants when sharedness is unknown;
- invent unsupported views, dimensions, packaging, or claims;
- call independent AI-generated products a precise size comparison;
- create decorative duplicates while important buyer questions remain blocked;
- claim a named output preset is compliant without verification.

## Planning statuses

- \`READY\`
- \`REVIEW\`
- \`BLOCKED\`
- \`NOT_APPLICABLE\`

## Outputs

Create:
- \`buyer-decision-map.json\`
- \`image-plan.json\`
- \`variant-asset-map.json\`
- \`plan-summary.md\`
- \`blocked-assets.md\`
- \`copy-deck.md\`

The plan becomes the source of truth for execution-state, asset-derivation, QA, and Delivery Gate accounting.