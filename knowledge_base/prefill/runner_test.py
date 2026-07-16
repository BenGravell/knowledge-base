import tempfile
import unittest
from pathlib import Path
from unittest.mock import call, patch

from knowledge_base.prefill.runner import SourceSpec, run_populated_sources


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


if __name__ == "__main__":
    unittest.main()
