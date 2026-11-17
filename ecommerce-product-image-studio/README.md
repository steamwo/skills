# E-commerce AI Product Visual Production Suite

This is the orchestrator package for the e-commerce visual workflow.

## Key architecture

The workflow now has four explicit contracts before and after generation:

1. **Task input contract** — what the user actually requested.
2. **Product evidence contract** — what authoritative product assets actually prove.
3. **Prompt rendering contract** — how generation prompts are built deterministically.
4. **Delivery contract** — what must exist, pass QA, and be surfaced before the task is called complete.

This separation prevents two common failures:
- inferring user intent from the product image;
- generating files but not actually delivering / accounting for them.

## Intake

Read:
- \`references/task-input-schema.json\`
- \`references/intake-contract.md\`

Create \`task-input.json\`.

Important distinction:

- **User intent** such as marketplace, ratio, language, market, requested style, deliverables, and extra requirements comes from explicit user input.
- **Product evidence** such as visible geometry, hardware, texture, and supported view MUST be extracted from authoritative product images.

商品图片必须读取用于商品身份锁定；但不能从图片去猜用户要淘宝还是 Amazon、中文还是英文、4:9 还是 1:1。

Validate intake:

\`\`\`bash
python ecommerce-product-image-studio/scripts/validate_task_input.py \
  --input sku-001/task-input.json
\`\`\`

## Product fidelity

If the user supplies a real SKU photo:

\`\`\`text
real SKU photo
→ alpha mask
→ ORIGINAL PRODUCT RGB
→ generated EMPTY background / independent person
→ scale-aware compositing
→ programmatic typography
→ QA
\`\`\`

A generated lookalike is not the same SKU.

## Deterministic prompts

Read:
- \`references/prompt-rendering.md\`
- \`templates/empty-scene-prompt.md\`
- \`templates/person-layer-prompt.md\`

Required unresolved placeholders block the asset. Optional absent fields are omitted. Fixed product-exclusion clauses are never removed.

## Delivery gate

Read \`references/delivery-gate.md\`.

Create \`delivery-manifest.json\` and track:
- planned;
- blocked;
- expected;
- produced;
- QA-completed;
- delivered.

Do not claim “complete” unless every expected final asset has QA status and an accessible delivery reference.

## Project structure

\`\`\`text
sku-001/
  input/
  task-input.json
  product.json
  product-identity.json
  product-dimensions.json
  brand.json
  plan/
    asset-audit.md
    evidence-matrix.json
    missing-assets.md
    image-plan.json
    scale-calibration.json
    copy-deck.md
  work/
    prompts/
    masks/
    cutouts/
    backgrounds/
    people/
    shadows/
    composites/
    layouts/
  output/
    master/
    platform/
    detail-modules/
  qa/
    per-image/
    qa-report.md
  delivery-manifest.json
\`\`\`

## China marketplace notes / 中国电商说明

淘宝、天猫、京东、拼多多的主图槽位、详情页宽度、文字限制和文件大小等必须按当前卖家后台 / 官方资料核验。

用户指定的 4:9、1:1 等比例可以作为设计要求，但不能自动解释为所有平台的统一官方规则。

中文、数字、尺寸线、Logo 和参数表使用可控排版工具，不依赖图像模型生成最终文字。