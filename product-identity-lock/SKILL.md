---
name: product-identity-lock
description: Build a traceable SKU identity contract that locks visible geometry, structure, hardware, color, texture, markings, and authoritative source views so generative tools cannot silently redesign the product.
---

# Product Identity Lock

## Objective

Create a machine-readable contract for what makes the current SKU visually itself.

This skill controls identity. Physical measurement values belong to \`product-dimension-lock\`.

## Authoritative source rule

If the user provides a real product photo for the current SKU, it is authoritative for the visible product body.

**MUST**
- preserve visible silhouette;
- preserve component count and relative positions;
- preserve holes, joints, screws, seams, handles, supports, logos, edge profiles, and end geometry;
- preserve visible color, texture, grain, marks, and natural variation;
- record which camera views are actually supported;
- link every locked feature to evidence.

**MUST NOT**
- replace the product with a visually similar generated product;
- redraw product geometry from text;
- invent unsupported sides or hidden construction;
- remove visible product characteristics just to make the result “cleaner”;
- treat style similarity as identity fidelity.

## Region classes

Define:
- \`LOCKED_PRODUCT_REGION\`: product identity pixels / geometry.
- \`EDITABLE_REGION\`: background, layout space, independent props, graphics, copy.
- \`CONDITIONAL_REGION\`: changes require explicit authorization and traceability.

## Pixel-preservation policy

When source-pixel compositing is possible:

\`\`\`text
source photo RGB + alpha mask
→ transform only as a whole layer
→ composite into scene
\`\`\`

Allowed by default:
- uniform scale;
- translation;
- limited rotation that does not invent a new product view;
- edge cleanup that does not remove real structure.

Not allowed by default:
- non-uniform scaling;
- liquify / warp;
- generative fill over the product body;
- product-aware style transfer;
- geometry repair by diffusion.

## Output schema

Create \`product-identity.json\` containing:
- \`sku\`
- \`variant\`
- \`authoritative_references\`
- \`geometry\`
- \`visible_features\`
- \`material_appearance\`
- \`must_preserve\`
- \`must_not_invent\`
- \`supported_views\`
- \`unsupported_views\`
- \`region_policy\`
- \`dimension_profile_ref\`
- \`provenance_policy\`
- \`approved_edits\`
- \`unknowns\`
- \`conflicts\`
- \`version\`

## Gate

Any final image that changes an identity-critical feature from the authoritative reference is \`FAIL\`.

If the requested composition requires an unsupported product view, request another real view or verified CAD/3D; otherwise mark the asset \`BLOCKED\` or \`CONCEPT_ONLY\`.