#!/usr/bin/env python3
"""Validate buyer-decision, variant-matrix, and asset-derivation records."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Any


DECISION_STATES = {"COVERED", "PARTIALLY_COVERED", "BLOCKED", "NOT_APPLICABLE"}
SHAREDNESS = {"SHARED_VERIFIED", "VARIANT_SPECIFIC", "UNKNOWN_SHAREDNESS", "NOT_APPLICABLE"}
ASSET_LEVELS = {"AUTHORITATIVE_SOURCE", "PRODUCTION_MASTER", "SEMANTIC_ASSET", "SURFACE_DERIVATIVE"}


def load(path: Path) -> Any:
    with path.open("r", encoding="utf-8") as f:
        return json.load(f)


def validate_buyer_map(data: dict[str, Any], errors: list[str]) -> None:
    stages = data.get("decision_stages")
    if not isinstance(stages, list):
        errors.append("buyer-decision-map: decision_stages must be an array.")
        return
    for i, item in enumerate(stages):
        if not isinstance(item, dict):
            errors.append(f"buyer-decision-map[{i}]: expected object.")
            continue
        status = item.get("status")
        if status not in DECISION_STATES:
            errors.append(f"buyer-decision-map[{i}]: illegal status {status!r}.")
        if not item.get("buyer_question"):
            errors.append(f"buyer-decision-map[{i}]: buyer_question is required.")
        if status in {"COVERED", "PARTIALLY_COVERED"} and not item.get("evidence_refs"):
            errors.append(f"buyer-decision-map[{i}]: covered decisions require evidence_refs.")


def validate_variant_matrix(data: dict[str, Any], errors: list[str]) -> None:
    axes = data.get("variant_axes", [])
    if not isinstance(axes, list) or not all(isinstance(x, str) and x for x in axes):
        errors.append("variant-matrix: variant_axes must be an array of strings.")
        axes = []

    variants = data.get("variants")
    if not isinstance(variants, list) or not variants:
        errors.append("variant-matrix: variants must be a non-empty array.")
        return

    ids: set[str] = set()
    for i, variant in enumerate(variants):
        if not isinstance(variant, dict):
            errors.append(f"variant-matrix[{i}]: expected object.")
            continue
        variant_id = variant.get("variant_id")
        if not isinstance(variant_id, str) or not variant_id:
            errors.append(f"variant-matrix[{i}]: variant_id is required.")
        elif variant_id in ids:
            errors.append(f"variant-matrix: duplicate variant_id {variant_id!r}.")
        else:
            ids.add(variant_id)

        values = variant.get("axes", {})
        if axes and not isinstance(values, dict):
            errors.append(f"variant-matrix[{i}]: axes must be an object.")
        elif isinstance(values, dict):
            missing = [axis for axis in axes if axis not in values]
            if missing:
                errors.append(f"variant-matrix[{i}]: missing variant axes {missing}.")

        for field_name in ("sharedness", "asset_scope"):
            value = variant.get(field_name)
            if field_name == "sharedness" and value is not None and value not in SHAREDNESS:
                errors.append(f"variant-matrix[{i}]: illegal sharedness {value!r}.")

    shared = data.get("shared_identity_features", [])
    if isinstance(shared, list):
        for i, feature in enumerate(shared):
            if not isinstance(feature, dict):
                continue
            state = feature.get("sharedness")
            if state is not None and state not in SHAREDNESS:
                errors.append(
                    f"variant-matrix.shared_identity_features[{i}]: "
                    f"illegal sharedness {state!r}."
                )


def validate_derivation_map(data: dict[str, Any], errors: list[str]) -> None:
    assets = data.get("assets")
    if not isinstance(assets, list):
        errors.append("asset-derivation-map: assets must be an array.")
        return

    by_id: dict[str, dict[str, Any]] = {}
    for i, asset in enumerate(assets):
        if not isinstance(asset, dict):
            errors.append(f"asset-derivation-map[{i}]: expected object.")
            continue
        asset_id = asset.get("asset_id")
        if not isinstance(asset_id, str) or not asset_id:
            errors.append(f"asset-derivation-map[{i}]: asset_id is required.")
            continue
        if asset_id in by_id:
            errors.append(f"asset-derivation-map: duplicate asset_id {asset_id!r}.")
            continue
        by_id[asset_id] = asset

        level = asset.get("level")
        if level is not None and level not in ASSET_LEVELS:
            errors.append(f"asset-derivation-map[{i}]: illegal level {level!r}.")

        parents = asset.get("parent_asset_ids", [])
        if not isinstance(parents, list) or not all(isinstance(x, str) for x in parents):
            errors.append(f"asset-derivation-map[{i}]: parent_asset_ids must be an array.")
        elif asset_id in parents:
            errors.append(f"asset-derivation-map[{i}]: asset cannot depend on itself.")

        scope = asset.get("variant_scope")
        if scope is not None and (
            not isinstance(scope, list) or not all(isinstance(x, str) and x for x in scope)
        ):
            errors.append(f"asset-derivation-map[{i}]: variant_scope must be an array of strings.")

    # Only inspect cycles among assets declared inside this map.
    graph = {
        asset_id: [p for p in asset.get("parent_asset_ids", []) if p in by_id]
        for asset_id, asset in by_id.items()
    }
    visiting: set[str] = set()
    visited: set[str] = set()

    def dfs(node: str) -> None:
        if node in visiting:
            errors.append(f"asset-derivation-map: dependency cycle detected at {node!r}.")
            return
        if node in visited:
            return
        visiting.add(node)
        for parent in graph.get(node, []):
            dfs(parent)
        visiting.remove(node)
        visited.add(node)

    for node in graph:
        dfs(node)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--buyer-decision-map", type=Path)
    parser.add_argument("--variant-matrix", type=Path)
    parser.add_argument("--asset-derivation-map", type=Path)
    args = parser.parse_args()

    paths = [
        args.buyer_decision_map,
        args.variant_matrix,
        args.asset_derivation_map,
    ]
    if not any(paths):
        parser.error("provide at least one input file")

    errors: list[str] = []

    try:
        if args.buyer_decision_map:
            validate_buyer_map(load(args.buyer_decision_map), errors)
        if args.variant_matrix:
            validate_variant_matrix(load(args.variant_matrix), errors)
        if args.asset_derivation_map:
            validate_derivation_map(load(args.asset_derivation_map), errors)
    except (OSError, json.JSONDecodeError) as exc:
        print(f"ERROR: {exc}")
        return 1

    for error in errors:
        print(f"ERROR: {error}")

    if errors:
        print("Result: FAIL")
        return 1

    print("Result: PASS")
    return 0


if __name__ == "__main__":
    sys.exit(main())
