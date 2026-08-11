import tempfile
import unittest
from pathlib import Path
from unittest.mock import call, patch

from knowledge_base.prefill.runner import SourceSpec, run_populated_sources, run_source


class RunPopulatedSourcesTest(unittest.TestCase):
    def test_runs_only_populated_sources(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            empty = root / "EMPTY.md"
            ready = root / "READY.md"
            empty.write_text("# Nothing queued\n", encoding="utf-8")
            ready.write_text("# Papers\nhttps://example.com/paper\n", encoding="utf-8")
            specs = {
                "ready": SourceSpec("ready", "Ready", ready, "citation"),
                "empty": SourceSpec("empty", "Empty", empty, "citation"),
            }

            with patch("knowledge_base.prefill.runner.run_source") as run_source:
                run_populated_sources(specs)

            self.assertEqual(run_source.call_args_list, [call("ready")])

    def test_new_arxiv_backed_metadata_ingests_full_text(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            source = root / "PAPERS.md"
            source.write_text("paper\n", encoding="utf-8")
            out = root / "docs" / "papers" / "2024" / "2401.00001" / "metadata.yml"

            def write_metadata(_entry, _fields, yaml_text: str):
                out.parent.mkdir(parents=True)
                out.write_text(yaml_text, encoding="utf-8")
                return out

            spec = SourceSpec(
                "fixture",
                "Fixture",
                source,
                "custom",
                extract_entries=lambda _path, _record_failure: ["paper"],
                prepare_context=lambda _entries, _args: {},
                existing_for_entry=lambda _entry, _context: None,
                fetch_fields=lambda _entry, _context: {},
                build_metadata=lambda _entry, _fields: {"arxiv_id": "2401.00001"},
                write_metadata=write_metadata,
            )

            with (
                patch("knowledge_base.prefill.sources.registry.source_specs", return_value={"fixture": spec}),
                patch("knowledge_base.prefill.runner.ingest_arxiv", create=True, return_value=0) as ingest_arxiv,
            ):
                run_source("fixture", [])

            ingest_arxiv.assert_called_once_with(["--paper-id", "2401_00001", "--sleep", "0"])


if __name__ == "__main__":
    unittest.main()
