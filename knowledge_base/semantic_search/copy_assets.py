"""MkDocs gen-files script: publish semantic-search assets."""

from __future__ import annotations

import json
from pathlib import Path

import mkdocs_gen_files

from knowledge_base.catalog import Catalog

ASSET_DIR = Path(__file__).resolve().parent
KB_DIR = ASSET_DIR.parent
METADATA_ROOT = KB_DIR / "docs" / "papers"

PLACEHOLDER_MANIFEST = (
    '{"model":"none","browserModel":"Xenova/all-MiniLM-L6-v2",'
    '"dimension":0,"count":0,"vectors":"semantic-search-vectors.i8",'
    '"quantization":{"type":"int8","scale":127,"normalized":true},'
    '"scoreThreshold":0.25,'
    '"scoreThresholdCalibration":{"method":"shared-tag-proxy","status":"placeholder"},'
    '"papers":[]}'
)

TEXT_ASSETS = {
    "semantic-search-index.json": PLACEHOLDER_MANIFEST,
    "semantic-search-settings.json": (
        '{"model":"none","browserModel":"Xenova/all-MiniLM-L6-v2","count":0,'
        '"scoreThreshold":0.25,'
        '"scoreThresholdCalibration":{"method":"shared-tag-proxy","status":"placeholder"}}'
    ),
}

BINARY_ASSETS = {
    "semantic-search-vectors.i8": b"",
}


def read_json(path: Path) -> dict[str, object]:
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        raise RuntimeError(f"{path} is not valid JSON; run python semantic_search/generate_semantic_search_index.py") from exc
    if not isinstance(data, dict):
        raise RuntimeError(f"{path} must contain an object; run python semantic_search/generate_semantic_search_index.py")
    return data


def validate_semantic_assets() -> tuple[dict[str, str], dict[str, bytes]]:
    manifest_path = ASSET_DIR / "semantic-search-index.json"
    settings_path = ASSET_DIR / "semantic-search-settings.json"
    vector_candidates = [path for path in ASSET_DIR.glob("semantic-search-vectors*.i8") if path.is_file()]

    if not manifest_path.exists():
        if settings_path.exists() or any(path.stat().st_size for path in vector_candidates):
            raise RuntimeError(
                "Semantic Search assets are partial; run python semantic_search/generate_semantic_search_index.py"
            )
        return TEXT_ASSETS, BINARY_ASSETS

    manifest = read_json(manifest_path)
    papers = manifest.get("papers")
    if not isinstance(papers, list):
        raise RuntimeError(
            "semantic-search-index.json has no paper list; "
            "run python semantic_search/generate_semantic_search_index.py"
        )
    indexed_ids = [
        str(paper["id"])
        for paper in papers
        if isinstance(paper, dict) and isinstance(paper.get("id"), str)
    ]
    current_ids = [entry.id for entry in Catalog.from_metadata_root(METADATA_ROOT).entries]
    if indexed_ids != current_ids:
        missing = sorted(set(current_ids) - set(indexed_ids))
        extra = sorted(set(indexed_ids) - set(current_ids))
        detail = []
        if missing:
            detail.append(f"missing {len(missing)} current paper(s)")
        if extra:
            detail.append(f"contains {len(extra)} stale paper(s)")
        reason = f" ({', '.join(detail)})" if detail else ""
        raise RuntimeError(
            f"semantic-search-index.json is stale for current metadata{reason}; "
            "run python semantic_search/generate_semantic_search_index.py"
        )

    if not settings_path.exists():
        raise RuntimeError(f"Missing {settings_path}; run python semantic_search/generate_semantic_search_index.py")
    settings = read_json(settings_path)

    for key in ("model", "browserModel", "count", "scoreThreshold"):
        if settings.get(key) != manifest.get(key):
            raise RuntimeError(
                f"{settings_path} is stale for {key}; run python semantic_search/generate_semantic_search_index.py"
            )

    count = manifest.get("count")
    dimension = manifest.get("dimension")
    if not isinstance(count, int) or count < 0 or not isinstance(dimension, int) or dimension < 0:
        raise RuntimeError(
            "semantic-search-index.json has invalid count/dimension; "
            "run python semantic_search/generate_semantic_search_index.py"
        )

    quantization = manifest.get("quantization")
    if not isinstance(quantization, dict) or quantization.get("type") != "int8":
        raise RuntimeError(
            "semantic-search-index.json must point at int8 vectors; "
            "run python semantic_search/generate_semantic_search_index.py"
        )

    vector_name = manifest.get("vectors")
    if not isinstance(vector_name, str) or not vector_name or Path(vector_name).name != vector_name:
        raise RuntimeError("semantic-search-index.json has an invalid vectors filename")
    vector_path = ASSET_DIR / vector_name
    expected_bytes = count * dimension
    if expected_bytes and not vector_path.exists():
        raise RuntimeError(f"Missing {vector_path}; run python semantic_search/generate_semantic_search_index.py")
    if vector_path.exists() and vector_path.stat().st_size != expected_bytes:
        raise RuntimeError(
            f"{vector_path} is stale ({vector_path.stat().st_size} bytes, expected {expected_bytes}); "
            "run python semantic_search/generate_semantic_search_index.py"
        )

    return (
        {
            "semantic-search-index.json": manifest_path.read_text(encoding="utf-8"),
            "semantic-search-settings.json": settings_path.read_text(encoding="utf-8"),
        },
        {vector_name: vector_path.read_bytes() if vector_path.exists() else b""},
    )


text_assets, binary_assets = validate_semantic_assets()

for name, content in text_assets.items():
    with mkdocs_gen_files.open(f"javascripts/{name}", "w") as out:
        out.write(content)

for name, content in binary_assets.items():
    with mkdocs_gen_files.open(f"javascripts/{name}", "wb") as out:
        out.write(content)
