"""YAML loading helpers for metadata audit modules."""

from typing import Any

import yaml

_YAML_LOADER = getattr(yaml, "CSafeLoader", yaml.SafeLoader)


def _yaml_safe_load(stream: Any) -> Any:
    return yaml.load(stream, Loader=_YAML_LOADER)
