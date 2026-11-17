# E-commerce Product Image Studio

The orchestrator for fidelity-first e-commerce product visual production.

## Architecture

The project now uses explicit contracts for:

- task intake;
- execution preflight;
- product evidence;
- product identity / dimensions;
- scale / perspective;
- semantic asset planning;
- output profiles;
- detail-page modules;
- deterministic prompt rendering;
- source-pixel production;
- execution state / resume;
- QA;
- delivery;
- marketplace export.

## Important distinction

### User intent

Platform, surface/profile, ratio, language, market, style, requested deliverables, and extra requirements come from explicit user input.

### Product evidence

Authoritative product images MUST be inspected for:
- visible geometry;
- component count;
- hardware;
- texture/color;
- supported camera view;
- visible markings.

Do not infer user intent from product appearance.

## Execution preflight

Before expensive generation:

- verify source files;
- verify required tools;
- preserve originals;
- verify output destinations;
- identify required surface profiles;
- record blockers.

See \`references/execution-preflight.md\`.

## Output profiles

Do not model output as “ratio only”.

Use:
- marketplace;
- surface;
- slot;
- device;
- design preset;
- verified rule source.

Named presets such as Amazon A+ standard / premium web / premium mobile are useful planning labels, but must be re-verified before compliance export.

See \`references/output-profile-contract.md\`.

## Detail modules

Build semantic modules first, then render them into one or more profiles.

Independent modules are the preferred editable masters.

A stitched long image is normally a derivative.

See \`references/detail-module-contract.md\`.

## Resumable execution

Create \`execution-state.json\`.

Use stable asset IDs and durable checkpoints.

If execution is interrupted:
- reuse valid outputs;
- resume from the first invalid/incomplete stage;
- do not resubmit the same expensive job blindly.

See \`references/execution-state-contract.md\`.

## Product fidelity

\`\`\`text
real SKU photo
→ reviewed alpha mask
→ ORIGINAL PRODUCT RGB
→ generated empty background / independent person
→ scale-aware compositing
→ typography / detail modules
→ QA
\`\`\`

A generated lookalike is not the same SKU.

## Machine-readable examples

- \`references/task-input-schema.json\`
- \`templates/task-input.example.json\`
- \`templates/output-profile.example.json\`
- \`templates/execution-state.example.json\`
- \`templates/delivery-manifest.example.json\`

## Validation

Validate task intake:

\`\`\`bash
python ecommerce-product-image-studio/scripts/validate_task_input.py \
  --input sku-001/task-input.json
\`\`\`

## China marketplace notes / 中国电商说明

平台详情页应优先保留独立分屏 / 模块源文件，再根据平台输出长图、移动端版、Web 版等派生版本。

历史尺寸、示例档位和经验比例不能当成永久平台规则。