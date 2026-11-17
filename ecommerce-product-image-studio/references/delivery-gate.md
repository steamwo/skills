# Delivery Gate

## Purpose

A task is not complete merely because files were generated. Final assets must be QA-accounted and actually delivered to the user.

## Counters

Maintain:
- \`planned_assets_total\`
- \`blocked_assets_total\`
- \`expected_deliverables_total\`
- \`produced_assets_total\`
- \`qa_completed_assets_total\`
- \`delivered_assets_total\`

Where:

\`\`\`text
expected_deliverables_total =
planned_assets_total - blocked_assets_total
\`\`\`

## Completion statuses

- \`COMPLETE\`
- \`PARTIAL\`
- \`BLOCKED\`
- \`IN_PROGRESS\`

## COMPLETE requires

- every non-blocked planned asset has a produced file;
- every produced final asset has QA status;
- every final asset has an accessible delivery reference (attachment, file path made available to the user, or supported URL);
- the delivered count matches the expected deliverable count;
- no asset marked \`FAIL\` is silently delivered as approved.

## PARTIAL

Use when useful assets were delivered but:
- some planned assets are missing;
- some assets remain \`REVIEW\`;
- a tool limitation prevented a subset of deliverables.

The response MUST state what is missing.

## BLOCKED

Use when the requested deliverable cannot be truthfully produced, for example:
- missing authoritative view;
- missing required dimensions;
- missing sale-quantity evidence;
- interaction requires product deformation.

## Delivery manifest

Create \`delivery-manifest.json\` containing, for each asset:
- \`id\`
- \`role\`
- \`planned_status\`
- \`production_status\`
- \`qa_status\`
- \`delivery_status\`
- \`delivery_reference\`
- \`product_provenance\`
- \`notes\`

Never claim “all images completed” when the delivery manifest does not support it.