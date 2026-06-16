# knowledge-base agent instructions

This repository uses repo-local skills as the shared instruction surface for coding agents.

Treat `.agents/skills/*/SKILL.md` as the source of truth for detailed workflows.

## How to use the skills

Before acting on a task, read `.agents/skills/core/SKILL.md`. Then read the most specific matching skill below, including its listed dependencies, before editing files or running task commands.

Use this dependency chain:

- `.agents/skills/core/SKILL.md`: shared project layout, commands, conventions, and validation rules.
- `.agents/skills/ponytail/SKILL.md`: default minimalism guardrail for every repo skill unless the user says "stop ponytail" or "normal mode". Depends on core guardrails.
- `.agents/skills/arxiv-version/SKILL.md`: find and verify arXiv versions before metadata work. Depends on core and ponytail.
- `.agents/skills/paper-metadata/SKILL.md`: create or update one paper `metadata.yml`. Depends on core, ponytail, and arXiv lookup.
- `.agents/skills/tree-placement/SKILL.md`: audit and place metadata-backed papers in `knowledge_base/tree.yml`. Depends on core and ponytail.
- `.agents/skills/batch-metadata/SKILL.md`: process a list or group of papers into metadata entries and tree placements. Depends on core, ponytail, arXiv lookup, paper metadata, and tree placement.
- `.agents/skills/raw-metadata-audit/SKILL.md`: run the raw metadata audit and fix reported issues. Depends on core, ponytail, and, when research or metadata reconstruction is needed, paper metadata.

Additional repo-local skills are available under `.agents/skills/`:

- Ponytail skills: `ponytail`, `ponytail-review`, `ponytail-audit`, `ponytail-debt`, and `ponytail-help`.
- Matt Pocock engineering skills: `diagnose`, `grill-with-docs`, `improve-codebase-architecture`, `prototype`, `setup-matt-pocock-skills`, `tdd`, `to-issues`, `to-prd`, `triage`, and `zoom-out`.

Run `setup-matt-pocock-skills` before the first Matt Pocock issue-tracker workflow (`to-issues`, `to-prd`, or `triage`) so `docs/agents/` records this repo's issue tracker, triage labels, and domain-doc layout.

## Global guardrails

- Do not edit `knowledge_base/site/`; it is generated.
- New knowledge entries belong under `knowledge_base/docs/`.
- The editable Tree nav source is `knowledge_base/tree.yml`.
- Agents may move `audit_status` to `partial`, but must not promote it to `reviewed`.
- Do not run programmatic tests unless a loaded skill calls for a verification command or the change touches actual UX controls.
- Ponytail's runnable-check rule does not override the previous line; use the smallest verification command permitted by the loaded repository skill.
