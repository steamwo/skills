---
name: ecommerce-infographic-detail-builder
description: Build traceable e-commerce copy, dimension graphics, structural callouts, detail-page modules, and long-form layouts from verified product data without delegating final numeric or Chinese text accuracy to image generation.
---

# Ecommerce Infographic & Detail Builder

## Objective

Turn verified product facts into readable, editable e-commerce graphics.

Image generation MAY provide background or visual atmosphere. Final customer-facing copy, numbers, dimension lines, logos, and tables SHOULD be laid out programmatically or in a design tool.

## Inputs

- product identity record;
- \`product-dimensions.json\`;
- approved claims and evidence;
- verified packaging / included items;
- brand system;
- image plan;
- marketplace constraints.

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

## Detail image design

A detail module SHOULD have one primary purpose:
- overall product;
- verified feature;
- lifestyle scene;
- material / structure detail;
- dimension / specification;
- packaging / included items;
- usage note.

For China-market detail pages, independent vertical modules are often preferable to one pre-stitched image when the user wants separately editable assets.

## Typography / 中国电商排版

中文标题、正文、单位、数字、尺寸线、Logo、图标：
- 应使用可控字体和排版工具；
- 不应依赖图像模型生成最终文案；
- 应检查错别字、数字、单位、标点、移动端可读性；
- 平台比例和画布尺寸以当前后台要求为准。

## Outputs

Create:
- \`copy-deck.md\`
- \`dimensions-source-map.md\`
- independent module images
- editable layout sources
- stitched long image only when requested / required
- infographic QA report

## Gate

A visually attractive infographic with an unsupported number or claim is \`FAIL\`.