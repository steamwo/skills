---
name: ecommerce-product-image-studio
description: Orchestrate a conversion-first ecommerce visual production system from real SKU references using product identity locks, platform commerce style profiles, reference-image generation, commercial scene routing, candidate ranking/repair, SKU variants, responsive derivatives, QA, and accountable delivery.
---

# Ecommerce Product Image Studio

## Objective

Produce a **commercially strong, platform-aware, same-SKU image set**.

Priority order:
1. same-SKU identity;
2. truthful product facts;
3. buyer-decision / conversion job;
4. platform commerce style fit;
5. natural commercial photography;
6. variant correctness;
7. campaign consistency;
8. efficient reuse / derivatives;
9. official platform compliance.

Exact source pixels are not the default objective for every asset.

## Required contracts

Read:
- task input / intake;
- product identity;
- real-world scale contract;
- reference generation contract;
- platform commerce style contract + profiles;
- commercial scene router;
- buyer decision framework;
- variant matrix;
- campaign / brand visual system;
- candidate repair loop;
- output profile / detail module;
- execution state / delivery gate.

## Stage 1 — Intake / evidence

Separate:
- explicit user intent;
- product evidence;
- platform selection;
- verified claims / dimensions.

## Stage 2 — Product identity lock

Study all authoritative product photos.

Create one concise \`PRODUCT IDENTITY LOCK\` and reuse it verbatim across the set.

## Stage 3 — Variant / dimension model

Build variant matrix and dimension records where needed.

When verified physical dimensions exist for a scale-bearing scene, create a `REAL-WORLD SCALE LOCK` from those dimensions and relevant human / scene references.

Unknown facts stay unknown.

## Stage 4 — Platform commerce style

If platform is specified, load its heuristic style profile.

Create \`PLATFORM COMMERCE STYLE LOCK\`.

Do not confuse this with official compliance rules.

## Stage 5 — Campaign style lock

Create one stable campaign block:
- palette;
- light family;
- background family;
- camera family;
- grade;
- typography mood;
- prop density;
- hard avoids.

Use selective injection by asset type.

## Stage 6 — Buyer-decision / asset plan

Plan the set by purchase questions and platform conversion mix.

Each asset gets one dominant job.

## Stage 7 — Fidelity route per asset

Choose:

\`\`\`text
REFERENCE_GENERATE   ← default for most hero / scene / in-use / detail photography
REFERENCE_EDIT
STRICT_PIXEL_COMPOSITE
VERIFIED_CAD_3D
CONCEPT_ONLY
\`\`\`

Do not default to segmentation.

Use strict-pixel only when exact source details require it.

## Stage 8 — Commercial shot / scene router

For each generative asset, define:
- story;
- camera;
- lighting;
- product occupancy;
- props;
- person action;
- platform style;
- scale reference where relevant;
- `REAL-WORLD SCALE LOCK` when verified dimensions and scale-bearing context exist.

Product occupancy is a composition target. It MUST NOT override verified real-world physical scale.

## Stage 9 — Generate candidates

For important hero / lifestyle / person assets, generate 2–3 candidates when budget allows.

Keep:
- product identity block stable;
- campaign/platform style stable.

Vary:
- camera;
- scene;
- action;
- light

one axis at a time.

## Stage 10 — Candidate QA / repair

Rank candidates on commercial and factual dimensions.

Reject hard identity / claim / anatomy / verified-scale failures.

For a failed asset:
- output targeted repair sentences;
- append them to that asset prompt;
- regenerate only that asset.

Do not restart the whole set.

## Stage 11 — Detail modules / text

Use one-screen-one-job.

Short Chinese copy can be generated when the model is reliable; exact / repeated copy should be rendered deterministically if necessary.

For gallery images, test thumbnail readability.

## Stage 12 — Derivatives

Reuse approved semantic masters across:
- platform;
- mobile / web;
- language;
- crop / surface

when dependencies remain valid.

## Stage 13 — Platform compliance

Verify current official marketplace rules separately from style heuristics.

## Stage 14 — Delivery

Deliver accepted assets, prompts / manifests where useful, QA and repair history.

A complete task means the requested final derivatives are actually accessible to the user.

## Failure conditions

\`FAIL\` when:
- product is recognisably another SKU;
- scene is physically implausible;
- required text is wrong;
- claim or dimension is invented;
- verified product dimensions contradict apparent person / scene scale;
- wrong variant appears;
- person/product interaction is broken.

\`REVIEW\` when:
- scene is commercially weak;
- platform style fit is weak;
- scale is only visually approximate;
- product identity is plausible but not confidently verifiable.

## Core principle

A natural reference-rendered scene with the correct product is often better ecommerce output than a technically perfect cutout pasted into a weak artificial background.