---
name: product-identity-lock
description: Build a traceable SKU identity contract that locks the product's recognisable geometry, structure, hardware, colour, texture, markings, and authoritative views for both reference-image generation and strict-pixel fallback.
---

# Product Identity Lock

## Objective

Describe what makes the current SKU recognisably itself.

Identity fidelity is not the same as pixel identity.

For most consumer-product lifestyle work, a capable reference-image model MAY re-render the product if identity-critical features remain correct. Strict source-pixel preservation is reserved for assets that require it.

Read \`ecommerce-product-image-studio/references/reference-generation-contract.md\`.

## Authoritative source rule

Real current-SKU product photos are authoritative evidence for visible identity.

Lock:
- silhouette / proportions;
- component count;
- relative positions;
- holes / joints / screws / seams / handles / supports;
- edge and end geometry;
- visible colour / finish / texture;
- logos / labels / printed graphics when relevant;
- supported camera views;
- must-not-appear features.

Every lock item SHOULD link to evidence.

## Product Identity Lock block

Create a concise reusable block:

\`\`\`text
PRODUCT IDENTITY LOCK — DO NOT CHANGE
Shape & proportions: ...
Colour & finish: ...
Visible material / texture: ...
Parts & details: ...
Logo / printed text: ...
Component count: ...
Must NOT change: ...
Must NOT appear: ...
\`\`\`

Unknown values are omitted.

Paste the same lock verbatim into all candidates for the same asset family.

## Fidelity modes

### \`REFERENCE_RENDERED_PRODUCT\`

Allowed when:
- authoritative product reference is passed directly to the image model;
- result keeps the same recognisable SKU;
- no strict-pixel trigger applies.

### \`SOURCE_PRODUCT_PIXEL\`

Use when exact source appearance is required:
- packaging / label text;
- logos that must be exact;
- fine model plates;
- precision interfaces;
- repeated reference-generation drift.

### \`VERIFIED_CAD_3D\`

Use for unsupported camera views only when the CAD / 3D source is verified for the same SKU.

### \`CONCEPT_ONLY\`

Use when no authoritative product reference exists.

## MUST NOT

- substitute a visually similar product;
- change product topology / component count;
- invent hidden construction;
- change colourway / material / logo;
- stretch geometry to fit a scene;
- call an unsupported new camera view factual unless verified CAD/3D supports it.

## Output

Create \`product-identity.json\` containing:
- \`sku\`
- \`variant\`
- \`authoritative_references\`
- \`identity_lock_text\`
- \`geometry\`
- \`visible_features\`
- \`material_appearance\`
- \`must_preserve\`
- \`must_not_invent\`
- \`supported_views\`
- \`unsupported_views\`
- \`strict_pixel_triggers\`
- \`recommended_fidelity_mode\`
- \`dimension_profile_ref\`
- \`unknowns\`
- \`conflicts\`
- \`version\`

## Gate

If the result no longer reads as the same SKU, it is \`FAIL\` regardless of scene quality.

Exact pixel matching is required only when the asset's fidelity mode is \`SOURCE_PRODUCT_PIXEL\`.