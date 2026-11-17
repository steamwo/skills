---
name: ecommerce-infographic-detail-builder
description: Build evidence-backed e-commerce semantic detail modules and variant-aware responsive derivatives from verified product facts, buyer-decision goals, SKU scope, and output profiles.
---

# Ecommerce Infographic & Detail Builder

## Objective

Build independent detail-page modules that answer purchase questions and can be reused across variants / markets only when their evidence scope permits.

Read:
- buyer-decision framework;
- variant-matrix contract;
- asset-reuse contract;
- detail-module contract;
- output-profile contract.

## Inputs

- \`buyer-decision-map.json\`
- \`variant-matrix.json\` when applicable
- product identity
- product dimensions
- approved claims
- verified packaging / included items
- brand system
- image plan
- output profiles
- asset derivation map

## Content-before-canvas

Each module MUST first define:
- buyer question;
- verified answer;
- variant scope;
- evidence;
- semantic priority.

Only then define layout / canvas.

## Variant-aware module rule

Each module MUST declare:
- \`variant_scope\`
- \`reuse_class\`

Family-shared modules may reuse layout / copy only when all referenced facts are verified shared.

Variant-specific numbers, color, packaging, included items, or product cutouts must be parameterized or rendered per variant.

## Asset reuse

Prefer a reusable semantic master.

Example:

\`\`\`text
semantic module: "How to choose length"
  evidence: variant matrix
  scope: family
  ├── Chinese mobile render
  ├── Amazon web render
  └── generic detail render
\`\`\`

For a per-variant dimension module:

\`\`\`text
semantic template: "Dimensions"
  ├── 25cm render → 25cm variant facts
  ├── 30cm render → 30cm variant facts
  ├── 35cm render → 35cm variant facts
  └── 40cm render → 40cm variant facts
\`\`\`

The template may be shared; the product cutout and dimension values remain variant-bound.

## Dimension rules

Use only verified values by default.

MUST distinguish:
- product vs packaging;
- net vs gross;
- measurement states;
- variant-specific dimensions.

If a single axis is verified, show only that axis.

## Copy rules

Every claim MUST have scope:
- family;
- variant;
- bundle;
- market.

Do not put a variant-specific number into family-shared static copy unless the render parameterizes it correctly.

## Multi-surface rendering

One semantic module MAY render to:
- mobile;
- web;
- marketplace-specific surface;
- long-image derivative.

All renders inherit:
- evidence;
- variant scope;
- product provenance;
- copy version.

They may change composition and typography.

## Outputs

Create:
- module manifest
- copy deck
- dimension source map
- independent semantic masters
- variant/profile derivatives
- editable layout sources
- optional stitched long image
- QA records

## Gate

A module is \`FAIL\` if:
- its buyer answer lacks evidence;
- variant scope is wrong;
- shared copy contains a wrong variant-specific value;
- a derivative loses product provenance;
- an unverified fact appears as customer-facing truth.