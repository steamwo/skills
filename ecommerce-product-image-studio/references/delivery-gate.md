# Delivery Gate

## Purpose

A task is complete only when every expected final derivative is QA-accounted and actually delivered.

For product families, do **not** calculate expected output as:

\`\`\`text
number_of_SKUs × fixed_image_count
\`\`\`

because some semantic assets are legitimately shared and others are variant-bound.

## Delivery unit

The final delivery unit is:

\`\`\`text
semantic_asset
× required_variant_scope
× required_output_profile
\`\`\`

Examples:

- family-shared brand module × 1 family scope × 2 profiles = 2 deliverables;
- variant-bound hero × 4 variants × 1 profile = 4 deliverables;
- family size-comparison module × 1 family scope × 2 profiles = 2 deliverables;
- 4 variant dimension modules × 4 variants × 2 profiles = 8 deliverables.

## Counters

Maintain:
- \`planned_semantic_assets_total\`
- \`blocked_semantic_assets_total\`
- \`expected_derivatives_total\`
- \`produced_derivatives_total\`
- \`qa_completed_derivatives_total\`
- \`delivered_derivatives_total\`

The expected derivative total comes from the image plan + variant matrix + output-profile requirements.

Do not derive it from a hard-coded image count.

## Completion statuses

- \`COMPLETE\`
- \`PARTIAL\`
- \`BLOCKED\`
- \`IN_PROGRESS\`

## COMPLETE requires

- every expected non-blocked derivative has a produced file;
- every final derivative has QA status;
- every final derivative has an accessible delivery reference;
- delivered derivative count equals expected derivative count;
- no \`FAIL\` asset is silently counted as approved;
- family-shared assets are not duplicated merely to inflate counts;
- variant-bound assets are not collapsed into one shared file.

## Shared asset handling

A family-shared semantic asset may satisfy multiple variants only when its scope is \`SHARED_VERIFIED\`.

The delivery manifest SHOULD record the family scope explicitly rather than copying the same file once per SKU.

## Variant-bound handling

A variant-bound asset MUST have:
- explicit \`variant_id\`;
- correct variant provenance / dimensions / copy;
- its own final derivative where required.

## Output-profile handling

The same semantic asset rendered for web and mobile counts as separate final derivatives when both are requested.

A single mechanically resized file MUST NOT be counted as two valid derivatives if the second profile requires a redesigned layout.

## Delivery manifest

Create \`delivery-manifest.json\`.

Each final entry SHOULD include:
- \`delivery_id\`
- \`semantic_asset_id\`
- \`role\`
- \`decision_stage\`
- \`variant_scope\`
- \`reuse_class\`
- \`output_profile\`
- \`parent_asset_ids\`
- \`production_status\`
- \`qa_status\`
- \`delivery_status\`
- \`delivery_reference\`
- \`product_provenance\`
- \`copy_version\`
- \`notes\`

## PARTIAL

Use when useful derivatives were delivered but some expected outputs are missing, blocked, or still in review.

State exactly which semantic asset / variant / profile combinations are missing.

## BLOCKED

Use when requested outputs cannot be truthfully produced, for example:
- missing authoritative variant source;
- missing dimensions;
- unknown cross-variant sharedness;
- missing packaging evidence;
- unsupported product view;
- interaction requires product deformation.

Never claim “all images complete” unless the manifest supports it.