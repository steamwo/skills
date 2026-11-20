# E-commerce Prompt Rendering

## Purpose

Use stable locks for identity and geometry while allowing each semantic master to have its own commercial shot logic.

A good prompt is not the longest prompt. Weak-model reliability comes from **fixed blocks + narrow asset jobs**.

## Prompt architecture

For generative semantic masters:

```text
1. PRODUCT IDENTITY LOCK          ← stable across SKU asset family
2. CRITICAL GEOMETRY LOCK         ← stable when activated
3. REAL-WORLD SCALE LOCK          ← stable for scale-bearing family when activated
4. CAMPAIGN STYLE LOCK            ← stable across campaign / set
5. PLATFORM COMMERCE STYLE LOCK   ← stable per target platform
6. ASSET JOB / BUYER QUESTION     ← specific to this image
7. SHOT / SCENE GRAMMAR           ← specific to this image
8. HARD NEGATIVES                 ← specific, evidence-aware
```

Default semantic masters contain **no final marketing typography**.

Do not repeat irrelevant context.

## Identity lock

Derived from authoritative references.

MUST remain verbatim across candidates unless source evidence changes.

## Critical geometry lock

Read `critical-geometry-lock.md`.

Use explicit spatial relations for:
- joints;
- screws/bolts;
- holes/ports;
- cradles/supports;
- orientation;
- component separation.

MUST remain verbatim across candidates for the same SKU/revision.

Do not replace relational rules with vague adjectives.

## Campaign style lock

May include:
- palette;
- lighting;
- background family;
- camera family;
- grade;
- typography mood;
- prop density.

Do not freeze shot composition across every image.

## Platform style lock

Use `platform-style-profiles.json` as heuristic creative guidance.

Do not represent heuristic style as official platform rules.

## Weak-model reference-image template

```text
Use the exact current-SKU product shown in the supplied authoritative references.

{PRODUCT_IDENTITY_LOCK}

{CRITICAL_GEOMETRY_LOCK}

{REAL_WORLD_SCALE_LOCK}

{CAMPAIGN_STYLE_LOCK}

{PLATFORM_STYLE_LOCK}

ASSET JOB
Buyer question: {buyer_question}
Role: {asset_role}

SHOT
Camera: {camera}
Lighting: {lighting}
Composition: {composition}
Product occupancy: {occupancy}
Supporting props: {props}

PRESERVE
- all identity-critical components and proportions;
- every relation in CRITICAL GEOMETRY LOCK;
- verified scale when activated.

MUST NOT
- invent or remove components;
- relocate hardware;
- merge separate product parts;
- replace material texture with a different product;
- add unapproved accessories;
- add marketing text, dimensions, logos, certifications, or claims unless explicitly part of this asset job.
```

Omit inactive blocks rather than filling placeholders with guesses.

## Suite consistency pattern

For a multi-image set:

```text
[product identity — same]
+ [critical geometry — same when active]
+ [scale — same when active]
+ [campaign/platform style — same]
+ [shot / buyer-decision role — changes]
```

This preserves set consistency without making every image repetitive.

## Information graphics

Do not ask the image model to simultaneously:
- redraw the product;
- create multiple panels;
- typeset exact Chinese;
- draw dimension lines;
- invent icons;
- decide copy.

Instead:

```text
approved semantic masters
+ approved copy deck
+ deterministic layout manifest
→ final infographic / six-grid
```

Use `scripts/render_infographic_grid.py` or another deterministic design tool for exact final layout.

## Copy

Read `copy-guard-contract.md`.

When image-model text is unavoidable:
- use only approved exact copy;
- keep it short;
- quote exact text;
- define zones;
- QA every character/number/unit.

After repeated text failure, stop regenerating the image and move typography to deterministic layout.

## Deterministic omission

- unresolved required factual field → `BLOCKED`;
- missing optional field → omit;
- unknown fact → never fill;
- irrelevant brand section → do not inject.

## Prompt repair

QA outputs 1–3 targeted repair sentences.

For geometry drift, repair the explicit relation:

```text
Observed: screw appears in the circular end-grain face.
Expected: screw is recessed into the top surface of the cylindrical handle near the end; axis vertical to the floor.
Repair: move only the screw to the verified top-surface position. Preserve all other approved geometry, material and composition.
```

Do not rewrite the entire prompt after every failure.

## Output

Record:
- lock versions;
- final prompt;
- reference assets;
- fidelity mode;
- platform profile;
- candidate ID / round;
- repair sentences;
- accepted result.
