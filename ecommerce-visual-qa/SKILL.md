---
name: ecommerce-visual-qa
description: Run ecommerce visual QA for SKU identity, commercial composition, platform style fit, buyer-decision coverage, reference fidelity, person/contact realism, text readability, evidence truth, derivatives, and delivery completeness; output targeted repair instructions for failed assets.
---

# Ecommerce Visual QA

## Objective

Decide whether an asset is **good enough to sell with**, not merely whether it is technically valid.

## Hard gates

A hard failure cannot be averaged away:
- wrong SKU / identity drift;
- wrong variant;
- invented specification / claim;
- broken anatomy / product interaction;
- unreadable or wrong required text;
- false compliance claim.

## Gate A — Product identity

Compare directly with authoritative product reference.

Check:
- silhouette / proportions;
- component count;
- hardware / holes / supports;
- colour / finish;
- logo / printed graphics where relevant;
- variant-specific details.

## Gate B — Commercial composition

Check:
- product is visually obvious;
- product size is appropriate for role;
- scene supports rather than competes;
- props are relevant;
- hierarchy survives mobile / thumbnail viewing;
- image feels like intentional commercial photography rather than a pasted collage.

## Gate C — Scene story

For lifestyle/person scenes:
- who / where / action is understandable;
- scene is relevant to the product;
- lighting and contact feel coherent;
- use context answers a buyer question.

A generic beautiful room with no product story is \`REVIEW\` or \`FAIL\`.

## Gate D — Platform style fit

Evaluate against the selected heuristic profile:
- Taobao/Tmall/1688: enough factual/trust-building coverage, coherent detail-page language;
- Pinduoduo: direct value/variant clarity and thumbnail readability;
- Douyin: content-native mobile impact, believable scene/person use, product/content relevance.

Report \`platform_style_fit\` separately from official compliance.

## Gate E — Buyer-decision coverage

Check that the asset actually answers its declared buyer question.

## Gate F — Fidelity mode

If \`REFERENCE_RENDERED_PRODUCT\`:
- same-product identity must pass;
- exact source pixels are not required.

If \`SOURCE_PRODUCT_PIXEL\`:
- source pixel provenance and mask quality must pass.

Do not fail a natural reference-rendered scene merely because its pixels differ from the input photo.

## Gate G — Dimensions / facts

Check value, unit, axis, variant scope and evidence.

## Gate H — Person interaction

Check anatomy, grip/contact, weight-bearing logic, occlusion and product geometry.

## Gate I — Text / information graphics

Check:
- exact approved wording;
- spelling / units;
- hierarchy;
- mobile / thumbnail readability;
- no model-invented text.

## Gate J — Set consistency

Check:
- campaign palette / light / grade;
- same product family;
- no contradictory copy;
- varied shot roles without stylistic chaos.

## Gate K — Candidate ranking

Score:
- identity_fidelity
- commercial_composition
- scene_story
- product_salience
- platform_style_fit
- lighting_realism
- person_interaction
- text_readability
- claim_truth

Select the best candidate only after hard gates pass.

## Repair output

When an asset fails, output:
- failure reason;
- severity;
- 1–3 targeted prompt repair sentences;
- whether to retry same route, change scene/camera, or escalate fidelity mode.

Examples:
- product drift → restate exact identity features;
- product too small → increase occupancy / sharpest-element instruction;
- scene too busy → remove unrelated props;
- person contact wrong → specify exact contact geometry;
- platform mismatch → reapply platform style lock;
- text bad → shorten or move to deterministic layout.

## Retry gate

Regenerate **only the failed asset**.

After bounded repair rounds, escalate route or mark for human review.

## Delivery

QA report SHOULD include:
- accepted candidate ID;
- fidelity mode;
- platform style profile;
- hard-gate statuses;
- commercial score fields;
- repair history;
- final recommendation.