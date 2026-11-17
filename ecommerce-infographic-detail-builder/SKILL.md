---
name: ecommerce-infographic-detail-builder
description: Build evidence-backed e-commerce detail-page modules, dimension graphics, structural callouts, responsive surface variants, and optional long-form derivatives from verified product data.
---

# Ecommerce Infographic & Detail Builder

## Objective

Build product detail content as **independent semantic modules** that can be rendered into different marketplace, desktop, mobile, and long-image profiles without changing product facts.

Read:
- \`ecommerce-product-image-studio/references/detail-module-contract.md\`
- \`ecommerce-product-image-studio/references/output-profile-contract.md\`

## Inputs

- \`task-input.json\`
- product identity record
- \`product-dimensions.json\`
- approved claims and evidence
- verified packaging / included items
- brand system
- image plan
- one or more output profiles

## Content-before-canvas rule

Plan semantic content first:
- what buyer question this module answers;
- which verified facts / claims it communicates;
- which product source it uses.

Only then choose a canvas / surface profile.

MUST NOT distort content strategy merely to fit a remembered platform size.

## Module model

Each module SHOULD define:
- \`module_id\`
- role
- buyer question
- semantic priority
- source product asset
- verified claims
- copy source
- product provenance
- dimension source
- output profiles
- dependencies
- QA status

Typical module roles:
- product overview
- verified feature
- lifestyle use
- material / structure
- dimensions / specification
- comparison
- packaging / included items
- usage / care note

## Independent-master rule

Independent modules SHOULD be the editable masters.

A stitched long image MAY be created as a derivative when requested or required, but MUST NOT be the only source of truth.

## Multi-surface / responsive rendering

One semantic module MAY render to:
- desktop / web
- mobile
- generic detail-page module
- named marketplace surface
- long-image derivative

Different renders SHOULD share:
- copy evidence
- SKU / variant
- product provenance
- semantic priority

They MAY change:
- crop
- stacking
- typography scale
- line breaks
- negative space
- image / copy balance

Do not mechanically shrink a desktop module into a mobile module if hierarchy or readability breaks.

## Dimension graphic rules

**MUST**
- use only verified values by default;
- preserve axis definitions;
- distinguish product vs packaging dimensions;
- distinguish net vs gross weight;
- distinguish folded / assembled / extended states;
- point dimension arrows to the correct physical boundaries;
- keep a source map for every published number.

**MUST NOT**
- infer dimensions from a lifestyle scene;
- infer dimensions from person scale;
- fill unknown axes with estimated numbers;
- mix packaging values into product values;
- let an image model invent numeric labels.

If only one dimension is confirmed, only show that dimension.

## Copy rules

Each claim MUST map to:
- user confirmation;
- visible evidence;
- official current-SKU documentation.

Unsupported marketing copy is removed or marked for review.

## Named platform presets

Named presets such as Amazon A+ standard / premium web / premium mobile MAY be used as planning labels.

Their pixel dimensions MUST be re-verified before compliance export. A named preset alone is \`DESIGN_ONLY\`, not proof of marketplace compliance.

## Typography / 中国电商排版

中文标题、正文、单位、数字、尺寸线、Logo、图标：
- 使用可控字体和排版工具；
- 不依赖图像模型生成最终文案；
- 检查错别字、数字、单位、标点和移动端可读性；
- 平台比例和画布尺寸以当前后台 / 官方要求为准。

## Outputs

Create:
- \`copy-deck.md\`
- \`dimensions-source-map.md\`
- module manifest
- independent module images
- output-profile variants
- editable layout sources
- stitched long image only when requested / required
- infographic QA report

## Gate

A visually attractive module with unsupported claims, unverified numeric specs, or a falsely claimed platform profile is \`FAIL\`.