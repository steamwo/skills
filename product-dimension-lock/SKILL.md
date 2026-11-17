---
name: product-dimension-lock
description: Build traceable physical dimension records for each SKU and variant, including axis definitions, units, measurement basis, evidence, tolerance, state, and packaging separation; never promote guessed measurements to specifications.
---

# Product Dimension Lock

## Objective

Create one authoritative physical dimension profile that downstream scene, person, specification, and packaging graphics must reference.

## Evidence priority

Prefer:
1. user-confirmed measurements;
2. current-SKU engineering / CAD / manufacturing documents;
3. current-SKU measurement photos or videos with clear measurement geometry;
4. indirect visual estimates only as \`estimated\`.

Competitor dimensions and category norms MUST NOT become current-SKU specifications.

## Normalized storage

Use mm and g internally.

Common product fields:
- \`length_mm\`
- \`width_mm\`
- \`height_mm\`
- \`net_weight_g\`

Packaging fields:
- \`package_length_mm\`
- \`package_width_mm\`
- \`package_height_mm\`
- \`gross_weight_g\`

Product dimensions and packaging dimensions MUST remain separate.

## Axis definition

Every dimension set MUST define what length, width, and height mean for the product.

For irregular, circular, foldable, extendable, or multi-state products, also define:
- measurement state;
- maximum envelope vs usable size;
- whether projections, feet, handles, lids, or accessories are included.

## States

Use:
- \`user_confirmed\`
- \`document_verified\`
- \`partial\`
- \`estimated\`
- \`unknown\`
- \`conflicting\`

A \`partial\` profile MUST record evidence per known axis.

## MUST

For every published number record:
- value;
- normalized unit;
- original unit/value where relevant;
- axis definition;
- measurement state;
- evidence source;
- measurement method;
- tolerance / uncertainty if known.

## MUST NOT

- infer all three axes from one known dimension;
- infer dimensions from a composite scene;
- use person height as an undocumented product ruler;
- average conflicting sources without explicit resolution;
- fill missing values to make a spec table look complete.

## Output

Create:
- \`product-dimensions.json\`
- \`dimensions-evidence.md\`
- \`missing-dimensions.md\`
- \`dimension-diagram-brief.md\`

Example:

\`\`\`json
{
  "sku": "SKU-001",
  "unit": "mm",
  "dimensions": {
    "length_mm": null,
    "width_mm": null,
    "height_mm": null,
    "net_weight_g": null,
    "status": "unknown",
    "measurement_state": "assembled",
    "axis_definition": {},
    "tolerance_mm": null,
    "evidence": []
  }
}
\`\`\`

## Gate

Only \`user_confirmed\` and \`document_verified\` values may be presented as formal specifications by default.

\`estimated\` values MAY be used for internal layout planning only if clearly labeled and must not become customer-facing numeric claims.