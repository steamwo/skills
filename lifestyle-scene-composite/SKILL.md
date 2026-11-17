---
name: lifestyle-scene-composite
description: Build product lifestyle scenes by generating or sourcing an empty environment, calibrating scale and perspective, then compositing the authoritative product pixels without generative redraw.
---

# Lifestyle Scene Composite

## Objective

Place a real SKU into a believable lifestyle environment without changing the product.

## Required inputs

- \`product-identity.json\`
- \`product-dimensions.json\`
- \`scale-calibration.json\`
- authoritative product view or verified CAD/3D
- source audit

## Correct pipeline

\`\`\`text
1. select a supported product view
2. plan contact plane + scale + camera
3. generate EMPTY scene
4. create product alpha mask
5. composite ORIGINAL PRODUCT RGB
6. add independent contact / cast shadows
7. run identity + scale + composite QA
\`\`\`

## Empty scene generation

Background generation MAY create:
- room;
- floor / table / wall;
- non-product props;
- lighting;
- negative space.

Prompt SHOULD include:
- camera direction;
- perspective;
- contact plane;
- expected product placement area;
- lighting direction;
- negative constraints such as:
  \`no target product, no product duplicate, no similar product, no text, no logo\`.

## MUST

- use a source product view compatible with the scene camera;
- preserve product geometry;
- place with uniform scaling;
- align contact plane and gravity;
- keep product and scene shadows separate;
- record scale state.

## MUST NOT

- generate the product together with the scene when source-pixel fidelity is required;
- distort product perspective to fit the background;
- use AI furniture as an undocumented metric reference;
- redraw product texture / hardware / supports;
- claim accurate real-world scale when \`SCALE_UNVERIFIED\`.

## View mismatch

If the product source view does not match the scene:
1. regenerate / change the background;
2. use another verified source view;
3. use verified CAD/3D.

Do not warp the product to fake a new camera view.

## Output

Save:
- scene brief;
- empty background;
- source product;
- mask;
- cutout;
- shadow layers;
- composite;
- scale-calibration reference;
- provenance record;
- \`lifestyle-qa.md\`.

## Gate

A scene can be visually attractive and still fail.

Set \`FAIL\` when product identity changes.
Set \`REVIEW\` when visual placement is plausible but metric scale is not grounded.