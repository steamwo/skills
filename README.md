# steamwo / Skills

Reusable Agent Skills for e-commerce visual production.

This repository is **English-first for machine-executable rules** and **Chinese-friendly for China-commerce workflows**.

**Orchestrator:** [ecommerce-product-image-studio](./ecommerce-product-image-studio/SKILL.md)

## Positioning

This is not a generic “AI image prompt collection”.

It is an **E-commerce Visual Production System** designed around:
- real SKU fidelity;
- product-family / variant correctness;
- buyer-decision coverage;
- reusable production masters;
- multi-platform derivatives;
- resumable execution;
- evidence-backed QA;
- accountable delivery.

## Production model

\`\`\`text
explicit task intake
→ execution preflight
→ product evidence audit
→ product family / variant matrix
→ identity + dimensions
→ buyer-decision map
→ semantic asset planning
→ scale calibration
→ reusable master production
→ asset derivation graph
→ output profiles
→ responsive / marketplace renders
→ QA
→ delivery gate
→ export
\`\`\`

## E-commerce completeness

A “complete set” is not defined by a fixed number such as 8 or 9 images.

It is defined by whether the required purchase questions are truthfully covered:
- product recognition;
- relevance / use case;
- verified value / benefit;
- usage;
- fit / scale;
- trust / construction;
- specifications;
- variant selection;
- included items;
- risk / compatibility notes.

## SKU / variant production

For a product family:

\`\`\`text
family
├── shared verified assets
├── variant A bound assets
├── variant B bound assets
└── unknown-sharedness assets → REVIEW / BLOCKED
\`\`\`

Do not multiply every image by every SKU.

Do not reuse a product image / dimension / packaging fact across variants unless the sharedness is verified.

## Asset reuse

Use a derivative graph:

\`\`\`text
authoritative source
→ reviewed production master
→ semantic asset
→ marketplace / surface / language derivative
\`\`\`

Examples:
- real product cutout can feed multiple marketplace compositions;
- one verified semantic detail module can render to mobile / web profiles;
- copy localization can reuse the visual composite;
- a new output profile should not force product regeneration.

## Product fidelity

If an authoritative product photo exists, the product MUST NOT be regenerated from text or replaced by a visually similar AI product.

Use original product RGB + reviewed alpha mask or verified current-SKU CAD/3D.

## Key contracts

The orchestrator includes contracts for:
- intake;
- preflight;
- buyer decisions;
- variants;
- asset reuse;
- output profiles;
- detail modules;
- deterministic prompts;
- execution state;
- QA;
- delivery.

See [AGENT_SPEC_CONVENTIONS.md](./AGENT_SPEC_CONVENTIONS.md).

## China marketplace notes / 中国电商

淘宝、天猫、1688、京东、拼多多、抖音、Amazon 等应当作为不同的输出 surface / profile，而不是重新生成一个“长得差不多的商品”。

多规格商品的正确目标是：

> 一套真实商品事实与可复用视觉母版，派生所有需要的 SKU / 平台 / 端侧资产。