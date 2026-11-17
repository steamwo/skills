---
name: product-reference-audit
description: Audit real product photos, videos, dimension drawings, CAD, packaging references, and SKU documents to establish view coverage, evidence quality, provenance, and missing inputs before any e-commerce image production.
---

# Product Reference Audit

## Objective

Determine what the supplied assets actually prove before any product image generation or compositing begins.

## Inputs

MAY include:
- real SKU photos;
- video frames;
- dimension drawings;
- CAD / 3D files;
- BOM / engineering documents;
- packaging photos;
- spec sheets;
- user-confirmed product facts.

## MUST

- inventory every relevant source file;
- record SKU / variant identity;
- classify image view: front, rear, left, right, top, bottom, three-quarter, detail, dimension reference, scene;
- record resolution, occlusion, glare, blur, crop, and background complexity;
- list directly visible geometry, hardware, texture, labels, logos, seams, holes, joints, and edges;
- record dimension evidence with axis, unit, measurement basis, and source location;
- map each planned claim or specification to evidence;
- identify unsupported views and facts;
- preserve source provenance.

## MUST NOT

- infer unseen rear / bottom / internal construction from one view;
- infer sale quantity from the number of objects visible in a photo;
- infer exact dimensions from pixels without a valid scale basis;
- use competitor images as current-SKU evidence;
- guess wood species, certification, load capacity, food-contact status, safety rating, or material grade;
- “complete” missing product views with generative imagery and then mark them as factual.

## Evidence states

Use:
- \`visible_in_reference\`
- \`user_confirmed\`
- \`document_verified\`
- \`estimated\`
- \`unknown\`
- \`conflicting\`

## Dimension evidence

A measurement photo MUST be treated as verified only when:
- scale markings are readable;
- the measurement axis is clear;
- the reference and product geometry are sufficiently aligned;
- perspective does not invalidate the reading.

Otherwise use \`estimated\` or \`unknown\`.

## Outputs

Create:
- \`asset-audit.md\`
- \`evidence-matrix.json\` or CSV
- \`dimension-evidence.md\`
- \`missing-assets.md\`
- \`usage-map.md\`

Each source entry SHOULD include:
- file path;
- source type;
- SKU / variant;
- view;
- supports;
- limitations;
- evidence state;
- provenance notes.

## Gate

Do not pass unsupported product facts downstream as verified. Hand the audit to \`product-identity-lock\`, \`product-dimension-lock\`, and \`ecommerce-gallery-planner\`.