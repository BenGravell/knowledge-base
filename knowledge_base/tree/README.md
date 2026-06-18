# Tree Module

This package owns the in-process model of the Knowledge Base Tree.
The editable source of truth is still `knowledge_base/tree.yml`; the model gives scripts one place to ask what that Tree means.

## Source Flow

`tree.yml` stores human-edited navigation entries.
Paper leaves should point at literal metadata files, for example:

```yaml
- Frank-Wolfe Algorithm: docs/papers/1956/1956.frank.an_algorithm_for_quadratic/metadata.yml
```

The generated site later publishes those papers as `papers/<paper_id>.md`.
`TreeModel` keeps both forms:

- `source`: the raw Tree source, used for formatting-preserving edits to
  `tree.yml`.
- `generated_source`: the generated site paper page, used by Map, Timeline,
  Tree browser, and generated site data.
- `metadata_path`: the resolved metadata file when a leaf points at metadata.

## Main Modules

- `nav_source.py` loads the standalone Tree nav from `tree.yml` or from
  `mkdocs.yml` fallback config. It also contains low-level source path helpers.
- `model.py` converts raw nav data into `TreeModel`, `TreeBranch`, `TreeLeaf`,
  `TreeChild`, `TreePlacement`, and `TreeOrder`.
- `validation.py` checks local links, metadata coverage, and optional
  Tree/metadata algorithm-label drift.
- `generate_tree_data.py` is a generated-site adapter. It turns `TreeModel`
  into browser, Analytics, and Timeline JavaScript payloads.

## Preferred Entry Point

Use `load_tree_model(...)` when code needs the repository Tree with metadata-aware source resolution:

```python
from knowledge_base.tree.model import load_tree_model

model = load_tree_model(
    tree_path,
    config=config,
    base_dir=tree_path.parent,
    metadata_root=metadata_root,
)
```

Use `TreeModel.from_tree(...)` directly only when the caller already has raw nav data and intentionally wants custom source resolution, such as small unit tests or already-normalized Map category parsing.

## Invariants

- The synthetic `Tree` wrapper is transparent for taxonomy paths. A placement
  under `Tree > Theory > Leaf` has `path == ("Theory",)` and
  `nav_path == ("Theory", "Leaf")`.
- Landing pages such as `tree.md` and `tree/index.md` remain in
  `TreeModel.leaves`, but they are not taxonomy children of branches.
- `TreeBranch.children` contains immediate taxonomy children only. Branch child
  items carry all descendant paper IDs so branch-level analysis does not need to
  walk the raw YAML again.
- `TreePlacement` records the first resolved placement for each paper ID.
- `TreeOrder` records branch order as it appears in the Tree, not alphabetically.

## Adapter Boundaries

Keep shared Tree meaning in `model.py`: source resolution, paper placement, branch ancestry, child counts, descendant paper IDs, order, and tree distance.

Keep output-specific shaping in adapters:

- Browser node IDs, URLs, and JS payloads stay in `generate_tree_data.py`.
- Validation issue wording and link diagnostics stay in `validation.py`.
- Formatting-preserving `tree.yml` line edits stay in scripts that write the
  Tree, because those edits depend on the original YAML layout.
- Map-specific aggregate rows, filters, and visualization data stay in
  `map/generate_map_data.py`.

## Useful Checks

Run focused checks from the repository root:

```bash
.venv/bin/python -m unittest tests/test_tree_model.py tests/test_tree_scripts.py
.venv/bin/python knowledge_base/scripts/validate_tree.py --max-results 5
```

When changing `generate_tree_data.py`, also build the Zensical site from the
repository root:

```bash
kb build
```
