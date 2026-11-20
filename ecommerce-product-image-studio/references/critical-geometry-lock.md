# Critical Geometry Lock Contract

## Purpose

Protect **identity-critical spatial relationships** that are easy for image models to simplify, relocate, merge, or redraw incorrectly.

A PRODUCT IDENTITY LOCK describes what parts exist. A `CRITICAL GEOMETRY LOCK` describes **how those parts are related in space**.

Use both when the product has joints, fasteners, ports, hinges, cradles, brackets, seams, interfaces, or other construction details whose position/orientation distinguishes the real SKU.

## Activation

Create a `CRITICAL GEOMETRY LOCK` when any of these are true:

- two or more visible components meet through a specific joint or support;
- screw / bolt / hole / port placement matters;
- a fastener axis or opening direction matters;
- a handle, rail, leg, panel, bracket, or base has a specific relative position;
- the user corrects a geometry detail;
- a previous candidate drifted on construction;
- a close-up/detail asset makes the relationship commercially important.

Do not activate it for decorative details that are not identity-critical.

## Evidence

Every locked relation MUST come from:
- authoritative current-SKU photos;
- user confirmation;
- verified CAD / engineering drawings;
- or other document-verified evidence.

Unknown hidden geometry remains unknown.

## Relation model

Record each critical relation as a small tuple:

```text
subject
+ relation
+ object / anchor
+ orientation / axis
+ location
+ must-not condition
+ evidence reference
```

Examples:
- screw + embedded in + round handle + axis vertical to floor + near handle end + MUST NOT appear in end-grain center;
- round handle + rests in + semicircular cradle + horizontal + above triangular base + MUST NOT merge into base.

Prefer explicit relational language over adjectives such as “sturdy”, “precise”, or “premium”.

## Lock format

Keep the block short and reuse it verbatim across candidates for the same SKU/revision:

```text
CRITICAL GEOMETRY LOCK
- ...
- ...
- ...
HARD RULE: any violation of a listed relation is identity failure, not a styling variation.
```

For weak-model execution, do not paraphrase the lock between candidates.

## Example — wooden parallette / push-up support

This example is illustrative and only applies when supported by the current SKU references:

```text
CRITICAL GEOMETRY LOCK
- The cylindrical wooden handle runs horizontally above two separate triangular wooden bases.
- Each base supports the handle at its top cradle; handle and base remain visibly separate components.
- The circular end grain of the handle remains visible from supported end views.
- A recessed metal hex screw sits on the TOP surface of the cylindrical handle near each end.
- The screw axis is approximately vertical to the floor.
- The screw MUST NOT appear in the center of the circular end-grain face.
- Black anti-slip pads remain on the bottom contact surfaces of the bases.
HARD RULE: do not relocate hardware, merge handle and base, or invent a different joint.
```

## Prompt placement

For generative assets, inject in this order:

```text
PRODUCT IDENTITY LOCK
CRITICAL GEOMETRY LOCK
REAL-WORLD SCALE LOCK (when activated)
CAMPAIGN STYLE LOCK
PLATFORM COMMERCE STYLE LOCK
ASSET JOB
SHOT / SCENE
HARD NEGATIVES
```

Geometry locks come before creative styling.

## Detail-route escalation

For an identity-critical joint / hardware close-up:

1. use an authoritative real crop when it already proves the detail;
2. otherwise use REFERENCE_EDIT / REFERENCE_GENERATE with the geometry lock;
3. after one geometry failure, strengthen only the failed relation;
4. after two geometry failures, escalate to SOURCE_PRODUCT_PIXEL / STRICT_PIXEL_COMPOSITE or verified CAD rather than repeatedly redrawing the joint.

Do not use a generated close-up as factual proof when the joint cannot be verified.

## QA

Evaluate every locked relation separately.

Return for each relation:
- `PASS`;
- `FAIL`;
- `NOT_VISIBLE`;
- `NOT_CHECKED`.

A visible contradiction on a critical relation = `FAIL`.

Do not average geometry failure away with high composition or lighting scores.

## Repair output

For a failed relation, produce one precise repair instruction:

```text
Observed: ...
Expected: ...
Repair: ...
Preserve: all other approved geometry and styling.
```

Repair the smallest responsible region/asset. Do not redesign the whole product.
