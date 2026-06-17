"""Suggest canonical labels for Tree/metadata algorithm disagreements.

Usage:
  python scripts/suggest_tree_algorithm_labels.py
  python scripts/suggest_tree_algorithm_labels.py --max-results 50
  python scripts/suggest_tree_algorithm_labels.py --format json
  python scripts/suggest_tree_algorithm_labels.py --action update-tree-label
  python scripts/suggest_tree_algorithm_labels.py --min-confidence high
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from collections import Counter
from dataclasses import dataclass
from pathlib import Path
from typing import Any

import yaml


REPO_ROOT = Path(__file__).resolve().parents[2]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

from knowledge_base.scripts.audit_metadata import find_algorithm_issues  # noqa: E402
from knowledge_base.tree.nav_source import YAML_LOADER  # noqa: E402
from knowledge_base.tree.validation import (  # noqa: E402
    METADATA_ROOT,
    TREE_YML,
    TreeIssue,
    format_nav_path,
    relative_to_kb,
    validate_tree,
)


ACTION_UPDATE_TREE = "update-tree-label"
ACTION_UPDATE_METADATA = "update-metadata-algorithm"
ACTION_ACCEPT_ALIAS = "accept-alias"
ACTION_REVIEW = "review"
ACTIONS = (
    ACTION_UPDATE_TREE,
    ACTION_UPDATE_METADATA,
    ACTION_ACCEPT_ALIAS,
    ACTION_REVIEW,
)

CONFIDENCE_HIGH = "high"
CONFIDENCE_MEDIUM = "medium"
CONFIDENCE_LOW = "low"
CONFIDENCES = (CONFIDENCE_HIGH, CONFIDENCE_MEDIUM, CONFIDENCE_LOW)
CONFIDENCE_RANK = {
    CONFIDENCE_LOW: 0,
    CONFIDENCE_MEDIUM: 1,
    CONFIDENCE_HIGH: 2,
}

WORD_RE = re.compile(r"[A-Za-z0-9]+")

STOP_WORDS = {
    "a",
    "an",
    "and",
    "are",
    "as",
    "at",
    "by",
    "for",
    "from",
    "in",
    "into",
    "is",
    "of",
    "on",
    "or",
    "the",
    "to",
    "toward",
    "towards",
    "using",
    "via",
    "with",
}

TYPE_WORDS = {
    "algorithm",
    "algorithms",
    "approach",
    "approaches",
    "framework",
    "frameworks",
    "method",
    "methods",
    "model",
    "models",
    "rule",
    "rules",
    "scheme",
    "schemes",
    "technique",
    "techniques",
    "theorem",
    "theorems",
}

GENERIC_ALGORITHM_LABELS = {
    "algorithm",
    "algorithms",
    "analysis",
    "control",
    "learning",
    "method",
    "methods",
    "model",
    "optimization",
    "planning",
}

ROMAN_PART_LABELS = {"i", "ii", "iii", "iv", "v", "vi", "vii", "viii", "ix", "x"}


@dataclass(frozen=True)
class Suggestion:
    nav_path: tuple[str, ...]
    tree_label: str
    algorithm: str
    title: str
    audit_status: str
    source: str
    metadata_path: Path
    action: str
    confidence: str
    suggested_tree_label: str | None
    suggested_metadata_algorithm: str | None
    canonical_label: str | None
    reason: str


def clean_text(value: Any) -> str:
    return " ".join(str(value or "").split())


def words(value: str) -> list[str]:
    return WORD_RE.findall(clean_text(value).casefold())


def content_words(value: str) -> list[str]:
    return [word for word in words(value) if word not in STOP_WORDS]


def alnum_key(value: str) -> str:
    return "".join(words(value))


def stripped_type_words(value: str) -> list[str]:
    return [word for word in content_words(value) if word not in TYPE_WORDS]


def without_trailing_parenthetical(value: str) -> str:
    return re.sub(r"\s*\([^)]*\)\s*$", "", clean_text(value))


def is_title_like(value: str) -> bool:
    text = clean_text(value)
    return len(content_words(text)) >= 5 or ":" in text or "?" in text


def is_code_like(value: str) -> bool:
    text = clean_text(value)
    if not text or " " in text:
        return False

    core = re.sub(r"[^A-Za-z0-9]", "", text)
    if not core or len(core) > 14:
        return False

    alpha = [char for char in text if char.isalpha()]
    uppercase = [char for char in alpha if char.isupper()]
    if len(alpha) > 1 and len(uppercase) >= max(2, int(len(alpha) * 0.6)):
        return True
    if re.search(r"[0-9+_*]", text):
        return True
    if len(alpha) > 1 and any(char.isupper() for char in alpha[1:]):
        return True
    return False


def algorithm_looks_invalid(algorithm: str) -> bool:
    text = clean_text(algorithm)
    folded = " ".join(words(text))
    core = re.sub(r"[^A-Za-z0-9]", "", text)
    tokens = words(text)
    if not core:
        return True
    if tokens and tokens[0] in STOP_WORDS:
        return True
    if folded in GENERIC_ALGORITHM_LABELS:
        return True
    if folded in ROMAN_PART_LABELS and text.isupper():
        return True
    if len(core) <= 2 and not is_code_like(text):
        return True
    return False


def soft_equivalence_reason(tree_label: str, algorithm: str) -> str | None:
    if alnum_key(tree_label) == alnum_key(algorithm):
        return "Labels differ only by punctuation, case, or lightweight markup."

    if stripped_type_words(tree_label) == stripped_type_words(algorithm):
        return "Labels differ only by generic type words such as algorithm or method."

    tree_base = without_trailing_parenthetical(tree_label)
    if tree_base != clean_text(tree_label) and (
        alnum_key(tree_base) == alnum_key(algorithm)
        or stripped_type_words(tree_base) == stripped_type_words(algorithm)
    ):
        return "Tree label adds a parenthetical disambiguator to an otherwise equivalent label."

    return None


def phrase_in_text(phrase: str, text: str) -> bool:
    phrase = clean_text(phrase)
    if not phrase:
        return False
    escaped = re.escape(phrase).replace(r"\ ", r"\s+")
    return re.search(rf"(?<![A-Za-z0-9]){escaped}(?![A-Za-z0-9])", text, re.I) is not None


def algorithm_in_metadata_text(algorithm: str, data: dict[str, Any]) -> bool:
    tags = " ".join(str(tag) for tag in data.get("tags") or [])
    body = " ".join(
        clean_text(data.get(field)) for field in ("title", "abstract", "summary")
    )
    return phrase_in_text(algorithm, f"{body} {tags}")


def algorithm_in_tags(algorithm: str, data: dict[str, Any]) -> bool:
    return any(
        alnum_key(str(tag)) == alnum_key(algorithm)
        for tag in data.get("tags") or []
    )


def title_head(value: str) -> str | None:
    head = clean_text(value).split(":", 1)[0].strip()
    if head and head != clean_text(value) and len(content_words(head)) <= 6:
        return head
    return None


def text_introduces_algorithm(algorithm: str, data: dict[str, Any]) -> bool:
    text = " ".join(
        clean_text(data.get(field)) for field in ("title", "abstract", "summary")
    )
    algorithm_pattern = re.escape(clean_text(algorithm)).replace(r"\ ", r"\s+")
    intro = (
        r"\b(?:we|this\s+(?:paper|work|article|letter)|in\s+this\s+"
        r"(?:paper|work|article|letter))\s+(?:first\s+)?"
        r"(?:introduce|propose|present|develop|derive|formulate)\b"
    )
    method_word = (
        r"(?:algorithm|method|approach|optimizer|planner|controller|"
        r"framework|tool|system)"
    )
    patterns = (
        rf"^\s*{algorithm_pattern}\s*:",
        rf"{intro}[^.\n]{{0,180}}\b{algorithm_pattern}\b",
        rf"{intro}[^.\n]{{0,180}}\b{method_word}\s+"
        rf"(?:called\s+|named\s+)?{algorithm_pattern}\b",
        rf"\b(?:called|named|coined)\s+{algorithm_pattern}\b",
    )
    return any(re.search(pattern, text, re.I) for pattern in patterns)


def audit_suggested_algorithm(data: dict[str, Any], metadata_path: Path) -> str | None:
    for issue in find_algorithm_issues(metadata_path, data):
        if not issue.suggestion:
            continue
        match = re.search(r"for example '([^']+)'", issue.suggestion)
        if match:
            return match.group(1)
    return None


def load_metadata(path: Path) -> dict[str, Any]:
    with path.open("r", encoding="utf-8") as f:
        data = yaml.load(f, Loader=YAML_LOADER) or {}
    return data if isinstance(data, dict) else {}


def yaml_inline_value(value: str) -> str:
    dumped = yaml.safe_dump(
        {"value": value},
        allow_unicode=True,
        default_flow_style=False,
        sort_keys=False,
        width=10_000,
    ).strip()
    prefix = "value: "
    if dumped.startswith(prefix):
        return dumped.removeprefix(prefix)
    raise ValueError(f"Could not render YAML scalar for {value!r}")


def yaml_key(value: str) -> str:
    placeholder = "__KB_TREE_LABEL_VALUE__"
    dumped = yaml.safe_dump(
        [{value: placeholder}],
        allow_unicode=True,
        default_flow_style=False,
        sort_keys=False,
        width=10_000,
    ).strip()
    match = re.fullmatch(r"- (.*): " + re.escape(placeholder), dumped)
    if not match:
        raise ValueError(f"Could not render YAML key for {value!r}")
    return match.group(1)


def replace_metadata_algorithm(metadata_path: Path, algorithm: str) -> bool:
    lines = metadata_path.read_text(encoding="utf-8").splitlines(keepends=True)
    algorithm = clean_text(algorithm)
    replacement = (
        "algorithm:\n"
        if not algorithm
        else f"algorithm: {yaml_inline_value(algorithm)}\n"
    )
    for index, line in enumerate(lines):
        if re.match(r"^algorithm\s*:", line):
            if line == replacement:
                return False
            lines[index] = replacement
            metadata_path.write_text("".join(lines), encoding="utf-8")
            return True

    for index, line in enumerate(lines):
        if re.match(r"^title\s*:", line):
            lines.insert(index + 1, replacement)
            metadata_path.write_text("".join(lines), encoding="utf-8")
            return True

    lines.insert(0, replacement)
    metadata_path.write_text("".join(lines), encoding="utf-8")
    return True


def replace_tree_label(tree_path: Path, source: str, new_label: str) -> bool:
    lines = tree_path.read_text(encoding="utf-8").splitlines(keepends=True)
    source_pattern = re.escape(source)
    leaf_pattern = re.compile(
        rf"^(?P<indent>\s*)-\s+(?P<label>.+):\s+{source_pattern}\s*(?P<comment>#.*)?$"
    )
    for index, line in enumerate(lines):
        body = line.rstrip("\n")
        match = leaf_pattern.match(body)
        if not match:
            continue

        rendered_key = yaml_key(new_label)
        comment = f" {match.group('comment')}" if match.group("comment") else ""
        replacement = f"{match.group('indent')}- {rendered_key}: {source}{comment}\n"
        if line == replacement:
            return False
        lines[index] = replacement
        tree_path.write_text("".join(lines), encoding="utf-8")
        return True

    raise ValueError(f"Could not find Tree leaf source {source!r} in {tree_path}")


def apply_canonical_label(
    suggestion: Suggestion,
    canonical_label: str,
    *,
    tree_path: Path = TREE_YML,
) -> list[Path]:
    label = clean_text(canonical_label)
    if not label:
        raise ValueError("Canonical label cannot be empty.")

    changed: list[Path] = []
    if replace_tree_label(tree_path, suggestion.source, label):
        changed.append(tree_path)
    if replace_metadata_algorithm(suggestion.metadata_path, label):
        changed.append(suggestion.metadata_path)
    return changed


def metadata_algorithm_counts(metadata_root: Path) -> Counter[str]:
    counts: Counter[str] = Counter()
    for metadata_path in sorted(metadata_root.rglob("metadata.yml")):
        data = load_metadata(metadata_path)
        algorithm = clean_text(data.get("algorithm"))
        if algorithm:
            counts[" ".join(words(algorithm))] += 1
    return counts


def make_suggestion(
    issue: TreeIssue,
    data: dict[str, Any],
    *,
    algorithm_count: int,
) -> Suggestion:
    tree_label = clean_text(issue.tree_label)
    algorithm = clean_text(issue.algorithm)
    title = clean_text(data.get("title"))
    audit_status = clean_text(data.get("audit_status")) or "<none>"
    metadata_path = issue.metadata_path or Path()

    alias_reason = soft_equivalence_reason(tree_label, algorithm)
    if alias_reason is not None:
        return Suggestion(
            nav_path=issue.nav_path,
            tree_label=tree_label,
            algorithm=algorithm,
            title=title,
            audit_status=audit_status,
            source=issue.source or "",
            metadata_path=metadata_path,
            action=ACTION_ACCEPT_ALIAS,
            confidence=CONFIDENCE_HIGH,
            suggested_tree_label=None,
            suggested_metadata_algorithm=None,
            canonical_label=algorithm,
            reason=alias_reason,
        )

    if algorithm_looks_invalid(algorithm):
        replacement = title_head(title) or tree_label
        return Suggestion(
            nav_path=issue.nav_path,
            tree_label=tree_label,
            algorithm=algorithm,
            title=title,
            audit_status=audit_status,
            source=issue.source or "",
            metadata_path=metadata_path,
            action=ACTION_UPDATE_METADATA,
            confidence=CONFIDENCE_HIGH,
            suggested_tree_label=None,
            suggested_metadata_algorithm=replacement,
            canonical_label=replacement,
            reason="Metadata algorithm looks generic, empty, too short, or like a part number.",
        )

    audit_replacement = audit_suggested_algorithm(data, metadata_path)
    if audit_replacement is not None:
        return Suggestion(
            nav_path=issue.nav_path,
            tree_label=tree_label,
            algorithm=algorithm,
            title=title,
            audit_status=audit_status,
            source=issue.source or "",
            metadata_path=metadata_path,
            action=ACTION_UPDATE_METADATA,
            confidence=CONFIDENCE_MEDIUM,
            suggested_tree_label=None,
            suggested_metadata_algorithm=audit_replacement,
            canonical_label=audit_replacement,
            reason=(
                "Existing metadata audit says the algorithm field names an "
                "existing method rather than this paper's contribution."
            ),
        )

    duplicate_method = algorithm_count > 1
    broad_duplicate = duplicate_method and not is_code_like(algorithm)
    strong_method_signal = (
        is_code_like(algorithm)
        or algorithm_in_tags(algorithm, data)
        or text_introduces_algorithm(algorithm, data)
    ) and algorithm_in_metadata_text(algorithm, data)

    if duplicate_method and strong_method_signal:
        return Suggestion(
            nav_path=issue.nav_path,
            tree_label=tree_label,
            algorithm=algorithm,
            title=title,
            audit_status=audit_status,
            source=issue.source or "",
            metadata_path=metadata_path,
            action=ACTION_REVIEW,
            confidence=CONFIDENCE_LOW,
            suggested_tree_label=None,
            suggested_metadata_algorithm=None,
            canonical_label=algorithm,
            reason=(
                f"Metadata algorithm is used by {algorithm_count} papers; "
                "the Tree label may intentionally disambiguate this item."
            ),
        )

    if audit_status == "reviewed" and strong_method_signal:
        return Suggestion(
            nav_path=issue.nav_path,
            tree_label=tree_label,
            algorithm=algorithm,
            title=title,
            audit_status=audit_status,
            source=issue.source or "",
            metadata_path=metadata_path,
            action=ACTION_UPDATE_TREE,
            confidence=CONFIDENCE_HIGH,
            suggested_tree_label=algorithm,
            suggested_metadata_algorithm=None,
            canonical_label=algorithm,
            reason="Reviewed metadata has a strong method-name signal.",
        )

    if (
        alnum_key(tree_label) == alnum_key(title)
        and strong_method_signal
    ):
        return Suggestion(
            nav_path=issue.nav_path,
            tree_label=tree_label,
            algorithm=algorithm,
            title=title,
            audit_status=audit_status,
            source=issue.source or "",
            metadata_path=metadata_path,
            action=ACTION_UPDATE_TREE,
            confidence=CONFIDENCE_MEDIUM,
            suggested_tree_label=algorithm,
            suggested_metadata_algorithm=None,
            canonical_label=algorithm,
            reason=(
                "Tree label is the paper title, while metadata contains a "
                "method-like algorithm mentioned in the metadata text."
            ),
        )

    if is_code_like(tree_label) and not is_code_like(algorithm):
        return Suggestion(
            nav_path=issue.nav_path,
            tree_label=tree_label,
            algorithm=algorithm,
            title=title,
            audit_status=audit_status,
            source=issue.source or "",
            metadata_path=metadata_path,
            action=ACTION_UPDATE_METADATA,
            confidence=CONFIDENCE_MEDIUM,
            suggested_tree_label=None,
            suggested_metadata_algorithm=tree_label,
            canonical_label=tree_label,
            reason="Tree label is a compact code-like method name and metadata is expanded or descriptive.",
        )

    if clean_text(tree_label).casefold() in clean_text(algorithm).casefold():
        return Suggestion(
            nav_path=issue.nav_path,
            tree_label=tree_label,
            algorithm=algorithm,
            title=title,
            audit_status=audit_status,
            source=issue.source or "",
            metadata_path=metadata_path,
            action=ACTION_UPDATE_METADATA,
            confidence=CONFIDENCE_MEDIUM,
            suggested_tree_label=None,
            suggested_metadata_algorithm=tree_label,
            canonical_label=tree_label,
            reason="Metadata algorithm wraps the existing Tree label in extra descriptive words.",
        )

    if broad_duplicate:
        return Suggestion(
            nav_path=issue.nav_path,
            tree_label=tree_label,
            algorithm=algorithm,
            title=title,
            audit_status=audit_status,
            source=issue.source or "",
            metadata_path=metadata_path,
            action=ACTION_REVIEW,
            confidence=CONFIDENCE_LOW,
            suggested_tree_label=None,
            suggested_metadata_algorithm=None,
            canonical_label=None,
            reason=(
                f"Metadata algorithm is used by {algorithm_count} papers "
                "and is not a compact code-like method name."
            ),
        )

    if alnum_key(tree_label) == alnum_key(title) and not is_title_like(algorithm):
        return Suggestion(
            nav_path=issue.nav_path,
            tree_label=tree_label,
            algorithm=algorithm,
            title=title,
            audit_status=audit_status,
            source=issue.source or "",
            metadata_path=metadata_path,
            action=ACTION_REVIEW,
            confidence=CONFIDENCE_LOW,
            suggested_tree_label=None,
            suggested_metadata_algorithm=None,
            canonical_label=None,
            reason=(
                "Tree label is the paper title, but metadata algorithm is not "
                "strong enough to update automatically."
            ),
        )

    return Suggestion(
        nav_path=issue.nav_path,
        tree_label=tree_label,
        algorithm=algorithm,
        title=title,
        audit_status=audit_status,
        source=issue.source or "",
        metadata_path=metadata_path,
        action=ACTION_REVIEW,
        confidence=CONFIDENCE_LOW,
        suggested_tree_label=None,
        suggested_metadata_algorithm=None,
        canonical_label=None,
        reason="No conservative rule could choose a canonical label.",
    )


def collect_suggestions(tree_path: Path, metadata_root: Path) -> list[Suggestion]:
    algorithm_counts = metadata_algorithm_counts(metadata_root)
    report = validate_tree(
        tree_path,
        metadata_root=metadata_root,
        check_algorithm_labels=True,
    )
    suggestions: list[Suggestion] = []
    for issue in report.issues:
        if issue.code != "algorithm-label-mismatch" or issue.metadata_path is None:
            continue
        data = load_metadata(issue.metadata_path)
        algorithm_key = " ".join(words(clean_text(issue.algorithm)))
        suggestions.append(
            make_suggestion(
                issue,
                data,
                algorithm_count=algorithm_counts.get(algorithm_key, 0),
            )
        )
    return suggestions


def suggestion_to_dict(suggestion: Suggestion) -> dict[str, Any]:
    return {
        "action": suggestion.action,
        "confidence": suggestion.confidence,
        "canonical_label": suggestion.canonical_label,
        "suggested_tree_label": suggestion.suggested_tree_label,
        "suggested_metadata_algorithm": suggestion.suggested_metadata_algorithm,
        "reason": suggestion.reason,
        "tree_label": suggestion.tree_label,
        "metadata_algorithm": suggestion.algorithm,
        "title": suggestion.title,
        "audit_status": suggestion.audit_status,
        "source": suggestion.source,
        "metadata_path": relative_to_kb(suggestion.metadata_path),
        "nav_path": list(suggestion.nav_path),
    }


def filter_suggestions(
    suggestions: list[Suggestion],
    *,
    action: str | None,
    min_confidence: str,
) -> list[Suggestion]:
    minimum = CONFIDENCE_RANK[min_confidence]
    return [
        suggestion
        for suggestion in suggestions
        if (action is None or suggestion.action == action)
        and CONFIDENCE_RANK[suggestion.confidence] >= minimum
    ]


def print_markdown(suggestions: list[Suggestion], *, total: int, max_results: int) -> None:
    action_counts = Counter(suggestion.action for suggestion in suggestions)
    confidence_counts = Counter(suggestion.confidence for suggestion in suggestions)
    shown_count = min(len(suggestions), max_results)

    print("# Tree Algorithm Label Suggestions\n")
    print(f"{shown_count} of {total} suggestion(s) shown.\n")
    if suggestions:
        print("## Summary\n")
        for action in ACTIONS:
            if action_counts[action]:
                print(f"- `{action}`: {action_counts[action]}")
        for confidence in CONFIDENCES:
            if confidence_counts[confidence]:
                print(f"- `{confidence}` confidence: {confidence_counts[confidence]}")
        print()

    for suggestion in suggestions[:max_results]:
        print(f"- `{suggestion.action}` ({suggestion.confidence})")
        print(f"  - Tree: `{suggestion.tree_label}`")
        print(f"  - Metadata algorithm: `{suggestion.algorithm}`")
        if suggestion.canonical_label:
            print(f"  - Canonical: `{suggestion.canonical_label}`")
        if suggestion.suggested_tree_label:
            print(f"  - Suggested tree label: `{suggestion.suggested_tree_label}`")
        if suggestion.suggested_metadata_algorithm:
            print(
                "  - Suggested metadata algorithm: "
                f"`{suggestion.suggested_metadata_algorithm}`"
            )
        print(f"  - Reason: {suggestion.reason}")
        print(f"  - Audit status: `{suggestion.audit_status}`")
        print(f"  - Title: {suggestion.title}")
        print(f"  - Metadata: `{relative_to_kb(suggestion.metadata_path)}`")
        print(f"  - Nav: `{format_nav_path(suggestion.nav_path)}`")
    if len(suggestions) > max_results:
        print(f"\n... {len(suggestions) - max_results} more suggestion(s) not shown.")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Suggest canonical labels for Tree/metadata algorithm disagreements."
    )
    parser.add_argument(
        "--tree-yml",
        type=Path,
        default=TREE_YML,
        help="Path to the Tree YAML source.",
    )
    parser.add_argument(
        "--metadata-root",
        type=Path,
        default=METADATA_ROOT,
        help="Path to docs/papers metadata source.",
    )
    parser.add_argument(
        "--format",
        choices=("markdown", "json"),
        default="markdown",
        help="Output format.",
    )
    parser.add_argument(
        "--action",
        choices=ACTIONS,
        default=None,
        help="Only show suggestions with this recommended action.",
    )
    parser.add_argument(
        "--min-confidence",
        choices=CONFIDENCES,
        default=CONFIDENCE_LOW,
        help="Only show suggestions at or above this confidence.",
    )
    parser.add_argument(
        "--max-results",
        type=int,
        default=100,
        help="Maximum number of suggestions to print in Markdown output.",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    if args.max_results < 1:
        raise SystemExit("--max-results must be at least 1")

    suggestions = collect_suggestions(args.tree_yml, args.metadata_root)
    filtered = filter_suggestions(
        suggestions,
        action=args.action,
        min_confidence=args.min_confidence,
    )

    if args.format == "json":
        print(
            json.dumps(
                {
                    "total_suggestions": len(suggestions),
                    "shown_suggestions": len(filtered),
                    "suggestions": [suggestion_to_dict(item) for item in filtered],
                },
                indent=2,
                ensure_ascii=False,
            )
        )
    else:
        print_markdown(
            filtered,
            total=len(suggestions),
            max_results=args.max_results,
        )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
