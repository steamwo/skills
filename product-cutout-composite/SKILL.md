---
name: product-cutout-composite
description: Extract and composite the real SKU product while preserving original product RGB; use segmentation only for alpha/masks and keep product pixels traceable through placement, shadow, and export.
---

# Product Cutout Composite

## Objective

Create a reusable product cutout without redrawing the product body.

## Core rule

The segmentation model may create an alpha mask. It MUST NOT replace product RGB.

\`\`\`text
source image RGB
+ reviewed alpha mask
= product cutout
\`\`\`

## Inputs

- authoritative source image;
- product identity contract;
- optional user-supplied transparent PNG / mask;
- target background / scene;
- placement plan.

## MUST

- preserve the original source RGB inside valid product pixels;
- save the alpha mask separately;
- inspect holes, gaps, thin parts, transparent parts, and low-contrast edges;
- record source image path / hash when possible;
- use uniform layer scaling by default;
- preserve aspect ratio;
- keep shadows on separate layers.

## MUST NOT

- use generative fill to reconstruct the product body;
- erase real holes, joints, hardware, or texture because the mask is inconvenient;
- non-uniformly scale the product;
- alter product color to match the scene;
- paint shadows over the product RGB;
- infer missing parts outside the original visible view.

## Allowed post-processing

MAY include, when traceable:
- alpha cleanup;
- edge decontamination;
- minor fringe removal;
- uniform scale;
- translation;
- limited rotation consistent with the source view.

If cleanup changes identity-relevant pixels, it requires review.

## Scene placement

The background SHOULD be generated or prepared without the target product.

Composition sequence:

\`\`\`text
background
→ independent shadow
→ original-RGB product cutout
→ foreground occluders if required
→ typography / graphics
\`\`\`

## Outputs

Save:
- source reference;
- \`mask.png\`
- \`product-cutout.png\`
- composite;
- shadow layer;
- placement metadata;
- provenance record.

## Gate

A final composite fails if:
- product RGB was generatively redrawn;
- the mask deletes real structure;
- geometry was warped;
- product identity differs from the source.

Pixel preservation and mask correctness are separate checks.