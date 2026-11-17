# steamwo / Skills

Reusable Agent Skills for Claude Code, Codex, Cursor, and similar agent environments.

This repository is **English-first for technical execution rules** and **Chinese-friendly for China-commerce workflows**. See [AGENT_SPEC_CONVENTIONS.md](./AGENT_SPEC_CONVENTIONS.md).

## E-commerce Product Visual Production Suite

The e-commerce suite turns real SKU references and verified product facts into a traceable set of product images, lifestyle scenes, person-use scenes, dimension graphics, detail modules, QA reports, and marketplace exports.

**Orchestrator:** [ecommerce-product-image-studio](./ecommerce-product-image-studio/SKILL.md)

### Core pipeline

\`\`\`text
product references
→ reference audit
→ product identity lock
→ physical dimension lock
→ scale / perspective calibration
→ gallery planning
→ source-pixel cutout
→ empty scene / person / graphics generation
→ compositing
→ typography / dimensions
→ visual QA
→ marketplace export preflight
\`\`\`

### Non-negotiable rule

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
| [ecommerce-visual-qa](./ecommerce-visual-qa/SKILL.md) | Identity, provenance, scale, copy, interaction, cross-image QA |
| [marketplace-export-preflight](./marketplace-export-preflight/SKILL.md) | Verify current marketplace export constraints |
| [wood-product-fidelity](./wood-product-fidelity/SKILL.md) | Wood-product-specific fidelity constraints |

## Default deliverables

A SKU project SHOULD include, where evidence supports them:
- multiple differentiated product / hero images;
- lifestyle scenes;
- person-use scenes when appropriate;
- verified dimension / specification graphics;
- material and structural detail images;
- packaging / included-item graphics when verified;
- independent detail-page modules;
- product identity, dimension, scale-calibration, provenance, and QA records.

Do not invent assets just to fill image slots.

## Quick start / 快速使用

Provide the SKU photos, verified product information, and target marketplace, then ask the agent:

> Use \`ecommerce-product-image-studio\` for this SKU. Audit the source assets first. Build the product identity and dimension records. Treat my product photo as authoritative. Do not redraw or replace the product. Use original product pixels for the product body, generate only independent scene/person/background layers, then composite and run provenance + identity + scale QA before producing the complete image set.

中文可以直接说：

> 使用 ecommerce-product-image-studio 处理这个 SKU。先审查素材和事实。我的商品实拍图是权威参考，禁止重新生成或替换商品本体；商品本体优先保留原图 RGB，只生成独立背景、人物和图形层，再合成并执行商品身份、像素来源、尺寸和尺度 QA。

## Design principles

- **Evidence before creativity.**
- **Source product pixels before generative product redraw.**
- **Physical dimensions before metric scene claims.**
- **No perspective repair by distorting product geometry.**
- **Programmatic typography for final Chinese copy and dimensions.**
- **Traceable source assets, masks, layers, prompts, tools, and QA.**
- **Current marketplace rules must be re-verified.**
- **Human review before publishing.**

This repository does not include a built-in image model, paid API key, or automatic product publishing.