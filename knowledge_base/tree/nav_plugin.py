"""MkDocs plugin that injects the standalone Tree into ``nav``."""

from __future__ import annotations

from pathlib import Path
from typing import Any

from mkdocs.config import config_options
from mkdocs.plugins import BasePlugin

from knowledge_base.tree.nav_source import tree_nav_item_from_file


class TreeNavPlugin(BasePlugin):
    config_scheme = (("source", config_options.Type(str, default="tree.yml")),)

    def on_config(self, config: Any) -> Any:
        config_file = Path(config.config_file_path or "mkdocs.yml")
        source_path = Path(self.config["source"])
        if not source_path.is_absolute():
            source_path = config_file.parent / source_path

        tree_item = tree_nav_item_from_file(source_path)
        nav = list(config.get("nav") or [])

        for index, item in enumerate(nav):
            if isinstance(item, dict) and "Tree" in item:
                nav[index] = tree_item
                break
        else:
            nav.append(tree_item)

        config["nav"] = nav
        return config
