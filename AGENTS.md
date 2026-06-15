# knowledge-base agent instructions

This repository uses repo-local skills as the shared instruction surface for coding agents.

Treat `.agents/skills/*/SKILL.md` as the source of truth for detailed workflows.

## How to use the skills

Before acting on a task, read `.agents/skills/core/SKILL.md`. Then read the most specific matching skill below, including its listed dependencies, before editing files or running task commands.

Use this dependency chain:

- `.agents/skills/core/SKILL.md`: shared project layout, commands, conventions, and validation rules.
- `.agents/skills/arxiv-version/SKILL.md`: find and verify arXiv versions before metadata work. Depends on core.
- `.agents/skills/paper-metadata/SKILL.md`: create or update one paper `metadata.yml`. Depends on core and arXiv lookup.
- `.agents/skills/tree-placement/SKILL.md`: audit and place metadata-backed papers in `knowledge_base/tree.yml`. Depends on core.
- `.agents/skills/batch-metadata/SKILL.md`: process a list or group of papers into metadata entries and tree placements. Depends on core, arXiv lookup, paper metadata, and tree placement.
- `.agents/skills/raw-metadata-audit/SKILL.md`: run the raw metadata audit and fix reported issues. Depends on core and, when research or metadata reconstruction is needed, paper metadata.

## Global guardrails

- Do not edit `knowledge_base/site/`; it is generated.
- New knowledge entries belong under `knowledge_base/docs/`.
- The editable Tree nav source is `knowledge_base/tree.yml`.
- Agents may move `audit_status` to `partial`, but must not promote it to `reviewed`.
- Do not run programmatic tests unless a loaded skill calls for a verification command or the change touches actual UX controls.
