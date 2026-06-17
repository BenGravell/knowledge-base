from __future__ import annotations

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


class GeneratedAssetTests(unittest.TestCase):
    def test_js_asset_publishes_under_javascripts(self) -> None:
        self.assertEqual(SITE_LINK_DATA.published_path, "javascripts/site-link-data.js")

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
