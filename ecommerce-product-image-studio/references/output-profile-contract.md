# Output Profile Contract

## Purpose

Model e-commerce output as a **surface profile**, not merely a width:height ratio.

A marketplace may require different image families for:
- hero / gallery;
- detail page;
- A+ / enhanced content;
- desktop / web;
- mobile;
- SKU thumbnail;
- campaign / ad placement.

The semantic content may stay the same while composition, density, crop, typography, and canvas change.

## Design preset vs compliance profile

Two distinct concepts:

### Design preset

A user-selected layout target such as:
- \`1:1\`
- \`3:4\`
- \`4:9\`
- \`9:16\`
- a named A+ design tier

A design preset guides layout.

### Verified compliance profile

A profile backed by a current marketplace / seller-backend rule source and verification date.

Only a verified compliance profile may be described as platform-compliant.

## Profile fields

A profile SHOULD contain:
- \`profile_id\`
- \`marketplace\`
- \`surface\`
- \`slot\`
- \`device\`
- \`design_preset\`
- \`width_px\`
- \`height_px\`
- \`aspect_ratio\`
- \`safe_area\`
- \`text_density\`
- \`crop_policy\`
- \`module_policy\`
- \`rule_source\`
- \`verified_at\`
- \`compliance_status\`

Compliance statuses:
- \`DESIGN_ONLY\`
- \`VERIFIED\`
- \`NEEDS_REVIEW\`
- \`BLOCKED\`

## Responsive / multi-surface families

A single semantic module MAY produce multiple renders.

Example:

\`\`\`text
semantic module: "core feature + product close-up"
        ├── desktop / web render
        ├── mobile render
        └── marketplace-specific render
\`\`\`

These renders SHOULD share:
- copy source;
- claim evidence;
- product provenance;
- semantic priority.

They MAY differ in:
- crop;
- stacking;
- text size;
- line breaks;
- negative space;
- image-to-copy ratio.

Do not mechanically resize a desktop composition and call it a mobile composition when readability or hierarchy breaks.

## Named platform presets

Repository examples MAY include named presets such as Amazon A+ standard / premium web / premium mobile.

These names are useful as planning concepts, but their pixel dimensions MUST be re-verified before compliance export.

## China marketplace notes / 中国电商

淘宝、天猫、1688、京东、拼多多、抖音等也应按“surface profile”理解：
- 主图
- SKU 图
- 详情页分屏
- 长图
- 活动位
- 移动端展示

用户说“4:9”时，先视为设计比例；只有当对应平台规则经过核验后，才升级为合规 profile。