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
from knowledge_base.components.map.pipeline.settings import BROWSER_DIR, GENERATED_DIR, METADATA_ROOT, VENDOR_DIR
from knowledge_base.publishing.generated_assets import (
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
    validate_map_data_contract,
)
from knowledge_base.publishing.generated_files import open_generated

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


def validate_generated_map_data(map_data: dict[str, object]) -> tuple[str, Path]:
    current_ids = [entry.id for entry in Catalog.from_metadata_root(METADATA_ROOT).entries]
    try:
        contract = validate_map_data_contract(map_data, generated_dir=GENERATED_DIR, current_ids=current_ids)
    except ValueError as exc:
        raise RuntimeError(f"{exc}; run {RUN_GENERATE_MAP_DATA}") from exc
    return contract.similarity_sidecar.name, contract.similarity_sidecar.path


map_data_src = GENERATED_DIR / MAP_DATA.name
map_data_content = PLACEHOLDER_DATA
similarity_name = MAP_SIMILARITY.name
similarity = GENERATED_DIR / similarity_name
if map_data_src.exists():
    map_data_content = map_data_src.read_text(encoding="utf-8")
    parsed_map_data = load_map_data(map_data_content)
    similarity_name, similarity = validate_generated_map_data(parsed_map_data)

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

if VENDOR_DIR.exists():
    for src in sorted(VENDOR_DIR.iterdir()):
        if not src.is_file():
            continue
        with open_generated(f"javascripts/vendor/{src.name}", "w") as out:
            out.write(src.read_text(encoding="utf-8"))
