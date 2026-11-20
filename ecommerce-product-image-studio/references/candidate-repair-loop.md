# Candidate Generation, Ranking and Repair Loop

## Purpose

High-quality ecommerce visuals should not rely on the first random generation.

Use a bounded loop:

```text
brief
→ generate candidates
→ identity QA
→ critical-geometry QA
→ commercial composition QA
→ platform-style QA
→ rank
→ accept best OR repair smallest failed asset/region
```

## Candidate policy

For visually important generative semantic masters:
- hero: 2–3 candidates when budget allows;
- lifestyle: 2–3 distinct candidates;
- person-use: 2–3 candidates because anatomy/contact failure rate is higher;
- simple source-pixel detail / deterministic graphic: one candidate may be enough.

Candidates should vary **one creative axis at a time**:
- camera;
- environment;
- lighting;
- person action;
- product placement.

Do not vary the identity or critical-geometry lock.

## Hard gates before scoring

Before numerical ranking, reject candidates with:
- wrong SKU / component count;
- critical geometry relation failure;
- wrong variant;
- invented claim/dimension;
- broken person/product contact;
- verified-scale contradiction.

Never average away a hard failure.

## Ranking dimensions

For candidates that pass hard gates, score separately:
- `identity_fidelity`;
- `critical_geometry_fidelity`;
- `commercial_composition`;
- `scene_story`;
- `product_salience`;
- `platform_style_fit`;
- `lighting_realism`;
- `person_interaction` when applicable;
- `real_world_scale_fidelity` when applicable;
- `text_readability` when applicable;
- `claim_truth`.

## Structured failure output

Weak-model QA SHOULD return:

```text
asset_id:
status: PASS | FAIL | REVIEW
failure_type:
error_region:
observed:
expected:
evidence_ref:
repair_sentence:
preserve:
route_action: RETRY_SAME | ESCALATE_FIDELITY | CHANGE_SCENE | BLOCK
```

This is preferred over free-form critique.

## Repair sentences

QA SHOULD output 1–3 specific repair instructions.

Examples:
- hardware relocation → “Move the recessed screw from the end-grain face to the verified top surface of the handle near its end; keep screw axis vertical to floor; preserve all other geometry.”
- merged parts → “Restore visible separation between handle and base cradle; do not redesign either component.”
- scene too busy → reduce props and simplify background;
- product too small → increase frame occupancy without changing physical scale;
- product too large/small relative to person → restate verified dimensions and body reference;
- lighting conflict → specify one dominant light direction;
- person contact wrong → specify exact hand/foot/support contact;
- platform mismatch → reapply platform style lock;
- text error → stop regenerating imagery and move exact copy to deterministic layout.

## Geometry escalation rule

For the same critical relation:
- first failure → retry with explicit observed/expected repair sentence;
- second failure → escalate fidelity mode for that asset/region;
- do not spend a third ordinary redraw attempt merely hoping the relation changes.

For factual joint/hardware proof, prefer source product pixels or verified CAD after repeated drift.

## Retry cap

Default maximum:
- 2 repair rounds for ordinary scenes;
- 3 for high-value person-use assets only when the failure is not identity/critical-geometry drift;
- critical-geometry repeated failure escalates after 2 attempts.

After cap:
- escalate fidelity mode;
- change scene/camera;
- switch tool/model;
- or mark `REVIEW/BLOCKED`.

Do not loop indefinitely.

## Layout repair

If a six-grid/detail board has one bad cell:
- replace only the failed source master or copy block;
- rerender deterministic layout;
- do not regenerate all cells as one image.

## Manifest

Record each round:
- candidate ID;
- prompt;
- reference inputs;
- hard-gate results;
- scores;
- failures;
- repair sentences;
- route action;
- accepted candidate;
- reason.

This makes visual iteration reproducible instead of subjective.
