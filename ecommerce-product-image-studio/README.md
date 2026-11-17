# E-commerce Product Image Studio

A fidelity-first production system for real e-commerce product families and SKUs.

## What the system optimizes

Not “generate more pictures”.

It optimizes:
- product truth;
- buyer-decision coverage;
- correct SKU / variant scope;
- reusable masters;
- targeted derivatives;
- multi-platform / multi-surface output;
- resumable production;
- QA-accounted delivery.

## Core contracts

- \`task-input-schema.json\` — explicit user intent
- \`execution-preflight.md\` — source/tool/output readiness
- \`buyer-decision-framework.md\` — purchase-question coverage
- \`variant-matrix-contract.md\` — family vs variant truth
- \`asset-reuse-contract.md\` — reusable masters and derivative graph
- \`output-profile-contract.md\` — marketplace / surface / device profiles
- \`detail-module-contract.md\` — semantic detail-page modules
- \`prompt-rendering.md\` — deterministic generation prompts
- \`execution-state-contract.md\` — resume / targeted invalidation
- \`delivery-gate.md\` — actual final derivative delivery

## Buyer-decision-first planning

A complete image set should answer the important buyer questions, for example:

\`\`\`text
What is it?
→ Is it for me?
→ Why choose it?
→ How is it used?
→ Will it fit?
→ Which variant should I choose?
→ What are the verified specs?
→ What is included?
\`\`\`

Image count is not the goal.

## Variant matrix

For multi-SKU families, create \`variant-matrix.json\`.

Do not assume all dimensions / product visuals / packaging / copy are shared.

Use:
- \`SHARED_VERIFIED\`
- \`VARIANT_SPECIFIC\`
- \`UNKNOWN_SHAREDNESS\`
- \`NOT_APPLICABLE\`

Unknown sharedness means “do not reuse yet”.

## Reuse / derivative graph

Prefer:

\`\`\`text
authoritative source
→ reusable production master
→ semantic asset
→ platform / surface derivative
\`\`\`

Example:

\`\`\`text
SOURCE product cutout
      ↓
lifestyle semantic composite
      ├── Taobao detail render
      ├── Amazon render
      └── mobile render
\`\`\`

Do not regenerate the real product for every marketplace.

## Detail modules

Independent semantic modules are preferred masters.

A long image is normally a derivative assembled from those modules.

## Delivery accounting

Expected outputs are calculated from:

\`\`\`text
semantic asset
× required variant scope
× requested output profiles
\`\`\`

not from:

\`\`\`text
SKU count × fixed image count
\`\`\`

This keeps shared assets shared and variant-bound assets correct.

## Product fidelity

If an authoritative product photo exists:

\`\`\`text
real SKU photo
→ reviewed alpha mask
→ ORIGINAL PRODUCT RGB
→ generated empty background / independent person
→ composite
→ semantic modules
→ profile derivatives
→ QA
\`\`\`

A generated lookalike is not the same SKU.

## Machine-readable examples

- \`templates/task-input.example.json\`
- \`templates/buyer-decision-map.example.json\`
- \`templates/variant-matrix.example.json\`
- \`templates/asset-derivation-map.example.json\`
- \`templates/output-profile.example.json\`
- \`templates/execution-state.example.json\`
- \`templates/delivery-manifest.example.json\`

## China marketplace notes / 中国电商

对于多规格商品，不建议“每个 SKU 从头生成一整套”。

正确做法是：
- 商品主体、尺寸、颜色、包装等按 SKU 锁定；
- 可共用背景、品牌系统和部分语义模块按证据复用；
- 再派生淘宝 / 天猫 / 1688 / 京东 / 拼多多 / 抖音 / Amazon 等平台版本；
- 最终逐个 variant + profile 做 QA。