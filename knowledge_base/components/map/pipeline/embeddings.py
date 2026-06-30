"""Embedding rows and backend selection for the Map pipeline.

Embeddings are expensive, so the generator refreshes ordered chunk rows through
the shared Embedding Workbench and only embeds changed chunks. The default
backend is fastembed with ``sentence-transformers/all-MiniLM-L6-v2`` so Map and
Semantic Search can share the tracked chunk cache.
"""

from __future__ import annotations

import importlib.util
import sys
from collections.abc import Callable
from pathlib import Path
from typing import Any

import numpy as np

from knowledge_base.components.map.pipeline.settings import (
    DEFAULT_FASTEMBED_MODEL,
    DEFAULT_SHARED_CHUNK_CACHE,
    EMBED_PROGRESS_INTERVAL,
)
from knowledge_base.embedding_workbench import (
    EmbeddingRow,
    available_onnx_providers,
    fastembed_effective_device,
    load_embedding_table,
    preload_onnxruntime_cuda,
)
from knowledge_base.progress import emit_progress


def paper_embedding_rows(papers: list[dict[str, Any]]) -> list[EmbeddingRow]:
    return [EmbeddingRow(id=str(paper["id"]), text="", content_hash=str(paper["hash"])) for paper in papers]


def default_chunk_cache_for_model(model: str, map_cache: Path) -> Path:
    if model == DEFAULT_FASTEMBED_MODEL:
        return DEFAULT_SHARED_CHUNK_CACHE
    return map_cache.with_name(f"{map_cache.stem}.chunks.json")


def paper_embedding_cache_is_current(cache_path: Path, rows: list[EmbeddingRow], model: str) -> bool:
    if not cache_path.exists():
        return False
    table = load_embedding_table(cache_path, mmap_mode="r", aggregate=False)
    return (
        table.model == model
        and table.ids == tuple(row.id for row in rows)
        and table.hashes == {row.id: row.content_hash for row in rows}
    )


def embed_fastembed(
    texts: list[str],
    model: str = DEFAULT_FASTEMBED_MODEL,
    device: str = "auto",
) -> np.ndarray:
    """
    Embed *texts* using fastembed (local ONNX inference, no API key needed).

    Requires:
        pip install fastembed

    The model is downloaded from HuggingFace on first use and cached in
    ``~/.cache/fastembed``.  Subsequent runs use the cached copy.

    ``sentence-transformers/all-MiniLM-L6-v2`` is the default so Map and
    Semantic Search can share the tracked chunk embedding cache.
    """
    from fastembed import TextEmbedding  # type: ignore[import]
    from fastembed.common.types import Device  # type: ignore[import]

    cuda_setting_by_device = {
        "auto": Device.AUTO,
        "cpu": Device.CPU,
        "cuda": Device.CUDA,
    }
    providers = available_onnx_providers()
    effective_device = fastembed_effective_device(device, providers)
    if effective_device == "cuda":
        preload_onnxruntime_cuda()

    print(f"    Loading fastembed model: {model}")
    print(f"    fastembed device: requested={device}, effective={effective_device}")
    print(f"    ONNX Runtime providers: {', '.join(providers) or 'none'}")
    print("    (First run downloads the model; subsequent runs use the cache.)")
    embedder = TextEmbedding(model, cuda=cuda_setting_by_device[device])
    session = getattr(getattr(embedder, "model", None), "model", None)
    if session is not None:
        print(f"    Active ONNX providers: {', '.join(session.get_providers())}")
    print(f"    Embedding {len(texts)} texts…")
    vecs = []
    for index, vector in enumerate(embedder.embed(texts, batch_size=EMBED_PROGRESS_INTERVAL), start=1):
        vecs.append(vector)
        if index % EMBED_PROGRESS_INTERVAL == 0 or index == len(texts):
            print(f"    Embedded {index}/{len(texts)} text(s)")
            emit_progress(index, len(texts), "Embed map chunks")
    return np.array(vecs, dtype=np.float32)


def choose_backend(
    requested: str | None,
    *,
    fastembed_device: str = "auto",
    fastembed_model: str = DEFAULT_FASTEMBED_MODEL,
) -> tuple[str, Callable[[list[str]], np.ndarray]]:
    """
    Select the embedding backend.

    Returns (backend_name, embed_function).  The embed function has the
    signature: ``fn(texts: list[str]) -> np.ndarray``.
    """
    if requested not in (None, "fastembed"):
        sys.exit(f"ERROR: unsupported embedding backend: {requested}")

    if importlib.util.find_spec("fastembed") is None:
        sys.exit("ERROR: fastembed is not available. Install fastembed: pip install fastembed")

    model = fastembed_model
    print(f"Backend: fastembed {model} (local ONNX)")
    return model, lambda texts: embed_fastembed(texts, model, fastembed_device)
