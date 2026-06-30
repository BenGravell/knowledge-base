"""Argument parsing for offline refresh."""

from __future__ import annotations

import argparse

FASTEMBED_DEVICE_CHOICES = ("auto", "cpu", "cuda")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Refresh offline generated data and validate site consistency.",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )
    parser.add_argument(
        "--force",
        action="store_true",
        help="Recompute Map and Semantic Search embeddings instead of using caches.",
    )
    parser.add_argument(
        "--map-backend",
        choices=("fastembed", "auto"),
        default="fastembed",
        help="Map embedding backend. fastembed is the local default; auto lets the map generator choose.",
    )
    parser.add_argument(
        "--fastembed-device",
        choices=FASTEMBED_DEVICE_CHOICES,
        default="auto",
        help="Device for local fastembed inference in Map and Semantic Search: auto uses CUDA when available.",
    )
    parser.add_argument(
        "--skip-force-layout",
        action="store_true",
        help="Pass through to components/map/generate_map_data.py for quicker Map refreshes.",
    )
    parser.add_argument(
        "--audit-severity",
        choices=("error", "warning", "info"),
        default="error",
        help="Minimum metadata audit severity to print.",
    )
    parser.add_argument(
        "--strict",
        action="store_true",
        help="Enable Tree algorithm-label checks and Zensical strict mode.",
    )
    parser.add_argument("--skip-map", action="store_true", help="Do not regenerate Map data.")
    parser.add_argument(
        "--skip-semantic-search",
        action="store_true",
        help="Do not regenerate Semantic Search data.",
    )
    parser.add_argument("--skip-audit", action="store_true", help="Do not run the metadata/map-data audit.")
    parser.add_argument("--skip-build", action="store_true", help="Do not run the final Zensical asset refresh build.")
    parser.add_argument(
        "--full-build",
        action="store_true",
        help="Accepted for compatibility; Zensical builds always render generated paper detail pages.",
    )
    parser.add_argument("--dry-run", action="store_true", help="Print the planned commands without running them.")
    parser.add_argument(
        "--no-fast-path",
        action="store_true",
        help="Always run refresh steps even when the default hot-start no-op check is clean.",
    )
    return parser.parse_args()
