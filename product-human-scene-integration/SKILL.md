---
name: product-human-scene-integration
description: Integrate authoritative product pixels, independent person layers, and a scene using calibrated placement, occlusion, contact points, and shadows without redrawing or deforming the product.
---

# Product Human Scene Integration

## Objective

Create a believable product + person + environment composition while preserving the SKU identity.

## Required inputs

- \`product-identity.json\`
- \`product-dimensions.json\`
- \`scale-calibration.json\`
- product cutout from authoritative source pixels
- person layers / pose plan
- empty background
- applicable wood fidelity rules

## Layer model

A useful structure is:

\`\`\`text
background
background props
rear person parts
product shadow
SOURCE PRODUCT PIXELS
front person parts
foreground props
text / graphics
\`\`\`

Split the person into front / rear regions when needed for realistic hand or body occlusion.

## MUST

- preserve product pixels and geometry;
- use the same camera / contact-plane assumptions across product, person, and scene;
- align all contact points;
- ensure correct foreground / background order;
- keep contact and cast shadows independent;
- verify hands, fingers, feet, body support, and gravity;
- record person scale status.

## MUST NOT

- fuse a generated person and generated lookalike product into a single image and call it the real SKU;
- generatively repaint the product under hands;
- stretch the product to match hand position;
- move hardware / supports / handles to improve interaction;
- imply unverified product capability.

## Interaction problem handling

If a hand cannot grip the real product geometry:
- change hand pose;
- change person placement;
- change camera / crop;
- use another verified product view.

Never “fix” the product.

## Failure conditions

\`FAIL\`:
- product structure changes;
- product texture / hardware / component count changes;
- person intersects impossible product geometry;
- occlusion produces impossible structure.

\`REVIEW\`:
- interaction is visually plausible but person or scene scale is estimated.

\`BLOCKED\`:
- required interaction cannot be achieved from available source views without product redraw.

## Outputs

Save:
- integration brief;
- product source / cutout;
- person source / split layers;
- background;
- masks;
- shadow layers;
- layered composite;
- \`integration-qa.md\`;
- asset provenance.

Final QA MUST report product identity, product pixel provenance, scale, and person interaction separately.