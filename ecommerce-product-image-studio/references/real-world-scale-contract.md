# Real-World Scale Contract

## Purpose

Keep a product's apparent physical size believable when an e-commerce asset includes people, hands, furniture, tools, rooms, or other scale-bearing context.

Composition size and real-world size are separate constraints:

```text
product_occupancy = how much of the frame the product occupies
real_world_scale = how large the product is relative to the scene
```

A product MUST NOT be enlarged or shrunk relative to a person merely to improve salience.

## Activation

Create a `REAL-WORLD SCALE LOCK` when both are true:
- the asset contains a person, hand, body part, furniture, architecture, or another useful scale reference;
- one or more relevant product dimensions are `user_confirmed` or `document_verified`.

If dimensions are only `estimated`, `visible_in_reference`, `unknown`, or `conflicting`, do not turn them into metric scale claims. Use qualitative visual consistency and mark uncertainty for QA.

## Lock format

Use a concise block and keep it stable across candidates for the same asset family:

```text
REAL-WORLD SCALE LOCK
- verified dimensions: ...
- scale-bearing references: ...
- required contact / anchor plane: ...
- preserve uniform product scale;
- camera perspective may change apparent foreshortening, but must not imply a materially different physical size;
- product occupancy must not override verified physical scale;
- do not enlarge the product for prominence.
```

Only include verified dimensions that matter to the visible scene.

## Person-use scenes

When a person interacts with the product:
- calibrate against the relevant hand, forearm, foot, torso, or full-body reference;
- preserve the verified product dimensions relative to that body reference;
- preserve contact geometry and occlusion order;
- keep all repeated units / paired products at one consistent physical scale;
- use uniform scaling only;
- do not stretch one axis to make the product read larger;
- do not let a close camera angle silently turn a compact product into an oversized one.

If the product is handheld or gripped, hand size is a primary scale cue unless another verified reference is stronger.

## Perspective

Perspective changes projected image size, not physical dimensions.

Allowed:
- foreshortening;
- distance-based apparent size change;
- lens perspective consistent with the camera.

Not allowed:
- contradictory scale between near and far repeated products;
- a product that is materially too large or too small relative to a body or known scene reference;
- non-uniform scaling or geometry warp;
- using wide-angle exaggeration to defeat verified scale.

## Prompt injection

For a scale-bearing generated asset, append the lock after the product identity block and before creative scene styling.

State the numerical dimensions plainly when verified.

Example:

```text
REAL-WORLD SCALE LOCK
The handle length is a verified 40 cm and total height is a verified 8 cm.
Render both units at those real-world dimensions relative to the adult user's hands and forearms.
Do not enlarge the bars for visual prominence.
Keep both bars uniformly scaled and physically consistent with one another.
```

The numbers above are an example only; never reuse them for another SKU without evidence.

## QA

`PASS` when:
- verified dimensions and human / scene scale cues are mutually plausible;
- repeated units remain consistently scaled;
- contact plane, perspective and product size agree.

`REVIEW` when:
- no reliable metric calibration exists but qualitative scale looks plausible.

`FAIL` when:
- verified dimensions contradict the apparent person / scene scale;
- the product has been enlarged or shrunk for salience;
- repeated units use inconsistent physical scale;
- non-uniform scaling or warp changes physical proportions.

A scale failure is a factual failure, not merely a composition preference.
