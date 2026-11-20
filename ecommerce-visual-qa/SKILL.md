---
name: ecommerce-visual-qa
description: Run ecommerce visual QA for SKU identity, critical geometry, commercial composition, platform style fit, buyer-decision coverage, reference fidelity, person/contact realism, copy truth, deterministic layout provenance, derivatives, and delivery completeness; output targeted repair instructions.
---

# Ecommerce Visual QA

## Objective

Decide whether an asset is **good enough to sell with**, not merely whether it is technically attractive.

## Hard gates

A hard failure cannot be averaged away:
- wrong SKU / identity drift;
- critical geometry relation failure;
- wrong variant;
- invented specification / claim;
- broken anatomy / product interaction;
- unreadable or wrong required text;
- false compliance claim;
- final layout containing an unapproved product redraw.

## Gate A — Product identity

Compare directly with authoritative product reference.

Check:
- silhouette / proportions;
- component count;
- hardware / holes / supports;
- colour / finish;
- logo / printed graphics where relevant;
- variant-specific details.

## Gate A2 — Critical geometry

When a critical geometry lock exists, check each relation explicitly:
- correct component;
- correct anchor/object;
- correct location;
- correct orientation/axis;
- must-not conditions absent;
- separate parts remain separate.

Return `PASS/FAIL/NOT_VISIBLE` per relation.

Any visible contradiction = hard `FAIL`.

## Gate B — Commercial composition

Check:
- product is visually obvious;
- product size is appropriate for role;
- scene supports rather than competes;
- props are relevant;
- hierarchy survives mobile / thumbnail viewing;
- image feels like intentional commercial photography.

## Gate C — Scene story

For lifestyle/person scenes:
- who / where / action is understandable;
- scene is relevant;
- lighting and contact feel coherent;
- use context answers a buyer question.

## Gate D — Platform style fit

Evaluate against selected heuristic profile.

Report `platform_style_fit` separately from official compliance.

## Gate E — Buyer-decision coverage

Check that the asset actually answers its declared buyer question.

## Gate F — Fidelity mode

If `REFERENCE_RENDERED_PRODUCT`:
- same-product identity and critical geometry must pass;
- exact source pixels are not required.

If `SOURCE_PRODUCT_PIXEL`:
- source pixel provenance and mask quality must pass.

For factual joint/hardware proof, repeated model-rendered drift should escalate route.

## Gate G — Dimensions / facts

Check value, unit, axis, variant scope and evidence.

## Gate H — Person interaction

Check anatomy, grip/contact, weight-bearing logic, occlusion, product geometry and verified scale.

## Gate I — Text / information graphics

Check against approved copy deck:
- exact wording;
- spelling / units;
- hierarchy;
- mobile / thumbnail readability;
- no model-invented text;
- no semantic strengthening of claims.

## Gate I2 — Layout provenance

For multi-panel/detail boards:
- every cell comes from an approved semantic master;
- every text block maps to approved copy;
- product images are only cropped/contained, not warped/redrawn;
- a one-cell repair does not require whole-board regeneration.

A one-shot factual AI poster that bypasses master QA is a hard failure.

## Gate J — Set consistency

Check:
- campaign palette / light / grade;
- same product family;
- same critical geometry;
- no contradictory copy;
- varied shot roles without stylistic chaos.

## Gate K — Candidate ranking

First apply hard gates.

Then score:
- identity_fidelity;
- critical_geometry_fidelity;
- commercial_composition;
- scene_story;
- product_salience;
- platform_style_fit;
- lighting_realism;
- person_interaction;
- text_readability;
- claim_truth.

## Repair output

When an asset fails, output structured fields:
- failure reason;
- severity;
- error region;
- observed;
- expected;
- evidence reference;
- 1–3 targeted repair sentences;
- preserve list;
- route action.

Examples:
- screw location wrong → state verified surface, axis and forbidden location;
- merged joint → restore separation without redesign;
- scene too busy → remove unrelated props;
- person contact wrong → specify exact contact geometry;
- text bad → move exact copy to deterministic layout;
- one grid cell bad → replace only that master/cell.

## Retry gate

Regenerate **only the failed semantic master**.

After bounded repair rounds, escalate route or mark for human review.

## Delivery

QA report SHOULD include:
- accepted candidate/master ID;
- fidelity mode;
- lock versions;
- hard-gate statuses;
- commercial score fields;
- repair history;
- layout provenance when applicable;
- final recommendation.
