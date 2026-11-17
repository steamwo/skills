# Detail Page Module Contract

## Purpose

Treat a product detail page as a set of semantic modules, not one monolithic generated image.

Independent modules are easier to:
- adapt to desktop / mobile;
- localize;
- reorder;
- QA;
- replace when one claim changes;
- export to different marketplaces;
- preserve editability.

## Module model

Each module SHOULD define:
- \`module_id\`
- semantic purpose;
- buyer question;
- source product asset;
- verified claims;
- copy source;
- product provenance;
- output profiles;
- layout template;
- dependencies;
- QA status.

Example module roles:
- product overview;
- core feature;
- lifestyle use;
- material / structure;
- dimension / specification;
- comparison;
- packaging / included items;
- usage / care note.

## Content-before-canvas principle

Plan semantic content first.

Then render the same semantic module into one or more output profiles.

\`\`\`text
verified content module
        ↓
semantic priority
        ↓
desktop / mobile / marketplace render profiles
\`\`\`

Do not start by stretching content to fit a canvas.

## Module independence

A module SHOULD remain independently editable and exportable.

A stitched long image MAY be created as a derivative deliverable, but SHOULD NOT be the only master source.

## Claim and provenance inheritance

Every render of the same module inherits:
- claim evidence;
- product provenance;
- dimension source;
- SKU / variant identity.

Changing canvas size does not create permission to change product facts.

## Responsive behavior

For narrower / mobile surfaces:
- stack rather than squeeze;
- enlarge critical text;
- shorten line length;
- preserve product visibility;
- reduce non-essential decorative density.

For wider desktop surfaces:
- MAY use split layouts;
- MAY distribute copy and product imagery horizontally;
- MUST preserve reading hierarchy.

## Gate

If one render cannot preserve readability or product visibility under a requested profile, redesign the layout for that profile rather than mechanically resize the original.