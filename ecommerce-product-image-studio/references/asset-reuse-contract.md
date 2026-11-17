# Commerce Asset Reuse and Derivative Contract

## Purpose

Treat production assets as reusable masters with controlled derivatives.

The goal is:
- preserve product truth;
- avoid unnecessary generation cost;
- keep marketplace variants consistent;
- invalidate only what actually changed.

## Asset layers

### Level 0 — Authoritative source

Examples:
- real product photo;
- verified CAD / 3D;
- merchant spec document.

Never overwrite.

### Level 1 — Reusable production master

Examples:
- reviewed product cutout;
- verified close-up crop;
- approved copy block;
- semantic detail module;
- empty scene background;
- approved person layer.

### Level 2 — Composed semantic asset

Examples:
- lifestyle composite;
- dimension module;
- product overview module;
- variant comparison.

### Level 3 — Surface / marketplace derivative

Examples:
- Taobao detail render;
- Amazon A+ web render;
- mobile render;
- 1:1 gallery crop;
- 4:9 merchant-requested derivative.

## Derivative graph

Every derivative SHOULD record:
- \`asset_id\`
- \`parent_asset_ids\`
- \`variant_scope\`
- \`output_profile\`
- \`transforms\`
- \`copy_version\`
- \`product_provenance\`
- \`invalidation_inputs\`

## Reuse rules

MUST reuse valid upstream assets when:
- product source is unchanged;
- variant scope remains valid;
- evidence has not changed;
- output profile can be derived without violating readability or geometry.

MUST regenerate / rebuild only the smallest invalidated stage.

Examples:
- new marketplace crop → reuse product cutout and semantic module;
- copy translation → reuse product composite, redo layout / copy QA;
- size variant changes product length → reuse background if valid, replace variant-bound product cutout and scale placement;
- product source photo changes → invalidate cutout and downstream composites;
- verified dimension changes → invalidate dimension graphics and any scale-dependent scene.

## Reuse vs duplication

A new file is not necessarily a new semantic asset.

Example:

\`\`\`text
semantic asset: "wood structure detail"
  ├── zh-CN mobile render
  ├── en-US Amazon render
  └── generic web render
\`\`\`

These SHOULD inherit one evidence/provenance record.

## Background reuse

A generated empty background MAY be reused across variants when:
- product placement zone remains compatible;
- scale / perspective remain valid;
- no product-specific object exists in the background;
- reuse does not imply false variant identity.

## Person-layer reuse

A person asset MAY be reused when:
- pose/contact geometry still fits the variant;
- scale assumptions remain valid;
- wardrobe / market / language requirements do not invalidate the concept.

Do not force a different variant to fit an old person pose by deforming the product.

## Localization

Copy translation / localization SHOULD be a downstream derivative.

Localization MUST NOT rewrite:
- dimensions;
- material facts;
- included items;
- certifications;
- performance claims

unless source evidence also changes.

## Output

Create \`asset-derivation-map.json\`.

The execution state SHOULD use this dependency graph for targeted invalidation and resume.

## Gate

If an upstream asset becomes invalid, all dependent derivatives must be marked stale until rebuilt / re-QA'd.