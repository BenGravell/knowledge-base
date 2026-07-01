"""Refresh step construction."""

from __future__ import annotations

import argparse
import sys

from knowledge_base.scripts.offline_refresh.model import Step


def build_steps(args: argparse.Namespace) -> list[Step]:
    py = sys.executable
    steps: list[Step] = []

    validate_tree = [py, "knowledge_base/scripts/validate_tree.py"]
    if args.strict:
        validate_tree.append("--check-algorithm-labels")
    steps.append(Step("Validate", "Tree nav", "Validate Tree nav links and paper coverage", validate_tree))

    steps.append(
        Step(
            "Validate",
            "Tree coverage",
            "Check that every metadata-backed paper is in the Tree",
            [
                py,
                "-m",
                "knowledge_base.scripts.list_unplaced_papers",
                "--neighbors",
                "0",
                "--fail-on-missing",
            ],
        )
    )

    if not args.skip_semantic_search:
        semantic_search = [
            py,
            "knowledge_base/components/semantic_search/generate_semantic_search_index.py",
            "--fastembed-device",
            args.fastembed_device,
        ]
        if args.force:
            semantic_search.append("--force")
        steps.append(
            Step(
                "Generate",
                "Semantic Search",
                "Regenerate Semantic Search index, settings, and vector table",
                semantic_search,
            )
        )

    if not args.skip_map:
        map_data = [
            py,
            "knowledge_base/components/map/pipeline/generate_data.py",
            "--fastembed-device",
            args.fastembed_device,
        ]
        if args.map_backend != "auto":
            map_data.extend(["--backend", args.map_backend])
        if args.force:
            map_data.append("--force")
        if args.skip_force_layout:
            map_data.append("--skip-force-layout")
        steps.append(
            Step("Generate", "Map data", "Regenerate Map embeddings, layout, map-data.js, and sidecar", map_data)
        )

    if not args.skip_audit:
        steps.append(
            Step(
                "Verify",
                "Metadata audit",
                "Audit metadata and generated Map/Search assets",
                [
                    py,
                    "-m",
                    "knowledge_base.scripts.audit_metadata",
                    "knowledge_base",
                    "--severity",
                    args.audit_severity,
                ],
            )
        )

    if not args.skip_build:
        build = [py, "-m", "knowledge_base.dev_cli", "build"]
        if args.strict:
            build.append("--strict")
        steps.append(Step("Verify", "Zensical build", "Build Zensical site and generated assets", build))

    return steps
