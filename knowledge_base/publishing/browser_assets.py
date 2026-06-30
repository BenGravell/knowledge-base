"""Generated-file script: publish component browser assets."""

from __future__ import annotations

from pathlib import Path

from knowledge_base.publishing.generated_assets import (
    HEADER_LINK_SCRIPT,
    HOME_BENTO_SCRIPT,
    MATH_FIT_SCRIPT,
    MATHJAX_CONFIG_SCRIPT,
    NAV_DRAWER_STATE_SCRIPT,
    PAPER_LINK_PILLS_SCRIPT,
    SEARCH_SCRIPT,
    SEMANTIC_SEARCH_WORKER_SCRIPT,
    TREE_NAVIGATOR_SCRIPT,
    TREE_SCRIPT,
    GeneratedAsset,
)
from knowledge_base.publishing.generated_files import open_generated

COMPONENTS_DIR = Path(__file__).resolve().parent.parent / "components"

BROWSER_ASSETS: dict[GeneratedAsset, Path] = {
    MATHJAX_CONFIG_SCRIPT: COMPONENTS_DIR / "site_shell" / "browser" / "mathjax.js",
    MATH_FIT_SCRIPT: COMPONENTS_DIR / "site_shell" / "browser" / "math-fit.js",
    HEADER_LINK_SCRIPT: COMPONENTS_DIR / "site_shell" / "browser" / "header-link.js",
    NAV_DRAWER_STATE_SCRIPT: COMPONENTS_DIR / "site_shell" / "browser" / "nav-drawer-state.js",
    HOME_BENTO_SCRIPT: COMPONENTS_DIR / "home" / "browser" / "home-bento.js",
    PAPER_LINK_PILLS_SCRIPT: COMPONENTS_DIR / "paper_links" / "browser" / "paper-link-pills.js",
    SEARCH_SCRIPT: COMPONENTS_DIR / "search" / "browser" / "search-page.js",
    SEMANTIC_SEARCH_WORKER_SCRIPT: COMPONENTS_DIR / "semantic_search" / "browser" / "semantic-search-worker.js",
    TREE_NAVIGATOR_SCRIPT: COMPONENTS_DIR / "tree" / "browser" / "tree-navigator.js",
    TREE_SCRIPT: COMPONENTS_DIR / "tree" / "browser" / "tree.js",
}


def main() -> None:
    for asset, source in BROWSER_ASSETS.items():
        with open_generated(asset.published_path, "w") as out:
            out.write(source.read_text(encoding="utf-8"))


if __name__ == "__main__":
    main()
