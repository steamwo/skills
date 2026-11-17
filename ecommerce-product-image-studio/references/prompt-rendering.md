# E-commerce Prompt Rendering

## Purpose

Use stable locks for identity and campaign consistency while allowing each asset to have its own commercial shot logic.

A good prompt is not the longest prompt.

## Prompt architecture

For generative e-commerce assets:

\`\`\`text
1. PRODUCT IDENTITY LOCK          ← stable across SKU asset family
2. CAMPAIGN STYLE LOCK            ← stable across campaign / set
3. PLATFORM COMMERCE STYLE LOCK   ← stable per target platform
4. ASSET JOB / BUYER QUESTION     ← specific to this image
5. SHOT / SCENE GRAMMAR           ← specific to this image
6. COPY / LAYOUT                  ← only when needed
7. HARD NEGATIVES                 ← specific, evidence-aware
\`\`\`

Do not repeat irrelevant context.

## Identity lock

Derived from authoritative references.

MUST remain verbatim across candidates unless source evidence changes.

## Campaign style lock

May include:
- palette;
- lighting;
- background family;
- camera family;
- grade;
- typography mood;
- prop density.

Do not freeze shot composition across every image.

## Platform style lock

Use \`platform-style-profiles.json\` as heuristic creative guidance.

Do not represent heuristic style as official platform rules.

## Reference-image prompt

When using \`REFERENCE_GENERATE\` / \`REFERENCE_EDIT\`:

\`\`\`text
Use the exact product from the supplied reference image(s).
{IDENTITY_LOCK}
{CAMPAIGN_STYLE_LOCK}
{PLATFORM_STYLE_LOCK}

Asset job: {buyer_question / role}.
Scene / composition: {shot brief}.
The product is the clear commercial hero, {occupancy / placement}.
Lighting: {lighting}.
Supporting props: {2–4 relevant props}.
{person interaction if required}.
No invented product features, no alternate product design, no extra accessories.
\`\`\`

## Suite consistency pattern

For a multi-image set, use three conceptual blocks:

\`\`\`text
[product identity — same]
+ [campaign/platform style — same]
+ [shot / buyer-decision role — changes]
\`\`\`

This preserves set consistency without making every image repetitive.

## Copy

When image-model text is appropriate:
- keep copy short;
- quote exact text;
- define title / subtitle / badge zones;
- require correct language characters.

When exact text reliability is critical, render text programmatically / in a design tool.

## Deterministic omission

- unresolved required factual field → \`BLOCKED\`;
- missing optional field → omit;
- unknown fact → never fill;
- irrelevant brand section → do not inject.

## Prompt repair

QA may produce 1–3 targeted repair sentences.

Append only repair instructions relevant to the failed asset.

Do not rewrite the entire prompt after every failure.

## Output

Record:
- locks and versions;
- final prompt;
- reference assets;
- fidelity mode;
- platform profile;
- candidate ID / round;
- repair sentences;
- accepted result.