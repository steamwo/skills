# Wood Fidelity Rules

## Visible wood identity

Treat the following as identity-relevant when visible:
- grain direction;
- grain density / pattern;
- knots;
- natural color variation;
- end grain;
- joints;
- seams;
- fasteners;
- holes;
- edge profiles;
- chamfers / radii;
- component thickness / visible proportions.

## MUST NOT

- replace real grain with generated grain;
- remove knots by default;
- clone grain across components;
- invent end grain;
- move screws or joints;
- make raw / matte wood glossy without evidence;
- infer species from appearance alone;
- infer oil / wax / lacquer / paint treatment without confirmation;
- infer “eco-friendly”, “zero formaldehyde”, “food safe”, or certification claims from appearance.

## Detail image rule

Preferred source:
1. real high-resolution detail photo;
2. real crop from the authoritative photo;
3. verified macro reference for the same SKU.

Do not synthesize missing product detail and present it as factual.

## Color rule

Background and brand graphics may be color-graded.

Product color SHOULD remain source-based unless:
- color calibration data exists; or
- the user explicitly authorizes a correction.

## Scene rule

Generate the scene without the target product.

Then composite the real product RGB into the scene. Match atmosphere through background, shadow, and independent lighting layers instead of repainting the wood.

## QA

Set \`FAIL\` if:
- visible wood identity materially changes;
- generated lookalike replaces the real SKU;
- hardware / joints / structure drift;
- unverified material claims appear in customer-facing copy.