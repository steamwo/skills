---
name: lifestyle-scene-composite
description: Create commercially believable lifestyle and in-use scenes from real product references using reference-image generation first, product identity locks, scene routing, platform style locks, candidate ranking, and strict-pixel compositing only when required.
---

# Lifestyle Scene Production

## Objective

Create a scene buyers can imagine themselves in while keeping the product recognisably the same SKU.

Read:
- \`ecommerce-product-image-studio/references/reference-generation-contract.md\`
- \`ecommerce-product-image-studio/references/commercial-scene-router.md\`
- \`ecommerce-product-image-studio/references/platform-commerce-style-contract.md\`
- \`ecommerce-product-image-studio/references/candidate-repair-loop.md\`

## Default route

\`\`\`text
authoritative product photo
→ PRODUCT IDENTITY LOCK
→ platform + campaign style lock
→ commercial scene brief
→ reference-image generation / edit
→ candidate QA
→ accept best
\`\`\`

Do **not** begin by cutting the product out unless strict-pixel fidelity is required.

## Scene brief

MUST define:
- buyer question;
- who / where / action;
- camera;
- lighting;
- product occupancy target;
- 2–4 relevant props maximum;
- scale reference when useful;
- platform commerce style profile.

The environment needs a story, not arbitrary decoration.

## Reference generation

Pass the authoritative product image(s) directly to the capable image-generation/edit tool.

Prompt structure:

\`\`\`text
PRODUCT IDENTITY LOCK
+ CAMPAIGN STYLE LOCK
+ PLATFORM COMMERCE STYLE LOCK
+ scene story
+ camera / lighting
+ product salience / occupancy
+ exact interaction
+ negative constraints
\`\`\`

## Candidate exploration

For an important lifestyle scene, generate 2–3 candidates when budget allows.

Vary one axis at a time:
- camera;
- environment;
- light;
- person action.

Rank by:
- identity fidelity;
- commercial composition;
- scene story;
- product salience;
- platform fit;
- lighting realism;
- physical interaction.

## Composition heuristics

Starting points:
- product roughly 25–50% of useful frame for lifestyle;
- product should be among the sharpest / highest-salience elements;
- supporting props: usually 2–4;
- shallow depth of field MAY help keep scene subordinate;
- leave usable copy space only when the planned asset needs copy.

These are heuristics, not compliance rules.

## Strict-pixel fallback

Escalate to \`product-cutout-composite\` only when:
- logo / label / packaging text must be exact;
- precision interfaces must remain pixel-identical;
- reference generation repeatedly changes identity-critical details;
- user explicitly requests source-pixel preservation.

## MUST NOT

- use a generic empty background + pasted cutout merely because it is easy;
- accept a scene that looks like a collage when a reference-generation route can integrate light and perspective naturally;
- let props become the subject;
- change product structure;
- imply unverified load / safety / performance;
- claim metric scale when scale evidence is insufficient.

## Outputs

Save:
- scene brief;
- identity lock version;
- platform / campaign style versions;
- rendered prompts;
- candidate images;
- candidate scores;
- accepted asset;
- fidelity mode;
- repair history;
- QA record.

## Gate

Commercial scene quality and product identity must both pass.

If candidate quality stays poor after bounded repair, change the scene or fidelity route instead of polishing a bad composition.