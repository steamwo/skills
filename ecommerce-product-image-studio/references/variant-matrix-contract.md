# SKU / Variant Matrix Contract

## Purpose

Represent product families explicitly so shared assets can be reused safely while variant-specific facts and visuals remain isolated.

This prevents:
- cross-SKU drift;
- wrong dimensions on the wrong image;
- one color / size silently replacing another;
- unnecessary regeneration of identical assets.

## Product family model

A family MAY vary by:
- size;
- length;
- color;
- material;
- bundle quantity;
- included accessories;
- model / generation;
- region-specific package;
- other merchant-defined axes.

Create \`variant-matrix.json\`.

## Variant matrix fields

At family level:
- \`family_id\`
- \`variant_axes\`
- \`shared_identity_features\`
- \`shared_claims\`
- \`shared_assets\`
- \`unknown_sharedness\`

Per variant:
- \`variant_id\`
- \`sku\`
- axis values
- authoritative references
- dimensions
- color / finish
- packaging / included items
- approved claims
- variant-specific assets
- inheritance exceptions

## Sharedness states

For any fact or asset use:
- \`SHARED_VERIFIED\`
- \`VARIANT_SPECIFIC\`
- \`UNKNOWN_SHAREDNESS\`
- \`NOT_APPLICABLE\`

Do not assume a feature is shared just because only one variant was photographed.

## Asset reuse classes

### Family-shared

May be reused only when verified invariant across variants.

Examples:
- brand layout system;
- generic care module;
- some non-product backgrounds;
- verified shared construction detail.

### Variant-bound

MUST be specific to the current variant.

Examples:
- product cutout;
- dimensions;
- color-sensitive hero image;
- variant packaging;
- included-item quantity;
- variant-specific person-scale scene when geometry changes.

### Conditionally reusable

Requires an explicit rule.

Example:
- a lifestyle background may be shared;
- the product cutout inside it must be replaced per variant.

## Dimension rules

Variant dimensions MUST live at variant level when they differ.

A family-level dimension may exist only when verified identical across all applicable variants.

Do not infer width / height / diameter equality from a shared product shape.

## Copy rules

Claims SHOULD declare scope:
- \`family\`
- \`variant\`
- \`bundle\`
- \`market\`

A family-level copy block MUST NOT contain a variant-specific number unless parameterized per render.

## Cross-variant scale rule

When a comparison image shows multiple size variants:
- use one controlled scale / camera basis;
- preserve verified ratios;
- do not compose independently generated lookalikes and call them a precise size comparison.

## Outputs

Create:
- \`variant-matrix.json\`
- \`variant-asset-map.json\`
- \`variant-copy-map.json\`

The gallery planner and Delivery Gate SHOULD count semantic assets per required variant scope, not simply multiply every asset by every SKU.

## Gate

If an asset's variant scope is unknown, mark it \`REVIEW\` or \`BLOCKED\`; do not silently reuse it across the family.