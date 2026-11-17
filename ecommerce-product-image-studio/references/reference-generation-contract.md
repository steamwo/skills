# Reference-First Image Generation Contract

## Purpose

Use a capable reference-image generation/edit model as the default route for natural e-commerce photography.

Do **not** force segmentation + cutout compositing as the first step for every product.

The primary goal is **same-product identity with commercially believable photography**.

## Fidelity modes

### \`REFERENCE_GENERATE\` — default for most consumer products

Input:
- one or more authoritative product photos;
- product identity lock;
- scene / shot brief;
- platform commerce style profile.

The image model receives the real product photo directly as a visual reference and creates the scene while keeping the product recognisably identical.

Best for:
- furniture;
- fitness equipment;
- home goods;
- tools;
- kitchenware;
- ordinary consumer products;
- lifestyle / in-use photography.

### \`REFERENCE_EDIT\`

Use when the source composition is already useful and only a controlled edit is needed:
- background replacement;
- removing unrelated clutter;
- lighting / scene extension;
- adding a person or prop while keeping product identity.

### \`STRICT_PIXEL_COMPOSITE\`

Escalate when exact source pixels matter more than natural generative integration.

Typical triggers:
- packaging text;
- logos / labels that must be exact;
- serial / model plates;
- precision ports / interfaces;
- regulated labels;
- dense printed graphics;
- repeated reference generation still changes identity-critical structure.

This is a fallback / strict-fidelity route, not the universal default.

### \`VERIFIED_CAD_3D\`

Use verified current-SKU CAD / 3D when a new camera angle is required and the real photographs do not cover it.

### \`CONCEPT_ONLY\`

Allowed only when no authoritative visual reference exists. Must not be presented as the actual SKU.

## Identity fidelity vs pixel identity

Default priority:

\`\`\`text
same SKU identity
+ believable commercial photography
+ natural light / contact / perspective
> exact source pixel preservation
\`\`\`

unless the asset has a strict-pixel trigger.

A product may be re-rendered by a reference-image model only if identity-critical geometry and visible details remain correct.

## Product Identity Lock

Before generation, create a short lock from authoritative evidence:

\`\`\`text
PRODUCT IDENTITY LOCK
- shape / proportions
- colour / finish
- visible material / texture
- hardware / seams / holes / supports
- logo / printed text where relevant
- component count
- must-not-change details
- must-not-appear items
\`\`\`

Paste the same lock verbatim into every candidate prompt for the asset family.

Unknown facts stay out.

## Escalation ladder

\`\`\`text
REFERENCE_GENERATE
    ↓ identity fails
REFERENCE_EDIT / stronger identity lock
    ↓ identity still fails
STRICT_PIXEL_COMPOSITE
    ↓ unsupported view
VERIFIED_CAD_3D or BLOCKED
\`\`\`

Do not jump directly to cutout compositing merely because it is deterministic.

## Provenance

Record:
- reference product asset IDs;
- fidelity mode;
- identity lock version;
- model/tool;
- prompt version;
- whether product pixels are original or model-rendered;
- strict-pixel trigger, if any.

Recommended provenance values:
- \`REFERENCE_RENDERED_PRODUCT\`
- \`SOURCE_PRODUCT_PIXEL\`
- \`VERIFIED_CAD_3D\`
- \`CONCEPT_ONLY\`

## Gate

Reference generation passes only when the resulting product remains recognisably the same SKU.

A beautiful scene with changed structure is \`FAIL\`.