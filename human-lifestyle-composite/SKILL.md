---
name: human-lifestyle-composite
description: Plan and create independent person assets for e-commerce scenes using explicit user intent, deterministic prompt rendering, pose/contact plans, body-scale assumptions, occlusion plans, and cross-image consistency.
---

# Human Lifestyle Composite

## Objective

Create the person layer independently from the product so product identity can remain locked.

## Inputs

- \`task-input.json\`
- image plan
- product dimensions / scale state
- verified product use logic
- explicit brand / style direction
- optional person reference
- scene camera / contact plane
- \`ecommerce-product-image-studio/templates/person-layer-prompt.md\`

## Intent rule

Do not invent person attributes the user did not request when they materially affect the brief.

The product image MUST NOT be used to infer:
- target person gender;
- age;
- ethnicity;
- wardrobe style;
- market;
- desired lifestyle tone.

If the user only requests “a person using the product”, choose a neutral adult-use concept that does not add unsupported product claims and record it as a planning assumption.

## Person brief

Define:
- \`person_id\`
- role;
- age range;
- visible appearance;
- wardrobe;
- pose / action;
- gaze / expression;
- scale basis;
- product contact points;
- occlusion plan;
- consistency reference.

## Prompt rendering

Use the person-layer template.

Fixed product-fidelity clauses MUST remain intact:
- do not generate target product;
- do not redraw product;
- do not invent product capability.

## MUST

- describe concrete body orientation and action;
- identify hand, foot, body, or support contact points;
- record whether person height is known or estimated;
- preserve the person as an independent layer where possible;
- plan front / rear occlusion relative to the product;
- check hands, fingers, joints, feet, and weight-bearing logic.

## MUST NOT

- use the person as a metric ruler without known dimensions;
- force the product to deform to fit the person;
- imply unverified load capacity, safety, medical, or ergonomic performance;
- cover identity-critical product regions unless the image role requires it and QA can still verify identity;
- promise same-person consistency across images without a stable reference workflow.

## Output

Create:
- \`person-brief.md\`
- rendered person prompt
- \`pose-plan.json\`
- person reference assets
- person layers / masks
- \`person-qa.md\`

## Gate

If the intended interaction cannot be made physically plausible without modifying product geometry, change the pose or mark the scene \`BLOCKED\`.