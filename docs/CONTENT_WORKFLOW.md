# Content ingest workflow

The starting point for adding new items is ingestion. Commands in this file run
from the repository root.

## Manual ingest

Create a new directory under `knowledge_base/docs/papers/` and add a
`metadata.yml` based on `knowledge_base/docs/templates/metadata.yml`.

After metadata exists:

```bash
python knowledge_base/scripts/audit_metadata.py
python knowledge_base/scripts/validate_tree.py
```

## Batch funnel

Place paper URLs in `todo/PAPERS_FUNNEL.md`, one URL per line. Then route them
into source-specific files under `todo/papers/`, or into `todo/PAPERS_MISC.md`
when the source is unknown:

```bash
python knowledge_base/scripts/funnel_papers.py --dry-run
python knowledge_base/scripts/funnel_papers.py
```

## Source prefill scripts

Source-specific prefill scripts read URL or ID lists from `todo/papers/*.md`,
fetch initial metadata, and write
`knowledge_base/docs/papers/<YEAR>/<SLUG>/metadata.yml`.

Generated metadata starts as `audit_status: raw` and should be reviewed with
`knowledge_base/scripts/audit_metadata.py`. Agents may move reviewed entries to
`audit_status: partial`; `reviewed` is reserved for human review.

Run a prefill script with its default input file:

```bash
python knowledge_base/scripts/prefill/arxiv.py
python knowledge_base/scripts/prefill/ieee.py
```

Common options shared by the prefill scripts:

```bash
python knowledge_base/scripts/prefill/<source>.py --input todo/papers/<SOURCE>.md
python knowledge_base/scripts/prefill/<source>.py --first 5
python knowledge_base/scripts/prefill/<source>.py --list-skipped
python knowledge_base/scripts/prefill/<source>.py --overwrite
python knowledge_base/scripts/prefill/<source>.py --reingest
```

## Metadata audit

Audit all paper metadata files:

```bash
python knowledge_base/scripts/audit_metadata.py
```

Audit only entries marked `audit_status: partial`:

```bash
python knowledge_base/scripts/audit_metadata.py --audit-status partial
```

List entries still marked `audit_status: raw`:

```bash
python knowledge_base/scripts/list_raw_papers.py
```

Add `audit_status` to older metadata files that do not have it yet:

```bash
python knowledge_base/scripts/add_audit_status.py --dry-run
python knowledge_base/scripts/add_audit_status.py
```

## Tree placement

The Tree nav itself is edited in `knowledge_base/tree.yml`. Paper entries still
use metadata paths relative to `knowledge_base/`, such as:

```yaml
docs/papers/2025/2506.11513/metadata.yml
```

The build converts those paths to generated `papers/<slug>.md` pages behind the
scenes.

Validate `knowledge_base/tree.yml` local links and paper placement:

```bash
python knowledge_base/scripts/validate_tree.py
python knowledge_base/scripts/validate_tree.py --check-algorithm-labels
```

Suggest likely fixes for Tree and metadata algorithm-label disagreements:

```bash
python knowledge_base/scripts/suggest_tree_algorithm_labels.py
python knowledge_base/scripts/suggest_tree_algorithm_labels.py --min-confidence high
python knowledge_base/scripts/suggest_tree_algorithm_labels.py --format json
streamlit run knowledge_base/apps/tree_label_review_app.py
```

Find generated paper pages that are missing from the Tree nav:

```bash
python knowledge_base/scripts/list_unplaced_papers.py --neighbors 3
python knowledge_base/scripts/list_unplaced_papers.py --format paths
python knowledge_base/scripts/list_unplaced_papers.py --neighbors 0 --fail-on-missing
```
