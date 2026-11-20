# Product Identity and Evidence Contract

## Purpose

Define what counts as factual product evidence and what must remain unchanged across ecommerce assets.

Product identity is independent of fidelity route: a reference-rendered product may be valid when it remains the same SKU, while an identity-critical detail may require original source pixels.

## Evidence states

Use:
- `visible_in_reference`
- `user_confirmed`
- `document_verified`
- `estimated`
- `unknown`
- `conflicting`

An agent MUST NOT promote `estimated` or `unknown` to a verified state.

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

When a relative position/orientation is identity-critical, promote it into a separate `CRITICAL GEOMETRY LOCK`.

### Material appearance

Track:
- visible color;
- texture direction;
- grain / knots / natural variation;
- end-grain appearance;
- surface gloss / finish appearance;
- metal / fabric / plastic visible properties.

Appearance is not proof of species, certification, chemical composition, or environmental performance.

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

## Product Identity Lock

Create a concise stable block from authoritative evidence.

It describes:
- what visible components exist;
- proportions/silhouette;
- visible materials/finish;
- visible hardware/features;
- must-not-change details;
- must-not-appear items.

Reuse it verbatim across candidates until evidence changes.

## Critical Geometry Lock

Read `critical-geometry-lock.md`.

Use it when spatial relations matter, for example:
- screw location and axis;
- handle-to-base cradle relationship;
- hinge direction;
- port placement;
- bracket orientation;
- component separation.

A PRODUCT IDENTITY LOCK answers “what is present”; a CRITICAL GEOMETRY LOCK answers “where/how is it connected”.

## Real-world scale identity

Verified dimensions are part of product identity when an asset contains a person or another useful scale-bearing reference.

When relevant dimensions are `user_confirmed` or `document_verified`:
- preserve them as a `REAL-WORLD SCALE LOCK`;
- calibrate against hands, body parts, furniture, architecture, or other scene references as appropriate;
- preserve one uniform physical scale across repeated / paired units;
- do not enlarge the product merely to increase visual prominence;
- treat perspective as projected appearance, not permission to change physical size.

Visible proportions without metric evidence can guide qualitative consistency but MUST NOT be promoted into verified dimensions.

See `real-world-scale-contract.md`.

## Fidelity-route-specific pixel rules

Do not apply a universal “source RGB only” rule to every ecommerce asset.

### REFERENCE_GENERATE / REFERENCE_EDIT

The model may re-render product pixels when:
- authoritative current-SKU references are provided;
- identity lock is active;
- critical geometry lock is active when needed;
- resulting identity and geometry pass QA;
- the output is not used as factual proof for a detail that cannot be verified.

Exact source pixels are not required.

### SOURCE_PRODUCT_PIXEL / STRICT_PIXEL_COMPOSITE

When exact source pixels are selected/required:

```text
LOCKED PRODUCT BODY = authoritative source RGB
```

Allowed:
- alpha extraction;
- edge cleanup;
- uniform scaling;
- translation;
- limited source-view-consistent rotation;
- non-destructive crop.

Prohibited:
- generative redraw/repaint of locked product region;
- non-uniform scale;
- liquify / warp;
- invented unseen geometry;
- texture replacement;
- hardware relocation;
- component removal/addition.

### VERIFIED_CAD_3D

Permitted only when the CAD/3D source is verified for the current SKU and the requested view is supported.

### CONCEPT_ONLY

Must not be represented as the actual verified SKU.

## Region classes for source-pixel routes

1. `LOCKED_PRODUCT_REGION`
2. `EDITABLE_REGION`
3. `CONDITIONAL_REGION`

The alpha mask is not automatically correct. Mask errors can delete real structure and must be QA-reviewed.

## Reference priority

1. current-SKU user-confirmed real photos;
2. other current-SKU real views / details;
3. current-SKU CAD / engineering / dimension documents;
4. same-series products as style/context only;
5. competitor / web / AI-generated images as non-factual references only.

AI-generated candidates NEVER become higher-priority factual evidence than authoritative source assets.

## Change control

Any authorized change to an identity-critical region/relation SHOULD record:
- purpose;
- authorization/evidence;
- affected region/relation;
- before/after asset;
- factual impact;
- QA result;
- reviewer.

A generated lookalike is not compliant merely because it is visually attractive.
