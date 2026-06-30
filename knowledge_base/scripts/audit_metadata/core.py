"""Compatibility surface for metadata audit orchestration."""

from knowledge_base.scripts.audit_metadata.file_audit import audit_file
from knowledge_base.scripts.audit_metadata.fixes.apply_fixes import apply_fixes, console, err_console

__all__ = ["apply_fixes", "audit_file", "console", "err_console"]
