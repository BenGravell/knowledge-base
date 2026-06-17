"""Contract for generated static-site assets."""

from __future__ import annotations

import json
import re
from dataclasses import dataclass
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
