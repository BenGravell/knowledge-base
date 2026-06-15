---
name: tree-placement
description: Audit and place metadata-backed papers in the knowledge-base Tree nav. Use when papers are missing from knowledge_base/tree.yml, when adding new metadata entries to the nav, or when checking conceptual paper placement.
---

# Tree Placement

## Dependencies

Read `../core/SKILL.md` first.

## Audit Workflow

Run from `knowledge_base/`:

```bash
python scripts/list_unplaced_papers.py --neighbors 3
```

The audit lists every `docs/papers/**/metadata.yml` item whose generated `papers/<ID>.md` page is not under the Tree nav in `tree.yml`. It also uses `map/embedding_cache.json` to show nearest already-placed neighbors as initial placement hints.

## Placement Workflow

1. Insert each missing paper into `knowledge_base/tree.yml` under the closest appropriate branch.
2. Refer to paper entries with their literal metadata path, such as `docs/papers/2025/2506.11513/metadata.yml`.
3. Remember that the site build converts literal metadata paths to generated MkDocs pages such as `papers/2506_11513.md`.
4. Use embedding nearest neighbors as an initial guess, not as the final answer.
5. Prefer existing categories whenever they fit.
6. Create new categories only when the abstract and tags make existing tree branches a poor conceptual fit.
7. Prefer the metadata `algorithm` as the nav label when it is present and useful; otherwise use the cleaned paper title.

## Final Pass

Take a final pass over proposed placements using each paper's `metadata.yml` title, abstract, tags, and summary.

Watch for false-neighbor matches caused by broad words such as `control`, `optimization`, `planning`, `safety`, or `model predictive`. Move those papers into the branch that reflects the primary contribution.

## Verification

Run from `knowledge_base/`:

```bash
python scripts/list_unplaced_papers.py --neighbors 0 --fail-on-missing
mkdocs build
```
