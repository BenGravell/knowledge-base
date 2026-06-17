# Content ingest workflow

The starting point for adding new items is ingestion. Commands in this file run
from `knowledge_base/` unless noted otherwise.

## Manual ingest

Create a new directory under `docs/papers/` and add a `metadata.yml` based on
`docs/templates/metadata.yml`.

After metadata exists:

```bash
python scripts/audit_metadata.py
python scripts/validate_tree.py
```

## Batch funnel

Place paper URLs in `todo/PAPERS_FUNNEL.md`, one URL per line. Then route them
into source-specific files under `todo/papers/`, or into `todo/PAPERS_MISC.md`
when the source is unknown:

```bash
python scripts/funnel_papers.py --dry-run
python scripts/funnel_papers.py
```

## Source prefill scripts

Source-specific prefill scripts read URL or ID lists from `todo/papers/*.md`,
fetch initial metadata, and write
`docs/papers/<YEAR>/<SLUG>/metadata.yml`.

Generated metadata starts as `audit_status: raw` and should be reviewed with
`scripts/audit_metadata.py`. Agents may move reviewed entries to
`audit_status: partial`; `reviewed` is reserved for human review.

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

## Metadata audit

Audit all paper metadata files:

```bash
python scripts/audit_metadata.py
```

Audit only entries marked `audit_status: partial`:

```bash
python scripts/audit_metadata.py --audit-status partial
```

List entries still marked `audit_status: raw`:

```bash
python scripts/list_raw_papers.py
```

Add `audit_status` to older metadata files that do not have it yet:

```bash
python scripts/add_audit_status.py --dry-run
python scripts/add_audit_status.py
```

## Tree placement

The Tree nav itself is edited in `tree.yml`. Paper entries in `tree.yml` should
use their literal metadata paths, such as:

```yaml
docs/papers/2025/2506.11513/metadata.yml
```

The build converts those paths to generated `papers/<slug>.md` pages behind the
scenes.

Validate `tree.yml` local links and paper placement:

```bash
python scripts/validate_tree.py
python scripts/validate_tree.py --check-algorithm-labels
```

Suggest likely fixes for Tree and metadata algorithm-label disagreements:

```bash
python scripts/suggest_tree_algorithm_labels.py
python scripts/suggest_tree_algorithm_labels.py --min-confidence high
python scripts/suggest_tree_algorithm_labels.py --format json
streamlit run apps/tree_label_review_app.py
```

Find generated paper pages that are missing from the Tree nav:

```bash
python scripts/list_unplaced_papers.py --neighbors 3
python scripts/list_unplaced_papers.py --format paths
python scripts/list_unplaced_papers.py --neighbors 0 --fail-on-missing
```
