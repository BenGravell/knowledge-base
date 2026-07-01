"""Contract for generated static-site assets."""

from __future__ import annotations

import json
import posixpath
import re
from dataclasses import dataclass
from pathlib import Path, PurePosixPath
from typing import Any


@dataclass(frozen=True)
class GeneratedAsset:
    name: str
    directory: str = "javascripts"

    @property
    def published_path(self) -> str:
        return f"{self.directory}/{self.name}" if self.directory else self.name


@dataclass(frozen=True)
class JsonAsset:
    name: str
    global_name: str | None = None
    assignment_prefix: str | None = None
    directory: str = "javascripts"

    @property
    def published_path(self) -> str:
        return f"{self.directory}/{self.name}" if self.directory else self.name

    def dumps(
        self,
        payload: Any,
        *,
        indent: int | None = None,
        separators: tuple[str, str] | None = None,
        ensure_ascii: bool = False,
    ) -> str:
        return json.dumps(payload, indent=indent, separators=separators, ensure_ascii=ensure_ascii)

    def js_assignment(
        self,
        payload: Any,
        *,
        indent: int | None = None,
        separators: tuple[str, str] | None = None,
        ensure_ascii: bool = False,
    ) -> str:
        if self.assignment_prefix is None:
            raise ValueError(f"{self.name} has no JavaScript assignment prefix")
        return f"{self.assignment_prefix}{self.dumps(payload, indent=indent, separators=separators, ensure_ascii=ensure_ascii)};\n"

    def loads_js_assignment(self, content: str) -> dict[str, Any]:
        if self.global_name is None:
            raise ValueError(f"{self.name} has no JavaScript global")
        variable = re.escape(self.global_name)
        match = re.match(
            rf"^\s*(?:const\s+{variable}\s*=\s*|window\.{variable}\s*=\s*)(?P<json>.*);\s*$",
            content,
            re.S,
        )
        if not match:
            raise ValueError(f"{self.name} must assign {self.global_name}")
        data = json.loads(match.group("json"))
        if not isinstance(data, dict):
            raise ValueError(f"{self.name} must contain a JSON object")
        return data


@dataclass(frozen=True)
class AppScriptBundle:
    name: str
    assets: tuple[GeneratedAsset | JsonAsset, ...]


@dataclass(frozen=True)
class SidecarCheck:
    name: str
    path: Path
    expected_bytes: int


@dataclass(frozen=True)
class MapDataContract:
    node_ids: list[str]
    similarity_ids: list[str]
    similarity_sidecar: SidecarCheck


@dataclass(frozen=True)
class SemanticSearchContract:
    paper_ids: list[str]
    vector_sidecar: SidecarCheck


SITE_LINK_DATA = JsonAsset(
    "site-link-data.js",
    global_name="kbSiteLinkData",
    assignment_prefix="window.kbSiteLinkData = ",
)
SEARCH_DATA = JsonAsset(
    "search-data.js",
    global_name="tagSearchData",
    assignment_prefix="window.tagSearchData = ",
)
TAG_SEARCH_DATA = JsonAsset(
    "tag-search-data.js",
    global_name="tagSearchData",
    assignment_prefix="window.tagSearchData = ",
)
MAP_DATA = JsonAsset(
    "map-data.js",
    global_name="mapData",
    assignment_prefix="const mapData=",
)
TREE_DATA = JsonAsset(
    "tree-data.js",
    global_name="treeData",
    assignment_prefix="window.treeData = ",
)
ANALYTICS_DATA = JsonAsset(
    "analytics-data.js",
    global_name="analyticsData",
    assignment_prefix="window.analyticsData = ",
)
TIMELINE_DATA = JsonAsset(
    "timeline-data.js",
    global_name="timelineData",
    assignment_prefix="window.timelineData = ",
)

MAP_SIMILARITY = GeneratedAsset("map-similarity.i16")
SEMANTIC_SEARCH_INDEX = JsonAsset("semantic-search-index.json")
SEMANTIC_SEARCH_SETTINGS = JsonAsset("semantic-search-settings.json")
SEMANTIC_SEARCH_VECTORS = GeneratedAsset("semantic-search-vectors.i8")

ANALYTICS_SCRIPT = GeneratedAsset("analytics.js")
GRAPHOLOGY_VENDOR_SCRIPT = GeneratedAsset("graphology.umd.min.js", "javascripts/vendor")
HEADER_LINK_SCRIPT = GeneratedAsset("header-link.js")
HOME_BENTO_SCRIPT = GeneratedAsset("home-bento.js")
BROWSER_MAP_MODEL_SCRIPT = GeneratedAsset("browser-map-model.js")
MAP_BRANCH_FILTER_SCRIPT = GeneratedAsset("map-branch-filter.js")
MAP_CAMERA_SCRIPT = GeneratedAsset("map-camera.js")
MATH_FIT_SCRIPT = GeneratedAsset("math-fit.js")
MATHJAX_CONFIG_SCRIPT = GeneratedAsset("mathjax.js")
MAP_OVERLAYS_SCRIPT = GeneratedAsset("map-overlays.js")
MAP_PAPER_DERIVATIONS_SCRIPT = GeneratedAsset("map-paper-derivations.js")
MAP_RELEVANCE_FILTER_SCRIPT = GeneratedAsset("map-relevance-filter.js")
MAP_RENDERING_SCRIPT = GeneratedAsset("map-rendering.js")
MAP_VIEW_STATE_SCRIPT = GeneratedAsset("map-view-state.js")
MAP_SCRIPT = GeneratedAsset("map.js")
NAV_DRAWER_STATE_SCRIPT = GeneratedAsset("nav-drawer-state.js")
PAPER_LINK_PILLS_SCRIPT = GeneratedAsset("paper-link-pills.js")
SEARCH_SCRIPT = GeneratedAsset("search.js")
SEMANTIC_SEARCH_WORKER_SCRIPT = GeneratedAsset("semantic-search-worker.js")
SIGMA_VENDOR_SCRIPT = GeneratedAsset("sigma.min.js", "javascripts/vendor")
TIMELINE_SCRIPT = GeneratedAsset("timeline.js")
TREE_NAVIGATOR_SCRIPT = GeneratedAsset("tree-navigator.js")
TREE_SCRIPT = GeneratedAsset("tree.js")

HOME_APP_SCRIPTS = AppScriptBundle(
    "home",
    (ANALYTICS_DATA, HOME_BENTO_SCRIPT, ANALYTICS_SCRIPT),
)
MAP_APP_SCRIPTS = AppScriptBundle(
    "map",
    (
        GRAPHOLOGY_VENDOR_SCRIPT,
        SIGMA_VENDOR_SCRIPT,
        MAP_DATA,
        SITE_LINK_DATA,
        PAPER_LINK_PILLS_SCRIPT,
        TREE_NAVIGATOR_SCRIPT,
        MAP_PAPER_DERIVATIONS_SCRIPT,
        BROWSER_MAP_MODEL_SCRIPT,
        MAP_VIEW_STATE_SCRIPT,
        MAP_RENDERING_SCRIPT,
        MAP_RELEVANCE_FILTER_SCRIPT,
        MAP_OVERLAYS_SCRIPT,
        MAP_CAMERA_SCRIPT,
        MAP_BRANCH_FILTER_SCRIPT,
        MAP_SCRIPT,
    ),
)
SEARCH_APP_SCRIPTS = AppScriptBundle(
    "search",
    (SITE_LINK_DATA, PAPER_LINK_PILLS_SCRIPT, SEARCH_DATA, SEARCH_SCRIPT),
)
TREE_APP_SCRIPTS = AppScriptBundle(
    "tree",
    (SITE_LINK_DATA, PAPER_LINK_PILLS_SCRIPT, TREE_DATA, TREE_NAVIGATOR_SCRIPT, TREE_SCRIPT),
)
TIMELINE_APP_SCRIPTS = AppScriptBundle(
    "timeline",
    (SITE_LINK_DATA, PAPER_LINK_PILLS_SCRIPT, TIMELINE_DATA, TIMELINE_SCRIPT),
)
ANALYTICS_APP_SCRIPTS = AppScriptBundle(
    "analytics",
    (ANALYTICS_DATA, ANALYTICS_SCRIPT),
)

APP_SCRIPT_BUNDLES = {
    bundle.name: bundle
    for bundle in (
        HOME_APP_SCRIPTS,
        MAP_APP_SCRIPTS,
        SEARCH_APP_SCRIPTS,
        TREE_APP_SCRIPTS,
        TIMELINE_APP_SCRIPTS,
        ANALYTICS_APP_SCRIPTS,
    )
}
APP_SCRIPT_PAGES = {
    "index.md": HOME_APP_SCRIPTS,
    "map.md": MAP_APP_SCRIPTS,
    "search.md": SEARCH_APP_SCRIPTS,
    "tree.md": TREE_APP_SCRIPTS,
    "timeline.md": TIMELINE_APP_SCRIPTS,
}
APP_SCRIPT_BLOCK_RE = re.compile(
    r"<!--\s*kb:app-scripts\s+(?P<bundle>[a-z0-9_-]+)\s*-->" r".*?" r"<!--\s*/kb:app-scripts\s*-->",
    re.S,
)

SEMANTIC_BROWSER_MODEL = "Xenova/all-MiniLM-L6-v2"
SEMANTIC_SCORE_THRESHOLD = 0.25

MAP_PLACEHOLDER_PAYLOAD: dict[str, Any] = {
    "nodes": [],
    "similarity": {
        "scale": 1,
        "ids": [],
        "file": MAP_SIMILARITY.name,
        "dtype": "int16",
        "shape": [0, 0],
    },
    "meta": {"model": "none", "total_papers": 0},
}

SEMANTIC_SEARCH_PLACEHOLDER_MANIFEST: dict[str, Any] = {
    "model": "none",
    "browserModel": SEMANTIC_BROWSER_MODEL,
    "dimension": 0,
    "count": 0,
    "vectors": SEMANTIC_SEARCH_VECTORS.name,
    "quantization": {"type": "int8", "scale": 127, "normalized": True},
    "scoreThreshold": SEMANTIC_SCORE_THRESHOLD,
    "scoreThresholdCalibration": {"method": "shared-tag-proxy", "status": "placeholder"},
    "papers": [],
}

SEMANTIC_SEARCH_PLACEHOLDER_SETTINGS: dict[str, Any] = {
    "model": SEMANTIC_SEARCH_PLACEHOLDER_MANIFEST["model"],
    "browserModel": SEMANTIC_SEARCH_PLACEHOLDER_MANIFEST["browserModel"],
    "count": SEMANTIC_SEARCH_PLACEHOLDER_MANIFEST["count"],
    "scoreThreshold": SEMANTIC_SEARCH_PLACEHOLDER_MANIFEST["scoreThreshold"],
    "scoreThresholdCalibration": SEMANTIC_SEARCH_PLACEHOLDER_MANIFEST["scoreThresholdCalibration"],
}


def id_set_difference_message(
    label: str, actual_ids: set[str], expected_ids: set[str], *, report_stale: bool
) -> str | None:
    messages = id_set_difference_messages(label, actual_ids, expected_ids, report_stale=report_stale)
    return messages[0] if messages else None


def id_set_difference_messages(
    label: str,
    actual_ids: set[str],
    expected_ids: set[str],
    *,
    report_stale: bool,
) -> list[str]:
    messages: list[str] = []
    missing = expected_ids - actual_ids
    if missing:
        messages.append(f"{label} missing {len(missing)} metadata-backed paper ID(s): {format_id_examples(missing)}")
    stale = actual_ids - expected_ids
    if report_stale and stale:
        messages.append(
            f"{label} contains {len(stale)} stale paper ID(s) with no metadata.yml: {format_id_examples(stale)}"
        )
    return messages


def current_ids_error(label: str, actual_ids: list[str], current_ids: list[str]) -> str | None:
    if actual_ids == current_ids:
        return None
    missing = sorted(set(current_ids) - set(actual_ids))
    extra = sorted(set(actual_ids) - set(current_ids))
    detail = []
    if missing:
        detail.append(f"missing {len(missing)} current paper(s)")
    if extra:
        detail.append(f"contains {len(extra)} stale paper(s)")
    reason = f" ({', '.join(detail)})" if detail else ""
    return f"{label} is stale for current metadata{reason}"


def format_id_examples(ids: set[str] | list[str], limit: int = 8) -> str:
    ordered = sorted(ids)
    examples = ", ".join(ordered[:limit])
    if len(ordered) > limit:
        examples += f", ... ({len(ordered)} total)"
    return examples


def duplicate_values(values: list[str]) -> set[str]:
    seen: set[str] = set()
    dupes: set[str] = set()
    for value in values:
        if value in seen:
            dupes.add(value)
        seen.add(value)
    return dupes


def load_json_object(path: Path, *, run_hint: str | None = None) -> dict[str, object]:
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        suffix = f"; run {run_hint}" if run_hint else ""
        raise RuntimeError(f"{path} is not valid JSON{suffix}") from exc
    if not isinstance(data, dict):
        suffix = f"; run {run_hint}" if run_hint else ""
        raise RuntimeError(f"{path} must contain an object{suffix}")
    return data


def map_node_ids(map_data: dict[str, object]) -> tuple[list[str], int]:
    nodes = map_data.get("nodes")
    if not isinstance(nodes, list):
        raise ValueError("mapData.nodes is not a list")
    node_ids: list[str] = []
    bad_nodes = 0
    for node in nodes:
        data = node.get("data") if isinstance(node, dict) else None
        node_id = data.get("id") if isinstance(data, dict) else None
        if isinstance(node_id, str) and node_id:
            node_ids.append(node_id)
        else:
            bad_nodes += 1
    return node_ids, bad_nodes


def map_similarity_ids(map_data: dict[str, object]) -> list[str]:
    similarity = map_data.get("similarity")
    if not isinstance(similarity, dict):
        raise ValueError("mapData.similarity is not an object")
    similarity_ids = similarity.get("ids")
    if not isinstance(similarity_ids, list) or not all(isinstance(item, str) for item in similarity_ids):
        raise ValueError("mapData.similarity.ids is not a string list")
    return similarity_ids


def map_similarity_sidecar(
    map_data: dict[str, object],
    *,
    generated_dir: Path,
    expected_size: int | None = None,
) -> SidecarCheck:
    similarity = map_data.get("similarity")
    if not isinstance(similarity, dict):
        raise ValueError("mapData.similarity is not an object")

    file_name = similarity.get("file")
    shape = similarity.get("shape")
    if not isinstance(file_name, str) or not file_name or Path(file_name).name != file_name:
        raise ValueError("mapData.similarity has an invalid sidecar name")
    if similarity.get("dtype") != "int16":
        raise ValueError("mapData.similarity dtype must be int16")
    if (
        not isinstance(shape, list)
        or len(shape) != 2
        or not all(isinstance(value, int) and value >= 0 for value in shape)
    ):
        raise ValueError("mapData.similarity has an invalid sidecar shape")
    if expected_size is not None and shape != [expected_size, expected_size]:
        raise ValueError("mapData.similarity sidecar shape does not match similarity.ids")
    return SidecarCheck(file_name, generated_dir / file_name, int(shape[0]) * int(shape[1]) * 2)


def validate_sidecar_file(sidecar: SidecarCheck) -> str | None:
    if sidecar.expected_bytes and not sidecar.path.exists():
        return f"Missing {sidecar.path}"
    if sidecar.path.exists() and sidecar.path.stat().st_size != sidecar.expected_bytes:
        return f"{sidecar.path} is stale ({sidecar.path.stat().st_size} bytes, expected {sidecar.expected_bytes})"
    return None


def validate_map_data_contract(
    map_data: dict[str, object],
    *,
    generated_dir: Path,
    current_ids: list[str] | None = None,
) -> MapDataContract:
    node_ids, bad_nodes = map_node_ids(map_data)
    if bad_nodes:
        raise ValueError(f"mapData.nodes has {bad_nodes} node(s) without data.id")
    if duplicate_ids := duplicate_values(node_ids):
        raise ValueError(f"mapData.nodes has duplicate paper ID(s): {format_id_examples(duplicate_ids)}")
    if current_ids is not None and (error := current_ids_error("map-data.js", node_ids, current_ids)):
        raise ValueError(error)

    similarity_ids = map_similarity_ids(map_data)
    if duplicate_ids := duplicate_values(similarity_ids):
        raise ValueError(f"mapData.similarity.ids has duplicate paper ID(s): {format_id_examples(duplicate_ids)}")
    if similarity_ids != node_ids:
        raise ValueError("mapData.similarity.ids does not exactly match mapData.nodes order")

    sidecar = map_similarity_sidecar(map_data, generated_dir=generated_dir, expected_size=len(similarity_ids))
    if error := validate_sidecar_file(sidecar):
        raise ValueError(error)
    return MapDataContract(node_ids, similarity_ids, sidecar)


def semantic_paper_ids(manifest: dict[str, object]) -> tuple[list[str], int]:
    papers = manifest.get("papers")
    if not isinstance(papers, list):
        raise ValueError("semantic-search-index.json papers field is not a list")
    ids: list[str] = []
    bad_papers = 0
    for paper in papers:
        paper_id = paper.get("id") if isinstance(paper, dict) else None
        if isinstance(paper_id, str) and paper_id:
            ids.append(paper_id)
        else:
            bad_papers += 1
    return ids, bad_papers


def semantic_vector_sidecar(manifest: dict[str, object], *, asset_dir: Path) -> SidecarCheck:
    count = manifest.get("count")
    dimension = manifest.get("dimension")
    if not isinstance(count, int) or count < 0 or not isinstance(dimension, int) or dimension < 0:
        raise ValueError("semantic-search-index.json has invalid count/dimension")
    quantization = manifest.get("quantization")
    if not isinstance(quantization, dict) or quantization.get("type") != "int8":
        raise ValueError("semantic-search-index.json quantization.type is not int8")
    vector_name = manifest.get("vectors")
    if not isinstance(vector_name, str) or not vector_name or Path(vector_name).name != vector_name:
        raise ValueError("semantic-search-index.json vectors field is invalid")
    return SidecarCheck(vector_name, asset_dir / vector_name, count * dimension)


def semantic_settings_errors(manifest: dict[str, object], settings: dict[str, object]) -> list[str]:
    return [
        f"semantic-search-settings.json {key} does not match semantic-search-index.json"
        for key in ("model", "browserModel", "count", "scoreThreshold")
        if settings.get(key) != manifest.get(key)
    ]


def validate_semantic_search_contract(
    manifest: dict[str, object],
    settings: dict[str, object],
    *,
    asset_dir: Path,
    current_ids: list[str] | None = None,
) -> SemanticSearchContract:
    paper_ids, bad_papers = semantic_paper_ids(manifest)
    if bad_papers:
        raise ValueError(f"semantic-search-index.json has {bad_papers} paper(s) without id")
    if duplicate_ids := duplicate_values(paper_ids):
        raise ValueError(f"semantic-search-index.json has duplicate paper ID(s): {format_id_examples(duplicate_ids)}")
    if current_ids is not None and (error := current_ids_error("semantic-search-index.json", paper_ids, current_ids)):
        raise ValueError(error)

    count = manifest.get("count")
    if count != len(paper_ids):
        raise ValueError(f"semantic-search-index.json count is {count}; expected {len(paper_ids)}")
    if errors := semantic_settings_errors(manifest, settings):
        raise ValueError(errors[0])

    vector = semantic_vector_sidecar(manifest, asset_dir=asset_dir)
    if error := validate_sidecar_file(vector):
        raise ValueError(error)
    return SemanticSearchContract(paper_ids, vector)


def page_relative_asset_path(page_source: str | PurePosixPath, asset: GeneratedAsset | JsonAsset) -> str:
    source = PurePosixPath(str(page_source).replace("\\", "/"))
    source_parent = source.parent.as_posix()
    start = "." if source_parent == "." else source_parent
    return posixpath.relpath(asset.published_path, start)


def app_script_bundle(bundle: str | AppScriptBundle) -> AppScriptBundle:
    if isinstance(bundle, AppScriptBundle):
        return bundle
    try:
        return APP_SCRIPT_BUNDLES[bundle]
    except KeyError as exc:
        raise ValueError(f"Unknown app script bundle: {bundle}") from exc


def render_app_script_tags(page_source: str | PurePosixPath, bundle: str | AppScriptBundle) -> str:
    scripts = app_script_bundle(bundle).assets
    return "\n".join(f'<script src="{page_relative_asset_path(page_source, asset)}"></script>' for asset in scripts)


def render_app_script_blocks(markdown: str, page_source: str | PurePosixPath) -> str:
    def replace(match: re.Match[str]) -> str:
        bundle = app_script_bundle(match.group("bundle"))
        return (
            f"<!-- kb:app-scripts {bundle.name} -->\n"
            f"{render_app_script_tags(page_source, bundle)}\n"
            "<!-- /kb:app-scripts -->"
        )

    return APP_SCRIPT_BLOCK_RE.sub(replace, markdown)
