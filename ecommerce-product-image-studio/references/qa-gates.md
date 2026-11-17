# E-commerce Product Visual QA Gates

Evaluate every image independently and then evaluate the complete set.

Do not use one image passing QA to imply the whole set passes.

## Gate 0 — Task input integrity

- \`task-input.json\` exists when the orchestrator workflow is used;
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
- no unsupported view or hidden structure was invented.

Identity drift = \`FAIL\`.

## Gate 3 — Product pixel provenance

- product body source is recorded;
- alpha / mask source is recorded;
- transformations are recorded;
- source product RGB is preserved when required;
- no lookalike generated product silently replaces the SKU.

If an authoritative photo existed and the production asset is a generated redraw, default to \`FAIL\`.

## Gate 4 — Dimensions / specifications

- values match the dimension profile;
- units and axes are correct;
- product vs packaging is separated;
- unknown / estimated values are not presented as verified;
- dimension lines point to correct boundaries.

## Gate 5 — Scale / perspective

- scale calibration is referenced;
- contact plane and anchor are coherent;
- camera / projection assumptions are recorded;
- product is uniformly scaled;
- geometry is not warped;
- metric claims match the scale state.

## Gate 6 — Prompt traceability

For generated background / person assets:
- prompt template version is recorded;
- required placeholders were resolved;
- missing optional values were omitted rather than guessed;
- fixed “do not generate target product” constraints remain present;
- unsupported facts were not introduced by prompt writing.

## Gate 7 — Person interaction

- hand / body contact is physically plausible;
- occlusion order is correct;
- person does not pass through product;
- product geometry remains unchanged;
- no unverified load / safety / ergonomic claim is implied.

## Gate 8 — Material / compositing

- texture / grain / color remain credible and source-aligned;
- mask preserves holes / thin structures;
- no obvious fringe;
- shadows are independent and physically coherent;
- product RGB is not covered by generated shadow paint.

## Gate 9 — Copy / graphics

- Chinese copy is correct;
- numbers / units / punctuation are correct;
- claims have evidence;
- packaging / certification / compatibility claims are verified;
- typography is readable.

## Gate 10 — Cross-image consistency

- same SKU / variant;
- same structure;
- same verified dimensions;
- same product appearance;
- no contradictory claims;
- no variant mixing.

## Gate 11 — Delivery completeness

Read \`delivery-manifest.json\`.

- planned, blocked, expected, produced, QA-completed, and delivered counts reconcile;
- every final asset has a delivery reference;
- no \`FAIL\` asset is silently counted as approved delivery;
- the run is not called complete when only a subset of artifacts was surfaced.

## Gate 12 — Marketplace export

- marketplace / category / slot is known when platform export is requested;
- rule source is recorded;
- verification date is recorded;
- file dimensions / format / size / naming pass current checks.

## Result states

- \`PASS\`: evidence-backed, no blocking issue found.
- \`REVIEW\`: uncertainty remains.
- \`FAIL\`: confirmed identity / factual / scale / prompt / delivery / compliance error.
- \`NOT_CHECKED\`: insufficient evidence or check not performed.

## Critical separation

Always report separately:
- \`visual_plausibility\`
- \`product_pixel_provenance\`
- \`metric_grounding\`
- \`input_source_integrity\`
- \`delivery_completeness\`

A beautiful generated product can pass visual plausibility and still fail product identity.