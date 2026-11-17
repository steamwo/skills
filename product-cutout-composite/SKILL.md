---
name: product-cutout-composite
description: Strict-pixel fallback for e-commerce assets where exact source product pixels, logos, packaging text, model plates, or precision details must survive unchanged.
---

# Product Cutout Composite — Strict Fidelity Route

## Objective

Preserve original product RGB when exact pixel fidelity is necessary.

This is **not** the default route for ordinary lifestyle photography.

Read \`ecommerce-product-image-studio/references/reference-generation-contract.md\`.

## Use this route when

- packaging text must be exact;
- logo / label fidelity is critical;
- precision ports / interfaces / model plates matter;
- a reference-generation model repeatedly changes identity-critical structure;
- user explicitly requests source-pixel preservation;
- a platform asset is better served by deterministic composition.

## Do not use merely because

- a product has a white background;
- masking is technically possible;
- compositing feels safer;
- the model might make a small visual change.

For many home, fitness, furniture and lifestyle products, reference-image generation produces more natural light, contact and scene integration.

## Core rule

\`\`\`text
source image RGB
+ reviewed alpha mask
= strict-fidelity product cutout
\`\`\`

Segmentation creates alpha only; it MUST NOT replace product RGB.

## MUST

- preserve original RGB inside product region;
- save mask separately;
- inspect thin parts / holes / low-contrast edges;
- maintain aspect ratio;
- keep shadows / foreground effects independent;
- record source and transformations.

## MUST NOT

- warp product geometry;
- paint generated shadows onto product RGB;
- generatively repair missing product body and call it source pixels;
- erase identity details for cleaner masking.

## Scene integration

If the result looks like a pasted sticker:
- improve contact / cast shadow;
- adjust scene lighting around the product;
- add foreground occluders when physically plausible;
- or return to a better reference-generation/edit route if exact pixels are not mandatory.

## Gate

Strict-pixel fidelity can still fail commercial quality.

Pass only when:
- product pixels are correct;
- edges are correct;
- contact / perspective / lighting are believable enough for the intended asset.