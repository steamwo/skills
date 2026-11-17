---
name: product-scale-calibration
description: Calibrate product, scene, person, camera, contact planes, and reference-object scale before e-commerce lifestyle compositing; explicitly downgrade cases that cannot support metric scale claims.
---

# Product Scale Calibration

## Objective

Establish how large the product should appear in a scene and how it relates to the camera, ground/contact plane, reference objects, and people.

Visual plausibility is not metric calibration.

## Scale states

- \`METRICALLY_GROUNDED\`: product dimensions plus scene/camera/reference geometry support physical scale.
- \`VISUALLY_APPROXIMATED\`: plausible visual scale with explicit assumptions.
- \`SCALE_UNVERIFIED\`: insufficient evidence for scale claims.

## Inputs

- \`product-identity.json\`
- \`product-dimensions.json\`
- authoritative source view
- background / scene geometry
- contact plane
- camera information if known
- verified reference objects if used
- person height / scale basis if used

## MUST

- identify the visible product axes in the source view;
- define the product anchor and contact points;
- define ground / table / wall or other support planes;
- record camera direction and projection assumptions;
- record the method used for scale placement;
- record all assumptions and unknowns;
- preserve product geometry while placing it.

## MUST NOT

- use one global pixels-per-mm ratio across different depths in a perspective scene;
- use an AI-generated chair, door, table, or person as a metric reference unless its dimensions are intentionally controlled;
- use ground-plane homography to distort a vertical product body;
- repair view mismatch by non-uniform product scaling or generative geometry changes;
- claim camera calibration when the required camera information is unknown.

## Simplified same-plane case

Only when the target dimension and reference object are on the same plane, at approximately the same depth, and perspective is negligible:

\`\`\`text
pixel_scale = reference_span_px / reference_span_mm
target_span_px = target_span_mm * pixel_scale
\`\`\`

Document why the simplified case is valid.

## Perspective / 3D case

When depth varies materially, prefer:
- known camera parameters;
- 3D scene geometry;
- verified CAD / 3D model;
- calibrated multi-view reconstruction;
- same-depth reference geometry.

If these are unavailable, downgrade the result.

## Person scale

A person MAY be used as a metric reference only when height / relevant body dimension is known and the spatial relationship is controlled.

Otherwise:
- mark person scale as estimated;
- do not infer product dimensions from the person;
- do not claim metric accuracy.

## Output

Create \`scale-calibration.json\` with:
- \`sku\`
- \`status\`
- \`product_dimension_source\`
- \`scene_coordinate_system\`
- \`contact_planes\`
- \`reference_objects\`
- \`camera\`
- \`product_placement\`
- \`person_scale\`
- \`method\`
- \`assumptions\`
- \`uncertainties\`
- \`validation\`
- \`limitations\`

Also create a scale / placement sketch when useful.

## Gate

If status is \`SCALE_UNVERIFIED\`:
- do not use phrases such as “true scale”, “accurate proportion”, or “1:1 physical relationship”;
- avoid strong scale cues unless explicitly presented as illustrative;
- customer-facing scene images SHOULD be labeled internally as visual concepts pending scale verification.