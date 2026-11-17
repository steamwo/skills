# Deterministic Prompt Rendering

## Purpose

Generation prompts should be rendered from verified task data and fixed templates, not improvised from scratch for every asset.

This does not mean prompts must be short or rigid. It means:
- fixed safety / fidelity clauses remain stable;
- field order is predictable;
- missing optional fields are omitted;
- unsupported facts never enter the prompt.

## Rendering rules

1. Read the relevant template.
2. Replace placeholders only from approved fields in \`task-input.json\`, \`product-identity.json\`, \`product-dimensions.json\`, \`scale-calibration.json\`, and \`image-plan.json\`.
3. If a required placeholder is unresolved, set the asset to \`BLOCKED\`; do not leave \`{placeholder}\` text.
4. If an optional field is absent, delete the entire optional line or block.
5. Select / radio / checkbox fields must use a legal human-readable label from the task schema.
6. User free text must stay semantically faithful; do not expand it into generic marketing goals.
7. Generated prompts MUST NOT introduce product claims, dimensions, materials, package contents, or functions that are not evidence-backed.
8. Product fidelity clauses are fixed and MUST NOT be weakened by style instructions.

## Prompt layers

Render prompts from these layers:

\`\`\`text
FIXED SYSTEM CONSTRAINTS
+ asset role
+ camera / composition
+ scene or person description
+ verified scale assumptions
+ user-requested style
+ negative constraints
\`\`\`

## Product-body rule

For empty-scene and person generation:

\`\`\`text
DO NOT GENERATE THE TARGET PRODUCT.
DO NOT GENERATE A LOOKALIKE OR DUPLICATE PRODUCT.
THE REAL PRODUCT WILL BE COMPOSITED LATER FROM AUTHORITATIVE SOURCE PIXELS.
\`\`\`

This clause is mandatory when source-pixel compositing is required.

## Output

For each generated asset, save:
- rendered prompt;
- template version;
- input field sources;
- generation tool / model;
- parameters;
- resulting asset path / ID.

Prompt traceability is part of provenance.