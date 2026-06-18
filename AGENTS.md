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
- Engineering skills: `diagnose`, `grill-with-docs`, `improve-codebase-architecture`, `prototype`, `tdd`, `to-todos`, `to-prd`, and `zoom-out`.

This repo has no issue tracker workflow. Future work lives in markdown under `todo/`; use `to-todos` or `to-prd` for task breakdowns and PRDs. Do not create `docs/agents/` or triage-label setup for work tracking.

## Global guardrails

- Do not edit `knowledge_base/site/`; it is generated.
- New knowledge entries belong under `knowledge_base/docs/`.
- The editable Tree nav source is `knowledge_base/tree.yml`.
- Agents may move `audit_status` to `partial`, but must not promote it to `reviewed`.
- Run checks only when they add task-specific signal; do not run broad test/build commands by default.
- Unit tests are permitted for Python logic changes when they cover the touched behavior, when adding or editing tests, or when verifying test/pre-commit wiring. Prefer the narrowest useful command: a single test file or focused unittest target before the full unit suite.
- For metadata, Tree, or paper-placement work, use the smallest relevant repository script named by the loaded skill instead of a general test run.
- For UX control changes, use the smallest relevant site check; default to `kb build` from the repo root only when the change could affect rendered pages or navigation.
- For pre-commit changes, run the specific affected hook when possible; run all hooks only when hook composition changed or the user asks for full verification.
- Ponytail's runnable-check rule does not require checks outside the narrow cases above.
