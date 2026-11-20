# E-commerce Product Image Studio

The orchestrator for conversion-first, same-SKU ecommerce visual production.

The workflow is designed to remain predictable even when the executing model is weaker: product truth is represented as stable structured locks, visual jobs are generated independently, and final information graphics are assembled deterministically.

## Default production route

```text
authoritative product photos
→ PRODUCT IDENTITY LOCK
→ CRITICAL GEOMETRY LOCK (when needed)
→ variant / scale records
→ platform + campaign style locks
→ buyer-decision asset plan
→ single-job semantic masters
→ candidate QA / targeted repair
→ approved copy deck
→ deterministic infographic / grid layout
→ derivatives / export / delivery
```

Do not ask one image-model call to simultaneously reconstruct the product, create six panels, write Chinese copy, draw dimensions and invent marketing hierarchy.

## Stable locks

Use:
- PRODUCT IDENTITY LOCK
- CRITICAL GEOMETRY LOCK when construction relationships matter
- REAL-WORLD SCALE LOCK when activated
- CAMPAIGN STYLE LOCK
- PLATFORM COMMERCE STYLE LOCK

Keep stable locks verbatim across candidates.

## Fidelity modes

- `REFERENCE_GENERATE` — commercial photography route
- `REFERENCE_EDIT` — controlled edit of useful source image
- `SOURCE_PRODUCT_PIXEL / STRICT_PIXEL_COMPOSITE` — exact identity-critical detail / text / interface route
- `VERIFIED_CAD_3D` — verified unsupported camera view
- `CONCEPT_ONLY` — no authoritative visual source

Choose fidelity per semantic asset, not once for the entire project.

## Critical geometry

Read:
- `references/critical-geometry-lock.md`

Use it for:
- joints;
- screws / bolts;
- holes / ports;
- cradles / supports;
- component orientation;
- must-not-change spatial relationships.

A beautiful image with a wrong locked relation fails.

## Semantic masters

Read:
- `references/semantic-master-contract.md`

Generate and approve clean independent visual masters before making a six-grid/detail board.

Typical masters:
- hero;
- variants/sizes;
- material;
- joint/hardware detail;
- contact/anti-slip detail;
- lifestyle.

## Copy guard

Read:
- `references/copy-guard-contract.md`

Final ecommerce copy comes from approved facts.

Do not expand “unpainted” into “0 VOC”, or visible structural features into unsupported safety/performance claims.

## Deterministic prompt compiler

For weaker controller models, do not let the controller write the final image prompt.

The controller fills a bounded job record:

```bash
python ecommerce-product-image-studio/scripts/prompt_compiler.py \
  --job ecommerce-product-image-studio/templates/prompt-job.example.json \
  --locks ecommerce-product-image-studio/templates/prompt-locks.example.json \
  --output output/joint-detail.prompt.txt \
  --json-output output/joint-detail.request.json
```

The compiler:
- validates the fidelity route and required reference IDs;
- keeps stable locks outside the controller's dynamic output;
- injects locks in a fixed order;
- automatically adds standard preserve / must-not rules;
- appends only bounded targeted repairs;
- produces an API-agnostic compiled prompt that can be sent to GPT Image or another reference-image model.

The weak controller chooses structured parameters. The compiler writes the prompt.

## Deterministic layout

Read:
- `references/deterministic-grid-layout-contract.md`

Use approved masters + approved copy for final multi-panel graphics.

Baseline renderer:
```bash
python ecommerce-product-image-studio/scripts/render_infographic_grid.py \
  --manifest ecommerce-product-image-studio/templates/six-grid-layout.example.json \
  --font /path/to/cjk-font.ttf \
  --output output/six-grid.png
```

The renderer crops/contains images without warping product geometry and renders exact text with an explicitly supplied font.

## Guard validation

Examples:

```bash
python ecommerce-product-image-studio/scripts/validate_content_guards.py \
  --geometry-lock ecommerce-product-image-studio/templates/critical-geometry-lock.example.json \
  --copy-deck ecommerce-product-image-studio/templates/copy-deck.example.json
```

## Candidate / repair

Important generative masters generally explore 2–3 candidates.

Hard identity/critical-geometry/fact failures are rejected before commercial scoring.

QA failures become targeted repair instructions.

Only failed masters are rerun; deterministic layout is rerendered afterward.

## Platform style profiles

Read:
- `references/platform-commerce-style-contract.md`
- `references/platform-style-profiles.json`

Platform style is heuristic creative guidance.
Official compliance is verified separately.

## Machine-readable examples

- task input
- variant matrix
- buyer decision map
- critical geometry lock
- semantic master manifest
- copy deck
- six-grid layout manifest
- asset derivation map
- output profile
- execution state
- candidate selection
- delivery manifest
- prompt job
- prompt locks

## Research sources

See repository-level `ECOMMERCE_VISUAL_RESEARCH.md`.
