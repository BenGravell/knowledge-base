"""
Generated-file script: publish Map assets into the served site.

Runs before `zensical build` / `zensical serve` through the `kb` command.

Copies source files from ``components/map/browser/`` and generated data from
``components/map/generated/`` into the virtual ``javascripts/`` path:

  components/map/browser/paper-derivations.js -> site/javascripts/map-paper-derivations.js
  components/map/browser/model.js             -> site/javascripts/browser-map-model.js
  components/map/browser/view-state.js        -> site/javascripts/map-view-state.js
  components/map/browser/rendering.js         -> site/javascripts/map-rendering.js
  components/map/browser/relevance-filter.js  -> site/javascripts/map-relevance-filter.js
  components/map/browser/overlays.js          -> site/javascripts/map-overlays.js
  components/map/browser/camera.js            -> site/javascripts/map-camera.js
  components/map/browser/branch-filter.js     -> site/javascripts/map-branch-filter.js
  components/map/browser/app.js               -> site/javascripts/map.js
  components/map/generated/map-data.js        -> site/javascripts/map-data.js
  components/map/generated/map-similarity.i16 -> site/javascripts/map-similarity.i16
  components/map/vendor/*                     -> site/javascripts/vendor/*

If ``map-data.js`` has not yet been generated (i.e. the user has not
run ``generate_map_data.py`` yet), a minimal placeholder is written so
that the page loads without a JS error and shows a helpful message instead.
"""

from __future__ import annotations

import json
from pathlib import Path

from knowledge_base.catalog import Catalog
from knowledge_base.generated_assets import (
    BROWSER_MAP_MODEL_SCRIPT,
    MAP_BRANCH_FILTER_SCRIPT,
    MAP_CAMERA_SCRIPT,
    MAP_DATA,
    MAP_OVERLAYS_SCRIPT,
    MAP_PAPER_DERIVATIONS_SCRIPT,
    MAP_PLACEHOLDER_PAYLOAD,
    MAP_RELEVANCE_FILTER_SCRIPT,
    MAP_RENDERING_SCRIPT,
    MAP_SCRIPT,
    MAP_SIMILARITY,
    MAP_VIEW_STATE_SCRIPT,
)
from knowledge_base.generated_files import open_generated

MAP_DIR = Path(__file__).resolve().parents[1]
BROWSER_DIR = MAP_DIR / "browser"
GENERATED_DIR = MAP_DIR / "generated"
KB_DIR = MAP_DIR.parents[1]
METADATA_ROOT = KB_DIR / "docs" / "papers"
RUN_GENERATE_MAP_DATA = "python knowledge_base/components/map/generate_map_data.py"

PLACEHOLDER_DATA = MAP_DATA.js_assignment(MAP_PLACEHOLDER_PAYLOAD, separators=(",", ":"))


def load_map_data(content: str) -> dict[str, object]:
    try:
        return MAP_DATA.loads_js_assignment(content)
    except json.JSONDecodeError as exc:
        raise RuntimeError(
            f"components/map/generated/map-data.js is not valid JSON; run {RUN_GENERATE_MAP_DATA}"
        ) from exc
    except ValueError as exc:
        raise RuntimeError(f"components/map/generated/map-data.js is malformed; run {RUN_GENERATE_MAP_DATA}") from exc


def validate_similarity_sidecar(map_data: dict[str, object]) -> tuple[str, Path]:
    similarity = map_data.get("similarity")
    if not isinstance(similarity, dict):
        raise RuntimeError(
            f"components/map/generated/map-data.js has no similarity metadata; run {RUN_GENERATE_MAP_DATA}"
        )

    file_name = similarity.get("file")
    if not isinstance(file_name, str) or not file_name or Path(file_name).name != file_name:
        raise RuntimeError("components/map/generated/map-data.js has an invalid similarity sidecar name")
    if similarity.get("dtype") != "int16":
        raise RuntimeError(
            f"components/map/generated/map-data.js similarity dtype must be int16; run {RUN_GENERATE_MAP_DATA}"
        )

    shape = similarity.get("shape")
    if (
        not isinstance(shape, list)
        or len(shape) != 2
        or not all(isinstance(value, int) and value >= 0 for value in shape)
    ):
        raise RuntimeError(
            f"components/map/generated/map-data.js has an invalid similarity shape; run {RUN_GENERATE_MAP_DATA}"
        )

    expected_bytes = int(shape[0]) * int(shape[1]) * 2
    sidecar = GENERATED_DIR / file_name
    if expected_bytes and not sidecar.exists():
        raise RuntimeError(f"Missing {sidecar}; run {RUN_GENERATE_MAP_DATA}")
    if sidecar.exists() and sidecar.stat().st_size != expected_bytes:
        raise RuntimeError(
            f"{sidecar} is stale ({sidecar.stat().st_size} bytes, expected {expected_bytes}); "
            f"run {RUN_GENERATE_MAP_DATA}"
        )
    return file_name, sidecar


def validate_current_papers(map_data: dict[str, object]) -> None:
    nodes = map_data.get("nodes")
    if not isinstance(nodes, list):
        raise RuntimeError(f"components/map/generated/map-data.js has no node list; run {RUN_GENERATE_MAP_DATA}")
    node_ids = [
        str(node["data"]["id"])
        for node in nodes
        if isinstance(node, dict) and isinstance(node.get("data"), dict) and isinstance(node["data"].get("id"), str)
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
        raise RuntimeError(
            f"components/map/generated/map-data.js is stale for current metadata{reason}; run {RUN_GENERATE_MAP_DATA}"
        )


map_data_src = GENERATED_DIR / MAP_DATA.name
map_data_content = PLACEHOLDER_DATA
similarity_name = MAP_SIMILARITY.name
similarity = GENERATED_DIR / similarity_name
if map_data_src.exists():
    map_data_content = map_data_src.read_text(encoding="utf-8")
    parsed_map_data = load_map_data(map_data_content)
    validate_current_papers(parsed_map_data)
    similarity_name, similarity = validate_similarity_sidecar(parsed_map_data)

text_assets = {
    MAP_PAPER_DERIVATIONS_SCRIPT.name: BROWSER_DIR / "paper-derivations.js",
    BROWSER_MAP_MODEL_SCRIPT.name: BROWSER_DIR / "model.js",
    MAP_VIEW_STATE_SCRIPT.name: BROWSER_DIR / "view-state.js",
    MAP_RENDERING_SCRIPT.name: BROWSER_DIR / "rendering.js",
    MAP_RELEVANCE_FILTER_SCRIPT.name: BROWSER_DIR / "relevance-filter.js",
    MAP_OVERLAYS_SCRIPT.name: BROWSER_DIR / "overlays.js",
    MAP_CAMERA_SCRIPT.name: BROWSER_DIR / "camera.js",
    MAP_BRANCH_FILTER_SCRIPT.name: BROWSER_DIR / "branch-filter.js",
    MAP_SCRIPT.name: BROWSER_DIR / "app.js",
    MAP_DATA.name: map_data_content,
}

for fname, source in text_assets.items():
    if isinstance(source, Path):
        if not source.exists():
            continue
        content = source.read_text(encoding="utf-8")
    else:
        content = source

    with open_generated(f"javascripts/{fname}", "w") as out:
        out.write(content)

with open_generated(f"javascripts/{similarity_name}", "wb") as out:
    out.write(similarity.read_bytes() if similarity.exists() else b"")

VENDOR_DIR = MAP_DIR / "vendor"
if VENDOR_DIR.exists():
    for src in sorted(VENDOR_DIR.iterdir()):
        if not src.is_file():
            continue
        with open_generated(f"javascripts/vendor/{src.name}", "w") as out:
            out.write(src.read_text(encoding="utf-8"))
