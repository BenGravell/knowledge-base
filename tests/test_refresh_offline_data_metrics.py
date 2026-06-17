from __future__ import annotations

import argparse
import json
import tempfile
import unittest
from datetime import datetime, timezone
from pathlib import Path

from knowledge_base.scripts.build_metrics import StepTiming, write_build_metrics


class RefreshOfflineDataMetricsTests(unittest.TestCase):
    def test_write_build_metrics_appends_history_and_trace(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            args = argparse.Namespace(metrics_dir=Path(tmp), dry_run=False)
            record = write_build_metrics(
                args=args,
                run_started_at=datetime(2026, 1, 2, 3, 4, 5, tzinfo=timezone.utc),
                run_duration_s=1.25,
                status="success",
                returncode=0,
                steps=[
                    StepTiming(
                        name="Example phase",
                        command=["python", "-V"],
                        started_at="2026-01-02T03:04:05.000Z",
                        start_offset_s=0.1,
                        duration_s=1.0,
                        returncode=0,
                    )
                ],
            )

            history = Path(tmp) / "builds.jsonl"
            saved = json.loads(history.read_text(encoding="utf-8").splitlines()[0])
            trace = json.loads((Path(tmp) / record["trace_file"]).read_text(encoding="utf-8"))

        self.assertEqual(saved["schema"], "knowledge-base-build-metrics-v1")
        self.assertEqual(saved["steps"][0]["name"], "Example phase")
        self.assertEqual(trace["traceEvents"][0]["name"], "Example phase")
        self.assertEqual(trace["traceEvents"][0]["ph"], "X")


if __name__ == "__main__":
    unittest.main()
