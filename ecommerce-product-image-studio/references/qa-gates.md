# E-commerce Product Visual QA Gates

Evaluate every semantic master independently, then evaluate final layouts, then evaluate the complete set.

Do not use one image passing QA to imply the whole set passes.

## Gate 0 — Task input integrity

- `task-input.json` exists when the orchestrator workflow is used;
- required task fields are satisfied;
- select / radio / checkbox values are legal;
- marketplace / ratio / language / market / style / deliverables came from explicit user intent or an explicit legal auto policy;
- attachment appearance or filenames were not used to invent user intent;
- extra requirements map to actual user wording.

## Gate 1 — Product evidence

- source assets exist and can be opened;
- SKU / variant is identified when available;
- view coverage is recorded;
- dimensions / claims have evidence states;
- product images were inspected for visible identity evidence;
- packaging quantity is not inferred from photo count.

## Gate 2 — Product identity

- geometry matches authoritative references;
- component count matches;
- hardware, holes, seams, joints, handles, supports, logos, and edge profiles match;
- no unsupported hidden structure was invented.

Identity drift = `FAIL`.

## Gate 2A — Critical geometry

When `CRITICAL GEOMETRY LOCK` is active, evaluate every relation separately:

- subject is correct;
- relation to anchor/object is correct;
- location is correct;
- orientation/axis is correct;
- must-not conditions are absent;
- separate parts have not been merged;
- hardware has not been relocated.

Statuses per relation:
- `PASS`
- `FAIL`
- `NOT_VISIBLE`
- `NOT_CHECKED`

A visible contradiction on a locked relation = `FAIL`.

Do not average this away with composition/style scores.

## Gate 3 — Product provenance / fidelity route

Record whether the product is:
- `REFERENCE_RENDERED_PRODUCT`;
- `SOURCE_PRODUCT_PIXEL`;
- `VERIFIED_CAD_3D`;
- `CONCEPT_ONLY`.

For `REFERENCE_RENDERED_PRODUCT`:
- do NOT fail merely because pixels differ from the authoritative photo;
- same-SKU identity and critical geometry must pass.

For `SOURCE_PRODUCT_PIXEL`:
- source pixel provenance and mask quality must pass;
- transformations must be uniform/non-destructive as required.

For identity-critical factual detail, repeated reference-generation drift SHOULD escalate to source-pixel / verified CAD rather than being accepted as “close enough”.

## Gate 4 — Dimensions / specifications

- values match the dimension profile;
- units and axes are correct;
- product vs packaging is separated;
- unknown / estimated values are not presented as verified;
- dimension lines point to correct boundaries.

## Gate 5 — Scale / perspective

- scale calibration is referenced;
- `REAL-WORLD SCALE LOCK` is present when verified dimensions and scale-bearing context exist;
- verified dimensions remain plausible relative to selected human / scene scale references;
- contact plane and anchor are coherent;
- camera / projection assumptions are recorded;
- product is uniformly scaled;
- repeated / paired units use one consistent physical scale;
- geometry is not warped;
- product occupancy did not override verified physical scale;
- metric claims match the scale state.

If verified dimensions materially contradict apparent person / scene scale, result = `FAIL`.

## Gate 6 — Prompt traceability

For generated assets:
- prompt template version is recorded;
- required placeholders were resolved;
- missing optional values were omitted rather than guessed;
- product identity / critical geometry / scale locks are injected when required;
- unsupported facts were not introduced by prompt writing.

## Gate 7 — Person interaction

- hand / body contact is physically plausible;
- occlusion order is correct;
- person does not pass through product;
- product geometry remains unchanged;
- when verified dimensions exist, product size relative to hands/body agrees with scale lock;
- no unverified load / safety / ergonomic claim is implied.

## Gate 8 — Material / compositing

- texture / grain / color remain credible and source-aligned;
- identity-critical material proof is source-backed;
- mask preserves holes / thin structures;
- no obvious fringe;
- shadows are physically coherent;
- source-product RGB is not covered or repainted when source pixels are required.

## Gate 9 — Copy / graphics

Read the approved copy deck.

- every final text block maps to approved `copy_id`;
- Chinese copy is exact;
- numbers / units / punctuation are exact;
- source facts exist;
- user wording is not strengthened into unsupported environmental/safety/performance claims;
- typography is readable.

Model-invented final copy = `FAIL`.

## Gate 10 — Semantic master → layout provenance

For multi-panel/detail graphics:
- every cell points to an `APPROVED` semantic master;
- every copy block points to approved copy;
- layout uses contain/crop, not non-uniform warp;
- final layout did not create a new unreviewed product rendering;
- a failed cell can be replaced independently.

A one-shot AI collage that bypasses master QA = `FAIL` for factual ecommerce delivery.

## Gate 11 — Cross-image consistency

- same SKU / variant;
- same structure;
- same verified dimensions;
- same product appearance;
- critical geometry remains consistent;
- no contradictory claims;
- no variant mixing.

## Gate 12 — Delivery completeness

Read `delivery-manifest.json`.

- planned, blocked, expected, produced, QA-completed, and delivered counts reconcile;
- every final asset has a delivery reference;
- no `FAIL` asset is silently counted as approved delivery;
- the run is not called complete when only a subset of artifacts was surfaced.

## Gate 13 — Marketplace export

- marketplace / category / slot is known when platform export is requested;
- rule source is recorded;
- verification date is recorded;
- file dimensions / format / size / naming pass current checks.

## Result states

- `PASS`: evidence-backed, no blocking issue found.
- `REVIEW`: uncertainty remains.
- `FAIL`: confirmed identity / geometry / factual / scale / prompt / layout / delivery / compliance error.
- `NOT_CHECKED`: insufficient evidence or check not performed.

## Critical separation

Always report separately:
- `visual_plausibility`;
- `product_identity`;
- `critical_geometry`;
- `product_pixel_provenance`;
- `metric_grounding`;
- `copy_truth`;
- `layout_provenance`;
- `input_source_integrity`;
- `delivery_completeness`.

A beautiful generated product can pass visual plausibility and still fail product identity or critical geometry.
