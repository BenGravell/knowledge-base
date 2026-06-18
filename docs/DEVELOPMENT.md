# Setup and development

This file is the maintainer command reference for the repository. Run commands
from the repository root unless a section says otherwise.

## Fresh checkout

Needs `git` plus `curl` or `wget`; no Python or global Pixi install is required.
The `./dev` wrapper installs Pixi locally on first use, then uses the checked-in
`pixi.lock`.

```bash
git clone https://github.com/BenGravell/knowledge-base.git
cd knowledge-base
./dev install
./dev run serve
```

Build the site from the repository root:

```bash
./dev run build
```

Deploy to GitHub Pages from the repository root:

```bash
./dev run deploy
```

## Development checks

Lint and type-check Python code from the repository root:

```bash
./dev run lint
./dev run format-check
./dev run typecheck
```

Run unit tests from the repository root:

```bash
./dev run test
```

Install the pre-commit hooks once:

```bash
./dev run pre-commit install
```

Run all pre-commit hooks manually:

```bash
./dev run pre-commit run --all-files
```

## Local generated data

Refresh local generated data and validate that the site is self-consistent from
the repository root:

```bash
./dev run refresh
```

Use `--force` to recompute cached embeddings, or `--strict` to also fail on
Tree algorithm-label drift and MkDocs warnings.

The refresh script prints elapsed seconds for each step and a compact grouped
timing report at the end. For deeper profiling, wrap it with `/usr/bin/time`.

## Streamlit apps

Generate and edit a `metadata.yml` entry from an arXiv ID:

```bash
./dev run streamlit run knowledge_base/apps/generator_app.py
```

Review Tree and metadata algorithm-label disagreements interactively:

```bash
./dev run streamlit run knowledge_base/apps/tree_label_review_app.py
```

The Tree Label Review app uses the same suggestions as
`knowledge_base/scripts/suggest_tree_algorithm_labels.py`.

It shows the current Tree label, metadata `algorithm`, paper context, nearby `tree.yml` lines, and candidate canonical labels.

Applying a label writes back to `knowledge_base/tree.yml`, the affected `metadata.yml`, or both, so review the resulting diff before committing.

## Repo layout

- `knowledge_base/docs/` contains MkDocs markdown content, generated paper pages, paper metadata, and templates.
- `knowledge_base/docs/papers/` contains paper entries.
- `knowledge_base/docs/templates/metadata.yml` is the paper metadata template.
- `knowledge_base/tree.yml` is the editable Tree nav source.
- `knowledge_base/apps/` contains Streamlit apps.
- `knowledge_base/scripts/` contains maintenance, audit, placement, and prefill entrypoints.
- `knowledge_base/scripts/prefill/` contains source-specific paper metadata importers.
- `knowledge_base/map/` contains graph generation, preview, and MkDocs asset publishing.
- `knowledge_base/semantic_search/` contains client-side semantic search index generation and asset publishing.
- `knowledge_base/tree/` contains the Tree model, validation helpers, MkDocs nav plugin, and Tree data generator.
- `knowledge_base/utils/` contains shared DOI, arXiv, and prefill helpers.
- `knowledge_base/site/` is generated output. Do not edit it directly.
