"""Shared site-link ordering and icon helpers."""

from __future__ import annotations

import posixpath
from functools import lru_cache
from importlib import resources
from pathlib import Path, PurePosixPath
from typing import Any
from urllib.parse import quote, urlsplit, urlunsplit

import yaml

YAML_LOADER = getattr(yaml, "CSafeLoader", yaml.SafeLoader)

PAPER_SITE_LINK_KEYS = ("map", "tree", "search")
PAPER_SITE_LINK_LABELS = {
    "detail": "Detail",
    "map": "Map",
    "tree": "Tree",
    "search": "Search",
}
PAPER_SITE_LINK_SOURCES = {
    "explorer.md": ("map", "tree"),
    "search.md": ("search",),
}
FALLBACK_NAV_ICONS = {
    "detail": "lucide/file-text",
    "map": "lucide/map",
    "tree": "lucide/folder-tree",
    "search": "lucide/search",
}
FALLBACK_EXTERNAL_ICON = "lucide/external-link"
FALLBACK_INTERNAL_ICON = "lucide/chevron-right"


def clean_text(value: Any) -> str:
    return str(value or "").strip()


def as_list(value: Any) -> list[Any]:
    return value if isinstance(value, list) else []


@lru_cache(maxsize=8)
def load_site_config(path: str = "zensical.yml") -> dict[str, Any]:
    config_path = Path(path)
    if not config_path.exists():
        return {}
    with config_path.open("r", encoding="utf-8") as f:
        data = yaml.load(f, Loader=YAML_LOADER) or {}
    return data if isinstance(data, dict) else {}


@lru_cache(maxsize=128)
def site_icon_svg(icon_name: str) -> str:
    icon = clean_text(icon_name)
    if not icon:
        return ""

    icon_path = resources.files("zensical") / "templates" / ".icons" / f"{icon}.svg"
    if icon_path.is_file():
        return icon_path.read_text(encoding="utf-8")

    raise FileNotFoundError(f"Icon not found: {icon}")


def nav_page_order(config: dict[str, Any]) -> list[str]:
    order: list[str] = []
    for item in as_list(config.get("nav")):
        sources = item.values() if isinstance(item, dict) else (item,)
        for source in sources:
            source_text = clean_text(source).replace("\\", "/")
            order.extend(PAPER_SITE_LINK_SOURCES.get(source_text, ()))
    return list(dict.fromkeys((*order, *PAPER_SITE_LINK_KEYS)))


def nav_icon_for_key(config: dict[str, Any], key: str) -> str:
    nav_icons = config.get("extra", {}).get("nav_icons", {})
    if isinstance(nav_icons, dict):
        icon = clean_text(nav_icons.get(key))
        if icon:
            return icon
    return FALLBACK_NAV_ICONS.get(key, "")


def paper_site_link_specs(config_path: str = "zensical.yml") -> list[dict[str, str]]:
    config = load_site_config(config_path)
    return [
        {
            "key": key,
            "label": PAPER_SITE_LINK_LABELS[key],
            "icon": nav_icon_for_key(config, key),
        }
        for key in nav_page_order(config)
    ]


def site_link_data(config_path: str = "zensical.yml") -> dict[str, Any]:
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
                "iconSvg": site_icon_svg(spec["icon"]) if spec.get("icon") else "",
            }
            for spec in specs
        ],
        "fallbackIcons": {
            "external": site_icon_svg(FALLBACK_EXTERNAL_ICON),
            "internal": site_icon_svg(FALLBACK_INTERNAL_ICON),
        },
    }


def join_url(base_path: str, target: str) -> str:
    base = clean_text(base_path).rstrip("/")
    path = target.lstrip("/")
    return f"{base}/{path}" if base else path


def source_relative_url(from_source: str, target_source: str) -> str:
    parsed = urlsplit(target_source)
    from_parent = PurePosixPath(clean_text(from_source).replace("\\", "/")).parent.as_posix()
    start = "." if from_parent == "." else from_parent
    path = posixpath.relpath(parsed.path, start)
    return urlunsplit(("", "", path, parsed.query, parsed.fragment))


def paper_site_url(key: str, paper_id: str, base_path: str) -> str:
    quoted_paper_id = quote(paper_id, safe="")
    if key == "detail":
        return join_url(base_path, f"papers/{quoted_paper_id}/")
    if key in ("map", "tree"):
        return join_url(base_path, f"explorer/?mode={key}#paper={quoted_paper_id}")
    if key == "search":
        return join_url(base_path, f"search/?paper={quoted_paper_id}")
    return ""


def paper_site_source_url(key: str, paper_id: str, from_source: str) -> str:
    quoted_paper_id = quote(paper_id, safe="")
    if key == "detail":
        return source_relative_url(from_source, f"papers/{quoted_paper_id}.md")
    if key in ("map", "tree"):
        return source_relative_url(from_source, f"explorer.md?mode={key}&paper={quoted_paper_id}")
    if key == "search":
        return source_relative_url(from_source, f"search.md?paper={quoted_paper_id}")
    return ""


def make_paper_site_link(
    key: str,
    paper_id: str,
    *,
    base_path: str = "../..",
    from_source: str = "",
    icon: str = "",
) -> dict[str, str | bool]:
    label = PAPER_SITE_LINK_LABELS[key]
    icon_name = clean_text(icon) or FALLBACK_NAV_ICONS.get(key, "")
    return {
        "key": key,
        "label": label,
        "url": (
            paper_site_source_url(key, paper_id, from_source)
            if from_source
            else paper_site_url(key, paper_id, base_path)
        ),
        "detail": f"Open in {label}",
        "variant": "internal",
        "external": False,
        "icon": icon_name,
        "icon_svg": site_icon_svg(icon_name) if icon_name else "",
    }


def paper_site_links(
    paper_id: str,
    *,
    base_path: str = "../..",
    from_source: str = "",
    include_detail: bool = False,
    config_path: str = "zensical.yml",
) -> list[dict[str, str | bool]]:
    links: list[dict[str, str | bool]] = []
    if include_detail:
        links.append(make_paper_site_link("detail", paper_id, base_path=base_path, from_source=from_source))

    links.extend(
        make_paper_site_link(
            spec["key"],
            paper_id,
            base_path=base_path,
            from_source=from_source,
            icon=spec["icon"],
        )
        for spec in paper_site_link_specs(config_path)
    )
    return links
