"""Generate the static browser Map data by orchestrating pipeline modules."""

from __future__ import annotations

import hashlib
from pathlib import Path

import numpy as np
import yaml

from knowledge_base.components.map.pipeline.artifacts import write_browser_artifacts
from knowledge_base.components.map.pipeline.cli import parse_args
from knowledge_base.components.map.pipeline.embeddings import (
    choose_backend,
    default_chunk_cache_for_model,
    paper_embedding_cache_is_current,
    paper_embedding_rows,
)
from knowledge_base.components.map.pipeline.layouts import (
    default_force_params,
    load_or_build_force_layout,
    load_or_build_umap_layout,
)
from knowledge_base.components.map.pipeline.navigation import parse_nav_categories, parse_nav_category_order
from knowledge_base.components.map.pipeline.papers import collect_map_papers
from knowledge_base.components.map.pipeline.settings import METADATA_ROOT, SITE_CONFIG
from knowledge_base.embeddings.workbench import (
    load_embedding_cache,
    load_embedding_table,
    materialize_embedding_table,
    refresh_embedding_cache,
)
from knowledge_base.progress import emit_progress

SOURCE_FINGERPRINT_VERSION = 1


def source_fingerprint(root: Path, extra_files: tuple[Path, ...] = ()) -> str:
    h = hashlib.sha256()
    h.update(f"map-source-fingerprint:{SOURCE_FINGERPRINT_VERSION}".encode("ascii"))
    paths = sorted(
        path
        for pattern in ("metadata.yml", "embed_text.md", "embed_input.md")
        for path in root.rglob(pattern)
        if path.is_file()
    )
    paths.extend(path for path in extra_files if path.is_file())
    for path in paths:
        stat = path.stat()
        h.update(path.as_posix().encode("utf-8"))
        h.update(f"\0{stat.st_size}\0{stat.st_mtime_ns}\0".encode("ascii"))
    return h.hexdigest()[:24]


def map_outputs_current(cache: dict[str, object], source_key: str, output: Path, similarity_output: Path) -> bool:
    map_data = cache.get("mapData")
    return (
        isinstance(map_data, dict)
        and map_data.get("sourceFingerprint") == source_key
        and output.exists()
        and similarity_output.exists()
    )


def main() -> None:
    args = parse_args()

    print("=" * 60)
    print("Knowledge Base — Map Data Generator")
    print("=" * 60)
    source_key = source_fingerprint(METADATA_ROOT, (SITE_CONFIG,))
    cache = load_embedding_cache(args.cache)
    if not args.force and map_outputs_current(cache, source_key, args.output, args.similarity_output):
        print("Map data loaded from cache (source files unchanged)")
        print(f"    Output: {args.output}")
        return

    # ---- load config -------------------------------------------------------
    with open(SITE_CONFIG, encoding="utf-8") as f:
        config = yaml.safe_load(f)
    paper_to_category = parse_nav_categories(config)
    nav_order = parse_nav_category_order(config)

    # ---- collect papers ----------------------------------------------------
    print("\n[1/6] Collecting paper metadata…")
    papers, rows = collect_map_papers(paper_to_category)
    source_key = source_fingerprint(METADATA_ROOT, (SITE_CONFIG,))
    print(f"    Found {len(papers)} papers")

    # ---- choose backend ----------------------------------------------------
    print("\n[2/6] Selecting embedding backend…")
    model_name, embed_fn = choose_backend(
        args.backend,
        fastembed_device=args.fastembed_device,
        fastembed_model=args.fastembed_model,
    )
    paper_rows = paper_embedding_rows(papers)

    # ---- refresh embedding cache ------------------------------------------
    print("\n[3/6] Refreshing embedding cache…")
    if not args.force and paper_embedding_cache_is_current(args.cache, paper_rows, model_name):
        print(f"    Paper cache is current: {args.cache}")
        embeddings = load_embedding_table(args.cache, aggregate=False).matrix
    else:
        chunk_cache = args.chunk_cache or default_chunk_cache_for_model(model_name, args.cache)
        print(f"    Chunk cache: {chunk_cache}")

        def embed_changed(texts: list[str]) -> np.ndarray:
            print(f"    {len(texts)} chunk(s) need (re-)embedding")
            return embed_fn(texts)

        embedding_refresh = refresh_embedding_cache(
            rows,
            cache_path=chunk_cache,
            model=model_name,
            embed_texts=embed_changed,
            force=args.force,
            progress_callback=lambda current, total, label: emit_progress(current, total, label, every=512),
        )
        if embedding_refresh.model_changed:
            print(
                f"    Model changed ({embedding_refresh.previous_model} -> {model_name}). "
                "Discarded cached chunk embeddings."
            )
        if embedding_refresh.pruned_ids:
            print(f"    Removed {len(embedding_refresh.pruned_ids)} stale cached chunk(s)")
        if not embedding_refresh.changed_count:
            print(f"    All {len(rows)} embedding chunk(s) are cached — skipping embedding API call")
        else:
            print(f"    Refreshed {embedding_refresh.changed_count} chunk embedding(s)")

        embeddings = embedding_refresh.matrix
        print(f"    Materializing paper embedding cache: {args.cache}")
        cache = materialize_embedding_table(
            paper_rows,
            embeddings,
            cache_path=args.cache,
            model=model_name,
            cache=cache,
        )
    print(f"    Embedding matrix: {embeddings.shape}")

    # ---- UMAP layout -------------------------------------------------------
    print("\n[4/6] Computing UMAP 2-D layout…")
    umap_coords = load_or_build_umap_layout(
        cache=cache,
        cache_path=args.cache,
        papers=papers,
        embeddings=embeddings,
        force=args.force,
    )

    # ---- force-directed layout post-processing -----------------------------
    print("\n[5/6] Force-directed layout post-processing…")
    force_params = default_force_params()
    if args.skip_force_layout:
        print("    Skipped (--skip-force-layout)")
        layout_coords = umap_coords
    else:
        layout_coords = load_or_build_force_layout(
            cache=cache,
            cache_path=args.cache,
            papers=papers,
            umap_coords=umap_coords,
            embeddings=embeddings,
            force=args.force,
            force_params=force_params,
        )

    # ---- build browser data -----------------------------------------------
    print("\n[6/6] Building map data and writing output…")
    write_browser_artifacts(
        cache=cache,
        cache_path=args.cache,
        papers=papers,
        layout_coords=layout_coords,
        embeddings=embeddings,
        nav_order=nav_order,
        model_name=model_name,
        output=args.output,
        similarity_output=args.similarity_output,
        force_params=force_params,
        force=args.force,
        source_fingerprint=source_key,
    )
    print("\nDone!")


if __name__ == "__main__":
    main()
