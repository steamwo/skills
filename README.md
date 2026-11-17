# steamwo / Skills

Reusable Agent Skills for Claude Code, Codex, Cursor, and similar agent environments.

This repository is **English-first for technical execution rules** and **Chinese-friendly for China-commerce workflows**.

See [AGENT_SPEC_CONVENTIONS.md](./AGENT_SPEC_CONVENTIONS.md).

## E-commerce Product Visual Production Suite

The e-commerce suite converts real SKU references and verified product facts into traceable product images, lifestyle scenes, person-use scenes, semantic detail modules, responsive/platform renders, QA records, and delivery manifests.

**Orchestrator:** [ecommerce-product-image-studio](./ecommerce-product-image-studio/SKILL.md)

### Core pipeline

\`\`\`text
explicit task intake
→ execution preflight
→ product reference audit
→ identity + dimension lock
→ scale / perspective calibration
→ semantic asset & detail-module planning
→ output-profile planning
→ deterministic prompt rendering
→ source-pixel cutout
→ empty scene / person generation
→ compositing
→ detail-module / responsive rendering
→ QA
→ resumable execution checkpoints
→ delivery gate
→ marketplace export preflight
\`\`\`

### Key contracts

The suite now separates:

1. **Task Input Contract** — what the user explicitly requested.
2. **Execution Preflight Contract** — whether source files, tools, output paths, and required capabilities are ready.
3. **Product Evidence Contract** — what authoritative product assets actually prove.
4. **Output Profile Contract** — marketplace + surface + slot + device + design preset, not merely aspect ratio.
5. **Detail Module Contract** — semantic content first, then render to desktop/mobile/platform profiles.
6. **Prompt Rendering Contract** — fixed templates + verified inputs.
7. **Execution State Contract** — stable asset IDs, checkpoints, resumable/idempotent retries.
8. **Product Pixel Contract** — authoritative product pixels remain the product.
9. **QA Contract** — identity, provenance, scale, prompt, profile, execution, delivery.
10. **Delivery Contract** — completion means the expected files were actually delivered.

### What was learned from form-driven expert skills

Useful ideas adopted:
- machine-readable input fields and legal options;
- explicit source policy for every field;
- preflight before expensive work;
- named surface/output profiles;
- modular detail-page design;
- responsive web/mobile variants;
- resumable execution that does not duplicate costly generation;
- exact delivery accounting.

Deliberate difference:
- this repository **must inspect product images** for product evidence and identity locking;
- it **must not** use image content to infer user intent such as platform, language, ratio, market, or style.

### Non-negotiable product rule

If the user provides an authoritative product photograph, the product MUST NOT be regenerated from text or replaced by a visually similar AI product.

Use:
- original product RGB + alpha mask; or
- a verified current-SKU CAD/3D render.

AI generation is primarily for empty backgrounds, environments, independent people, props, and layout concepts.

## Skills

| Skill | Responsibility |
|---|---|
| [ecommerce-product-image-studio](./ecommerce-product-image-studio/SKILL.md) | End-to-end orchestration |
| [product-reference-audit](./product-reference-audit/SKILL.md) | Source/evidence audit |
| [product-identity-lock](./product-identity-lock/SKILL.md) | SKU identity lock |
| [product-dimension-lock](./product-dimension-lock/SKILL.md) | Physical dimension lock |
| [product-scale-calibration](./product-scale-calibration/SKILL.md) | Scene/person scale calibration |
| [ecommerce-gallery-planner](./ecommerce-gallery-planner/SKILL.md) | Semantic asset family planning |
| [product-cutout-composite](./product-cutout-composite/SKILL.md) | Source-pixel cutout/compositing |
| [lifestyle-scene-composite](./lifestyle-scene-composite/SKILL.md) | Product lifestyle scenes |
| [human-lifestyle-composite](./human-lifestyle-composite/SKILL.md) | Independent person assets |
| [product-human-scene-integration](./product-human-scene-integration/SKILL.md) | Product/person/scene integration |
| [ecommerce-infographic-detail-builder](./ecommerce-infographic-detail-builder/SKILL.md) | Semantic detail modules + responsive renders |
| [brand-visual-system](./brand-visual-system/SKILL.md) | Brand presentation |
| [ecommerce-visual-qa](./ecommerce-visual-qa/SKILL.md) | Multi-gate QA |
| [marketplace-export-preflight](./marketplace-export-preflight/SKILL.md) | Marketplace/surface/slot export verification |
| [wood-product-fidelity](./wood-product-fidelity/SKILL.md) | Wood-product fidelity |

## Important principles

- Explicit intent before inferred defaults.
- Preflight before expensive generation.
- Evidence before creativity.
- Source product pixels before generative product redraw.
- Semantic content before canvas size.
- Output profile ≠ aspect ratio only.
- Named platform preset ≠ verified compliance.
- Separate desktop/mobile renders when hierarchy requires it.
- Stable asset IDs + resumable execution.
- Retry only invalidated stages.
- Programmatic typography for final Chinese copy and dimensions.
- Complete delivery requires delivered artifact accounting.

## China marketplace notes / 中国电商

淘宝、天猫、1688、京东、拼多多、抖音等平台应按“平台 + surface + slot + 端侧”处理，而不是记一个固定“平台尺寸”。

用户说“4:9”时，先视为设计比例。只有经过当前平台规则核验后，才能称为对应平台合规输出。