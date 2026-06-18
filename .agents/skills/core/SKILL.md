---
name: core
description: Shared project context for the knowledge-base repository. Use before editing or auditing MkDocs content, paper metadata, tree navigation, map scripts, or repository agent workflows in this personal publications knowledge base.
---

# Core

## Purpose

Use this skill first for repository context. Other knowledge-base skills depend on it.

Read `../ponytail/SKILL.md` after this skill for the default repo working style unless the user says "stop ponytail" or "normal mode". Ponytail's minimalism rules do not override repository guardrails, especially the limits on programmatic test runs.

## Project Shape

This is a personal knowledge base of publications, distilled notes, and paper summaries, published as a static site via MkDocs.

Important paths:

- `knowledge_base/docs/`: MkDocs markdown content, generated paper pages, paper metadata, and templates.
- `knowledge_base/docs/papers/`: paper entries. New entries go here.
- `knowledge_base/docs/templates/metadata.yml`: template for paper metadata.
- `knowledge_base/tree.yml`: editable Tree nav source injected into `mkdocs.yml` through the local `tree-nav` plugin.
- `knowledge_base/map/`: embedding, UMAP, and graph generation scripts.
- `knowledge_base/scripts/`: audit and utility scripts. Source-specific prefill entrypoints live in `knowledge_base/scripts/prefill/`.
- `knowledge_base/site/`: generated site output. Do not edit it directly.
- `todo/papers/`: source-specific paper URL tracking lists.

## Commands

Run repository commands from the repo root unless a command says otherwise.

Install dependencies:

```bash
./dev install
```

Run MkDocs commands from the repo root:

```bash
./dev run mkdocs serve -f knowledge_base/mkdocs.yml
./dev run mkdocs build -f knowledge_base/mkdocs.yml
./dev run mkdocs gh-deploy -f knowledge_base/mkdocs.yml
```

Map utilities:

```bash
./dev run python knowledge_base/map/generate_map_data.py
./dev run python knowledge_base/map/preview_map.py
```

Human-oriented dev tools:

```bash
./dev run python knowledge_base/scripts/audit_metadata.py
./dev run streamlit run knowledge_base/apps/generator_app.py
```

## Conventions

- Python is `>=3.11, <3.14`; use `./dev` so uv can bootstrap Python and Poetry locally.
- New knowledge entries go under `knowledge_base/docs/` following the structure of existing files.
- Paper URL lists live under `todo/papers/<SOURCE>.md`.
- Source-specific prefill scripts live under `knowledge_base/scripts/prefill/<source>.py`.
- Valid metadata fields, item types, and audit statuses are defined in `knowledge_base/config.py`.
- Do not promote `audit_status` to `reviewed`. Agents may set it to `partial` after meaningful manual review or correction.
- There is no general test suite.
- Do not run programmatic tests except when a task skill explicitly requires a verification command or UX controls changed.
- When UX controls changed, verify with `./dev run mkdocs build -f knowledge_base/mkdocs.yml` from the repo root and check for warnings.

## Sub-Agent Delegation

Use sub-agents as an internal implementation detail whenever the primary agent judges they would improve exploration, validation, or parallel analysis. Do not wait for the user to request or approve sub-agent use. Keep delegation bounded to the task, pass only the context each sub-agent needs, and have the primary agent synthesize the result and decide what to do next.

## Extra Repo-Local Skills

Ponytail skills are vendored in this repo:

- `../ponytail/SKILL.md`: default minimalism guardrail.
- `../ponytail-review/SKILL.md`, `../ponytail-audit/SKILL.md`, `../ponytail-debt/SKILL.md`, and `../ponytail-help/SKILL.md`: callable complexity review, audit, debt ledger, and help workflows.

Matt Pocock engineering skills are forked and adapted for this repo:

- `../diagnose/SKILL.md`
- `../grill-with-docs/SKILL.md`
- `../improve-codebase-architecture/SKILL.md`
- `../prototype/SKILL.md`
- `../tdd/SKILL.md`
- `../to-todos/SKILL.md`
- `../to-prd/SKILL.md`
- `../zoom-out/SKILL.md`

This repo has no issue tracker workflow. Future work lives in markdown under `todo/`; use `to-todos` or `to-prd` for task breakdowns and PRDs. Do not create `docs/agents/` or triage-label setup for work tracking.

Upstream license notices live in `../vendor-licenses/`.
