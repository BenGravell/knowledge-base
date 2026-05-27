from pathlib import Path

import material


MATERIAL_ICON_DIR = Path(material.__file__).parent / "templates" / ".icons"


def define_env(env):
    @env.macro
    def material_icon(icon_name):
        icon_path = MATERIAL_ICON_DIR / f"{icon_name}.svg"
        if not icon_path.is_file():
            raise FileNotFoundError(f"Material icon not found: {icon_name}")
        return icon_path.read_text(encoding="utf-8")
