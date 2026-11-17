# steamwo / Skills

Reusable Agent Skills for Claude Code, Codex, Cursor, and similar agent environments.

This repository is **English-first for technical execution rules** and **Chinese-friendly for China-commerce workflows**. See [AGENT_SPEC_CONVENTIONS.md](./AGENT_SPEC_CONVENTIONS.md).

## E-commerce Product Visual Production Suite

The e-commerce suite turns real SKU references and verified product facts into a traceable set of product images, lifestyle scenes, person-use scenes, dimension graphics, detail modules, QA reports, and marketplace exports.

**Orchestrator:** [ecommerce-product-image-studio](./ecommerce-product-image-studio/SKILL.md)

### Core pipeline

\`\`\`text
explicit task intake
→ product reference audit
→ product identity lock
→ physical dimension lock
→ scale / perspective calibration
→ gallery planning
→ deterministic prompt rendering
→ source-pixel cutout
→ empty scene / person / graphics generation
→ compositing
→ typography / dimensions
→ visual QA
→ delivery gate
→ marketplace export preflight
\`\`\`

### Execution contracts

The orchestrator now separates four contracts:

1. **Task input contract** — what the user explicitly requested.
2. **Product evidence contract** — what authoritative product assets actually prove.
3. **Prompt rendering contract** — fixed templates + verified inputs, with unresolved required placeholders blocked rather than guessed.
4. **Delivery contract** — planned, produced, QA-completed, and actually delivered assets must reconcile before the run is called complete.

This matters because user intent and product evidence are different things.

For example:
- product images MUST be inspected to lock geometry and visible details;
- product images MUST NOT be used to guess marketplace, language, ratio, target market, style, or extra requirements.

### Non-negotiable product rule

If the user provides an authoritative product photograph, the product MUST NOT be regenerated from text or replaced by a visually similar AI product.

Use:
- original product RGB + alpha mask, or
- a verified CAD/3D render for the same SKU.

AI generation is primarily for:
- empty backgrounds;
- environments;
- independent people;
- non-product props;
- layout concepts.

A prompt that says “preserve the product” is not enough. Product fidelity is established by pixel / asset provenance and QA.

## Skills

| Skill | Responsibility |
|---|---|
| [ecommerce-product-image-studio](./ecommerce-product-image-studio/SKILL.md) | End-to-end orchestration |
| [product-reference-audit](./product-reference-audit/SKILL.md) | Audit source images, specs, CAD, packaging, evidence gaps |
| [product-identity-lock](./product-identity-lock/SKILL.md) | Lock SKU geometry, structure, appearance, visible details |
| [product-dimension-lock](./product-dimension-lock/SKILL.md) | Build traceable physical dimension records |
| [product-scale-calibration](./product-scale-calibration/SKILL.md) | Calibrate product / scene / person scale and perspective |
| [ecommerce-gallery-planner](./ecommerce-gallery-planner/SKILL.md) | Plan distinct hero, scene, dimension, detail, packaging modules |
| [product-cutout-composite](./product-cutout-composite/SKILL.md) | Preserve source product RGB and composite with alpha masks |
| [lifestyle-scene-composite](./lifestyle-scene-composite/SKILL.md) | Build scale-aware product lifestyle scenes |
| [human-lifestyle-composite](./human-lifestyle-composite/SKILL.md) | Plan people, poses, actions, and person layers |
| [product-human-scene-integration](./product-human-scene-integration/SKILL.md) | Integrate product + person + scene without product redraw |
| [ecommerce-infographic-detail-builder](./ecommerce-infographic-detail-builder/SKILL.md) | Build dimension, copy, detail, and long-form modules |
| [brand-visual-system](./brand-visual-system/SKILL.md) | Keep brand presentation consistent without recoloring product |
| [ecommerce-visual-qa](./ecommerce-visual-qa/SKILL.md) | Identity, provenance, scale, prompt, delivery, cross-image QA |
| [marketplace-export-preflight](./marketplace-export-preflight/SKILL.md) | Verify current marketplace export constraints |
| [wood-product-fidelity](./wood-product-fidelity/SKILL.md) | Wood-product-specific fidelity constraints |

## Machine-readable intake

The orchestrator includes:
- \`references/task-input-schema.json\`
- \`templates/task-input.example.json\`
- \`scripts/validate_task_input.py\`

This keeps configurable inputs explicit and source-traceable instead of letting the agent silently infer them.

## Default deliverables

A SKU project SHOULD include, where evidence and user intent support them:
- multiple differentiated product / hero images;
- lifestyle scenes;
- person-use scenes when appropriate;
- verified dimension / specification graphics;
- material and structural detail images;
- packaging / included-item graphics when verified;
- independent detail-page modules;
- product identity, dimension, scale-calibration, provenance, prompt, QA, and delivery records.

Do not invent assets just to fill image slots.

## Quick start / 快速使用

Provide the SKU photos and your actual business requirements, then ask:

> Use \`ecommerce-product-image-studio\` for this SKU. Build task-input.json from what I explicitly requested. Inspect my product photos for product evidence, but do not infer my marketplace, ratio, language, target market, or style from the images. Treat my product photo as authoritative. Do not redraw or replace the product. Use deterministic scene/person prompt templates, composite original product pixels, run QA, and do not claim completion until the delivery manifest reconciles all expected assets.

中文可以直接说：

> 使用 ecommerce-product-image-studio 处理这个 SKU。先把我明确说过的需求写入 task-input.json；商品图片必须读取用于商品身份锁定，但不要从图片猜平台、比例、语言、市场或风格。商品实拍图是权威参考，禁止重新生成或替换商品本体。背景和人物按模板生成，商品使用原图像素合成，最后做 QA 和 Delivery Gate，实际交付数量对不上就不能说“全部完成”。

## Design principles

- **Explicit intent before inferred defaults.**
- **Evidence before creativity.**
- **Source product pixels before generative product redraw.**
- **Physical dimensions before metric scene claims.**
- **Deterministic prompt templates before free-form prompt improvisation.**
- **No perspective repair by distorting product geometry.**
- **Programmatic typography for final Chinese copy and dimensions.**
- **Traceable source assets, masks, prompts, layers, tools, QA, and delivery.**
- **Current marketplace rules must be re-verified.**
- **Human review before publishing.**

This repository does not include a built-in image model, paid API key, or automatic product publishing.