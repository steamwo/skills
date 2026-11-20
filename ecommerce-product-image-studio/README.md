# E-commerce Product Image Studio

The orchestrator for conversion-first, same-SKU ecommerce visual production.

## Default generation route

For most consumer products:

\`\`\`text
authoritative product photo
→ product identity lock
→ platform + campaign style locks
→ commercial scene / shot brief
→ reference-image generation or edit
→ candidate ranking
→ repair failed asset only
\`\`\`

Do not start with segmentation unless strict pixel fidelity is actually needed.

## Fidelity modes

- \`REFERENCE_GENERATE\` — default commercial photography route
- \`REFERENCE_EDIT\` — controlled edit of useful source image
- \`STRICT_PIXEL_COMPOSITE\` — exact logos / packaging / precision details
- \`VERIFIED_CAD_3D\` — verified unsupported camera view
- \`CONCEPT_ONLY\` — no authoritative visual source

## Platform style profiles

Read:
- \`references/platform-commerce-style-contract.md\`
- \`references/platform-style-profiles.json\`

Platform style is heuristic creative guidance.
Official compliance is verified separately.

## Commercial scene routing

Read \`references/commercial-scene-router.md\`.

Every scene defines:
- buyer question;
- who / where / action;
- camera;
- lighting;
- product occupancy;
- relevant props;
- scale reference when useful;
- \`REAL-WORLD SCALE LOCK\` when verified dimensions meet scale-bearing context.

Read \`references/real-world-scale-contract.md\` for the distinction between frame occupancy and physical product scale.

## Candidate / repair

Read \`references/candidate-repair-loop.md\`.

Important assets generally explore 2–3 candidates, then rank them.

QA failures become targeted repair instructions.

Only failed assets are rerun.

## Stable locks

Use:
- PRODUCT IDENTITY LOCK
- CAMPAIGN STYLE LOCK
- PLATFORM COMMERCE STYLE LOCK
- REAL-WORLD SCALE LOCK when activated

Keep them stable across the set.

Change shot-specific instructions per asset.

## Chinese ecommerce graphics

Use one-screen-one-job.

Short copy + explicit zones + thumbnail review generally work better than dense poster-style layouts.

Move exact final text to deterministic typography when the image model is unreliable.

## Machine-readable examples

- task input
- variant matrix
- buyer decision map
- asset derivation map
- output profile
- execution state
- candidate selection
- delivery manifest

## Research sources

See the repository-level \`ECOMMERCE_VISUAL_RESEARCH.md\`.