---
name: wood-product-fidelity
description: Enforce fidelity-first production for real wood e-commerce products, preserving source wood grain, knots, joints, hardware, color, surface appearance, and geometry while using AI primarily for empty scenes, people, props, and layout.
---

# Wood Product Fidelity

## Objective

Produce e-commerce visuals for real wood products without turning the product into a generic AI recreation.

This is a material-specific fidelity layer. It complements the general e-commerce workflow.

## Applies to

Examples:
- wooden storage products;
- trays;
- furniture;
- kitchen / household goods;
- exercise accessories;
- other products where wood grain and construction are identity-relevant.

## Core rule

If a real product photograph is available:

**MUST use source product pixels as the default.**

Wood grain is product evidence, not decorative texture.

## MUST preserve

- wood grain direction;
- knots and natural variation;
- end-grain appearance;
- real color variation;
- joints;
- seams;
- holes;
- fasteners;
- chamfers / roundovers;
- edge profiles;
- component count;
- visible thickness / proportions;
- confirmed finish appearance.

## MUST NOT

- smooth away natural variation just to make the wood “premium”;
- clone or invent grain;
- change end grain;
- replace real screws / joints with cleaner AI geometry;
- infer wood species from appearance alone;
- convert an unconfirmed matte / raw appearance into an oil / lacquer / wax claim;
- infer “food safe”, “zero formaldehyde”, “eco certified”, or similar claims from visual appearance;
- generatively redraw the full product and mark it as fidelity-preserved.

## Production route

\`\`\`text
real wood product photo
→ reference audit
→ wood-specific identity lock
→ reviewed alpha mask
→ ORIGINAL RGB cutout
→ empty generated scene
→ scale-aware composite
→ independent text / graphics
→ wood fidelity QA
\`\`\`

## Detail images

Wood detail graphics SHOULD use:
- real high-resolution crops; or
- additional real macro photos.

Do not “AI enhance” missing texture into new grain / knots.

If detail resolution is insufficient, request another photo instead of hallucinating detail.

## Scene images

AI SHOULD generate the environment without the target wood product.

Avoid confusing background props that visually resemble the product or could be mistaken as included items.

Lighting MAY be matched through background / shadow design, but product surface color and grain SHOULD remain source-based.

## Product claims

Use only evidence-backed:
- species;
- finish;
- dimensions;
- weight;
- load capacity;
- certifications;
- included items.

Visible wood appearance alone is not proof of these facts.

## China marketplace notes / 中国电商

原木类商品详情页常见“材质、木纹、结构、尺寸、使用场景”模块，但这些模块必须建立在真实商品资料上。

- 木纹特写：用真实裁切 / 补拍。
- 木种：商家确认或文档支持。
- 尺寸：只用已确认规格。
- “环保”“无甲醛”“食品级”等词：必须有证据，不能根据原木外观推断。
- 中文文案、尺寸线和参数表由排版工具制作。

## QA

A wood-product image is \`FAIL\` if:
- grain / hardware / geometry is materially regenerated;
- a generated lookalike replaces the real product;
- finish / species claims are invented;
- source-product details change across images.

## Tool note

The existing \`scripts/render.py\` can support cutout / simple background compositing. It is a fidelity utility, not a substitute for the full orchestrated workflow.