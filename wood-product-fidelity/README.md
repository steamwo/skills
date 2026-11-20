# Wood Product Fidelity

A material- and construction-specific fidelity layer for real wood ecommerce products.

## Why this exists

Wood products are unusually easy for image models to “improve” into a different product:
- grain changes;
- knots disappear;
- joints become cleaner/different;
- screws move;
- screw axis changes;
- end grain changes;
- edge profiles shift;
- finish becomes glossier;
- separate parts merge;
- dimensions drift.

For ecommerce production, identity-critical changes are failures.

## Route by asset role

Do not use one universal route.

### Hero / lifestyle

Reference-image generation/edit may be used when:
- authoritative current-SKU photos are present;
- PRODUCT IDENTITY LOCK is active;
- CRITICAL GEOMETRY LOCK is active when needed;
- same-SKU identity and geometry pass QA.

This often produces more natural commercial photography than a cutout collage.

### Material / joint / hardware proof

Prefer:
- real high-resolution crop;
- additional macro photo;
- source-pixel composite;
- verified CAD when appropriate.

Do not let generated texture/joint detail become factual evidence unless it can be verified.

## Recommended workflow

```text
real product photos
→ reference audit
→ PRODUCT IDENTITY LOCK
→ CRITICAL GEOMETRY LOCK when needed
→ semantic master plan
→ route each master by fidelity need
→ master QA
→ approved copy deck
→ deterministic copy / dimensions / six-grid layout
→ final QA
```

## AI responsibilities

AI is useful for:
- commercial hero rendering with references;
- lifestyle scenes;
- people;
- independent props;
- empty backgrounds;
- visual concepts.

Deterministic layout tools should handle:
- exact Chinese;
- dimensions;
- repeated labels;
- six-grid / detail-board composition.

## China-commerce notes / 中国电商

原木类商品常见模块：
- 白底 / 主图
- 场景图
- 木纹 / 结构细节
- 尺寸规格
- 包装清单
- 详情页模块

这些模块必须基于真实商品资料。木种、涂层、承重、环保、食品级等声明不能仅凭图片外观推断。

See:
- `SKILL.md`
- `references/wood-rules.md`
- `scripts/render.py`
- `../ecommerce-product-image-studio/references/critical-geometry-lock.md`
