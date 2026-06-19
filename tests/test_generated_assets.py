from __future__ import annotations

from html.parser import HTMLParser
from pathlib import Path
import unittest

from knowledge_base.generated_assets import (
    MAP_DATA,
    MAP_PLACEHOLDER_PAYLOAD,
    MAP_SIMILARITY,
    SEMANTIC_SEARCH_INDEX,
    SEMANTIC_SEARCH_PLACEHOLDER_MANIFEST,
    SEMANTIC_SEARCH_PLACEHOLDER_SETTINGS,
    SEMANTIC_SEARCH_VECTORS,
    SITE_LINK_DATA,
)

DOCS_DIR = Path(__file__).resolve().parents[1] / "knowledge_base" / "docs"


class ScriptSrcParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.sources: list[str] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        if tag != "script":
            return
        values = dict(attrs)
        src = values.get("src")
        if src:
            self.sources.append(src)


def script_sources(path: Path) -> list[str]:
    parser = ScriptSrcParser()
    parser.feed(path.read_text(encoding="utf-8"))
    return parser.sources


class GeneratedAssetTests(unittest.TestCase):
    def test_js_asset_publishes_under_javascripts(self) -> None:
        self.assertEqual(SITE_LINK_DATA.published_path, "javascripts/site-link-data.js")

    def test_root_app_page_scripts_are_docs_relative(self) -> None:
        expected = {
            "search.md": {
                "javascripts/site-link-data.js",
                "javascripts/paper-link-pills.js",
                "javascripts/search-data.js",
                "javascripts/search.js",
            },
            "map.md": {
                "javascripts/vendor/graphology.umd.min.js",
                "javascripts/vendor/sigma.min.js",
                "javascripts/map-data.js",
                "javascripts/site-link-data.js",
                "javascripts/paper-link-pills.js",
                "javascripts/map.js",
            },
        }

        for page_name, expected_sources in expected.items():
            with self.subTest(page=page_name):
                local_sources = {
                    src
                    for src in script_sources(DOCS_DIR / page_name)
                    if src.startswith("javascripts/") or src.startswith("../javascripts/")
                }

                self.assertEqual(local_sources, expected_sources)

    def test_js_assignment_round_trips_payload(self) -> None:
        script = MAP_DATA.js_assignment({"nodes": []}, separators=(",", ":"))

        self.assertEqual(script, 'const mapData={"nodes":[]};\n')
        self.assertEqual(MAP_DATA.loads_js_assignment(script), {"nodes": []})

    def test_placeholder_sidecars_use_contract_names(self) -> None:
        self.assertEqual(MAP_PLACEHOLDER_PAYLOAD["similarity"]["file"], MAP_SIMILARITY.name)
        self.assertEqual(SEMANTIC_SEARCH_PLACEHOLDER_MANIFEST["vectors"], SEMANTIC_SEARCH_VECTORS.name)
        self.assertEqual(
            SEMANTIC_SEARCH_PLACEHOLDER_SETTINGS["browserModel"],
            SEMANTIC_SEARCH_PLACEHOLDER_MANIFEST["browserModel"],
        )

    def test_plain_json_asset_rejects_js_assignment(self) -> None:
        with self.assertRaises(ValueError):
            SEMANTIC_SEARCH_INDEX.js_assignment({})


if __name__ == "__main__":
    unittest.main()
