"""Generated-file script: publish Tree, Timeline, and Analytics projections."""

from __future__ import annotations

import yaml

from knowledge_base.components.tree.analytics_projection import build_analytics_data, write_analytics_assets
from knowledge_base.components.tree.model import load_tree_model
from knowledge_base.components.tree.projection_common import (
    KB_DIR,
    METADATA_ROOT,
    SITE_CONFIG,
    TREE_YML,
    collect_paper_details,
)
from knowledge_base.components.tree.timeline_projection import build_timeline_data, write_timeline_assets
from knowledge_base.components.tree.tree_projection import IdFactory, build_browser_tree
from knowledge_base.components.tree.validation import format_tree_validation_report, validate_tree
from knowledge_base.generated_assets import TREE_DATA
from knowledge_base.generated_files import open_generated

YAML_LOADER = getattr(yaml, "CSafeLoader", yaml.SafeLoader)


def main() -> None:
    tree_validation_report = validate_tree()
    if not tree_validation_report.ok:
        raise RuntimeError(format_tree_validation_report(tree_validation_report, max_results=50))

    with open(SITE_CONFIG, encoding="utf-8") as f:
        config = yaml.load(f, Loader=YAML_LOADER)

    paper_details_by_source = collect_paper_details()
    ids = IdFactory()
    tree_model = load_tree_model(
        TREE_YML,
        config=config,
        base_dir=KB_DIR,
        metadata_root=METADATA_ROOT,
    )
    root = build_browser_tree(tree_model, ids, paper_details_by_source)

    tree_data = {
        "root": root,
        "meta": {
            "totalLeaves": root["leafCount"],
            "totalBranches": root["branchCount"],
        },
    }

    with open_generated(TREE_DATA.published_path, "w") as out:
        out.write(TREE_DATA.js_assignment(tree_data, separators=(",", ":")))

    analytics_data = build_analytics_data(root, tree_model, paper_details_by_source)
    timeline_data = build_timeline_data(tree_model, paper_details_by_source)
    write_analytics_assets(analytics_data)
    write_timeline_assets(timeline_data)


if __name__ == "__main__":
    main()
