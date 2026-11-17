# Buyer Decision Framework

## Purpose

An e-commerce image set is not a fixed number of pictures. It is a sequence of visual answers to purchase questions.

The planner SHOULD optimize **decision coverage**, not image count.

## Core decision questions

Use only the stages relevant to the product:

1. **Recognition** — What is this product?
2. **Relevance** — Is it suitable for my use case?
3. **Value** — Why should I choose it?
4. **Usage** — How is it used?
5. **Fit / Scale** — Will it fit my body, space, device, or environment?
6. **Trust** — What material, structure, construction, or evidence supports the claim?
7. **Specification** — What are the verified dimensions / parameters?
8. **Variant choice** — Which size / color / bundle / model is right for me?
9. **Included items** — What exactly do I receive?
10. **Risk reduction** — What limitations, care, compatibility, or usage notes matter?

Not every SKU needs all ten.

## Decision coverage rules

Every planned semantic asset SHOULD declare:
- \`decision_stage\`
- \`buyer_question\`
- \`decision_answer\`
- \`evidence_refs\`
- \`asset_role\`

A visual asset without a decision purpose is usually decorative duplication.

## MUST

- map each asset to at least one buyer question;
- keep the answer evidence-backed;
- identify decision questions that remain uncovered;
- prioritize high-impact uncovered questions before adding decorative variants;
- reuse one semantic asset across multiple output profiles when the decision content is unchanged.

## MUST NOT

- create multiple near-identical lifestyle images that answer the same question without a clear reason;
- invent a benefit merely to create another image;
- use image count as a proxy for completeness;
- let visual style replace factual purchase information.

## Decision coverage status

Use:
- \`COVERED\`
- \`PARTIALLY_COVERED\`
- \`BLOCKED\`
- \`NOT_APPLICABLE\`

## Output

Create \`buyer-decision-map.json\` or embed equivalent fields in \`image-plan.json\`.

A complete set SHOULD report:
- covered decision stages;
- blocked decision stages;
- supporting assets;
- unresolved buyer questions.

## Example

\`\`\`text
buyer question: "Which length should I choose?"
decision stage: VARIANT_CHOICE
answer: "25 / 30 / 35 / 40 cm handle lengths are available."
evidence: user-confirmed variant dimensions
assets:
  - size-comparison-module
  - per-SKU dimension module
\`\`\`

The purpose is not to maximize content. It is to remove purchase uncertainty with the minimum truthful asset set.