# Intake Contract

## Purpose

Separate **user intent** from **product evidence** before production.

This contract adapts a useful pattern from form-driven expert skills: explicit fields, legal options, deterministic omission rules, and source tracking. It intentionally differs on one point: this e-commerce workflow MUST inspect authoritative product images because product identity and visual evidence depend on them.

## Two information planes

### A. Intent plane — user decision

These fields MUST come from explicit user text or an explicitly provided structured value:

- target marketplace;
- target market;
- image ratio;
- in-image language;
- requested deliverables;
- requested style / art direction;
- extra requirements;
- whether a person scene is requested;
- whether a stitched long image is requested.

**MUST NOT infer intent from:**
- product image appearance;
- filename;
- attachment title;
- inferred product category;
- previous marketplace defaults;
- “what usually works”.

Example: a Chinese-looking product image does not mean the user requested Chinese text.

### B. Evidence plane — product facts

These facts MAY be extracted from authoritative product assets when the evidence supports them:

- visible silhouette;
- component count;
- hardware position;
- visible material appearance;
- visible logos / markings;
- supported camera view;
- dimension values shown in verified drawings / measurement photos.

Product images MUST be inspected for identity lock.

However, visual evidence MUST NOT be promoted into unsupported business facts. Examples:
- visible quantity does not prove sale quantity;
- wood appearance does not prove species;
- a person holding the product does not prove load capacity;
- image pixels do not prove 3D dimensions without scale evidence.

## Machine-readable source

Read \`task-input-schema.json\` before intake.

Rules:
1. Required fields must be satisfied before the dependent stage runs.
2. Optional fields that are not specified remain absent; do not invent defaults unless an explicit \`auto\` option is selected by policy.
3. Select / radio / checkbox values must come from the declared option set.
4. \`extra_requirements\` must map to actual user wording.
5. Product evidence derived from attachments belongs in the reference audit / evidence matrix, not in user-intent fields.

## Missing information policy

Do not ask for every unknown field upfront.

Ask only when the missing item blocks the next requested deliverable.

Examples:
- missing marketplace does not block a generic master;
- missing full dimensions blocks metric dimension graphics and metric scene claims;
- missing sale quantity blocks package / included-item claims;
- missing rear-view photo blocks factual rear-view imagery.

## Intake output

Create \`task-input.json\` containing:
- values explicitly supplied by the user;
- source for each value;
- unresolved fields;
- fields intentionally omitted;
- downstream blockers.

Never store inferred user intent as if the user selected it.