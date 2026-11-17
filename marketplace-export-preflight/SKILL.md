---
name: marketplace-export-preflight
description: Verify current marketplace-, surface-, slot-, and device-specific export requirements before producing platform variants; distinguish design presets from verified compliance profiles and preserve product identity during export.
---

# Marketplace Export Preflight

## Objective

Convert approved masters into marketplace-specific output profiles without assuming stale rules.

Read \`ecommerce-product-image-studio/references/output-profile-contract.md\`.

## Inputs

MUST identify when platform-specific export is requested:
- marketplace
- product category
- surface / content type
- slot
- device / web / mobile when relevant
- current rule source
- verification date

## Design preset vs compliance

A design preset such as:
- 1:1
- 3:4
- 4:9
- Amazon A+ standard
- Amazon Premium A+ web
- Amazon Premium A+ mobile

is a layout target.

It is **not automatically a verified marketplace rule**.

Only a profile with current rule source + verification date may use \`VERIFIED\`.

## Rule source priority

Prefer:
1. current seller backend;
2. current official marketplace documentation;
3. user-provided current rule screenshots / docs.

Do not rely on memory for current compliance.

## Verify

As applicable:
- width / height / aspect ratio;
- minimum resolution;
- device-specific requirements;
- safe area;
- module / slot restrictions;
- format;
- file size;
- transparency;
- allowed text / logo / watermark;
- hero-image background requirements;
- detail-page segmentation;
- color mode;
- category-specific constraints;
- naming.

## Responsive output rule

If the same semantic content must serve web and mobile:
- create separate layout renders when needed;
- do not mechanically resize when readability, hierarchy, or product visibility degrades;
- inherit the same verified claims and product provenance.

## Allowed export operations

MAY:
- uniform resize;
- crop;
- padding;
- compression;
- format conversion;
- naming / directory organization;
- profile-specific layout rendering.

MUST NOT:
- stretch product geometry;
- change SKU identity;
- generatively “repair” a crop;
- introduce new unverified text or claims during export.

## Status

- \`DESIGN_ONLY\`
- \`VERIFIED\`
- \`NEEDS_REVIEW\`
- \`BLOCKED\`

## China marketplace notes / 中国电商平台

淘宝、天猫、1688、京东、拼多多、抖音等都应按 surface / slot 理解，而不是只有一个“平台尺寸”。

用户指定 4:9 等比例时，先视为设计要求；对应平台规则经过核验后，才升级为合规 profile。

## Output

Create \`platform-profile.json\` / output-profile records per marketplace + surface + slot + device and an export preflight report.

Passing preflight means the file passed the recorded checks; it does not guarantee marketplace acceptance.