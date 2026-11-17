# Agent Skill Specification Conventions

This repository is **English-first for machine-executable technical rules** and **Chinese-friendly for China-commerce localization**.

The goal is not to translate everything into English. The goal is to make the rules easier for Claude Code, Codex, Cursor, and other agents to execute consistently while keeping Chinese marketplace terminology and user-facing copy practical.

## Language policy

Use **English** for:
- YAML front matter: \`name\`, \`description\`.
- Section names that define execution logic.
- Status enums, field names, JSON keys, file names, directory names.
- \`MUST\`, \`MUST NOT\`, \`SHOULD\`, \`MAY\` rules.
- Inputs, outputs, gates, failure conditions, and pipeline steps.
- Cross-skill contracts.

Use **Chinese or bilingual text** for:
- Taobao / Tmall / JD / PDD operational notes.
- Chinese typography and copywriting guidance.
- Seller-facing examples.
- User-facing Chinese e-commerce text templates.
- Marketplace-specific terminology that would be less clear if translated.

## Normative keywords

- **MUST**: required for a valid execution.
- **MUST NOT**: prohibited.
- **SHOULD**: default behavior unless there is a documented reason to differ.
- **MAY**: optional.
- **BLOCKED**: execution cannot safely continue.
- **REVIEW**: execution may continue only with explicit uncertainty recorded.
- **PASS / FAIL / NOT_CHECKED**: QA states.

## Evidence states

Use these normalized evidence states whenever product facts are recorded:

- \`visible_in_reference\`
- \`user_confirmed\`
- \`document_verified\`
- \`estimated\`
- \`unknown\`
- \`conflicting\`

Never silently promote \`estimated\` or \`unknown\` to a verified state.

## Product identity rule

When the user provides an authoritative product photograph, the default production route is **pixel preservation**, not product regeneration.

\`\`\`text
AUTHORITATIVE PRODUCT PHOTO
        ↓
reference audit
        ↓
identity lock
        ↓
segmentation / alpha mask
        ↓
ORIGINAL PRODUCT RGB
        ↓
empty generated scene / graphics / person layers
        ↓
scale + perspective calibration
        ↓
compositing
        ↓
typography / dimensions
        ↓
QA
\`\`\`

A visually similar AI-generated product is **not** the same SKU.

## Product Pixel Preservation Rule

When a source photo is authoritative:

**MUST**
- preserve source product geometry;
- preserve visible hardware locations;
- preserve component count and support shape;
- preserve visible texture, grain, color, logos, seams, holes, and edge profiles;
- preserve the source camera view unless another verified view is available;
- keep the product RGB traceable to a source photo or verified CAD/3D render.

**MUST NOT**
- regenerate the product from text;
- use image-to-image generation that redraws the product body;
- substitute a visually similar product;
- change geometry to make a scene easier to compose;
- invent unseen sides, hidden construction, accessories, or dimensions;
- treat prompt fidelity as product fidelity.

## Asset provenance classes

Every visual asset SHOULD be tagged as one of:

- \`SOURCE_PRODUCT_PIXEL\`
- \`VERIFIED_CAD_3D\`
- \`GENERATED_BACKGROUND\`
- \`GENERATED_PERSON\`
- \`GENERATED_PROP\`
- \`PROGRAMMATIC_TEXT_GRAPHIC\`
- \`CONCEPT_ONLY\`

The final QA report MUST make product pixel provenance explicit.

## China marketplace notes / 中国电商平台说明

For 淘宝、天猫、京东、拼多多:
- MUST verify current category- and slot-specific rules before export.
- 不要把旧版平台尺寸要求硬编码为永久规则。
- 以当前卖家后台、官方帮助文档或用户提供的规则截图为准。
- 中文标题、尺寸数字、Logo、图标应由排版工具生成，而不是依赖图像模型生成最终文字。