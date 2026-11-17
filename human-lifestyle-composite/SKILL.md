---
name: human-lifestyle-composite
description: Plan and create independent person assets for e-commerce scenes, including pose, action, wardrobe, body scale assumptions, contact points, occlusion plan, and cross-image person consistency.
---

# Human Lifestyle Composite

## Objective

Create the person layer independently from the product so product identity can remain locked.

This skill produces people / pose assets. Final product interaction is handled by \`product-human-scene-integration\`.

## Inputs

- image plan;
- product dimensions / scale state;
- product use logic;
- brand direction;
- optional person reference;
- scene camera / contact plane.

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
- \`pose-plan.json\`
- person reference assets
- person layers / masks
- \`person-qa.md\`

## Gate

If the intended interaction cannot be made physically plausible without modifying product geometry, change the pose or mark the scene \`BLOCKED\`.