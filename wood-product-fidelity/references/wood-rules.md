# Wood Fidelity Rules

## Visible wood identity

Treat the following as identity-relevant when visible:
- grain direction;
- grain density/pattern;
- knots;
- natural color variation;
- end grain;
- joints;
- seams;
- fasteners;
- holes;
- edge profiles;
- chamfers/radii;
- component thickness / visible proportions.

## Critical construction relations

When relevant, also lock:
- what component supports/touches another;
- whether components remain visibly separate;
- screw/bolt/hole location;
- screw/bolt/hole axis/orientation;
- cradle/slot/tenon/groove relationship;
- forbidden alternate hardware placement.

Use `CRITICAL GEOMETRY LOCK` for these relations.

A candidate can match the parts list and still fail if the parts are connected incorrectly.

## MUST NOT

- replace real grain with generated grain when the asset is factual material proof;
- remove knots by default;
- clone grain across components;
- invent end grain;
- move screws/joints;
- change fastener axis;
- merge separate parts;
- make raw/matte wood glossy without evidence;
- infer species from appearance alone;
- infer oil/wax/lacquer/paint treatment without confirmation;
- infer “eco-friendly”, “zero formaldehyde”, “0 VOC”, “food safe”, or certification claims from appearance.

## Detail image rule

Preferred source:
1. real high-resolution detail photo;
2. real crop from authoritative photo;
3. verified macro reference for same SKU;
4. verified CAD for geometry where appropriate.

Reference generation MAY be used for non-critical commercial close-ups, but generated missing detail MUST NOT be presented as factual proof.

After repeated hardware/joint drift, escalate to source pixels rather than accepting “close enough”.

## Hero / lifestyle rule

Reference generation/edit may be used for natural commercial photography when:
- current-SKU references are supplied;
- identity lock passes;
- critical geometry lock passes;
- visible wood appearance remains credible;
- the image is not treated as higher-priority evidence than source photos.

## Color rule

Background and brand graphics may be color-graded.

Product color SHOULD remain source-aligned unless:
- color calibration data exists; or
- user explicitly authorizes correction.

## Layout rule

Do not ask the image model to redraw the product while also solving final six-grid layout and exact Chinese copy.

Use:
```text
approved wood-product masters
+ approved copy
+ deterministic layout
```

## QA

Set `FAIL` if:
- visible wood identity materially changes;
- locked geometry relation is wrong;
- hardware/joint/structure drifts;
- generated detail is presented as factual proof without verification;
- unverified material/environmental/safety claims appear in customer-facing copy.
