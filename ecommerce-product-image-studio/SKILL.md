---
name: ecommerce-product-image-studio
description: Orchestrate a conversion-first ecommerce visual production system from real SKU references using identity and critical-geometry locks, approved semantic masters, evidence-bound copy, deterministic layout, platform style profiles, candidate repair, SKU variants, QA, and accountable delivery.
---

# Ecommerce Product Image Studio

## Objective

Produce a **commercially strong, platform-aware, same-SKU image set** while remaining reliable on weaker models.

Priority order:
1. same-SKU identity;
2. critical geometry / construction truth;
3. truthful product facts and copy;
4. buyer-decision / conversion job;
5. platform commerce style fit;
6. natural commercial photography;
7. variant correctness;
8. campaign consistency;
9. efficient reuse / derivatives;
10. official platform compliance.

Exact source pixels are not the default objective for every asset, but identity-critical detail proof may require source pixels.

## Execution model

Treat this skill as a **gated state machine**, not a long free-form prompt.

Each stage produces a small durable artifact. A downstream stage MUST NOT silently invent missing upstream facts.

For weak-model execution:
- prefer structured records over prose memory;
- the controller outputs a small `prompt-job.json`, not a free-form image prompt;
- compile the final image prompt with `scripts/prompt_compiler.py`;
- keep stable locks outside the dynamic job and reuse them verbatim;
- generate one visual job at a time;
- approve semantic masters before layout;
- separate copy generation from image generation;
- repair the smallest failed asset/region;
- never let a final collage become the first place product geometry is evaluated.

## Required contracts

Read:
- task input / intake;
- product identity;
- critical geometry lock;
- real-world scale contract;
- reference generation contract;
- platform commerce style contract + profiles;
- commercial scene router;
- buyer decision framework;
- variant matrix;
- campaign / brand visual system;
- semantic master contract;
- evidence-bound copy guard;
- deterministic grid layout contract;
- candidate repair loop;
- output profile / detail module;
- QA gates;
- execution state / delivery gate.

## Stage 0 — Execution preflight

Verify:
- authoritative references are readable;
- required generation/edit/layout tools exist;
- output destination works;
- requested platform/profile facts are known when needed.

Write `execution-preflight.json`.

Blocked capability = downgrade explicitly or mark affected assets `BLOCKED`. Do not silently switch fidelity routes.

## Stage 1 — Intake / evidence

Separate:
- explicit user intent;
- product evidence;
- platform selection;
- verified claims / dimensions.

Write `task-input.json` and evidence records.

## Stage 2 — Product identity lock

Study all authoritative current-SKU photos.

Create one concise `PRODUCT IDENTITY LOCK` and reuse it verbatim across the set.

The lock describes:
- components;
- silhouette;
- proportions;
- visible material appearance;
- hardware/features;
- must-not-change details.

## Stage 3 — Critical geometry lock

Read `references/critical-geometry-lock.md`.

Activate when joints, fasteners, holes, ports, cradles, supports, interfaces, component orientation, or other spatial relationships are identity-critical.

Create one concise `CRITICAL GEOMETRY LOCK` from evidence.

This lock describes **relationships**, for example:
- screw on top surface of handle;
- screw axis vertical to floor;
- handle rests in base cradle;
- screw must not move to end-grain face.

A visible violation of a locked relation is `FAIL`, even if the image is attractive.

## Stage 4 — Variant / dimension model

Build variant matrix and dimension records where needed.

When verified physical dimensions exist for a scale-bearing scene, create a `REAL-WORLD SCALE LOCK` from those dimensions and relevant human / scene references.

Unknown facts stay unknown.

## Stage 5 — Platform + campaign style locks

If platform is specified, load its heuristic style profile and create `PLATFORM COMMERCE STYLE LOCK`.

Create one stable `CAMPAIGN STYLE LOCK`:
- palette;
- light family;
- background family;
- camera family;
- grade;
- typography mood;
- prop density;
- hard avoids.

These locks guide style; they do not authorize product changes or unsupported claims.

## Stage 6 — Buyer-decision / asset plan

Plan by purchase questions, not image count.

Each asset gets one dominant job.

Before adding decorative variants, cover high-impact unanswered questions such as:
- recognition;
- material / construction;
- usage;
- fit / scale;
- variant choice;
- dimensions;
- included items;
- risk reduction.

## Stage 7 — Semantic master plan

Read `references/semantic-master-contract.md`.

Plan independently QA-able visual masters such as:
- hero;
- size / variant visual;
- material crop;
- joint / hardware detail;
- contact / anti-slip detail;
- lifestyle/person-use scene.

Default rule: **no final marketing text inside generated semantic masters**.

For a six-grid/detail board, define the six jobs first. Do not ask an image model to invent the final six-panel board in one pass.

## Stage 8 — Fidelity route per master

Choose:

```text
REFERENCE_GENERATE   ← default for many hero / scene / in-use assets
REFERENCE_EDIT
SOURCE_PRODUCT_PIXEL / STRICT_PIXEL_COMPOSITE
VERIFIED_CAD_3D
CONCEPT_ONLY
```

Use stricter routes for:
- logos / packaging text;
- exact labels;
- precision interfaces;
- identity-critical joint/hardware detail that repeatedly drifts;
- material proof where generated texture would become false evidence.

Do not default to segmentation for every asset.

## Stage 9 — Compile prompt

For weak-model execution, the controller MUST NOT write the final natural-language image prompt.

Instead:
1. output `prompt-job.json` using `references/prompt-job.schema.json`;
2. load stable locks from a separate prompt-lock record;
3. run `scripts/prompt_compiler.py`;
4. send the compiled prompt plus authoritative reference images to the image model.

The compiler injects stable blocks in this order:

```text
PRODUCT IDENTITY LOCK
CRITICAL GEOMETRY LOCK (when activated)
REAL-WORLD SCALE LOCK (when activated)
CAMPAIGN STYLE LOCK
PLATFORM COMMERCE STYLE LOCK
ASSET JOB / BUYER QUESTION
SHOT / SCENE
PRESERVE
MUST NOT
TARGETED REPAIR (when present)
```

Weak-model rule: do not paraphrase stable locks between candidates and do not bypass the compiler with a handwritten prompt.

## Stage 10 — Generate candidates

For important hero / lifestyle / person assets, generate 2–3 candidates when budget allows.

Keep identity, critical geometry, scale, campaign and platform locks stable.

Vary one creative axis at a time:
- camera;
- scene;
- action;
- light;
- placement.

## Stage 11 — Semantic master QA / repair

Run identity, critical-geometry, facts, scale, interaction and material QA **before layout**.

Reject hard failures.

For a failed asset:
- identify the exact failed relation/region;
- output 1–3 targeted repair sentences;
- regenerate only that asset;
- preserve all approved geometry.

After bounded retries, escalate fidelity mode rather than endlessly redrawing the same detail.

Only `APPROVED` masters may enter final information layout.

## Stage 12 — Copy guard

Read `references/copy-guard-contract.md`.

Create an approved copy deck from evidence-backed facts.

The copy model MUST NOT:
- invent new product outcomes;
- strengthen user wording into safety/environmental/certification claims;
- change verified dimensions;
- add load capacity, medical, ergonomic, posture, performance or chemical claims without evidence.

Exact/repeated Chinese, numbers and units should be rendered deterministically.

## Stage 13 — Deterministic layout

Read `references/deterministic-grid-layout-contract.md`.

Compose approved masters + approved copy using deterministic layout tooling.

For a six-grid / multi-panel board:
- map each cell to one approved master;
- map every text block to approved copy IDs;
- use crop/contain only; never warp product geometry;
- repair a failed cell independently;
- do not regenerate the whole board to fix one panel.

`scripts/render_infographic_grid.py` is a baseline deterministic renderer.

## Stage 14 — Derivatives

Reuse approved semantic masters across:
- platform;
- mobile / web;
- language;
- crop / surface

when dependencies remain valid.

A different profile may require a redesigned layout rather than mechanical resizing.

## Stage 15 — Platform compliance

Verify current official marketplace rules separately from style heuristics.

A design preset is not automatically a verified compliance profile.

## Stage 16 — Delivery

Deliver:
- accepted assets;
- approved locks;
- copy deck;
- prompts/manifests where useful;
- QA and repair history;
- final derivatives.

A complete task means requested final derivatives are actually accessible and every delivered asset is QA-accounted.

## Weak-model invariants

When execution quality is uncertain, enforce these invariants:

1. facts come from evidence tables, not prose improvisation;
2. critical geometry is represented as explicit subject–relation–object rules;
3. semantic masters contain one visual job;
4. final text comes from approved copy deck;
5. final multi-panel layouts are deterministic;
6. a hard identity/geometry/fact failure cannot be averaged away;
7. retries modify only failed instructions/regions;
8. layout never creates a new unreviewed product rendering;
9. weak controllers emit structured prompt jobs, not final image prompts;
10. final image prompts are compiler output from stable locks + bounded job fields.

## Failure conditions

`FAIL` when:
- product is recognisably another SKU;
- a critical geometry relation is contradicted;
- scene is physically implausible;
- required text differs from approved exact copy;
- a claim or dimension is invented;
- verified product dimensions contradict apparent person / scene scale;
- wrong variant appears;
- person/product interaction is broken;
- final layout uses an unapproved semantic master;
- a factual detail board contains AI-invented construction presented as proof.

`REVIEW` when:
- scene is commercially weak;
- platform style fit is weak;
- scale is only visually approximate;
- product identity is plausible but not confidently verifiable.

## Core principle

Use image generation for **commercial photography**, structured locks for **product truth**, evidence-bound copy for **claims**, and deterministic tools for **final information layout**.

Do not force one model call to solve all four jobs at once.
