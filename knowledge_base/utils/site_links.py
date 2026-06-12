"""Shared site-link ordering and icon helpers."""

from __future__ import annotations

from functools import lru_cache
from pathlib import Path
from typing import Any
from urllib.parse import quote

import material
import yaml


YAML_LOADER = getattr(yaml, "CSafeLoader", yaml.SafeLoader)
MATERIAL_ICON_DIR = Path(material.__file__).parent / "templates" / ".icons"

PAPER_SITE_LINK_KEYS = ("map", "tree", "timeline", "search")
PAPER_SITE_LINK_LABELS = {
    "detail": "Detail",
    "map": "Map",
    "tree": "Tree",
    "timeline": "Timeline",
    "search": "Search",
}
PAPER_SITE_LINK_SOURCES = {
    "map": {"map.md"},
    "tree": {"tree.md", "tree/index.md"},
    "timeline": {"timeline.md"},
    "search": {"search.md"},
}
FALLBACK_NAV_ICONS = {
    "detail": "material/file-document-outline",
    "map": "material/map",
    "tree": "material/file-tree-outline",
    "timeline": "material/timeline-clock-outline",
    "search": "material/magnify",
}
FALLBACK_EXTERNAL_ICON = "material/open-in-new"
FALLBACK_INTERNAL_ICON = "material/chevron-right"


def clean_text(value: Any) -> str:
    return str(value or "").strip()


def as_list(value: Any) -> list[Any]:
    return value if isinstance(value, list) else []


@lru_cache(maxsize=8)
def load_mkdocs_config(path: str = "mkdocs.yml") -> dict[str, Any]:
    config_path = Path(path)
    if not config_path.exists():
        return {}
    with config_path.open("r", encoding="utf-8") as f:
        data = yaml.load(f, Loader=YAML_LOADER) or {}
    return data if isinstance(data, dict) else {}


@lru_cache(maxsize=128)
def material_icon_svg(icon_name: str) -> str:
    icon = clean_text(icon_name)
    if not icon:
        return ""
    icon_path = MATERIAL_ICON_DIR / f"{icon}.svg"
    if not icon_path.is_file():
        raise FileNotFoundError(f"Material icon not found: {icon}")
    return icon_path.read_text(encoding="utf-8")


def nav_page_key(label: str, source: Any) -> str:
    label_key = clean_text(label).casefold()
    if label_key in PAPER_SITE_LINK_KEYS:
        return label_key

    source_text = clean_text(source).replace("\\", "/")
    for key, sources in PAPER_SITE_LINK_SOURCES.items():
        if source_text in sources:
            return key
    return ""


def nav_page_order(config: dict[str, Any]) -> list[str]:
    order: list[str] = []
    seen: set[str] = set()
    for item in as_list(config.get("nav")):
        if isinstance(item, dict):
            pairs = item.items()
        else:
            pairs = ((item, item),)

        for label, source in pairs:
            key = nav_page_key(str(label), source)
            if key and key not in seen:
                seen.add(key)
                order.append(key)

    for key in PAPER_SITE_LINK_KEYS:
        if key not in seen:
            order.append(key)
    return order


def nav_icon_for_key(config: dict[str, Any], key: str) -> str:
    nav_icons = config.get("extra", {}).get("nav_icons", {})
    if isinstance(nav_icons, dict):
        icon = clean_text(nav_icons.get(key))
        if icon:
            return icon
    return FALLBACK_NAV_ICONS.get(key, "")


def paper_site_link_specs(config_path: str = "mkdocs.yml") -> list[dict[str, str]]:
    config = load_mkdocs_config(config_path)
    return [
        {
            "key": key,
            "label": PAPER_SITE_LINK_LABELS[key],
            "icon": nav_icon_for_key(config, key),
        }
        for key in nav_page_order(config)
    ]


def site_link_data(config_path: str = "mkdocs.yml") -> dict[str, Any]:
    specs = [
        {
            "key": "detail",
            "label": PAPER_SITE_LINK_LABELS["detail"],
            "icon": FALLBACK_NAV_ICONS["detail"],
        },
        *paper_site_link_specs(config_path),
    ]
    return {
        "links": [
            {
                **spec,
                "iconSvg": material_icon_svg(spec["icon"]) if spec.get("icon") else "",
            }
            for spec in specs
        ],
        "fallbackIcons": {
            "external": material_icon_svg(FALLBACK_EXTERNAL_ICON),
            "internal": material_icon_svg(FALLBACK_INTERNAL_ICON),
        },
    }


def join_url(base_path: str, target: str) -> str:
    base = clean_text(base_path).rstrip("/")
    path = target.lstrip("/")
    return f"{base}/{path}" if base else path


def paper_site_url(key: str, paper_id: str, base_path: str) -> str:
    quoted_paper_id = quote(paper_id, safe="")
    if key == "detail":
        return join_url(base_path, f"papers/{quoted_paper_id}/")
    if key == "map":
        return join_url(base_path, f"map/#paper={quoted_paper_id}")
    if key == "tree":
        return join_url(base_path, f"tree/#paper={quoted_paper_id}")
    if key == "timeline":
        return join_url(base_path, f"timeline/#paper={quoted_paper_id}")
    if key == "search":
        return join_url(base_path, f"search/?paper={quoted_paper_id}")
    return ""


def make_paper_site_link(
    key: str,
    paper_id: str,
    *,
    base_path: str = "../..",
    icon: str = "",
) -> dict[str, str | bool]:
    label = PAPER_SITE_LINK_LABELS[key]
    icon_name = clean_text(icon) or FALLBACK_NAV_ICONS.get(key, "")
    return {
        "key": key,
        "label": label,
        "url": paper_site_url(key, paper_id, base_path),
        "detail": f"Open in {label}",
        "variant": "internal",
        "external": False,
        "icon": icon_name,
        "icon_svg": material_icon_svg(icon_name) if icon_name else "",
    }


def paper_site_links(
    paper_id: str,
    *,
    base_path: str = "../..",
    include_detail: bool = False,
    config_path: str = "mkdocs.yml",
) -> list[dict[str, str | bool]]:
    links: list[dict[str, str | bool]] = []
    if include_detail:
        links.append(make_paper_site_link("detail", paper_id, base_path=base_path))

    for spec in paper_site_link_specs(config_path):
        links.append(
            make_paper_site_link(
                spec["key"],
                paper_id,
                base_path=base_path,
                icon=spec["icon"],
            )
        )
    return links
