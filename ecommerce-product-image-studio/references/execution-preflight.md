# Execution Preflight Contract

## Purpose

Validate the production environment and source assets **before** expensive generation or compositing begins.

A task can have valid business intent and still be operationally unready.

## Preflight principles

- Run preflight before creating costly generation jobs.
- Preserve original user assets; preprocessing creates derived copies.
- Preprocessing may make a file usable, but MUST NOT change user intent or product facts.
- Do not discover obvious input/tool/output failures only after multiple images have been generated.

## Preflight checks

### Source assets

Check as applicable:
- file exists and is readable;
- file type is supported by the intended tool;
- image dimensions are sufficient for the requested output/crop;
- alpha/transparency behavior is understood;
- source view supports the requested composition;
- asset count stays within tool / workflow limits;
- authoritative product references are identifiable.

Low resolution does not authorize AI invention of missing product detail.

### Production tools

Check only tools required for the requested plan:
- segmentation / mask capability;
- image generation capability;
- compositing / layout capability;
- typography capability;
- CAD / 3D capability when required;
- export capability.

If a capability is absent:
- downgrade the plan;
- mark affected assets \`BLOCKED\`; or
- choose an already-approved fallback.

Do not silently switch to a lower-fidelity product-generation route.

### Output destination

Check:
- output directory / artifact destination exists or can be created;
- naming does not collide with an approved final asset;
- master vs platform exports are separated;
- originals are never overwritten.

### Marketplace / surface profile

If platform-specific output is requested:
- identify marketplace;
- identify surface / slot / device;
- verify current rule source;
- record verification date;
- distinguish a **design preset** from a **verified compliance profile**.

A remembered or example size is not automatically a verified marketplace rule.

## Controlled preprocessing

Allowed preprocessing MAY include:
- non-destructive format conversion;
- lossless / quality-controlled image conversion;
- orientation normalization;
- metadata inspection;
- creating previews / proxies;
- creating derived copies for tools with input limits.

MUST:
- preserve the original;
- record source → derived mapping;
- record transformation;
- re-check derived output.

MUST NOT:
- use preprocessing results to infer user intent;
- destructively overwrite source assets;
- drop source pages/images silently;
- change product geometry;
- generate missing product details.

## Result

Create \`execution-preflight.json\` with:
- project / SKU;
- requested stages;
- source checks;
- tool checks;
- output checks;
- platform / surface profile status;
- preprocessing actions;
- blockers;
- warnings;
- overall status.

Statuses:
- \`READY\`
- \`READY_WITH_REVIEW\`
- \`BLOCKED\`

Production SHOULD NOT start for an asset whose required preflight status is \`BLOCKED\`.