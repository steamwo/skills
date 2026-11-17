---
name: marketplace-export-preflight
description: Verify current marketplace- and slot-specific image export requirements before producing platform variants; preserve product geometry while applying only compliant crop, scale, padding, compression, and naming operations.
---

# Marketplace Export Preflight

## Objective

Convert approved master assets into marketplace-specific exports without assuming stale platform rules.

## Inputs

MUST identify:
- marketplace;
- product category;
- image slot;
- current rule source;
- verification date;
- target device / surface when relevant.

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
- format;
- file size;
- transparency;
- allowed text / logo / watermark;
- hero-image background requirements;
- detail-page width / segmentation;
- color mode;
- category-specific constraints;
- naming.

## Allowed export operations

MAY:
- uniform resize;
- crop;
- padding;
- compression;
- format conversion;
- naming / directory organization.

MUST NOT:
- stretch product geometry;
- change SKU identity;
- generatively “repair” a crop;
- introduce new unverified text or claims during export.

## Status

- \`VERIFIED\`
- \`NEEDS_REVIEW\`
- \`BLOCKED\`

## China marketplace notes / 中国电商平台

淘宝、天猫、京东、拼多多的规则可能随类目、活动、客户端和卖家后台变化。

- 必须记录规则来源和核验日期。
- 不要把历史主图尺寸或详情页宽度写成永久硬编码规则。
- 如果用户只说“电商图一般 4:9”，应把它当作用户指定的设计比例，而不是所有平台的官方统一要求。

## Output

Create a \`platform-profile.json\` per marketplace / slot and an export preflight report.

Passing preflight means the file passed the recorded checks; it does not mean the marketplace guarantees acceptance.