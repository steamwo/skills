---
name: ecommerce-gallery-planner
description: Plan a buyer-decision-driven ecommerce asset family with platform-specific conversion mix, SKU/variant scope, commercial shot roles, reusable masters, output profiles, and candidate strategy.
---

# Ecommerce Gallery Planner

## Objective

Plan the minimum truthful asset family that resolves important buying questions **in the visual language of the target platform**.

Do not optimize for raw image count.

Read:
- buyer decision framework;
- variant matrix contract;
- asset reuse contract;
- platform commerce style contract;
- commercial scene router;
- output profile contract.

## Platform conversion mix

Platform selection changes the **asset mix and visual emphasis**, not product facts.

### Taobao / Tmall / 1688 heuristic

Prioritize a balanced sequence:
- clear hero;
- 1–2 high-priority selling-point graphics;
- believable lifestyle / use scene;
- material / structure detail;
- verified specification / dimensions;
- variant choice;
- package / included items when verified;
- modular detail-page screens.

The set should progressively answer buying questions rather than repeat mood imagery.

### Pinduoduo heuristic

Prioritize:
- instantly legible hero;
- core value / reason-to-buy;
- variant / bundle clarity;
- verified specification;
- direct usage proof;
- package / quantity when verified.

Use short, high-salience hierarchy. Avoid tiny copy and decorative luxury layouts that hide the product.

### Douyin heuristic

Prioritize:
- strong mobile hero / cover;
- in-use lifestyle scene;
- person interaction where useful;
- one clear benefit per asset;
- product detail proof;
- compact specification after interest is established.

The set should feel content-native and believable, not like a sterile catalog assembled from pasted cutouts.

## Buyer-decision coverage

Every semantic asset SHOULD declare:
- \`decision_stage\`
- \`buyer_question\`
- \`decision_answer\`
- \`evidence_refs\`

One asset should have one dominant conversion job.

## Shot roles

Recommended roles:
1. hero / recognition;
2. selling-point / single benefit;
3. lifestyle / context;
4. person-use / action;
5. macro / material proof;
6. structure / component proof;
7. specification / dimensions;
8. variant comparison;
9. package / included items;
10. detail-page semantic module.

Do not add another role if it does not answer a new question.

## Candidate strategy

For each generative asset record:
- \`candidate_count\`
- \`creative_axis\`
- \`fidelity_mode\`
- \`platform_style_profile\`

Default heuristics:
- hero: 2–3 candidates;
- lifestyle: 2–3;
- person-use: 2–3;
- deterministic dimension graphic: 1.

## Required record

For every semantic asset:
- \`asset_id\`
- \`role\`
- \`decision_stage\`
- \`buyer_question\`
- \`decision_answer\`
- \`variant_scope\`
- \`reuse_class\`
- \`source_images\`
- \`identity_lock_version\`
- \`campaign_style_version\`
- \`platform_style_profile\`
- \`fidelity_mode\`
- \`candidate_count\`
- \`commercial_shot_brief\`
- \`product_salience_target\`
- \`scale_status\`
- \`dimension_source\`
- \`copy_evidence\`
- \`output_profiles\`
- \`dependencies\`
- \`acceptance_criteria\`
- \`status\`

## MUST NOT

- multiply all roles by all SKUs automatically;
- make eight generic “nice scenes” with no distinct buying job;
- use the same shot grammar for every platform;
- reuse a product asset across variants when sharedness is unknown;
- turn a generated lookalike into a precise specification asset;
- claim heuristic platform style is official compliance.

## Outputs

Create:
- \`buyer-decision-map.json\`
- \`image-plan.json\`
- \`variant-asset-map.json\`
- \`platform-asset-mix.json\`
- \`plan-summary.md\`
- \`blocked-assets.md\`
- \`copy-deck.md\`.