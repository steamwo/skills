# Agent Skill Specification Conventions

This repository is **English-first for machine-executable rules** and **Chinese-friendly for China-commerce localization**.

## Core production principles

### Explicit intent vs product evidence

User intent comes from explicit user input.

Product evidence may and often must be extracted from authoritative attachments.

Do not infer marketplace, ratio, language, style, or requested deliverables from product appearance.

### Buyer-decision-first planning

E-commerce completeness is measured by purchase-question coverage, not raw image count.

Each semantic asset SHOULD answer a concrete buyer question and cite evidence.

### SKU / variant scope

Every fact, copy block, product visual, dimension, and package claim SHOULD have scope:
- family;
- variant;
- bundle;
- market.

Use sharedness states:
- \`SHARED_VERIFIED\`
- \`VARIANT_SPECIFIC\`
- \`UNKNOWN_SHAREDNESS\`
- \`NOT_APPLICABLE\`

Unknown sharedness is not permission to reuse.

### Reusable master / derivative model

Prefer:
- authoritative source;
- reusable production master;
- semantic asset;
- surface / marketplace derivative.

A derivative MUST inherit product provenance, evidence, variant scope, and relevant copy version.

If an upstream dependency changes, downstream derivatives become stale.

### Preflight before expensive work

Validate source assets, tools, output destination, and required profiles before costly generation.

### Output profiles

Treat output as marketplace + surface + slot + device + preset.

Design preset ≠ verified compliance.

### Product pixel preservation

When an authoritative photo exists, default to source-product pixels.

Do not replace the SKU with a generated lookalike.

### Content before canvas

For detail pages, define semantic content and buyer question before choosing canvas dimensions.

Independent modules SHOULD be editable masters; long images are usually derivatives.

### Resumable execution

Use stable semantic asset IDs, checkpoints, dependency-aware invalidation, and recorded retries.

Do not duplicate expensive work because monitoring was interrupted.

### Delivery contracts

Track planned, blocked, produced, QA-completed, and delivered outputs.

Count expected deliverables by actual asset scope and output profile, not naive multiplication.

## Evidence states

- \`visible_in_reference\`
- \`user_confirmed\`
- \`document_verified\`
- \`estimated\`
- \`unknown\`
- \`conflicting\`

## Asset provenance classes

- \`SOURCE_PRODUCT_PIXEL\`
- \`VERIFIED_CAD_3D\`
- \`GENERATED_BACKGROUND\`
- \`GENERATED_PERSON\`
- \`GENERATED_PROP\`
- \`PROGRAMMATIC_TEXT_GRAPHIC\`
- \`CONCEPT_ONLY\`

## China marketplace notes / 中国电商平台说明

- 淘宝、天猫、1688、京东、拼多多、抖音等应按平台 + surface + slot + 端侧理解。
- 同一个 SKU 资产应尽量复用真实商品母版，再派生不同平台版本。
- 多规格商品必须区分共用资产和规格专属资产，禁止串 SKU。
- 中文标题、数字、Logo、尺寸线和参数表使用可控排版工具。