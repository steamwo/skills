---
name: wood-product-fidelity
description: Enforce fidelity-first production for real wood ecommerce products, preserving source wood grain, end grain, joints, hardware, critical geometry, color, surface appearance, and proportions while routing hero/lifestyle and factual detail assets appropriately.
---

# Wood Product Fidelity

## Objective

Produce ecommerce visuals for real wood products without turning the product into a generic AI recreation.

This is a material- and construction-specific fidelity layer.

## Applies to

Examples:
- wooden storage products;
- trays;
- furniture;
- kitchen / household goods;
- exercise accessories;
- other products where wood grain and construction are identity-relevant.

## Core rule

Wood products have **two different fidelity needs**:

1. **commercial photography fidelity** — hero/lifestyle assets may use strong reference-image generation when the same SKU, material appearance and critical geometry survive QA;
2. **factual detail fidelity** — material/joint/hardware proof SHOULD default to real source pixels or verified CAD when generated detail could become false evidence.

Do not use one universal route for every asset.

## MUST preserve

- wood grain direction;
- knots and natural variation;
- end-grain appearance;
- real color variation;
- joints;
- seams;
- holes;
- fasteners;
- fastener location and axis;
- component-to-component contact relationships;
- chamfers / roundovers;
- edge profiles;
- component count;
- visible thickness / proportions;
- confirmed finish appearance.

## Critical geometry

When joints/hardware matter, create a `CRITICAL GEOMETRY LOCK`.

Describe relations explicitly:
- what component touches/supports what;
- where fasteners are located;
- fastener/hole/handle orientation;
- what must remain visibly separate;
- forbidden alternative placements.

Example pattern:
```text
screw + embedded in + handle top surface + axis vertical to floor + near end
MUST NOT move to circular end-grain face
```

A materially wrong relation = `FAIL`.

## MUST NOT

- smooth away natural variation just to make wood “premium”;
- clone or invent grain for factual material proof;
- change end grain;
- replace real screws/joints with cleaner but different geometry;
- relocate hardware;
- merge separate wood components;
- infer wood species from appearance alone;
- convert an unconfirmed matte/raw appearance into an oil/lacquer/wax claim;
- infer “food safe”, “zero formaldehyde”, “0 VOC”, “eco certified”, or similar claims from visual appearance;
- present a generated lookalike detail as factual proof when it cannot be verified.

## Route by asset role

### Hero / lifestyle / person-use

May use `REFERENCE_GENERATE` or `REFERENCE_EDIT` when:
- authoritative product references are supplied;
- PRODUCT IDENTITY LOCK is active;
- CRITICAL GEOMETRY LOCK is active when needed;
- same-SKU identity passes;
- material appearance remains credible;
- no generated detail is used as evidence beyond what references support.

### Material / joint / hardware close-up

Prefer:
1. real high-resolution crop;
2. additional real macro photo;
3. verified CAD for geometry;
4. reference generation only when identity-critical detail can be reliably verified.

After repeated geometry drift, escalate to source pixels instead of accepting “close enough”.

## Recommended production route

```text
real wood product photos
→ reference audit
→ PRODUCT IDENTITY LOCK
→ CRITICAL GEOMETRY LOCK when needed
→ semantic master plan
→ route each master:
     hero/lifestyle → reference generate/edit + QA
     material/joint proof → source pixels / verified detail preferred
→ master QA
→ approved copy deck
→ deterministic text / grid layout
→ wood fidelity QA
```

## Detail images

Wood detail graphics SHOULD use:
- real high-resolution crops; or
- additional real macro photos.

Do not “AI enhance” missing texture into new grain/knots.

If detail resolution is insufficient, request another photo or mark the detail `BLOCKED`.

## Scene images

AI MAY generate/re-render a commercial scene with the target product when the selected fidelity route permits it.

The scene MUST NOT:
- change critical construction;
- add confusing wood props that resemble included product;
- imply unsupported load/safety/performance claims.

## Product claims

Use only evidence-backed:
- species;
- finish;
- dimensions;
- weight;
- load capacity;
- certifications;
- included items.

User-confirmed wording may be retained at its stated scope, but MUST NOT be semantically strengthened.

## China marketplace notes / 中国电商

原木类商品详情页常见“材质、木纹、结构、尺寸、使用场景”模块，但这些模块必须建立在真实商品资料上。

- 木纹特写：优先真实裁切 / 补拍。
- 连接结构：螺丝、孔位、榫槽、支撑关系必须与实物一致。
- 木种：商家确认或文档支持。
- 尺寸：只用已确认规格。
- “环保”“无甲醛”“0 VOC”“食品级”等词：不能从外观推断；用户原话也不能自动扩写为更强声明。
- 中文文案、尺寸线、参数表和六宫格由确定性排版工具制作。

## QA

A wood-product image is `FAIL` if:
- identity-critical grain/hardware/geometry materially drifts;
- a locked joint relation is wrong;
- hardware location/orientation changes;
- a generated lookalike replaces factual detail proof;
- finish/species/chemical/safety claims are invented;
- source-product details contradict across images.

## Tool note

`scripts/render.py` supports source-pixel cutout/simple compositing for strict detail routes.

It is one fidelity utility, not a mandate to use cutouts for every commercial asset.
