from typing import Any

from knowledge_base.publishing.site_links import site_icon_svg


def define_env(env: Any) -> None:
    @env.macro
    def site_icon(icon_name: str) -> str:
        return site_icon_svg(icon_name)
