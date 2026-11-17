---
name: lifestyle-scene-composite
description: Build product lifestyle scenes by deterministically rendering an empty-environment prompt, calibrating scale and perspective, then compositing authoritative product pixels without generative redraw.
---

# Lifestyle Scene Composite

## Objective

Place a real SKU into a believable lifestyle environment without changing the product.

## Required inputs

- \`task-input.json\`
- \`product-identity.json\`
- \`product-dimensions.json\`
- \`scale-calibration.json\`
- authoritative product view or verified CAD/3D
- source audit
- \`ecommerce-product-image-studio/templates/empty-scene-prompt.md\`

## Correct pipeline

\`\`\`text
1. select supported product view
2. plan contact plane + scale + camera
3. render empty-scene prompt from template
4. generate EMPTY scene
5. create product alpha mask
6. composite ORIGINAL PRODUCT RGB
7. add independent contact / cast shadows
8. run identity + scale + composite QA
\`\`\`

## Prompt rendering

MUST use the repository prompt template when available.

- unresolved required fields → \`BLOCKED\`;
- missing optional fields → omit;
- user style text → preserve intent without generic embellishment;
- fixed “do not generate target product” clause → never remove.

Save the rendered prompt with provenance metadata.

## Empty scene generation

Background generation MAY create:
- room;
- floor / table / wall;
- non-product props;
- lighting;
- negative space.

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
- claim accurate real-world scale when \`SCALE_UNVERIFIED\`;
- infer scene style from the product image unless the user explicitly requested matching.

## View mismatch

If the product source view does not match the scene:
1. regenerate / change the background;
2. use another verified source view;
3. use verified CAD/3D.

Do not warp the product to fake a new camera view.

## Output

Save:
- scene brief;
- rendered prompt;
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
Set \`REVIEW\` when placement is plausible but metric scale is not grounded.