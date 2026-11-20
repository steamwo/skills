# Reference-First Image Generation Contract

## Purpose

Use a capable reference-image generation/edit model as the default route for natural ecommerce photography **when the asset role supports it**.

Do not force segmentation/cutout compositing as the first step for every product.

The primary goal is:
- same-product identity;
- correct critical geometry;
- commercially believable photography.

## Fidelity modes

### `REFERENCE_GENERATE`

Input:
- authoritative current-SKU product photo(s);
- PRODUCT IDENTITY LOCK;
- CRITICAL GEOMETRY LOCK when activated;
- REAL-WORLD SCALE LOCK when activated;
- one semantic asset job;
- scene/shot brief;
- platform/campaign style locks.

Best for many:
- hero images;
- lifestyle scenes;
- person-use scenes;
- commercial product photography.

The image model may re-render the product, but the result must remain recognisably the same SKU and preserve all locked relations.

### `REFERENCE_EDIT`

Use when source composition is useful and a controlled edit is needed:
- background replacement;
- clutter removal;
- lighting / scene extension;
- adding a person/prop while preserving product;
- repairing a bounded non-identity region.

### `SOURCE_PRODUCT_PIXEL / STRICT_PIXEL_COMPOSITE`

Escalate when exact source detail matters more than generative integration.

Typical triggers:
- packaging text;
- logos / labels;
- serial/model plates;
- precision ports/interfaces;
- regulated labels;
- factual material/joint/hardware detail;
- repeated critical-geometry drift.

This is a targeted fidelity route, not the universal default.

### `VERIFIED_CAD_3D`

Use verified current-SKU CAD/3D when a new supported camera view is required and real photographs do not cover it.

### `CONCEPT_ONLY`

Allowed only when no authoritative visual reference exists. Must not be presented as the actual verified SKU.

## Identity fidelity vs pixel identity

Default priority for suitable commercial photography:

```text
same SKU identity
+ correct critical geometry
+ believable commercial photography
+ natural light/contact/perspective
> exact source pixel preservation
```

For factual detail proof, source-pixel/CAD fidelity may outrank photorealistic generative integration.

## Stable locks

Before generation, create:

```text
PRODUCT IDENTITY LOCK
- components / shape / proportions
- colour / finish
- visible material / texture
- hardware / seams / holes / supports
- component count
- must-not-change details

CRITICAL GEOMETRY LOCK (when activated)
- explicit component-to-component relations
- hardware location/orientation
- forbidden placements/merges
```

Paste stable locks verbatim into every candidate prompt for the asset family.

Unknown facts stay out.

## Semantic-master rule

Generate one commercial job at a time.

Do not default to asking the image model to create a final six-grid/poster with:
- multiple product redraws;
- Chinese copy;
- dimensions;
- icons;
- lifestyle scenes;
- material details.

Instead approve semantic masters first, then use deterministic layout.

Read `semantic-master-contract.md`.

## Escalation ladder

```text
REFERENCE_GENERATE
    ↓ identity/geometry fails
targeted repair with same locks
    ↓ same critical relation fails again
REFERENCE_EDIT or SOURCE_PRODUCT_PIXEL / STRICT_PIXEL_COMPOSITE
    ↓ unsupported view
VERIFIED_CAD_3D or BLOCKED
```

For the same critical relation, do not spend repeated stochastic redraws after two failures.

## Provenance

Record:
- reference product asset IDs;
- fidelity mode;
- identity lock version;
- critical geometry lock version;
- scale lock version when applicable;
- model/tool;
- prompt version;
- whether product pixels are source or model-rendered;
- strict-pixel trigger, if any.

Recommended provenance values:
- `REFERENCE_RENDERED_PRODUCT`
- `SOURCE_PRODUCT_PIXEL`
- `VERIFIED_CAD_3D`
- `CONCEPT_ONLY`

## Gate

Reference generation passes only when:
- same-SKU identity passes;
- every visible critical geometry relation passes;
- no unsupported fact/claim is introduced;
- any person/product contact is plausible;
- verified scale passes when activated.

A beautiful scene with changed construction is `FAIL`.
