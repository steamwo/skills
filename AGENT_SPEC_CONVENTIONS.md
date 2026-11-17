# Agent Skill Specification Conventions

This repository is **English-first for machine-executable technical rules** and **Chinese-friendly for China-commerce localization**.

## Language policy

Use English for execution logic, schemas, status enums, field names, gates, and cross-skill contracts.

Use Chinese or bilingual text for China marketplace notes, Chinese typography/copy guidance, and seller-facing examples.

## Normative keywords

- **MUST**: required.
- **MUST NOT**: prohibited.
- **SHOULD**: default unless documented otherwise.
- **MAY**: optional.
- **BLOCKED**: cannot safely continue.
- **REVIEW**: uncertainty remains.
- **PASS / FAIL / NOT_CHECKED**: QA states.

## Input contracts

Structured skills SHOULD define machine-readable input contracts.

Fields SHOULD define:
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
- output / surface profile;
- language;
- style;
- requested deliverables;
- extra requirements.

**Product evidence** MAY and often MUST be extracted from authoritative attachments:
- visible geometry;
- component count;
- hardware;
- texture / color;
- supported camera view;
- verified dimensions shown in source documents.

Do not infer intent from evidence.

## Preflight before expensive work

Long or costly workflows SHOULD validate:
- source assets;
- required tools;
- output destination;
- requested surface/profile;
- known blockers

before expensive generation starts.

Preprocessing MUST be non-destructive and traceable.

Preprocessing MAY make a source usable but MUST NOT alter user intent or product truth.

## Evidence states

Use:
- \`visible_in_reference\`
- \`user_confirmed\`
- \`document_verified\`
- \`estimated\`
- \`unknown\`
- \`conflicting\`

Never silently promote \`estimated\` or \`unknown\` to verified.

## Output profiles

Treat output as **marketplace + surface + slot + device + design preset**, not merely an aspect ratio.

Distinguish:
- design preset;
- verified compliance profile.

A named marketplace preset is not proof of current compliance.

When desktop / mobile layouts differ materially, create separate renders rather than blindly resizing.

## Deterministic prompt rendering

When a stable prompt template exists:
- render from verified structured inputs;
- omit missing optional blocks;
- block unresolved required placeholders;
- preserve fixed fidelity constraints;
- do not enrich requirements with generic goals the user did not state.

## Product identity rule

When the user provides an authoritative product photograph, default to pixel preservation.

\`\`\`text
AUTHORITATIVE PRODUCT PHOTO
        ↓
reference audit
        ↓
identity lock
        ↓
alpha mask
        ↓
ORIGINAL PRODUCT RGB
        ↓
empty generated scene / person
        ↓
scale calibration
        ↓
compositing
        ↓
detail modules / typography
        ↓
QA
        ↓
delivery gate
\`\`\`

A visually similar generated product is not the same SKU.

## Product Pixel Preservation Rule

**MUST**
- preserve source product geometry and visible identity;
- keep product RGB traceable to a source photo or verified CAD/3D.

**MUST NOT**
- regenerate the product from text;
- substitute a lookalike;
- alter geometry to fit a scene;
- invent unseen product facts.

## Detail-page modules

Detail pages SHOULD be modeled as independent semantic modules.

Plan content before canvas.

A semantic module MAY render to multiple output profiles while inheriting the same:
- claim evidence;
- SKU identity;
- product provenance;
- dimensions.

A stitched long image SHOULD usually be a derivative, not the only editable master.

## Resumable execution

Multi-step skills SHOULD maintain stable asset IDs and durable checkpoints.

On resume:
- reuse valid completed artifacts;
- continue from the first invalid/incomplete stage;
- do not duplicate expensive work simply because monitoring was interrupted.

Input changes SHOULD invalidate only dependent downstream stages.

Retries MUST record why they occurred.

## Asset provenance classes

Use:
- \`SOURCE_PRODUCT_PIXEL\`
- \`VERIFIED_CAD_3D\`
- \`GENERATED_BACKGROUND\`
- \`GENERATED_PERSON\`
- \`GENERATED_PROP\`
- \`PROGRAMMATIC_TEXT_GRAPHIC\`
- \`CONCEPT_ONLY\`

## Delivery contracts

Artifact-generating skills SHOULD track:
- planned;
- blocked;
- produced;
- QA-completed;
- delivered.

Do not claim complete delivery unless every expected final asset has a user-accessible reference.

## China marketplace notes / 中国电商平台说明

- 淘宝、天猫、1688、京东、拼多多、抖音等应按 surface / slot 理解，不只是单一“平台尺寸”。
- 历史尺寸或示例档位不能硬编码成永久规则。
- 中文标题、数字、Logo、尺寸线和参数表使用可控排版工具。