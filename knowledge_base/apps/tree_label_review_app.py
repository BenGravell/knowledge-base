from __future__ import annotations

from pathlib import Path
from typing import Any

import streamlit as st

from knowledge_base.scripts.suggest_tree_algorithm_labels import (
    ACTIONS,
    CONFIDENCES,
    METADATA_ROOT,
    TREE_YML,
    Suggestion,
    apply_canonical_label,
    clean_text,
    collect_suggestions,
    format_nav_path,
    load_metadata,
    relative_to_kb,
    replace_metadata_algorithm,
    replace_tree_label,
)


def generate_suggestions() -> list[Suggestion]:
    return collect_suggestions(TREE_YML, METADATA_ROOT)


def ensure_state() -> None:
    if "tree_label_suggestions" not in st.session_state:
        st.session_state.tree_label_suggestions = generate_suggestions()
    if "tree_label_index" not in st.session_state:
        st.session_state.tree_label_index = 0
    if "tree_label_last_result" not in st.session_state:
        st.session_state.tree_label_last_result = ""


def refresh_suggestions() -> None:
    st.session_state.tree_label_suggestions = generate_suggestions()
    st.session_state.tree_label_index = min(
        st.session_state.tree_label_index,
        max(len(st.session_state.tree_label_suggestions) - 1, 0),
    )


def metadata_context(metadata_path: Path) -> dict[str, Any]:
    return load_metadata(metadata_path)


def tree_line_context(source: str, radius: int = 5) -> tuple[str, int | None]:
    lines = TREE_YML.read_text(encoding="utf-8").splitlines()
    line_index = next(
        (index for index, line in enumerate(lines) if source and source in line),
        None,
    )
    if line_index is None:
        return "", None

    start = max(0, line_index - radius)
    end = min(len(lines), line_index + radius + 1)
    rendered = []
    for index in range(start, end):
        marker = ">" if index == line_index else " "
        rendered.append(f"{marker} {index + 1:4d}: {lines[index]}")
    return "\n".join(rendered), line_index + 1


def dedupe_options(options: list[tuple[str, str | None]]) -> list[tuple[str, str]]:
    seen: set[str] = set()
    deduped: list[tuple[str, str]] = []
    for label, value in options:
        value = clean_text(value)
        key = value.casefold()
        if not value or key in seen:
            continue
        seen.add(key)
        deduped.append((label, value))
    return deduped


def display_label(value: str) -> str:
    value = clean_text(value)
    return f"`{value}`" if value else "`<empty>`"


def apply_algorithm(suggestion: Suggestion, algorithm: str) -> None:
    algorithm = clean_text(algorithm)
    changed_paths: list[Path] = []
    if not algorithm:
        title = clean_text(suggestion.title)
        if not title:
            st.error("Cannot use an empty algorithm because the paper title is empty.")
            return
        if replace_tree_label(TREE_YML, suggestion.source, title):
            changed_paths.append(TREE_YML)
    if replace_metadata_algorithm(suggestion.metadata_path, algorithm):
        changed_paths.append(suggestion.metadata_path)
    metadata_path = relative_to_kb(suggestion.metadata_path)
    if changed_paths:
        changed_text = ", ".join(f"`{relative_to_kb(path)}`" for path in changed_paths)
        if algorithm:
            st.session_state.tree_label_last_result = (
                f"Wrote algorithm {display_label(algorithm)} to `{metadata_path}`."
            )
        else:
            st.session_state.tree_label_last_result = (
                f"Cleared algorithm and labeled the Tree with {display_label(suggestion.title)} in {changed_text}."
            )
    elif algorithm:
        st.session_state.tree_label_last_result = f"Algorithm {display_label(algorithm)} was already applied."
    else:
        st.session_state.tree_label_last_result = "Empty algorithm and title Tree label were already applied."
    refresh_suggestions()
    st.rerun()


def apply_label(suggestion: Suggestion, label: str) -> None:
    if not clean_text(label):
        apply_algorithm(suggestion, "")
        return

    changed = apply_canonical_label(suggestion, label, tree_path=TREE_YML)
    if changed:
        changed_text = ", ".join(f"`{relative_to_kb(path)}`" for path in changed)
        st.session_state.tree_label_last_result = f"Applied {display_label(label)} to {changed_text}."
    else:
        st.session_state.tree_label_last_result = f"{display_label(label)} was already applied."
    refresh_suggestions()
    st.rerun()


def filtered_suggestions(
    suggestions: list[Suggestion],
    *,
    actions: list[str],
    min_confidence: str,
    query: str,
) -> list[Suggestion]:
    confidence_rank = {confidence: index for index, confidence in enumerate(reversed(CONFIDENCES))}
    minimum = confidence_rank[min_confidence]
    query = query.strip().casefold()

    filtered: list[Suggestion] = []
    for suggestion in suggestions:
        if actions and suggestion.action not in actions:
            continue
        if confidence_rank[suggestion.confidence] < minimum:
            continue
        if query:
            haystack = " ".join(
                [
                    suggestion.tree_label,
                    suggestion.algorithm,
                    suggestion.title,
                    suggestion.reason,
                    relative_to_kb(suggestion.metadata_path),
                    format_nav_path(suggestion.nav_path),
                ]
            ).casefold()
            if query not in haystack:
                continue
        filtered.append(suggestion)
    return filtered


st.set_page_config(page_title="Tree Label Review", layout="wide")
st.title("Tree Label Review")

ensure_state()

with st.sidebar:
    st.header("Queue")
    if st.button("Regenerate", use_container_width=True):
        refresh_suggestions()
        st.rerun()

    selected_actions = st.multiselect("Actions", ACTIONS, default=list(ACTIONS))
    min_confidence = st.selectbox(
        "Minimum confidence",
        CONFIDENCES,
        index=CONFIDENCES.index("low"),
    )
    query = st.text_input("Search")

all_suggestions: list[Suggestion] = st.session_state.tree_label_suggestions
suggestions = filtered_suggestions(
    all_suggestions,
    actions=selected_actions,
    min_confidence=min_confidence,
    query=query,
)

if st.session_state.tree_label_last_result:
    st.success(st.session_state.tree_label_last_result)
    st.session_state.tree_label_last_result = ""

st.caption(f"{len(suggestions)} shown · {len(all_suggestions)} total disagreements")

if not suggestions:
    st.info("No suggestions match the current filters.")
    st.stop()

st.session_state.tree_label_index = min(
    st.session_state.tree_label_index,
    max(len(suggestions) - 1, 0),
)
index = st.session_state.tree_label_index
suggestion = suggestions[index]
metadata = metadata_context(suggestion.metadata_path)

nav_prev, nav_status, nav_next = st.columns([1, 2, 1])
with nav_prev:
    if st.button("Previous", disabled=index == 0, use_container_width=True):
        st.session_state.tree_label_index = max(index - 1, 0)
        st.rerun()
with nav_status:
    st.markdown(
        f"<div style='text-align:center'>Item {index + 1} of {len(suggestions)}</div>",
        unsafe_allow_html=True,
    )
with nav_next:
    if st.button("Next", disabled=index >= len(suggestions) - 1, use_container_width=True):
        st.session_state.tree_label_index = min(index + 1, len(suggestions) - 1)
        st.rerun()

st.divider()

left, right = st.columns([1, 1])

with left:
    st.subheader("Suggestion")
    c1, c2 = st.columns(2)
    c1.metric("Action", suggestion.action)
    c2.metric("Confidence", suggestion.confidence)
    st.write(suggestion.reason)

    st.text_input("Tree label", value=suggestion.tree_label, disabled=True)
    st.text_input("Metadata algorithm", value=suggestion.algorithm, disabled=True)
    if suggestion.canonical_label:
        st.text_input("Suggested canonical", value=suggestion.canonical_label, disabled=True)

    options = dedupe_options(
        [
            ("Use suggested", suggestion.canonical_label),
            ("Use Tree label", suggestion.tree_label),
            ("Use metadata algorithm", suggestion.algorithm),
            ("Use title", suggestion.title),
        ]
    )
    for button_label, value in options:
        if value is None:
            continue
        if st.button(button_label, key=f"{button_label}-{value}", use_container_width=True):
            apply_label(suggestion, value)
    if st.button(
        "Use empty algorithm + title",
        key="Use empty algorithm",
        use_container_width=True,
    ):
        apply_algorithm(suggestion, "")

    manual_default = suggestion.canonical_label or suggestion.algorithm or suggestion.tree_label or ""
    manual_label = st.text_input("Manual canonical label", value=manual_default)
    if st.button("Apply manual label", type="primary", use_container_width=True):
        apply_label(suggestion, manual_label or "")

with right:
    st.subheader("Metadata")
    st.write(f"**Title:** {clean_text(metadata.get('title'))}")
    st.write(f"**Authors:** {', '.join(metadata.get('authors') or [])}")
    st.write(f"**Year:** {metadata.get('year') or ''}")
    st.write(f"**Source:** {clean_text(metadata.get('source'))}")
    st.write(f"**Audit status:** `{clean_text(metadata.get('audit_status')) or '<none>'}`")
    tags = metadata.get("tags") or []
    if tags:
        st.write(f"**Tags:** {', '.join(str(tag) for tag in tags)}")
    if summary := clean_text(metadata.get("summary")):
        st.write("**Summary**")
        st.write(summary)
    if abstract := clean_text(metadata.get("abstract")):
        st.write("**Abstract**")
        st.write(abstract)

st.divider()

context_left, context_right = st.columns([1, 1])
with context_left:
    st.subheader("Tree Context")
    tree_context, line_number = tree_line_context(suggestion.source)
    if line_number is None:
        st.warning(f"Could not find source `{suggestion.source}` in `tree.yml`.")
    else:
        st.caption(f"`tree.yml:{line_number}`")
        st.code(tree_context, language="yaml")

with context_right:
    st.subheader("Paths")
    st.write(f"**Nav:** `{format_nav_path(suggestion.nav_path)}`")
    st.write(f"**Tree source:** `{suggestion.source}`")
    st.write(f"**Metadata:** `{relative_to_kb(suggestion.metadata_path)}`")
    if link := clean_text(metadata.get("link")):
        st.link_button("Open paper", link)
