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
eval "$(./dev shell-hook)"
kb serve
```

Run `eval "$(./dev shell-hook)"` once per terminal, or let VS Code use the configured Pixi interpreter.

Build the site from the repository root:

```bash
kb build
```

Build the static files for GitHub Pages from the repository root:

```bash
kb build
```

GitHub Pages deployment is handled by `.github/workflows/docs.yml` on pushes to `main` or `master`.

## Development checks

Lint and type-check Python code from the repository root:

```bash
kb lint
kb format-check
kb typecheck
```

Run unit tests from the repository root:

```bash
kb test
```

Install the pre-commit hooks once:

```bash
pre-commit install
```

Run all pre-commit hooks manually:

```bash
pre-commit run --all-files
```

## Local generated data

Refresh local generated data and validate that the site is self-consistent from
the repository root:

```bash
kb refresh
```

Use `--force` to recompute cached embeddings, or `--strict` to also fail on
Tree algorithm-label drift and Zensical warnings.

The refresh script prints elapsed seconds for each step and a compact grouped
timing report at the end. For deeper profiling, wrap it with `/usr/bin/time`.

## Streamlit apps

Generate and edit a `metadata.yml` entry from an arXiv ID:

```bash
streamlit run dev_apps/generator_app.py
```

Review Tree and metadata algorithm-label disagreements interactively:

```bash
streamlit run dev_apps/tree_label_review_app.py
```

The Tree Label Review app uses the same suggestions as
`knowledge_base/scripts/suggest_tree_algorithm_labels.py`.

It shows the current Tree label, metadata `algorithm`, paper context, nearby `tree.yml` lines, and candidate canonical labels.

Applying a label writes back to `knowledge_base/tree.yml`, the affected `metadata.yml`, or both, so review the resulting diff before committing.

## Repo layout

- `knowledge_base/docs/` contains Zensical markdown content, generated paper pages, paper metadata, and templates.
- `knowledge_base/docs/papers/` contains paper entries.
- `knowledge_base/docs/templates/metadata.yml` is the paper metadata template.
- `knowledge_base/tree.yml` is the editable Tree nav source.
- `dev_apps/` contains Streamlit apps.
- `knowledge_base/components/` contains Map, Tree, Search, and shared browser component source.
- `knowledge_base/scripts/` contains maintenance, audit, placement, and prefill entrypoints.
- `knowledge_base/scripts/prefill/` contains source-specific paper metadata importers.
- `knowledge_base/components/map/` contains graph generation, preview, and site asset publishing.
- `knowledge_base/components/semantic_search/` contains client-side semantic search index generation and asset publishing.
- `knowledge_base/components/tree/` contains the Tree model, validation helpers, browser source, and Tree data generator.
- `knowledge_base/utils/` contains shared DOI, arXiv, and prefill helpers.
- `knowledge_base/site/` is generated output. Do not edit it directly.
