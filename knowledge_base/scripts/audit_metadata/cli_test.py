import tempfile
import unittest
from contextlib import chdir
from pathlib import Path
from unittest.mock import patch

from knowledge_base.scripts.audit_metadata.cli import _default_kb_root, main
from knowledge_base.scripts.audit_metadata.support.model import Issue


class MetadataOnlyAuditTest(unittest.TestCase):
    def test_default_root_ignores_cwd_lookalike_paper_directory(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            (root / "docs" / "papers").mkdir(parents=True)
            canonical = root / "canonical-knowledge-base"

            with patch("knowledge_base.scripts.audit_metadata.cli.KB_DIR", canonical), chdir(root):
                self.assertEqual(_default_kb_root(), canonical)

    def test_metadata_only_skips_generated_data_audit(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            metadata = root / "docs" / "papers" / "paper" / "metadata.yml"
            metadata.parent.mkdir(parents=True)
            metadata.write_text("title: Paper\n", encoding="utf-8")
            issue = Issue(metadata, "title", "Needs a fix")

            with (
                patch("sys.argv", ["audit-metadata", str(root), "--fix", "--metadata-only"]),
                patch(
                    "knowledge_base.scripts.audit_metadata.cli.audit_file",
                    side_effect=[({}, [issue]), ({}, [])],
                ),
                patch("knowledge_base.scripts.audit_metadata.cli.apply_fixes", return_value={}),
                patch("knowledge_base.scripts.audit_metadata.cli.audit_map_data_paths") as audit_generated_data,
                self.assertRaises(SystemExit) as exit_context,
            ):
                main()

            self.assertEqual(exit_context.exception.code, 0)
            audit_generated_data.assert_not_called()


if __name__ == "__main__":
    unittest.main()
