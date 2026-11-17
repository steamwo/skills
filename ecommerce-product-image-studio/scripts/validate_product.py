#!/usr/bin/env python3
"""Validate a SKU fact manifest and the referenced local source images."""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Any


def get_nested(data: dict[str, Any], *keys: str) -> Any:
    value: Any = data
    for key in keys:
        if not isinstance(value, dict):
            return None
        value = value.get(key)
    return value


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

    if get_nested(data, "material", "species", "value") in (None, ""):
        warnings.append("Wood/material species is not specified; do not invent it in marketing copy.")
    if get_nested(data, "material", "species", "status") in (None, "", "unknown"):
        warnings.append("Material species evidence is unverified or unknown.")
    if get_nested(data, "dimensions", "status") in (None, "", "unknown"):
        warnings.append("Dimensions are unverified; do not generate numeric size claims.")
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
        description="Validate product facts and referenced source images."
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
