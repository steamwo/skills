---
name: ecommerce-gallery-planner
description: Plan a complete evidence-backed e-commerce image set with distinct buyer-decision roles, source references, product-pixel policy, scale status, copy evidence, production method, and acceptance criteria.
---

# Ecommerce Gallery Planner

## Objective

Plan a complete image set where each asset answers a distinct buyer question. Do not create near-duplicate images just to fill slots.

## Required inputs

- \`product.json\`
- \`product-identity.json\`
- \`product-dimensions.json\`
- reference audit outputs
- \`scale-calibration.json\` for any scale-sensitive scene
- brand system if available
- current marketplace / slot requirements if known

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
- \`source_images\`
- \`supported_view\`
- \`product_pixel_policy\`
- \`scale_status\`
- \`dimension_source\`
- \`copy_evidence\`
- \`generation_method\`
- \`layer_plan\`
- \`acceptance_criteria\`
- \`risks\`
- \`status\`

## Product pixel policy

For authoritative product photos, default to:

\`SOURCE_PRODUCT_PIXEL\`

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
- treat a scene as metric when scale is unverified.

## Planning statuses

- \`READY\`
- \`REVIEW\`
- \`BLOCKED\`
- \`NOT_APPLICABLE\`

If an asset is blocked, record the missing source rather than filling it with invented content.

## China marketplace notes / 中国电商规划

淘宝、天猫、京东、拼多多的主图数量、视频封面、SKU 图、详情页模块等，应按当前类目和卖家后台核验。

中文详情页建议按购买决策组织，而不是机械重复卖点：
- 产品是什么
- 适合什么使用场景
- 可验证的结构 / 材质细节
- 已确认尺寸
- 包装 / 配件（已确认时）
- 使用提醒

## Outputs

Create:
- \`image-plan.json\`
- \`plan-summary.md\`
- \`blocked-assets.md\`
- \`copy-deck.md\`

When the user explicitly asks for direct execution, the agent MAY proceed to representative production samples, but MUST NOT skip identity / dimension / provenance requirements.