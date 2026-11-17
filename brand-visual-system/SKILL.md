---
name: brand-visual-system
description: Define a reusable e-commerce campaign style lock for palette, photography, lighting, camera, layout, typography, prop density, and forbidden treatments; inject only the relevant style sections into each asset prompt.
---

# Brand Visual System

## Objective

Keep an e-commerce image set visually coherent without turning every prompt into the same generic style paragraph.

## Inputs

- brand guide / logo;
- confirmed colours;
- target audience;
- marketplace / platform commerce profile;
- product identity;
- optional visual references.

## Campaign Style Lock

Create one stable block for the asset family:

\`\`\`text
CAMPAIGN STYLE LOCK
Palette: ...
Lighting family: ...
Background family: ...
Camera family: ...
Colour grade: ...
Typography mood: ...
Prop density: ...
Mood: ...
Hard avoids: ...
\`\`\`

The stable lock is reused across the set.

Shot-specific composition changes per asset.

## Structured style sections

Create \`brand-system.json\` with sections:

- \`brand.tone\`
- \`photography.background\`
- \`photography.lighting\`
- \`photography.camera\`
- \`photography.grade\`
- \`photography.crop\`
- \`layout.margin\`
- \`layout.typeface\`
- \`layout.text_color\`
- \`person\` when relevant
- \`forbid[]\`

## Selective prompt injection

Inject only relevant sections.

Examples:
- lifestyle scene → tone + photography + forbid;
- person-use → tone + person + photography + forbid;
- selling-point graphic → tone + layout + forbid;
- detail module → tone + layout + selected photography + forbid.

Irrelevant style fields SHOULD NOT enter the prompt.

A person-face description does not belong in a pure product-detail prompt.

## Product isolation

Brand styling MUST NOT silently recolour or redesign the real SKU.

Product colour changes require explicit variant evidence / authorization.

## China commerce

For Chinese conversion graphics:
- define title/subtitle/body/numeric hierarchy;
- prioritize mobile and thumbnail readability;
- keep copy short enough for the target surface;
- use deterministic typography when exact text matters.

## Outputs

Create:
- \`brand-system.json\`
- \`campaign-style-lock.txt\`
- \`brand-style-guide.md\`

Every planned asset SHOULD reference the campaign style version.