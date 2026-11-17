# Commercial Scene Router

## Purpose

Route a product into a commercially useful scene instead of asking the image model to invent an arbitrary background.

A scene must answer:
- who uses it;
- where;
- when / under what condition;
- what product benefit or use context the scene proves or suggests.

## Scene brief

Each scene record SHOULD contain:
- \`scene_id\`
- \`category\`
- \`buyer_question\`
- \`story_sentence\`
- \`environment\`
- \`person_action\`
- \`camera\`
- \`lighting\`
- \`product_occupancy\`
- \`props\`
- \`scale_reference\`
- \`platform_style_profile\`
- \`identity_lock_version\`

## Scene grammar

Write the scene in this order:

\`\`\`text
WHO
+ WHERE
+ ACTION / PRODUCT USE
+ CAMERA
+ LIGHT
+ PRODUCT SALIENCE
+ 2–4 SUPPORTING PROPS
+ SCALE REFERENCE
\`\`\`

Do not write a long list of decorative adjectives.

## Category seeds

These are starting points, not mandatory styles:

- fitness → bright home workout corner / boutique gym / training studio / outdoor calisthenics;
- home → lived-in room with realistic furniture and natural daylight;
- kitchen → clean worktop, ingredients/tools relevant to actual use;
- tech → desk / studio / commute context, controlled practical lighting;
- beauty → vanity / bathroom / dressing table, clean tactile materials;
- outdoor → trail / campsite / park / travel moment;
- tools → workshop / garage / field-use context.

## Fitness example

For a wooden push-up / parallette product:

\`\`\`text
A bright modern home-training corner in the morning.
An adult athlete uses the exact referenced wooden parallettes for an elevated push-up.
Camera at low three-quarter angle near floor level.
Soft side daylight through a window, realistic contact shadows.
The product remains a clear hero and occupies roughly 30–45% of the useful frame.
Only a yoga mat, towel and one small dumbbell pair as supporting props.
No extra bars, no alternate handle design, no text.
\`\`\`

## Product occupancy heuristics

Use as starting points:
- hero / clean commercial: 40–65%;
- lifestyle: 25–50%;
- person-use: enough to clearly identify product + body interaction;
- detail macro: 60–85%;
- infographic: reserve a dedicated product zone and copy zone.

These are composition heuristics, not platform rules.

## Scene QA

Reject scenes that are:
- technically clean but generic / meaningless;
- too empty to communicate use;
- too cluttered to read the product;
- physically impossible;
- stylistically mismatched to the selected platform profile;
- driven by props rather than the product.