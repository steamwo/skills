# Marketplace Export Checklist

## Before export

Record:
- marketplace;
- product category;
- image slot;
- official / seller-backend rule source;
- verification date;
- target surface / device if relevant.

## Verify

- width;
- height;
- aspect ratio;
- minimum resolution;
- file format;
- file size;
- transparency restrictions;
- background requirements;
- text / logo / watermark restrictions;
- detail-page width / segmentation rules;
- color mode;
- category-specific rules;
- filename conventions.

## Export operations

Allowed:
- uniform resize;
- crop;
- padding;
- compression;
- format conversion;
- naming.

Not allowed:
- non-uniform product stretch;
- generative product repair;
- adding unverified claims;
- changing SKU identity during export.

## China marketplace notes / 中国电商

淘宝、天猫、京东、拼多多的规则必须按当前类目和卖家后台核验。

用户指定的“4:9”“1:1”等设计比例可以作为交付要求，但不能自动解释为所有平台的统一官方规范。

如果平台规则不完整，使用 \`NEEDS_REVIEW\` 或 \`BLOCKED\`，不要声称已合规。