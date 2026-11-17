# steamwo / Skills

Reusable Agent Skills for **e-commerce visual production**.

This repository is not a generic AI image prompt pack. It is designed to turn real SKU references into commercially useful, platform-aware visual asset families.

**Orchestrator:** [ecommerce-product-image-studio](./ecommerce-product-image-studio/SKILL.md)

## Current production philosophy

\`\`\`text
real product references
→ evidence + PRODUCT IDENTITY LOCK
→ SKU / variant model
→ buyer-decision map
→ platform commerce style profile
→ CAMPAIGN STYLE LOCK
→ shot / scene routing
→ reference-image generation or edit
→ 2–3 candidates for important assets
→ commercial + identity QA
→ targeted repair / rerun only failures
→ semantic detail modules
→ marketplace / mobile / web derivatives
→ delivery gate
\`\`\`

## Reference-first, not cutout-first

For most consumer products, lifestyle and commercial scenes SHOULD pass the real product photo directly to a capable reference-image generation/edit tool.

Use strict source-pixel cutout/compositing only when exact pixels matter:
- packaging text;
- logos / labels;
- precision ports / interfaces;
- model plates;
- repeated identity drift.

A technically perfect mask pasted into a weak background is not a successful ecommerce image.

## Platform commerce styles

The repository separates:

- **platform commerce style** — heuristic conversion language;
- **official platform compliance** — current, source-backed rules.

Built-in heuristic profiles currently include:
- Taobao / Tmall / 1688;
- Pinduoduo;
- Douyin;
- generic master.

### Taobao / Tmall / 1688

Think:
- shelf / search / comparison;
- longer trust-building chain;
- hero + selling point + lifestyle + material/detail + dimensions + variants + detail modules.

### Pinduoduo

Think:
- fast value judgement;
- direct hierarchy;
- strong product / variant / quantity clarity;
- short readable copy;
- avoid decorative layouts that hide the offer.

### Douyin

Think:
- mobile content + shelf;
- strong product recognition;
- believable scene / person / usage moments;
- content-native framing;
- compact specs after interest is established.

These are creative heuristics, not official platform rules.

## Stable locks

A coherent set uses:

\`\`\`text
PRODUCT IDENTITY LOCK
+ CAMPAIGN STYLE LOCK
+ PLATFORM COMMERCE STYLE LOCK
+ asset-specific shot brief
\`\`\`

The first three remain stable.
The shot brief changes per image.

## Commercial scenes

A scene should answer:
- who uses it;
- where;
- what they are doing;
- why this scene helps a buyer decide.

Use:
- a clear story;
- camera + lighting;
- product salience;
- 2–4 relevant props;
- realistic interaction.

Do not generate empty “pretty rooms” with no product purpose.

## Candidate and repair loop

Important hero / lifestyle / person-use assets SHOULD use bounded candidate exploration.

\`\`\`text
generate
→ identity QA
→ commercial composition QA
→ platform-style QA
→ rank
→ targeted repair sentences
→ rerun failed asset only
\`\`\`

## Detail pages

Use one-screen-one-job:
- one benefit;
- one proof;
- one specification question;
- one material/detail question;
- one variant choice.

Independent modules are the editable masters.
A stitched long image is normally a derivative.

## Existing contracts

The orchestrator contains contracts for:
- task intake;
- execution preflight;
- product evidence / identity;
- dimensions;
- buyer decisions;
- variants;
- reference-generation strategy;
- platform commerce style;
- scene routing;
- campaign style;
- prompt rendering;
- candidate repair;
- output profiles;
- asset reuse / derivation;
- QA;
- delivery.

## Research / inspiration

See [ECOMMERCE_VISUAL_RESEARCH.md](./ECOMMERCE_VISUAL_RESEARCH.md).

The current visual-generation strategy was informed by public ecommerce-agent work including:
- \`xianyu110/ecommerce-image-skills\`;
- \`dlazy-ai/ecommerce-skills\`.

The repository adapts their useful workflow ideas into its own evidence, variant, buyer-decision and delivery architecture.