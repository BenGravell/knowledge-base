from __future__ import annotations

import os
import unittest
from html.parser import HTMLParser
from pathlib import Path
from typing import override
from unittest.mock import patch
from urllib.parse import ParseResult, unquote, urljoin, urlparse

from knowledge_base.dev_cli import SOURCE_DOCS_DIR, copy_docs_ignore
from knowledge_base.generated_assets import (
    APP_SCRIPT_PAGES,
    MAP_DATA,
    MAP_PLACEHOLDER_PAYLOAD,
    MAP_SIMILARITY,
    SEMANTIC_SEARCH_INDEX,
    SEMANTIC_SEARCH_PLACEHOLDER_MANIFEST,
    SEMANTIC_SEARCH_PLACEHOLDER_SETTINGS,
    SEMANTIC_SEARCH_VECTORS,
    SITE_LINK_DATA,
    page_relative_asset_path,
    render_app_script_blocks,
    render_app_script_tags,
)
from knowledge_base.utils.site_links import (
    paper_site_source_url,
    paper_site_url,
    source_relative_url,
)

DOCS_DIR = Path(__file__).resolve().parents[1] / "knowledge_base" / "docs"
REPO_ROOT = Path(__file__).resolve().parents[1]
COMPONENTS_DIR = REPO_ROOT / "knowledge_base" / "components"
SITE_DIR = REPO_ROOT / "knowledge_base" / "site"
SITE_URL = "https://bengravell.github.io/knowledge-base/"
SITE_PREFIX = "/knowledge-base/"
LOCAL_REF_ATTRS = {
    "a": ("href",),
    "link": ("href",),
    "script": ("src",),
    "img": ("src",),
    "source": ("src", "srcset"),
}
SKIPPED_REF_SCHEMES = {"http", "https", "mailto", "tel", "data", "javascript"}


class ScriptSrcParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.sources: list[str] = []

    @override
    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        if tag != "script":
            return
        values = dict(attrs)
        src = values.get("src")
        if src:
            self.sources.append(src)


class LocalRefParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.refs: list[tuple[str, str, str]] = []

    @override
    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        values = dict(attrs)
        for attr in LOCAL_REF_ATTRS.get(tag, ()):
            value = values.get(attr)
            if value:
                self.refs.append((tag, attr, value))


class ElementByIdParser(HTMLParser):
    def __init__(self, target_id: str) -> None:
        super().__init__()
        self.target_id = target_id
        self.attrs: dict[str, str | None] | None = None

    @override
    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        values = dict(attrs)
        if values.get("id") == self.target_id:
            self.attrs = values


def script_sources_from_text(text: str) -> list[str]:
    parser = ScriptSrcParser()
    parser.feed(text)
    return parser.sources


def script_sources(path: Path) -> list[str]:
    return script_sources_from_text(path.read_text(encoding="utf-8"))


def output_url_for_source(source_path: str) -> str:
    path = source_path.removesuffix(".md")
    if path.endswith("/index"):
        path = path.removesuffix("/index")
    return urljoin(SITE_URL, f"{path.strip('/')}/" if path.strip("/") else "")


def built_page_url(path: Path) -> str:
    rel = path.relative_to(SITE_DIR).as_posix()
    if rel == "index.html":
        return SITE_URL
    if rel.endswith("/index.html"):
        return urljoin(SITE_URL, rel[: -len("index.html")])
    return urljoin(SITE_URL, rel)


def built_local_target_exists(parsed_url: ParseResult) -> bool:
    rel = unquote(parsed_url.path.removeprefix(SITE_PREFIX))
    if not rel:
        return (SITE_DIR / "index.html").exists()
    target = SITE_DIR / rel
    return target.is_file() or (target / "index.html").is_file()


def expanded_refs(attr: str, value: str) -> list[str]:
    if attr != "srcset":
        return [value]
    return [part.strip().split()[0] for part in value.split(",") if part.strip()]


def attrs_for_html_fragment_by_id(fragment: str, target_id: str) -> dict[str, str | None]:
    parser = ElementByIdParser(target_id)
    parser.feed(fragment)
    if parser.attrs is None:
        raise AssertionError(f"{target_id} not found in HTML fragment")
    return parser.attrs


def search_page_input_attrs() -> dict[str, str | None]:
    source = (COMPONENTS_DIR / "search" / "browser" / "search-page.js").read_text(encoding="utf-8")
    start = source.index('<input id="unified-search-input"')
    return attrs_for_html_fragment_by_id(source[start : source.index(">", start) + 1], "unified-search-input")


class GeneratedAssetTests(unittest.TestCase):
    def test_js_asset_publishes_under_javascripts(self) -> None:
        self.assertEqual(SITE_LINK_DATA.published_path, "javascripts/site-link-data.js")

    def test_app_script_blocks_render_from_single_asset_contract(self) -> None:
        for page_name, bundle_name in APP_SCRIPT_PAGES.items():
            page_path = DOCS_DIR / page_name
            if not page_path.exists():
                continue

            with self.subTest(page=page_name):
                source = page_path.read_text(encoding="utf-8")
                rendered = render_app_script_blocks(source, page_name)
                expected_sources = [page_relative_asset_path(page_name, asset) for asset in bundle_name.assets]

                self.assertIn(f"kb:app-scripts {bundle_name.name}", source)
                self.assertEqual(script_sources_from_text(rendered), expected_sources)

    def test_app_script_paths_stay_under_deployed_site_prefix(self) -> None:
        for page_name, bundle in APP_SCRIPT_PAGES.items():
            with self.subTest(page=page_name):
                page_url = output_url_for_source(page_name)
                for src in script_sources_from_text(render_app_script_tags(page_name, bundle)):
                    resolved = urljoin(page_url, src)

                    self.assertTrue(
                        urlparse(resolved).path.startswith("/knowledge-base/"),
                        f"{page_name} script {src!r} escapes the deployed site prefix as {resolved}",
                    )

    def test_app_script_paths_are_not_hand_coded(self) -> None:
        sources = [
            *DOCS_DIR.rglob("*.md"),
            COMPONENTS_DIR / "tree" / "generate_tree_data.py",
        ]
        offenders = [
            f"{path.relative_to(REPO_ROOT).as_posix()}: {src}"
            for path in sources
            for src in script_sources(path)
            if src.startswith(("javascripts/", "../javascripts/"))
        ]

        self.assertEqual(offenders, [])

    def test_deliberate_page_relative_navigation_stays_under_deployed_site_prefix(self) -> None:
        cases = {
            "tree/index.md": (
                "../map/#paper=example",
                "../tree/#paper=example",
                "../timeline/#paper=example",
                "../search/?paper=example",
            ),
            "timeline.md": (
                "../map/#paper=example",
                "../tree/#paper=example",
                "../timeline/#paper=example",
                "../search/?paper=example",
            ),
            "papers/example.md": (
                "../../search/?paper=example&tag=planning",
                paper_site_url("detail", "other", "../.."),
                paper_site_url("map", "other", "../.."),
                paper_site_url("tree", "other", "../.."),
                paper_site_url("timeline", "other", "../.."),
                paper_site_url("search", "other", "../.."),
            ),
        }

        for page_name, targets in cases.items():
            page_url = output_url_for_source(page_name)
            for target in targets:
                with self.subTest(page=page_name, target=target):
                    resolved = urljoin(page_url, target)

                    self.assertTrue(
                        urlparse(resolved).path.startswith("/knowledge-base/"),
                        f"{page_name} link {target!r} escapes the deployed site prefix as {resolved}",
                    )

    def test_generated_paper_links_use_safe_route_targets(self) -> None:
        self.assertEqual(source_relative_url("papers/current.md", "search.md?author=Ada"), "../search.md?author=Ada")
        self.assertEqual(paper_site_source_url("detail", "other", "papers/current.md"), "other.md")
        self.assertEqual(paper_site_source_url("map", "other", "papers/current.md"), "../map.md?paper=other")
        self.assertEqual(paper_site_source_url("tree", "other", "papers/current.md"), "../tree/index.md?paper=other")
        self.assertEqual(paper_site_source_url("timeline", "other", "papers/current.md"), "../timeline.md?paper=other")
        self.assertEqual(paper_site_source_url("search", "other", "papers/current.md"), "../search.md?paper=other")

        for key in ("map", "tree", "timeline"):
            self.assertNotIn(".md#", paper_site_source_url(key, "other", "papers/current.md"))

    def test_build_staging_excludes_templates_from_published_pages(self) -> None:
        self.assertIn("templates", copy_docs_ignore(str(SOURCE_DOCS_DIR), ["papers", "templates"]))

    def test_built_site_local_links_stay_within_deployment_prefix(self) -> None:
        if os.environ.get("KB_CHECK_BUILT_SITE_LINKS") != "1":
            self.skipTest("set KB_CHECK_BUILT_SITE_LINKS=1 to scan generated site links")
        if not (SITE_DIR / "index.html").exists():
            self.skipTest("run `./dev run build` to materialize the generated site before scanning emitted links")

        checked = 0
        escaped: list[str] = []
        missing: list[str] = []

        for path in SITE_DIR.rglob("*.html"):
            parser = LocalRefParser()
            parser.feed(path.read_text(encoding="utf-8", errors="ignore"))
            origin = built_page_url(path)
            rel = path.relative_to(SITE_DIR).as_posix()

            for tag, attr, value in parser.refs:
                if value.startswith("#"):
                    continue
                for ref in expanded_refs(attr, value):
                    parsed_ref = urlparse(ref)
                    if parsed_ref.scheme in SKIPPED_REF_SCHEMES or parsed_ref.netloc:
                        continue

                    resolved = urljoin(origin, ref)
                    parsed = urlparse(resolved)
                    if parsed.netloc != urlparse(SITE_URL).netloc:
                        continue

                    checked += 1
                    detail = f"{rel}: <{tag} {attr}={ref!r}> -> {resolved}"
                    if not parsed.path.startswith(SITE_PREFIX):
                        escaped.append(detail)
                    elif not built_local_target_exists(parsed):
                        missing.append(detail)

        self.assertGreater(checked, 0)
        self.assertEqual(
            escaped, [], "local links escape the deployed /knowledge-base/ prefix:\n" + "\n".join(escaped[:20])
        )
        self.assertEqual(missing, [], "local links point at missing emitted files:\n" + "\n".join(missing[:20]))

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

    def test_search_page_placeholder_fits_compact_input(self) -> None:
        attrs = search_page_input_attrs()

        self.assertEqual(attrs["placeholder"], "Search papers")
        self.assertLessEqual(len(str(attrs["placeholder"])), 18)
        self.assertGreater(len(str(attrs["aria-label"])), len(str(attrs["placeholder"])))

    def test_plain_json_asset_rejects_js_assignment(self) -> None:
        with self.assertRaises(ValueError):
            SEMANTIC_SEARCH_INDEX.js_assignment({})

    def test_singleton_paper_tag_search_returns_the_selected_paper(self) -> None:
        from knowledge_base.generate_papers import build_tag_search_data

        records = [
            {
                "id": "2004_03853",
                "label": "SOS Shape-Constrained Regression",
                "year": 2020,
                "tags": ["Shape-constrained regression"],
            }
        ]

        with patch("knowledge_base.generate_papers.load_embedding_cache", return_value={}):
            data = build_tag_search_data(records)

        self.assertEqual(data["related"]["2004_03853::shape-constrained regression"], [{"id": "2004_03853"}])


if __name__ == "__main__":
    unittest.main()
