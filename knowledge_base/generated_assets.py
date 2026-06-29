"""Contract for generated static-site assets."""

from __future__ import annotations

import json
import posixpath
import re
from dataclasses import dataclass
from pathlib import PurePosixPath
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
    "tree/index.md": TREE_APP_SCRIPTS,
    "timeline.md": TIMELINE_APP_SCRIPTS,
}
APP_SCRIPT_BLOCK_RE = re.compile(
    r"<!--\s*kb:app-scripts\s+(?P<bundle>[a-z0-9_-]+)\s*-->"
    r".*?"
    r"<!--\s*/kb:app-scripts\s*-->",
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
