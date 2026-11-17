---
name: product-dimension-lock
description: Build traceable physical dimension records for each product family, SKU, and variant, including axis definitions, units, evidence, tolerance, state, inheritance, and packaging separation.
---

# Product Dimension Lock

## Objective

Create authoritative dimension records that downstream scene, person, specification, variant-comparison, and packaging graphics must reference.

Read \`ecommerce-product-image-studio/references/variant-matrix-contract.md\` when multiple variants exist.

## Evidence priority

Prefer:
1. user-confirmed measurements;
2. current-SKU engineering / CAD / manufacturing documents;
3. current-SKU measurement photos or videos with clear geometry;
4. visual estimates only as \`estimated\`.

## Normalized storage

Use mm and g internally.

Product:
- \`length_mm\`
- \`width_mm\`
- \`height_mm\`
- \`net_weight_g\`

Packaging:
- \`package_length_mm\`
- \`package_width_mm\`
- \`package_height_mm\`
- \`gross_weight_g\`

Product and packaging dimensions remain separate.

## Variant inheritance

When a family has variants:

- store differing dimensions at variant level;
- family-level dimensions require \`SHARED_VERIFIED\`;
- \`UNKNOWN_SHAREDNESS\` values MUST NOT be inherited;
- one known size axis does not prove other axes are identical;
- shared geometry appearance does not prove shared measurements.

Example:

\`\`\`text
family
├── 25cm variant → length 250mm, width unknown, height unknown
├── 30cm variant → length 300mm, width unknown, height unknown
├── 35cm variant → length 350mm, width unknown, height unknown
└── 40cm variant → length 400mm, width unknown, height unknown
\`\`\`

Width / height remain unknown until independently confirmed.

## Axis definition

Every dimension set MUST define length, width, and height meaning.

For irregular / foldable / multi-state products also define measurement state and envelope rules.

## States

Use:
- \`user_confirmed\`
- \`document_verified\`
- \`partial\`
- \`estimated\`
- \`unknown\`
- \`conflicting\`

## MUST

For every published number record:
- value;
- unit;
- axis;
- variant / family scope;
- measurement state;
- evidence source;
- measurement method;
- tolerance / uncertainty if known.

## MUST NOT

- infer all axes from one known dimension;
- inherit a variant value across the family without verified sharedness;
- infer measurements from a composite scene;
- average conflicts silently;
- fill missing values for visual completeness.

## Outputs

Create:
- \`product-dimensions.json\`
- variant dimension records where applicable
- \`dimensions-evidence.md\`
- \`missing-dimensions.md\`
- \`dimension-diagram-brief.md\`

## Gate

Only \`user_confirmed\` and \`document_verified\` values may be presented as formal specifications by default.

Estimated values are internal planning aids only unless explicitly labeled otherwise.