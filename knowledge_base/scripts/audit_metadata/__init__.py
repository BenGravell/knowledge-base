"""Import-compatible surface for the metadata auditor."""

from importlib import import_module

from knowledge_base.scripts.audit_metadata.fixes.fix_predicates import _is_fixable_tag_issue as _is_fixable_tag_issue
from knowledge_base.scripts.audit_metadata.rules.algorithm import find_algorithm_issues as find_algorithm_issues
from knowledge_base.scripts.audit_metadata.rules.algorithm_cues import (
    _algorithm_issue_cue as _algorithm_issue_cue,
)
from knowledge_base.scripts.audit_metadata.rules.algorithm_cues import (
    _text_introduces_algorithm_label as _text_introduces_algorithm_label,
)
from knowledge_base.scripts.audit_metadata.rules.tag_text import _tag_issue_index as _tag_issue_index
from knowledge_base.scripts.audit_metadata.rules.text_quality import (
    find_likely_misspelling_issues as find_likely_misspelling_issues,
)
from knowledge_base.scripts.audit_metadata.rules.text_quality import (
    find_ocr_spacing_issues as find_ocr_spacing_issues,
)
from knowledge_base.scripts.audit_metadata.support.model import RULE_TAG_VALUE as RULE_TAG_VALUE
from knowledge_base.scripts.audit_metadata.support.model import Issue as Issue

_module = _name = _value = None
_REEXPORT_MODULES = (
    ".support.checks",
    ".support.model",
    ".support.yaml_support",
    ".support.text",
    ".support.slugs",
    ".rules.abstract_data",
    ".rules.abstract_rules",
    ".rules.algorithm_cues",
    ".rules.algorithm_data",
    ".rules.algorithm_labels",
    ".rules.algorithm",
    ".rules.author_checks",
    ".rules.author_data",
    ".rules.author_rules",
    ".rules.encoding",
    ".rules.field_data",
    ".rules.latex_data",
    ".rules.latex_rules",
    ".rules.path_checks",
    ".rules.spacing_data",
    ".rules.string_fields",
    ".rules.tag_casing",
    ".rules.tag_data",
    ".rules.tag_database",
    ".rules.tag_duplicates",
    ".rules.tag_text",
    ".rules.tags",
    ".rules.text_artifacts",
    ".rules.text_quality",
    ".rules.title",
    ".rules.url_rules",
    ".rules.yaml_fields",
    ".fixes.parse_fixes",
    ".fixes.apply_fixes",
    ".fixes.author_fixes",
    ".fixes.field_fixes",
    ".fixes.fix_predicates",
    ".fixes.path_fixes",
    ".fixes.tag_fixes",
    ".fixes.text_fixes",
    ".fixes.title_fixes",
    ".fixes.yaml_rewrite",
    ".fixes.yaml_spans",
    ".generated_data.map_data",
    ".generated_data.map_data_helpers",
    ".generated_data.map_generated_audit",
    ".generated_data.semantic_search_audit",
    ".file_audit",
    ".core",
    ".cli",
)

for _module_name in _REEXPORT_MODULES:
    _module = import_module(_module_name, __name__)
    for _name, _value in vars(_module).items():
        if _name.startswith("__") and _name.endswith("__"):
            continue
        globals()[_name] = _value

del import_module, _REEXPORT_MODULES, _module, _module_name, _name, _value

__all__ = [
    "RULE_TAG_VALUE",
    "Issue",
    "_algorithm_issue_cue",
    "_is_fixable_tag_issue",
    "_tag_issue_index",
    "_text_introduces_algorithm_label",
    "find_algorithm_issues",
    "find_likely_misspelling_issues",
    "find_ocr_spacing_issues",
]
