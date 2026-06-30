"""Apply metadata audit autofixes."""

from pathlib import Path

from rich.console import Console

from knowledge_base.scripts.audit_metadata.fixes.author_fixes import (
    _fix_author_names_in_yaml,
    _fix_non_individual_authors_in_yaml,
)
from knowledge_base.scripts.audit_metadata.fixes.field_fixes import (
    _fix_folded_text_fields_in_yaml,
    _fix_multiline_fields_in_yaml,
    _fix_source_in_yaml,
)
from knowledge_base.scripts.audit_metadata.fixes.fix_predicates import (
    _is_abstract_dollar_math_issue,
    _is_abstract_latex_artifact_issue,
    _is_ascii_multi_dash_issue,
    _is_big_whitespace_issue,
    _is_clearable_summary_issue,
    _is_escaped_sequence_issue,
    _is_fixable_author_name_issue,
    _is_fixable_missing_tag_canonical_replacement,
    _is_fixable_non_individual_author_issue,
    _is_fixable_tag_issue,
    _is_folded_text_field_issue,
    _is_garbled_markup_issue,
    _is_high_confidence_ocr_artifact_issue,
    _is_multiline_field_issue,
    _is_publisher_mark_abstract_issue,
    _is_source_year_issue,
    _is_text_mojibake_issue,
    _is_tight_letter_parenthetical_spacing_issue,
    _is_title_value_fix_issue,
    _is_type_fix_issue,
)
from knowledge_base.scripts.audit_metadata.fixes.parse_fixes import (
    _fix_escaped_sequences_in_yaml,
    _fix_high_confidence_parse_errors_in_yaml,
)
from knowledge_base.scripts.audit_metadata.fixes.path_fixes import _apply_path_fix, _path_fix_for
from knowledge_base.scripts.audit_metadata.fixes.tag_fixes import (
    _fix_tags_in_yaml,
)
from knowledge_base.scripts.audit_metadata.fixes.text_fixes import (
    _delete_publisher_marks_from_abstract,
    _fix_ascii_multi_dash_in_yaml,
    _fix_big_whitespace_in_yaml,
    _fix_garbled_markup_in_yaml,
    _fix_high_confidence_ocr_artifacts_in_yaml,
    _fix_mojibake_text_fields_in_yaml,
    _fix_tight_letter_parenthetical_spacing_in_yaml,
)
from knowledge_base.scripts.audit_metadata.fixes.title_fixes import (
    _fix_title_in_yaml,
)
from knowledge_base.scripts.audit_metadata.fixes.yaml_rewrite import (
    _fix_metadata_scalar_field_in_yaml,
)
from knowledge_base.scripts.audit_metadata.rules.latex_rules import (
    _replace_dollar_math_in_text,
    _replace_plain_latex_math_artifacts_in_text,
)
from knowledge_base.scripts.audit_metadata.rules.string_fields import _metadata_field_root
from knowledge_base.scripts.audit_metadata.rules.tag_database import (
    _collect_missing_tag_canonical_fixes,
    _write_missing_tag_canonical_fixes,
)
from knowledge_base.scripts.audit_metadata.support.model import Issue
from knowledge_base.scripts.audit_metadata.support.yaml_support import _yaml_safe_load

console = Console(highlight=False)
err_console = Console(stderr=True, highlight=False)


def apply_fixes(
    results: list[tuple[Path, list[Issue]]],
    *,
    kb_root: Path,
    fix_paths: bool = True,
) -> dict[Path, Path]:
    fixed = 0
    path_replacements: dict[Path, Path] = {}
    metadata_paths_seen: set[Path] = set()
    added_tag_canonical_fixes = _write_missing_tag_canonical_fixes(_collect_missing_tag_canonical_fixes(results))
    added_canonical_tag_keys = set(added_tag_canonical_fixes)
    if added_tag_canonical_fixes:
        console.print("[green]Updated:[/] normalization/tags.yml")
        console.print(
            f"  added {len(added_tag_canonical_fixes)} canonical tag entr"
            f"{'y' if len(added_tag_canonical_fixes) == 1 else 'ies'}"
        )

    for path, issues in results:
        if path.name == "metadata.yml":
            metadata_paths_seen.add(path)
        has_parse_fixes = any(i.field == "parse" for i in issues)
        title_fixes = [
            i
            for i in issues
            if _is_title_value_fix_issue(i) and not _is_multiline_field_issue(i) and not _is_folded_text_field_issue(i)
        ]
        source_year_fixes = [i for i in issues if _is_source_year_issue(i)]
        tag_fixes = [
            i
            for i in issues
            if _is_fixable_tag_issue(i) or _is_fixable_missing_tag_canonical_replacement(i, added_canonical_tag_keys)
        ]
        abstract_publisher_fixes = [i for i in issues if _is_publisher_mark_abstract_issue(i)]
        abstract_dollar_math_fixes = [i for i in issues if _is_abstract_dollar_math_issue(i)]
        abstract_latex_artifact_fixes = [i for i in issues if _is_abstract_latex_artifact_issue(i)]
        author_name_fixes = [i for i in issues if _is_fixable_author_name_issue(i)]
        non_individual_author_fixes = [i for i in issues if _is_fixable_non_individual_author_issue(i)]
        type_fixes = [i for i in issues if _is_type_fix_issue(i)]
        summary_clear_fixes = [i for i in issues if _is_clearable_summary_issue(i)]
        mojibake_text_fields = {i.field for i in issues if _is_text_mojibake_issue(i)}
        ocr_artifact_fields = {i.field for i in issues if _is_high_confidence_ocr_artifact_issue(i)}
        multiline_fields = {i.field for i in issues if _is_multiline_field_issue(i)}
        folded_text_fields = {i.field for i in issues if _is_folded_text_field_issue(i)}
        has_escaped_sequence_fixes = any(_is_escaped_sequence_issue(i) for i in issues)
        has_garbled_markup_fixes = any(_is_garbled_markup_issue(i) for i in issues)
        whitespace_fields = {_metadata_field_root(i.field) for i in issues if _is_big_whitespace_issue(i)}
        tight_letter_parenthetical_fields = {
            _metadata_field_root(i.field) for i in issues if _is_tight_letter_parenthetical_spacing_issue(i)
        }
        ascii_multi_dash_fields = {_metadata_field_root(i.field) for i in issues if _is_ascii_multi_dash_issue(i)}
        fix_values = (
            has_parse_fixes,
            title_fixes,
            source_year_fixes,
            tag_fixes,
            abstract_publisher_fixes,
            abstract_dollar_math_fixes,
            abstract_latex_artifact_fixes,
            author_name_fixes,
            non_individual_author_fixes,
            type_fixes,
            summary_clear_fixes,
            mojibake_text_fields,
            ocr_artifact_fields,
            multiline_fields,
            folded_text_fields,
            has_escaped_sequence_fixes,
            has_garbled_markup_fixes,
            whitespace_fields,
            tight_letter_parenthetical_fields,
            ascii_multi_dash_fields,
        )
        if not any(fix_values):
            continue
        try:
            raw = path.read_text(encoding="utf-8")
            new_raw = raw
            messages = []

            if has_parse_fixes:
                new_raw, parse_messages = _fix_high_confidence_parse_errors_in_yaml(new_raw)
                messages.extend(parse_messages)

            if title_fixes and title_fixes[0].suggestion is not None:
                new_title = title_fixes[0].suggestion
                old_title = (_yaml_safe_load(new_raw) or {}).get("title", "")
                new_raw = _fix_title_in_yaml(new_raw, new_title)
                messages.append(f"  title: {old_title!r} [green]->[/] {new_title!r}")

            if source_year_fixes and source_year_fixes[0].suggestion is not None:
                old_source = _yaml_safe_load(new_raw).get("source", "")
                new_source = source_year_fixes[0].suggestion
                new_raw = _fix_source_in_yaml(new_raw, new_source)
                messages.append(f"  source: {old_source!r} [green]->[/] {new_source!r}")

            if abstract_publisher_fixes:
                parsed = _yaml_safe_load(new_raw) or {}
                old_abstract = str(parsed.get("abstract") or "")
                new_abstract, n_removed_marks = _delete_publisher_marks_from_abstract(old_abstract)
                if n_removed_marks and new_abstract != old_abstract:
                    new_raw = _fix_metadata_scalar_field_in_yaml(new_raw, "abstract", new_abstract)
                    messages.append(f"  removed {n_removed_marks} publisher/copyright notice(s) from abstract")

            if abstract_dollar_math_fixes:
                parsed = _yaml_safe_load(new_raw) or {}
                old_abstract = str(parsed.get("abstract") or "")
                new_abstract, n_math_spans = _replace_dollar_math_in_text(old_abstract)
                if n_math_spans and new_abstract != old_abstract:
                    new_raw = _fix_metadata_scalar_field_in_yaml(new_raw, "abstract", new_abstract)
                    messages.append(f"  converted {n_math_spans} dollar math span(s) in abstract")

            if abstract_latex_artifact_fixes:
                parsed = _yaml_safe_load(new_raw) or {}
                old_abstract = str(parsed.get("abstract") or "")
                new_abstract, n_artifacts = _replace_plain_latex_math_artifacts_in_text(old_abstract)
                if n_artifacts and new_abstract != old_abstract:
                    new_raw = _fix_metadata_scalar_field_in_yaml(new_raw, "abstract", new_abstract)
                    messages.append(f"  repaired {n_artifacts} plain LaTeX math artifact(s) in abstract")

            if author_name_fixes:
                parsed = _yaml_safe_load(new_raw) or {}
                new_raw, n_fixed_authors, n_decoded_author_sequences = _fix_author_names_in_yaml(new_raw, parsed)
                if n_fixed_authors:
                    if n_decoded_author_sequences:
                        messages.append(
                            "  decoded "
                            f"{n_decoded_author_sequences} author mojibake sequence(s) "
                            f"and ASCII-normalized {n_fixed_authors} name(s)"
                        )
                    else:
                        messages.append(f"  ASCII-normalized {n_fixed_authors} author name(s)")

            if non_individual_author_fixes:
                parsed = _yaml_safe_load(new_raw) or {}
                new_raw, n_repaired_authors = _fix_non_individual_authors_in_yaml(new_raw, parsed)
                if n_repaired_authors:
                    messages.append(f"  repaired {n_repaired_authors} non-individual author entry(s)")

            if type_fixes:
                parsed = _yaml_safe_load(new_raw) or {}
                old_type = parsed.get("type", "")
                new_type = type_fixes[0].suggestion
                new_raw = _fix_metadata_scalar_field_in_yaml(new_raw, "type", new_type)
                messages.append(f"  type: {old_type!r} [green]->[/] {new_type!r}")

            if summary_clear_fixes:
                new_raw = _fix_metadata_scalar_field_in_yaml(new_raw, "summary", "")
                messages.append("  cleared copied or low-signal summary")

            if mojibake_text_fields:
                parsed = _yaml_safe_load(new_raw) or {}
                new_raw, n_decoded_text = _fix_mojibake_text_fields_in_yaml(new_raw, parsed, mojibake_text_fields)
                if n_decoded_text:
                    fields = ", ".join(sorted(mojibake_text_fields))
                    messages.append(f"  decoded {n_decoded_text} text mojibake sequence(s): {fields}")

            if ocr_artifact_fields:
                parsed = _yaml_safe_load(new_raw) or {}
                new_raw, n_fixed_ocr = _fix_high_confidence_ocr_artifacts_in_yaml(new_raw, parsed, ocr_artifact_fields)
                if n_fixed_ocr:
                    fields = ", ".join(sorted(ocr_artifact_fields))
                    messages.append(f"  fixed {n_fixed_ocr} high-confidence OCR artifact(s): {fields}")

            if multiline_fields:
                parsed = _yaml_safe_load(new_raw) or {}
                new_raw, n_single_lined = _fix_multiline_fields_in_yaml(new_raw, parsed, multiline_fields)
                if n_single_lined:
                    fields = ", ".join(sorted(multiline_fields))
                    messages.append(f"  single-lined {n_single_lined} field(s): {fields}")

            if folded_text_fields:
                parsed = _yaml_safe_load(new_raw) or {}
                new_raw, folded_fields = _fix_folded_text_fields_in_yaml(new_raw, parsed, folded_text_fields)
                if folded_fields:
                    fields = ", ".join(folded_fields)
                    messages.append(f"  folded {len(folded_fields)} text field(s): {fields}")

            if tag_fixes:
                parsed = _yaml_safe_load(new_raw) or {}
                new_raw, n_fixed_tags = _fix_tags_in_yaml(new_raw, parsed, tag_fixes)
                if n_fixed_tags:
                    messages.append(f"  fixed {n_fixed_tags} tag(s)")

            if has_escaped_sequence_fixes:
                new_raw, n_decoded = _fix_escaped_sequences_in_yaml(new_raw)
                if n_decoded:
                    messages.append(f"  decoded {n_decoded} escaped sequence(s)")

            if has_garbled_markup_fixes:
                new_raw, n_cleaned_markup = _fix_garbled_markup_in_yaml(new_raw)
                if n_cleaned_markup:
                    messages.append(f"  cleaned {n_cleaned_markup} markup fragment(s)")

            if whitespace_fields:
                new_raw, n_collapsed_spaces = _fix_big_whitespace_in_yaml(new_raw, whitespace_fields)
                if n_collapsed_spaces:
                    fields = ", ".join(sorted(whitespace_fields))
                    messages.append(f"  collapsed {n_collapsed_spaces} large whitespace run(s): {fields}")

            if tight_letter_parenthetical_fields:
                parsed = _yaml_safe_load(new_raw) or {}
                new_raw, n_spaced_parentheticals = _fix_tight_letter_parenthetical_spacing_in_yaml(
                    new_raw, parsed, tight_letter_parenthetical_fields
                )
                if n_spaced_parentheticals:
                    fields = ", ".join(sorted(tight_letter_parenthetical_fields))
                    messages.append(f"  spaced {n_spaced_parentheticals} parenthetical abbreviation(s): {fields}")

            if ascii_multi_dash_fields:
                parsed = _yaml_safe_load(new_raw) or {}
                new_raw, n_fixed_dashes = _fix_ascii_multi_dash_in_yaml(new_raw, parsed, ascii_multi_dash_fields)
                if n_fixed_dashes:
                    fields = ", ".join(sorted(ascii_multi_dash_fields))
                    messages.append(f"  replaced {n_fixed_dashes} ASCII multi-dash run(s): {fields}")

            if new_raw == raw:
                err_console.print(f"  [dim](no change written for {path})[/]")
                continue
            _yaml_safe_load(new_raw)
            path.write_text(new_raw, encoding="utf-8")
            console.print(f"[green]Fixed:[/] {path}")
            for message in messages:
                console.print(message)
            fixed += 1
        except Exception as exc:
            err_console.print(f"[red]Error fixing {path}:[/] {exc}")

    moved = 0
    for path in sorted(metadata_paths_seen):
        if not fix_paths or not path.exists():
            continue
        path_fix = _path_fix_for(path, kb_root)
        if path_fix is None:
            continue
        if _apply_path_fix(path_fix, kb_root):
            path_replacements[path] = path_fix.new_path
            moved += 1

    tag_entry_summary = (
        f"; {len(added_tag_canonical_fixes)} canonical tag entr"
        f"{'y' if len(added_tag_canonical_fixes) == 1 else 'ies'} added"
        if added_tag_canonical_fixes
        else ""
    )
    console.print(f"\n[green]{fixed} file(s) fixed; {moved} path(s) moved{tag_entry_summary}.[/]")
    return path_replacements


__all__ = ["apply_fixes", "console", "err_console"]
