# Agent Skill Specification Conventions

This repository is an **e-commerce visual production system**, not a generic prompt collection.

## Core priorities

1. same-SKU identity;
2. truthful evidence;
3. buyer-decision value;
4. platform commerce style;
5. natural commercial photography;
6. variant correctness;
7. campaign consistency;
8. official compliance.

## Identity fidelity vs pixel fidelity

Default consumer-product route:
- pass real product photos directly to a capable reference-image model;
- enforce a stable PRODUCT IDENTITY LOCK;
- judge whether the output remains the same SKU.

Strict source-pixel compositing is a fallback / special mode for logos, packaging text, precision interfaces, regulated labels, model plates, or repeated identity drift.

Do not use “pixel preservation” as an excuse for bad collage-like ecommerce imagery.

## Stable locks

Use stable blocks:
- PRODUCT IDENTITY LOCK;
- CAMPAIGN STYLE LOCK;
- PLATFORM COMMERCE STYLE LOCK.

Identity and campaign locks remain stable across the set.
Shot role changes per asset.

## Platform style vs compliance

Platform style profiles are heuristic conversion guidance.

Official marketplace requirements are separate and must be current / source-backed.

## One asset, one dominant job

Each image/module should have one primary purchase-decision job.

Do not fill a set with near-duplicate mood shots.

## Reference-image generation

Reference generation is the default for most:
- hero photography;
- lifestyle scenes;
- person-use scenes;
- material / structure close-ups.

Strict compositing is not default.

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

QA outputs targeted repair instructions.

Regenerate only failed assets.

## Copy / layout

Short copy and clear zones improve mobile readability.

When exact text remains unreliable, move final typography to deterministic design/layout tooling.

## Variant scope

Unknown sharedness is not permission to reuse across SKUs.

## Resumable execution

Use stable asset IDs, dependency-aware invalidation, and bounded retries.

## China marketplace notes

- 淘宝/天猫/1688：货架/搜索/比较逻辑更强，详情页承担较长的信任与决策链。
- 拼多多：强调快速理解商品、规格/数量/价值信息与小卡片可读性；这属于转化启发式，不是官方模板。
- 抖音：内容 + 货架并存，移动端、场景、人物使用与内容相关性更重要；仍需符合当前官方主图/商城规则。
- 所有平台风格策略都不能授权虚假折扣、虚构卖点或未知规格。