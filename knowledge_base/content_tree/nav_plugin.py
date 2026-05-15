"""MkDocs plugin that injects the standalone Content Tree into ``nav``."""

from __future__ import annotations

from pathlib import Path
from typing import Any

from mkdocs.config import config_options
from mkdocs.plugins import BasePlugin

from knowledge_base.content_tree.nav_source import content_tree_nav_item_from_file


class ContentTreeNavPlugin(BasePlugin):
    config_scheme = (("source", config_options.Type(str, default="content_tree.yml")),)

    def on_config(self, config: Any) -> Any:
        config_file = Path(config.config_file_path or "mkdocs.yml")
        source_path = Path(self.config["source"])
        if not source_path.is_absolute():
            source_path = config_file.parent / source_path

        content_tree_item = content_tree_nav_item_from_file(source_path)
        nav = list(config.get("nav") or [])

        for index, item in enumerate(nav):
            if isinstance(item, dict) and "Content Tree" in item:
                nav[index] = content_tree_item
                break
        else:
            nav.append(content_tree_item)

        config["nav"] = nav
        return config
