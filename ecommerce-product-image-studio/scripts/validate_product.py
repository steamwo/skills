#!/usr/bin/env python3
"""Validate a SKU fact manifest and the referenced local source images."""
from __future__ import annotations

import argparse
import json
import math
import sys
from pathlib import Path
from typing import Any

DIMENSION_STATUSES = {
    "user_confirmed",
    "document_verified",
    "partial",
    "estimated",
    "unknown",
    "conflicting",
}
VERIFIED_STATUSES = {"user_confirmed", "document_verified"}
DIMENSION_FIELDS = (
    "length_mm",
    "width_mm",
    "height_mm",
)
OPTIONAL_MEASUREMENTS = ("weight_g",)


def get_nested(data: dict[str, Any], *keys: str) -> Any:
    value: Any = data
    for key in keys:
        if not isinstance(value, dict):
            return None
        value = value.get(key)
    return value


def validate_measurement_block(
    block: Any,
    label: str,
    errors: list[str],
    warnings: list[str],
    *,
    require_all_axes_when_verified: bool = True,
) -> None:
    if not isinstance(block, dict):
        errors.append(f"{label} must be a JSON object.")
        return

    status = block.get("status", "unknown")
    if status not in DIMENSION_STATUSES:
        errors.append(
            f"{label}.status must be one of: {', '.join(sorted(DIMENSION_STATUSES))}."
        )
        return

    unit = block.get("unit")
    if unit != "mm":
        warnings.append(f"{label}.unit should be mm for normalized storage.")

    for field in (*DIMENSION_FIELDS, *OPTIONAL_MEASUREMENTS):
        value = block.get(field)
        if value is None:
            continue
        if isinstance(value, bool) or not isinstance(value, (int, float)):
            errors.append(f"{label}.{field} must be a positive number or null.")
        elif not math.isfinite(float(value)) or value <= 0:
            errors.append(f"{label}.{field} must be a finite positive number.")

    evidence = block.get("evidence", [])
    if not isinstance(evidence, list):
        errors.append(f"{label}.evidence must be an array.")
        evidence = []

    if status in VERIFIED_STATUSES:
        missing = [field for field in DIMENSION_FIELDS if block.get(field) is None]
        if require_all_axes_when_verified and missing:
            errors.append(
                f"{label} is marked {status} but missing: {', '.join(missing)}."
            )
        if not evidence:
            errors.append(
                f"{label} is marked {status} but has no evidence source."
            )
    elif status == "partial":
        known_axes = [field for field in DIMENSION_FIELDS if block.get(field) is not None]
        if not known_axes:
            warnings.append(f"{label} is marked partial but no dimension axis has a value.")
        axis_evidence = block.get("axis_evidence", {})
        if known_axes and not isinstance(axis_evidence, dict):
            warnings.append(f"{label}.axis_evidence should map each known axis to its source.")
    elif status == "estimated":
        warnings.append(
            f"{label} contains estimated measurements; do not use them as formal specs."
        )
    elif status == "unknown":
        if any(block.get(field) is not None for field in (*DIMENSION_FIELDS, *OPTIONAL_MEASUREMENTS)):
            warnings.append(
                f"{label} has numeric values but status is unknown; verify the values before use."
            )
        else:
            warnings.append(f"{label} is unknown; do not invent numeric size claims.")
    elif status == "conflicting":
        warnings.append(f"{label} has conflicting sources; resolve before publishing dimensions.")

    tolerance = block.get("tolerance_mm")
    if tolerance is not None:
        if isinstance(tolerance, bool) or not isinstance(tolerance, (int, float)) or tolerance < 0:
            errors.append(f"{label}.tolerance_mm must be a non-negative number or null.")


def validate(manifest_path: Path, root: Path) -> tuple[list[str], list[str]]:
    errors: list[str] = []
    warnings: list[str] = []

    try:
        data = json.loads(manifest_path.read_text(encoding="utf-8"))
    except FileNotFoundError:
        return [f"Manifest not found: {manifest_path}"], warnings
    except json.JSONDecodeError as exc:
        return [f"Invalid JSON at line {exc.lineno}, column {exc.colno}: {exc.msg}"], warnings

    if not isinstance(data, dict):
        return ["Manifest root must be a JSON object."], warnings

    for field in ("sku", "product_name", "category"):
        if not isinstance(data.get(field), str) or not data[field].strip():
            errors.append(f"Required non-empty string missing: {field}")

    references = data.get("reference_images")
    if not isinstance(references, list) or not references:
        errors.append("reference_images must be a non-empty array.")
    else:
        for index, item in enumerate(references):
            if not isinstance(item, dict) or not isinstance(item.get("file"), str):
                errors.append(f"reference_images[{index}] must contain a file path.")
                continue
            candidate = (root / item["file"]).resolve()
            if not candidate.is_file():
                warnings.append(
                    f"Source image not found for reference_images[{index}]: {candidate}"
                )

    dimensions = data.get("dimensions")
    if dimensions is None:
        warnings.append("dimensions block is missing; physical scale cannot be verified.")
    else:
        validate_measurement_block(dimensions, "dimensions", errors, warnings)

    packaging = data.get("packaging_dimensions")
    if packaging is not None:
        validate_measurement_block(
            packaging,
            "packaging_dimensions",
            errors,
            warnings,
            require_all_axes_when_verified=True,
        )

    if get_nested(data, "material", "species", "value") in (None, ""):
        warnings.append("Wood/material species is not specified; do not invent it in marketing copy.")
    if get_nested(data, "material", "species", "status") in (None, "", "unknown"):
        warnings.append("Material species evidence is unverified or unknown.")
    if get_nested(data, "sale_unit", "quantity") is None:
        warnings.append("Sale quantity is not confirmed; do not infer it from the photo.")
    if not isinstance(data.get("claims", []), list):
        errors.append("claims must be an array.")

    targets = data.get("platform_targets", [])
    if not isinstance(targets, list):
        errors.append("platform_targets must be an array.")
    elif not targets:
        warnings.append("No target platforms selected.")

    return errors, warnings


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Validate product facts, dimensions and referenced local source images."
    )
    parser.add_argument("--manifest", type=Path, required=True, help="SKU product JSON")
    parser.add_argument(
        "--root",
        type=Path,
        default=Path("."),
        help="Project root used to resolve reference image paths",
    )
    args = parser.parse_args()

    manifest = args.manifest.resolve()
    root = args.root.resolve()
    errors, warnings = validate(manifest, root)

    print(f"Manifest: {manifest}")
    print(f"Project root: {root}")
    for warning in warnings:
        print(f"WARNING: {warning}")
    for error in errors:
        print(f"ERROR: {error}")

    if errors:
        print("Result: FAIL")
        return 1
    if warnings:
        print("Result: REVIEW")
        return 0
    print("Result: PASS")
    return 0


if __name__ == "__main__":
    sys.exit(main())
