---
name: to-todos
description: Break a plan, spec, or PRD into independently-grabbable markdown todo tasks under `todo/` using tracer-bullet vertical slices. Use when user wants to convert a plan into todo entries, implementation tasks, future-work notes, or a lightweight task breakdown without an issue tracker.
---

# To Todos

Break a plan into independently-grabbable todo tasks using vertical slices (tracer bullets).

This repo has no issue tracker. Future work lives in markdown files under `todo/`.

## Process

### 1. Gather context

Work from whatever is already in the conversation context. If the user passes a path, read it. If they name an existing todo topic, prefer updating the matching file under `todo/`.

### 2. Explore the codebase (optional)

If you have not already explored the codebase, do so to understand the current state of the code. Todo titles and descriptions should use the project's domain glossary vocabulary, and respect ADRs in the area you're touching.

### 3. Draft vertical slices

Break the plan into **tracer bullet** tasks. Each task is a thin vertical slice that cuts through ALL integration layers end-to-end, NOT a horizontal slice of one layer.

Slices may be `human-needed` or `agent-ready`. `human-needed` slices require human interaction, such as an architectural decision or a design review. `agent-ready` slices can be implemented by an agent without more human context. Prefer `agent-ready` where possible.

<vertical-slice-rules>
- Each slice delivers a narrow but COMPLETE path through every layer (schema, API, UI, tests)
- A completed slice is demoable or verifiable on its own
- Prefer many thin slices over few thick ones
</vertical-slice-rules>

### 4. Check the breakdown when needed

If the user asked to review the breakdown, present it as a numbered list. For each slice, show:

- **Title**: short descriptive name
- **Type**: human-needed / agent-ready
- **Blocked by**: which other slices (if any) must complete first
- **User stories covered**: which user stories this addresses (if the source material has them)

Ask only the questions that matter:

- Does the granularity feel right? (too coarse / too fine)
- Are the dependency relationships correct?
- Are the correct slices marked as human-needed and agent-ready?

If the user asked you to write todos directly, make reasonable assumptions and write the file.

### 5. Write the todo

Write plain markdown under `todo/`.

- Prefer appending to an existing topical todo file when there is an obvious match.
- Otherwise create `todo/<short-slug>.md`.
- Preserve existing notes and ordering in files you touch.
- Keep tasks in dependency order, blockers first.

<todo-template>
# <Plan Or Topic Title>

## <Task title>

Type: `agent-ready` or `human-needed`

Blocked by: `<task title>` or `None`

A concise description of this vertical slice. Describe the end-to-end behavior, not layer-by-layer implementation.

Acceptance criteria:

- [ ] Criterion 1
- [ ] Criterion 2
- [ ] Criterion 3

Notes:

- Add only durable context that will still help later.
</todo-template>
