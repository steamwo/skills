# Candidate Generation, Ranking and Repair Loop

## Purpose

High-quality e-commerce visuals should not rely on the first random generation.

Use a bounded loop:

\`\`\`text
brief
→ generate candidates
→ identity QA
→ commercial composition QA
→ platform-style QA
→ rank
→ accept best OR append targeted repair instructions
→ regenerate only failed asset
\`\`\`

## Candidate policy

For visually important generative assets:
- hero: 2–3 candidates when budget allows;
- lifestyle: 2–3 distinct candidates;
- person-use: 2–3 candidates because anatomy/contact failure rate is higher;
- simple detail crop / deterministic graphic: one candidate may be enough.

Candidates should vary **one creative axis at a time**:
- camera;
- environment;
- lighting;
- person action;
- product placement.

Do not create three nearly identical samples and call that exploration.

## Ranking dimensions

Score separately:
- \`identity_fidelity\`
- \`commercial_composition\`
- \`scene_story\`
- \`product_salience\`
- \`platform_style_fit\`
- \`lighting_realism\`
- \`person_interaction\` when applicable
- \`real_world_scale_fidelity\` when verified dimensions / scale references apply
- \`text_readability\` when applicable
- \`claim_truth\`

Never average away a hard identity failure.

## Repair sentences

QA SHOULD output 1–3 specific repair instructions that can be appended to the next prompt.

Examples:
- product drift → restate exact geometry / component details;
- scene too busy → reduce props and simplify background;
- product too small in frame → enforce occupancy / sharpest-element instruction without changing physical scale;
- product too large / small relative to person → restate the verified dimensions, name the body scale reference, require uniform scaling, and explicitly forbid enlarging the product for prominence;
- lighting conflict → specify one dominant light direction;
- person contact wrong → specify exact hand / foot / support contact;
- platform mismatch → append the relevant platform style lock;
- text error → shorten copy or move copy to deterministic layout.

## Retry cap

Default maximum:
- 2 repair rounds for ordinary scenes;
- 3 for high-value hero / person-use assets.

After cap:
- escalate fidelity mode;
- change scene/camera;
- switch tool/model;
- or mark \`REVIEW/BLOCKED\`.

Do not loop indefinitely.

## Manifest

Record each round:
- candidate ID;
- prompt;
- reference inputs;
- scores;
- failures;
- repair sentences;
- accepted candidate;
- reason.

This makes visual iteration reproducible instead of subjective.