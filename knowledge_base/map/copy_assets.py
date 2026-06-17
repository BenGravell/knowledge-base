"""
MkDocs gen-files script: publish map JS assets into the served site.

Runs automatically during `mkdocs build` / `mkdocs serve` because it is
listed under ``gen-files.scripts`` in mkdocs.yml.

Copies files from ``map/`` into the virtual ``javascripts/`` path:

  map/map.js     → site/javascripts/map.js
  map/map-data.js→ site/javascripts/map-data.js
  map/map-similarity.i16 → site/javascripts/map-similarity.i16
  map/vendor/*        → site/javascripts/vendor/*

If ``map-data.js`` has not yet been generated (i.e. the user has not
run ``generate_map_data.py`` yet), a minimal placeholder is written so
that the page loads without a JS error and shows a helpful message instead.
"""

from __future__ import annotations

import json
from pathlib import Path

import mkdocs_gen_files

from knowledge_base.catalog import Catalog
from knowledge_base.generated_assets import MAP_DATA, MAP_PLACEHOLDER_PAYLOAD, MAP_SIMILARITY

MAP_DIR = Path(__file__).resolve().parent
KB_DIR = MAP_DIR.parent
METADATA_ROOT = KB_DIR / "docs" / "papers"

PLACEHOLDER_DATA = MAP_DATA.js_assignment(MAP_PLACEHOLDER_PAYLOAD, separators=(",", ":"))


def load_map_data(content: str) -> dict[str, object]:
    try:
        return MAP_DATA.loads_js_assignment(content)
    except json.JSONDecodeError as exc:
        raise RuntimeError("map/map-data.js is not valid JSON; run python map/generate_map_data.py") from exc
    except ValueError as exc:
        raise RuntimeError("map/map-data.js is malformed; run python map/generate_map_data.py") from exc


def validate_similarity_sidecar(map_data: dict[str, object]) -> tuple[str, Path]:
    similarity = map_data.get("similarity")
    if not isinstance(similarity, dict):
        raise RuntimeError("map/map-data.js has no similarity metadata; run python map/generate_map_data.py")

    file_name = similarity.get("file")
    if not isinstance(file_name, str) or not file_name or Path(file_name).name != file_name:
        raise RuntimeError("map/map-data.js has an invalid similarity sidecar name")
    if similarity.get("dtype") != "int16":
        raise RuntimeError("map/map-data.js similarity dtype must be int16; run python map/generate_map_data.py")

    shape = similarity.get("shape")
    if (
        not isinstance(shape, list)
        or len(shape) != 2
        or not all(isinstance(value, int) and value >= 0 for value in shape)
    ):
        raise RuntimeError("map/map-data.js has an invalid similarity shape; run python map/generate_map_data.py")

    expected_bytes = int(shape[0]) * int(shape[1]) * 2
    sidecar = MAP_DIR / file_name
    if expected_bytes and not sidecar.exists():
        raise RuntimeError(f"Missing {sidecar}; run python map/generate_map_data.py")
    if sidecar.exists() and sidecar.stat().st_size != expected_bytes:
        raise RuntimeError(
            f"{sidecar} is stale ({sidecar.stat().st_size} bytes, expected {expected_bytes}); "
            "run python map/generate_map_data.py"
        )
    return file_name, sidecar


def validate_current_papers(map_data: dict[str, object]) -> None:
    nodes = map_data.get("nodes")
    if not isinstance(nodes, list):
        raise RuntimeError("map/map-data.js has no node list; run python map/generate_map_data.py")
    node_ids = [
        str(node["data"]["id"])
        for node in nodes
        if isinstance(node, dict)
        and isinstance(node.get("data"), dict)
        and isinstance(node["data"].get("id"), str)
    ]
    current_ids = [entry.id for entry in Catalog.from_metadata_root(METADATA_ROOT).entries]
    if node_ids != current_ids:
        missing = sorted(set(current_ids) - set(node_ids))
        extra = sorted(set(node_ids) - set(current_ids))
        detail = []
        if missing:
            detail.append(f"missing {len(missing)} current paper(s)")
        if extra:
            detail.append(f"contains {len(extra)} stale paper(s)")
        reason = f" ({', '.join(detail)})" if detail else ""
        raise RuntimeError(f"map/map-data.js is stale for current metadata{reason}; run python map/generate_map_data.py")


map_data_src = MAP_DIR / MAP_DATA.name
map_data_content = PLACEHOLDER_DATA
similarity_name = MAP_SIMILARITY.name
similarity = MAP_DIR / similarity_name
if map_data_src.exists():
    map_data_content = map_data_src.read_text(encoding="utf-8")
    parsed_map_data = load_map_data(map_data_content)
    validate_current_papers(parsed_map_data)
    similarity_name, similarity = validate_similarity_sidecar(parsed_map_data)

text_assets = {
    "map.js": MAP_DIR / "map.js",
    MAP_DATA.name: map_data_content,
}

for fname, source in text_assets.items():
    if isinstance(source, Path):
        if not source.exists():
            continue
        content = source.read_text(encoding="utf-8")
    else:
        content = source

    with mkdocs_gen_files.open(f"javascripts/{fname}", "w") as out:
        out.write(content)

with mkdocs_gen_files.open(f"javascripts/{similarity_name}", "wb") as out:
    out.write(similarity.read_bytes() if similarity.exists() else b"")

VENDOR_DIR = MAP_DIR / "vendor"
if VENDOR_DIR.exists():
    for src in sorted(VENDOR_DIR.iterdir()):
        if not src.is_file():
            continue
        with mkdocs_gen_files.open(f"javascripts/vendor/{src.name}", "w") as out:
            out.write(src.read_text(encoding="utf-8"))
