# Agent Skill Specification Conventions

This repository is an **ecommerce visual production system**, not a generic prompt collection.

## Core priorities

1. same-SKU identity;
2. critical construction / geometry truth;
3. truthful evidence and copy;
4. buyer-decision value;
5. platform commerce style;
6. natural commercial photography;
7. variant correctness;
8. campaign consistency;
9. official compliance.

## Identity fidelity vs pixel fidelity

Default consumer-product route:
- pass authoritative product photos directly to a capable reference-image model;
- enforce stable PRODUCT IDENTITY LOCK and CRITICAL GEOMETRY LOCK when needed;
- judge whether the output remains the same SKU.

Strict source-pixel compositing is a fallback/special mode for:
- logos;
- packaging text;
- precision interfaces;
- regulated labels;
- model plates;
- identity-critical joint/hardware details after repeated drift;
- material proof where generated texture would become false evidence.

Do not use pixel preservation as an excuse for weak collage-like imagery, and do not use natural generation as an excuse for incorrect construction.

## Stable locks

Use stable blocks:
- PRODUCT IDENTITY LOCK;
- CRITICAL GEOMETRY LOCK when joints/hardware/relations matter;
- REAL-WORLD SCALE LOCK when activated;
- CAMPAIGN STYLE LOCK;
- PLATFORM COMMERCE STYLE LOCK.

Keep locks verbatim across candidates unless evidence changes.

## Weak-model execution

When execution model capability is uncertain:
- use stage-gated structured artifacts;
- represent geometry as subject–relation–object rules;
- generate one semantic visual job at a time;
- approve semantic masters before infographic layout;
- create an evidence-bound copy deck;
- render final multi-panel typography/layout deterministically;
- repair only failed assets/regions.

Avoid one-shot prompts that ask a model to simultaneously solve product reconstruction, six-panel layout, Chinese copy, dimensions, icons and lifestyle photography.

## One asset, one dominant job

Each semantic master should have one primary purchase-decision job.

Do not fill a set with near-duplicate mood shots.

## Semantic masters before layout

For factual ecommerce boards:

```text
authoritative references
→ identity/geometry locks
→ semantic masters
→ master QA
→ approved copy deck
→ deterministic layout
```

A one-shot generated collage must not bypass product QA.

## Reference-image generation

Reference generation is appropriate for many:
- hero photographs;
- lifestyle scenes;
- person-use scenes;
- non-critical commercial close-ups.

Identity-critical material/joint proof may require source pixels or verified CAD.

## Commercial scene grammar

Scene prompts should express:
- who;
- where;
- action;
- camera;
- light;
- product salience;
- 2–4 relevant props;
- scale reference if useful.

## Candidate / repair loop

Important generative assets SHOULD use bounded candidates.

Hard identity/geometry/fact failures are rejected before scoring.

QA outputs targeted repair instructions.

Regenerate only failed semantic masters.

## Copy / layout

Copy must trace to approved evidence.

Do not strengthen:
- unpainted → 0 VOC;
- visible anti-slip pad → never slips;
- triangular base → safety guarantee;
- natural wood → eco certification.

Exact Chinese, numbers, dimensions and repeated text should be rendered with deterministic tooling.

## Variant scope

Unknown sharedness is not permission to reuse across SKUs.

## Resumable execution

Use stable asset IDs, dependency-aware invalidation, bounded retries and master/layout separation.

## China marketplace notes

- 淘宝/天猫/1688：货架/搜索/比较逻辑更强，详情页承担较长的信任与决策链。
- 拼多多：强调快速理解商品、规格/数量/价值信息与小卡片可读性；这属于转化启发式，不是官方模板。
- 抖音：内容 + 货架并存，移动端、场景、人物使用与内容相关性更重要；仍需符合当前官方主图/商城规则。
- 所有平台风格策略都不能授权虚假折扣、虚构卖点、未知规格或未经证据支持的环保/安全/性能声明。
