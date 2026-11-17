# Agent Skill Specification Conventions

This repository is **English-first for machine-executable technical rules** and **Chinese-friendly for China-commerce localization**.

The goal is not to translate everything into English. The goal is to make rules easier for Claude Code, Codex, Cursor, and similar agents to execute consistently.

## Language policy

Use **English** for:
- YAML front matter;
- execution logic;
- status enums;
- field names / JSON keys;
- MUST / MUST NOT / SHOULD / MAY rules;
- inputs, outputs, gates, failure conditions;
- cross-skill contracts.

Use **Chinese or bilingual text** for:
- China marketplace notes;
- Chinese typography / copy guidance;
- seller-facing examples;
- marketplace terminology where Chinese is clearer.

## Normative keywords

- **MUST**: required.
- **MUST NOT**: prohibited.
- **SHOULD**: default unless documented otherwise.
- **MAY**: optional.
- **BLOCKED**: cannot safely continue.
- **REVIEW**: uncertainty remains.
- **PASS / FAIL / NOT_CHECKED**: QA states.

## Input contracts

Skills SHOULD define a machine-readable input contract when inputs are structured or configurable.

Input fields SHOULD state:
- type;
- required / optional;
- legal options;
- source policy;
- omission / default behavior.

### Intent vs evidence

**User intent** MUST come from explicit user input:
- target platform;
- target market;
- image ratio;
- output language;
- requested style;
- requested deliverables;
- additional requirements.

Do not infer these from attachment content, filename, product category, or common practice.

**Product evidence** MAY and often MUST be extracted from authoritative attachments:
- visible product geometry;
- component count;
- hardware;
- texture / color;
- supported camera view;
- verified dimensions shown in source documents.

This repository intentionally distinguishes intent inference from evidence extraction.

## Evidence states

Use:
- \`visible_in_reference\`
- \`user_confirmed\`
- \`document_verified\`
- \`estimated\`
- \`unknown\`
- \`conflicting\`

Never silently promote \`estimated\` or \`unknown\` to verified.

## Deterministic prompt rendering

When a stable prompt template exists:
- render from verified structured inputs;
- remove missing optional blocks;
- block unresolved required placeholders;
- preserve fixed fidelity constraints;
- do not enrich user requirements with generic goals the user did not state.

Prompt traceability SHOULD be saved with the resulting asset.

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
        ↓
delivery gate
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
- keep product RGB traceable to a source photo or verified CAD/3D render.

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

## Delivery contracts

A skill that creates artifacts SHOULD define completion in terms of delivered outputs, not only successful generation.

Track:
- planned;
- blocked;
- produced;
- QA-completed;
- delivered.

Do not claim complete delivery unless every expected final asset has a user-accessible reference.

## China marketplace notes / 中国电商平台说明

For 淘宝、天猫、京东、拼多多:
- MUST verify current category- and slot-specific rules before export.
- 不要把旧版平台尺寸要求硬编码为永久规则。
- 以当前卖家后台、官方帮助文档或用户提供的规则截图为准。
- 中文标题、尺寸数字、Logo、图标应由排版工具生成，而不是依赖图像模型生成最终文字。