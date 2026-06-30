"""CLI parsing for the Map data generator."""

from __future__ import annotations

import argparse
from pathlib import Path

from knowledge_base.components.map.pipeline.settings import (
    DEFAULT_CACHE,
    DEFAULT_FASTEMBED_MODEL,
    DEFAULT_OUTPUT,
    DEFAULT_SIMILARITY_OUTPUT,
)
from knowledge_base.embedding_workbench import FASTEMBED_DEVICE_CHOICES

EPILOG = """
Usage
-----
Basic:
    python knowledge_base/components/map/generate_map_data.py

Force full re-embed:
    python knowledge_base/components/map/generate_map_data.py --force

Require CUDA for local fastembed inference:
    python knowledge_base/components/map/generate_map_data.py --fastembed-device cuda --force

Use a separate chunk cache:
    python knowledge_base/components/map/generate_map_data.py \\
        --fastembed-model mixedbread-ai/mxbai-embed-large-v1 \\
        --chunk-cache knowledge_base/components/map/cache/embedding_cache.chunks.json
"""


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Generate Sigma.js map data from paper embeddings.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=EPILOG,
    )
    parser.add_argument(
        "--backend",
        choices=["fastembed"],
        default=None,
        help="Embedding backend (default: fastembed).",
    )
    parser.add_argument(
        "--fastembed-device",
        choices=FASTEMBED_DEVICE_CHOICES,
        default="auto",
        help="Device for local fastembed inference: auto uses CUDA when ONNX Runtime exposes it (default: auto).",
    )
    parser.add_argument(
        "--fastembed-model",
        default=DEFAULT_FASTEMBED_MODEL,
        help=f"Local fastembed model to use with --backend fastembed (default: {DEFAULT_FASTEMBED_MODEL}).",
    )
    parser.add_argument(
        "--force",
        action="store_true",
        help="Ignore the embedding cache and re-embed every paper.",
    )
    parser.add_argument(
        "--cache",
        type=Path,
        default=DEFAULT_CACHE,
        help=f"Path to the embedding cache file (default: {DEFAULT_CACHE}).",
    )
    parser.add_argument(
        "--chunk-cache",
        type=Path,
        default=None,
        help=(
            "Path to materialized chunk embeddings. Defaults to the tracked Semantic Search cache for the "
            "default MiniLM model, otherwise <cache-stem>.chunks.json next to --cache."
        ),
    )
    parser.add_argument(
        "--output",
        type=Path,
        default=DEFAULT_OUTPUT,
        help=f"Path to the output JS file (default: {DEFAULT_OUTPUT}).",
    )
    parser.add_argument(
        "--similarity-output",
        type=Path,
        default=DEFAULT_SIMILARITY_OUTPUT,
        help=f"Path to the binary similarity matrix sidecar (default: {DEFAULT_SIMILARITY_OUTPUT}).",
    )
    parser.add_argument(
        "--skip-force-layout",
        action="store_true",
        dest="skip_force_layout",
        help="Skip the force-directed post-processing step after UMAP.",
    )
    return parser.parse_args()
