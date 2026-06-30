"""Tree projection helpers for the Map pipeline."""

from __future__ import annotations

from typing import Any

from knowledge_base.components.tree.model import TreeModel
from knowledge_base.components.tree.nav_source import load_tree


def find_tree_nav(config: dict[str, Any]) -> object | None:
    """Return the nav subtree under ``Tree`` if present."""
    return load_tree(config)


def parse_nav_categories(config: dict[str, Any]) -> dict[str, dict[str, Any]]:
    """
    Recursively walk the site ``Tree`` nav and record each paper's
    full tree branch path, plus legacy category fields used by the
    existing map filters and colour palette.

    The first branch level under ``Tree`` is the super-category level:

        Tree → Decision-Making → Optimization → Toolboxes & Solvers → ...

    This keeps the Map hierarchy synchronized with the site Tree instead
    of maintaining a separate list of super-categories.

    Returns a dict mapping paper_id to:

        {
            "super_category": str | None,
            "category": str,
            "sub_category": str | None,
            "nav_path": [str, ...],
        }
    """
    tree = find_tree_nav(config)
    if tree is None:
        return {}
    return TreeModel.from_tree(tree).placement_fields_by_paper_id()


def parse_nav_category_order(config: dict[str, Any]) -> dict[str, Any]:
    """
    Walk the site ``Tree`` nav and return ordered hierarchy lists as
    they appear in the site config (not alphabetically).

    Returns:
        {
            "superCategories": [str, ...],
            "categories": [str, ...],
            "categorySuperCategory": {"<category>": "<super-category>" | None, ...},
            "subCategoryOrder": {"<category>": [str, ...], ...},
            "navPathOrder": [["<branch>", ...], ...],
            "maxBranchDepth": int,
        }
    """
    tree = find_tree_nav(config)
    if tree is None:
        return TreeModel.from_tree([]).order.category_order_fields()
    return TreeModel.from_tree(tree).order.category_order_fields()
