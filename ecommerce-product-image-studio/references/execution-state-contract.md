# Execution State and Resume Contract

## Purpose

Make multi-step image production resumable, idempotent, and safe from duplicate expensive generation.

Long e-commerce workflows may pause because of:
- missing user input;
- tool failure;
- rate / quota limits;
- QA rejection;
- missing platform information;
- temporary interruption.

Resume from the last valid checkpoint instead of recreating the whole task.

## Stable asset identity

Every planned asset MUST have a stable \`asset_id\`.

Every stage SHOULD use:

\`\`\`text
execution_key =
project_id + asset_id + stage + input_revision
\`\`\`

Equivalent work with the same execution key SHOULD NOT be submitted twice unless an explicit retry is recorded.

## Asset states

Suggested states:

- \`PLANNED\`
- \`PREFLIGHTED\`
- \`PROMPT_RENDERED\`
- \`GENERATING_BACKGROUND\`
- \`GENERATING_PERSON\`
- \`CUTOUT_READY\`
- \`COMPOSITING\`
- \`LAYOUT_READY\`
- \`QA_PENDING\`
- \`QA_REVIEW\`
- \`QA_FAILED\`
- \`APPROVED\`
- \`DELIVERED\`
- \`BLOCKED\`
- \`FAILED\`

## Checkpoints

After a durable stage, record:
- asset_id;
- current state;
- input revision / hash if available;
- produced artifacts;
- tool / model;
- prompt version;
- retry count;
- next allowed action;
- blocker / failure reason;
- timestamps if available.

## Resume rules

On resume:

1. Read \`execution-state.json\`.
2. Reuse completed durable artifacts whose inputs have not changed.
3. Resume from the first incomplete / invalidated stage.
4. Do not create a second duplicate asset job merely because monitoring was interrupted.
5. If user input changes a dependency, invalidate only downstream stages.
6. QA rejection SHOULD return to the smallest responsible production stage.

Examples:
- copy changed → layout / QA invalidated; background need not regenerate.
- product source changed → cutout, composite, layout, QA invalidated.
- platform export profile changed → master composite may remain valid; export stage reruns.
- scene prompt changed → background and downstream composite rerun.

## Retry policy

A retry MUST record:
- previous attempt;
- reason;
- changed input / tool condition;
- whether the retry is identical or modified.

Blind repeated submission of the same expensive generation job is prohibited.

## User-input pause

When user input is required:
- preserve current outputs;
- record the exact missing decision;
- mark the asset / project \`BLOCKED\` or \`AWAITING_INPUT\`;
- resume the same project after the answer.

Do not rebuild unrelated completed assets.

## Output

Create \`execution-state.json\` at project level with per-asset state and checkpoint history.

This file is operational state, not product truth. Product facts continue to live in the evidence / identity / dimension contracts.