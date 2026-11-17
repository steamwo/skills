# Product Identity and Evidence Contract

## Purpose

Define what counts as factual product evidence and what must remain unchanged across e-commerce assets.

## Evidence states

Use:
- \`visible_in_reference\`
- \`user_confirmed\`
- \`document_verified\`
- \`estimated\`
- \`unknown\`
- \`conflicting\`

An agent MUST NOT promote \`estimated\` or \`unknown\` to a verified state.

## Identity fields

### Geometry / structure

Track:
- silhouette;
- visible proportions;
- component count;
- relative component positions;
- joints;
- holes;
- screws / fasteners;
- handles;
- supports;
- curves;
- chamfers / radii;
- edge profiles;
- contact points;
- supported camera views.

### Material appearance

Track:
- visible color;
- texture direction;
- grain / knots / natural variation;
- end-grain appearance;
- surface gloss / finish appearance;
- metal / fabric / plastic visible properties.

Appearance is not proof of species, certification, or chemical composition.

### Product facts

Track evidence for:
- brand / logo / model / SKU;
- sale quantity;
- included items;
- dimensions;
- weight;
- load capacity;
- compatibility;
- certification;
- function claims.

## Product pixel contract

When the user supplies an authoritative real product photo:

\`\`\`text
LOCKED PRODUCT BODY = authoritative source RGB
\`\`\`

Default allowed changes:
- alpha extraction;
- edge cleanup;
- uniform scaling;
- translation;
- limited source-view-consistent rotation.

Default prohibited changes:
- generative redraw;
- image-to-image repainting of the product body;
- non-uniform scale;
- liquify / warp;
- invented unseen geometry;
- texture replacement;
- hardware relocation;
- component removal / addition.

## Region classes

1. \`LOCKED_PRODUCT_REGION\`
2. \`EDITABLE_REGION\`
3. \`CONDITIONAL_REGION\`

The alpha mask is not automatically correct. Mask errors can delete real structure and must be QA-reviewed.

## Reference priority

1. current-SKU user-confirmed real photos;
2. other current-SKU real views / details;
3. current-SKU CAD / engineering / dimension documents;
4. same-series products as style/context only;
5. competitor / web / AI-generated images as non-factual references only.

## Change control

Any authorized change to a locked region MUST record:
- purpose;
- authorization;
- affected region;
- before / after asset;
- factual impact;
- QA result;
- reviewer.

A generated lookalike is not a compliant product-identity transformation.