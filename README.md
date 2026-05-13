# knowledge-base

Distilled knowledge on a variety of topics.

## Setup

Install dependencies from the repository root:

```bash
poetry install
```

Activate the environment:

```bash
poetry shell
```

Unless otherwise noted, run the commands below from the `knowledge_base/` directory.

## MkDocs Site

Serve the site locally:

```bash
mkdocs serve
```

Build the static site:

```bash
mkdocs build
```

Deploy to GitHub Pages:

```bash
mkdocs gh-deploy
```

During `mkdocs serve` and `mkdocs build`, MkDocs runs these Python gen-files
scripts automatically:

- `generate_papers.py` renders generated paper pages from `docs/papers/**/metadata.yml`.
- `mind_map/copy_assets.py` publishes Mind Map JavaScript and vendor assets.
- `content_tree/generate_content_tree_data.py` publishes Content Tree browser data.

## Streamlit Apps

Generate and edit a `metadata.yml` entry from an arXiv ID:

```bash
streamlit run apps/generator_app.py
```

## Paper Metadata Scripts

Audit all paper metadata files:

```bash
python scripts/audit_metadata.py
```

Useful variants:

```bash
python scripts/audit_metadata.py --file docs/papers/2024/2401.00001/metadata.yml
python scripts/audit_metadata.py --fix
python scripts/audit_metadata.py --check-malformed-abstracts
python scripts/audit_metadata.py --check-escaped-sequences
```

List entries still marked `audit_status: raw`:

```bash
python scripts/list_raw_papers.py
python scripts/list_raw_papers.py --max-results 5
```

Add `audit_status` to older metadata files that do not have it yet:

```bash
python scripts/add_audit_status.py --dry-run
python scripts/add_audit_status.py
```

Find generated paper pages that are missing from the `Content Tree` nav:

```bash
python scripts/list_unplaced_papers.py --neighbors 3
python scripts/list_unplaced_papers.py --format paths
python scripts/list_unplaced_papers.py --neighbors 0 --fail-on-missing
```

Route URLs from `todo/PAPERS_FUNNEL.md` into source-specific files under `todo/papers/`, or into `todo/PAPERS_MISC.md` when the source is unknown:

```bash
python scripts/funnel_papers.py --dry-run
python scripts/funnel_papers.py
```

## Source Prefill Scripts

Source-specific prefill scripts read URL or ID lists from `todo/papers/*.md`, fetch initial metadata, and write `docs/papers/<YEAR>/<SLUG>/metadata.yml`. 

Generated metadata starts as `audit_status: raw` and should be reviewed with `scripts/audit_metadata.py`.

Run a prefill script with its default input file:

```bash
python scripts/prefill/arxiv.py
python scripts/prefill/ieee.py
```

Common options shared by the prefill scripts:

```bash
python scripts/prefill/<source>.py --input ../todo/papers/<SOURCE>.md
python scripts/prefill/<source>.py --first 5
python scripts/prefill/<source>.py --list-skipped
python scripts/prefill/<source>.py --overwrite
python scripts/prefill/<source>.py --reingest
```

## Mind Map

The Mind Map embeds paper core content, computes semantic similarity edges, and renders the resulting graph with [Sigma.js](https://www.sigmajs.org/) and [Graphology](https://graphology.github.io/).

Regenerate embeddings and graph data:

```bash
python mind_map/generate_mind_map_data.py
```

Useful variants:

```bash
python mind_map/generate_mind_map_data.py --force
python mind_map/generate_mind_map_data.py --backend fastembed
python mind_map/generate_mind_map_data.py --backend voyage
python mind_map/generate_mind_map_data.py --threshold 0.82
python mind_map/generate_mind_map_data.py --skip-force-layout
```

Preview the graph quickly with Plotly:

```bash
python mind_map/preview_mind_map.py
python mind_map/preview_mind_map.py --serve
python mind_map/preview_mind_map.py --out preview.html
```

Smoke-test the served MkDocs Mind Map page in headless Chrome:

```bash
python scripts/verify_mind_map_view.py --url http://127.0.0.1:8000/mind-map/
```

## Explainer Helpers

Some explainers include small one-off Python helpers alongside the markdown.
For the PID explainer, recompute the cart-pole LQR gains with:

```bash
python docs/explainers/pid/compute_lqr_gains.py
```

## Repo Layout

`knowledge_base` contains the following:

- `apps/` contains Streamlit apps.
- `scripts/` contains maintenance, audit, placement, and prefill entrypoints.
- `scripts/prefill/` contains source-specific paper metadata importers.
- `mind_map/` contains graph generation, preview, and MkDocs asset publishing.
- `content_tree/` contains the MkDocs Content Tree data generator.
- `docs/explainers/` may contain small helper scripts used by individual explainers.
- `utils/` contains shared DOI, arXiv, and prefill helpers used by the scripts.
