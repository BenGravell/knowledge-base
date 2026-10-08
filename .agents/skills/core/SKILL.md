---
name: core
description: Shared project context for the knowledge-base repository. Use before editing or auditing Zensical site content, paper metadata, tree navigation, map scripts, or repository agent workflows in this personal publications knowledge base.
---

# Core

## Purpose

Use this skill first for repository context. Other knowledge-base skills depend on it.

Read `../ponytail/SKILL.md` after this skill for the default repo working style unless the user says "stop ponytail" or "normal mode". Ponytail's minimalism rules do not override repository guardrails, especially the limits on programmatic test runs.

## Project Shape

This is a personal knowledge base of publications, distilled notes, and paper summaries, published as a static site via Zensical.

Important paths:

- `knowledge_base/docs/`: Zensical markdown content, generated paper pages, paper metadata, and templates.
- `knowledge_base/docs/papers/`: paper entries. New entries go here.
- `knowledge_base/docs/templates/metadata.yml`: template for paper metadata.
- `knowledge_base/tree.yml`: editable Tree taxonomy source used by generated Tree and Map assets.
- `knowledge_base/tree/`: Tree Model, Tree validation, and Tree/Analytics generated-site projections.
- `knowledge_base/publishing/`: generated-site asset contracts, generated docs writer, paper page generation, site-link helpers, and shared browser asset publishing.
- `knowledge_base/prefill/`: metadata prefill workflow and source-specific paper importers.
- `knowledge_base/embeddings/`: Embedding Workbench and embedding cache helpers.
- `knowledge_base/components/`: browser component source and Map/Search adapters.
- `knowledge_base/components/map/`: embedding, UMAP, and graph generation scripts.
- `knowledge_base/scripts/`: command wrappers plus maintenance, audit, and placement entrypoints.
- `knowledge_base/site/`: generated site output. Do not edit it directly.
- `dev_apps/`: human-facing Streamlit development apps. `./dev` is the Pixi wrapper.
- `todo/papers/`: source-specific paper URL tracking lists.

## Commands

Run repository commands from the repo root unless a command says otherwise.

Install dependencies and activate the Pixi environment:

```bash
./dev install
eval "$(./dev shell-hook)"
```

Run Zensical commands through the local wrapper from the repo root:

```bash
kb serve
kb build
kb deploy
```

Map utilities:

```bash
python -m knowledge_base.components.map.pipeline.generate_data
python knowledge_base/components/map/preview_map.py
```

Human-oriented dev tools:

```bash
python knowledge_base/scripts/audit_metadata.py
streamlit run dev_apps/generator_app.py
```

## Conventions

- Python is `>=3.12, <3.13`; use `./dev` so Pixi can bootstrap the local environment.
- New knowledge entries go under `knowledge_base/docs/` following the structure of existing files.
- Paper URL lists live under `todo/papers/<SOURCE>.md`.
- Source-specific prefill adapters live under `knowledge_base/prefill/sources/<source>.py`.
- Valid metadata fields, item types, and audit statuses are defined in `knowledge_base/config.py`.
- Do not promote `audit_status` to `reviewed`. Agents may set it to `partial` after meaningful manual review or correction.
- There is no general test suite.
- Do not run programmatic tests except when a task skill explicitly requires a verification command or UX controls changed.
- When UX controls changed, verify with `kb build` from the repo root and check for warnings.

## Sub-Agent Delegation

Use sub-agents as an internal implementation detail whenever the primary agent judges they would improve exploration, validation, or parallel analysis. Do not wait for the user to request or approve sub-agent use. Keep delegation bounded to the task, pass only the context each sub-agent needs, and have the primary agent synthesize the result and decide what to do next.

## Extra Repo-Local Skills

Ponytail skills are vendored in this repo:

- `../ponytail/SKILL.md`: default minimalism guardrail.
- `../ponytail-review/SKILL.md`, `../ponytail-audit/SKILL.md`, `../ponytail-debt/SKILL.md`, and `../ponytail-help/SKILL.md`: callable quality review, audit, debt ledger, and help workflows.

Matt Pocock skills retain their upstream names and content, except for removing the architecture skill's grilling dependency:

- `../diagnosing-bugs/SKILL.md`
- `../improve-codebase-architecture/SKILL.md`
- `../codebase-design/SKILL.md`
- `../domain-modeling/SKILL.md`

This repo has no issue tracker workflow. Future work lives in markdown under `todo/`. Do not create `docs/agents/` or triage-label setup for work tracking.

### Applying upstream skills here

Keep vendored skills verbatim where possible; repository-specific rules belong here or in
`AGENTS.md`. These rules take precedence over upstream workflow defaults:

- When a skill says to call a Skill tool that the host does not provide, read
  `.agents/skills/<name>/SKILL.md` and follow it.
- The local planning destination is `todo/`: specs and task files go there.
  No tracker setup, external issue publication, or triage labels are needed.
- If this repo already has `CONTEXT.md` or `CONTEXT-MAP.md`, use it for the
  corresponding upstream `GLOSSARY.md` or `GLOSSARY-MAP.md` role.
- Ponytail plugin configuration and update commands in its help apply to the
  separately installed plugin, not these vendored files.

Upstream license notices live in `../vendor-licenses/`.
