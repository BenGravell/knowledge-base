# knowledge-base

Distilled knowledge on a variety of topics.

The public site is published at <https://bengravell.github.io/knowledge-base/>.

## Repo layout

- `knowledge_base/` contains the published site source and supporting tools.
  - `docs/` contains the Zensical source pages and paper metadata.
    - `papers/**/metadata.yml` drives generated paper pages.
    - `papers/**/embed_text.md` contains cleaned arXiv full-text conversions for embeddings.
  - `tree.yml` is the editable Tree navigation and classification source.
  - `components/` contains Map, Tree, Search, and shared browser component source.
  - `scripts/` contains maintenance, audit, placement, and prefill entrypoints.
  - `utils/` contains shared DOI, arXiv, and prefill helpers.
- `dev_apps/` contains Streamlit apps and other human-facing development tools.
  `./dev` is the Pixi wrapper command.
- `knowledge_base/components/map/`, `knowledge_base/components/tree/`, and
  `knowledge_base/components/semantic_search/` derive Map, Timeline, Tree, and
  Semantic Search from `docs/papers/**/metadata.yml` plus `tree.yml`.
- `todo/PAPERS_FUNNEL.md` and `todo/papers/*.md` hold incoming paper URLs before ingest.
- `docs/` contains repository docs for maintainers; it is not the published site content.
  - [Setup and development](docs/DEVELOPMENT.md)
  - [Content ingest workflow](docs/CONTENT_WORKFLOW.md)
  - [Site generation and derived features](docs/SITE_GENERATION.md)

## Spin up from scratch

Needs `git` plus `curl` or `wget`.
No Python or global Pixi install is required.
The `./dev` wrapper installs Pixi locally on first use, then uses the checked-in `pixi.lock`.

```bash
git clone https://github.com/BenGravell/knowledge-base.git
cd knowledge-base
./dev install
./dev run serve
```

`kb` is a Python console script. It is available whenever the active Python environment has this repo installed.

VS Code recommends Pixi Code plus the Python extensions.

Pixi Code follows the upstream extension behavior: it auto-discovers `pixi` on
`PATH`, then registers the `knowledge-base:default` environment after
`./dev install` creates `.pixi/envs/default`.
If VS Code does not select it automatically, choose that Pixi environment manually.

In a plain terminal without the Pixi environment active, use `./dev run serve` or `./dev run kb serve`.

Open the URL printed by Zensical, usually <http://127.0.0.1:8000/>.

## Common workflows

### Serve the site locally

From the repo root, run

```bash
kb serve
```

### Run pre-commit

Install the Git hooks once:

```bash
./dev run pre-commit install
```

Run the hooks manually:

```bash
./dev run pre-commit run --all-files
```

To run only one hook while iterating, pass its id and the files to check:

```bash
./dev run pre-commit run ruff-check --files knowledge_base/scripts/refresh_offline_data.py
```

### Add papers

Put URLs in `todo/PAPERS_FUNNEL.md`, route them, prefill metadata, audit it, then place entries in `knowledge_base/tree.yml`.

```bash
# Route URLs into todo/papers/<SOURCE>.md or todo/PAPERS_MISC.md.
python knowledge_base/scripts/funnel_papers.py

# List prefill sources, then run the populated ones.
python -m knowledge_base.scripts.prefill --help
python -m knowledge_base.scripts.prefill arxiv
python -m knowledge_base.scripts.prefill openreview

# Audit raw metadata after prefill and fix reported files.
python knowledge_base/scripts/audit_metadata.py knowledge_base --audit-status raw

# Find unplaced papers, edit knowledge_base/tree.yml, then verify.
python knowledge_base/scripts/list_unplaced_papers.py --neighbors 3
python knowledge_base/scripts/list_unplaced_papers.py --neighbors 0 --fail-on-missing
kb build
```

Use the source names printed by the prefill help, such as `ieee`, `mlr`, or
`taylor_francis`; replace the example source commands with whichever
`todo/papers/*.md` files the funnel populated.

### Ingest arXiv embed text

Some paper entries can have an optional `embed_text.md` sidecar next to `metadata.yml`.
These sidecars are cleaned Markdown conversions of arXiv HTML, LaTeX, or PDF sources for embedding and agentic search only.
They are not the canonical e-print, PDF, or LaTeX source of truth, and this
repo intentionally does not store PDFs, LaTeX source archives, images, or other
rich paper assets.
Reuse of paper text remains governed by each paper's original license and rights holder terms.

Run the ingest script from the repo root:

```bash
./dev run python knowledge_base/scripts/ingest_arxiv_full_text.py --id 2402.08954
```

The script skips existing sidecars unless `--force` is passed. For arXiv
entries it tries arXiv HTML, ar5iv HTML, arXiv LaTeX source, then the PDF
inferred from the arXiv ID. HTML conversion uses the Python environment's
project-managed `pandoc` CLI; LaTeX/PDF fallback uses the Python environment's
project-managed `docling` CLI.

### Develop Python scripts or site helpers

For a script-only change, run a syntax/import check on the edited file:

```bash
python -m py_compile knowledge_base/scripts/refresh_offline_data.py
```

Replace the path with the file you changed. If the change affects Zensical
rendering, navigation, or generated site assets, run:

```bash
kb build
```

### Refresh offline data

If local generated data is stale, refresh it from the repo root:

```bash
kb refresh
```

### Deploy

Push to `main` or `master`; the GitHub Pages workflow runs `kb build` and publishes `knowledge_base/site/`.
