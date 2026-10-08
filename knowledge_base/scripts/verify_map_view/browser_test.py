"""Chrome startup must tolerate slow runners and clean up failed launches."""

import io
import tempfile
import unittest
from pathlib import Path
from typing import BinaryIO
from unittest.mock import Mock, patch

from knowledge_base.scripts.verify_map_view import browser


class ChromeStartupTests(unittest.TestCase):
    def test_chrome_can_become_ready_after_ten_seconds(self):
        elapsed = 0.0

        def sleep(seconds: float) -> None:
            nonlocal elapsed
            elapsed += seconds

        def request(*_args, **_kwargs):
            if elapsed < 12:
                raise TimeoutError("Chrome is still starting")
            return io.BytesIO(b'{"Browser": "Chrome"}')

        with (
            tempfile.TemporaryDirectory() as profile,
            patch.object(browser, "free_port", return_value=9222),
            patch.object(browser.tempfile, "mkdtemp", return_value=profile),
            patch.object(browser.subprocess, "Popen") as popen,
            patch.object(browser.time, "time", side_effect=lambda: elapsed),
            patch.object(browser.time, "sleep", side_effect=sleep),
            patch.object(browser.urllib.request, "urlopen", side_effect=request),
        ):
            popen.return_value.poll.return_value = None
            session = browser.launch_chrome("chrome")
            self.assertGreaterEqual(elapsed, 12)
            self.assertIs(session.process, popen.return_value)
            popen.return_value.terminate.assert_not_called()

    def test_failed_startup_reports_stderr_and_removes_profile(self):
        process = Mock()

        def start(*_args: object, stderr: BinaryIO, **_kwargs: object) -> Mock:
            stderr.write(b"Chrome startup diagnostic\n")
            return process

        with (
            tempfile.TemporaryDirectory() as root,
            patch.object(browser, "free_port", return_value=9222),
            patch.object(browser.subprocess, "Popen", side_effect=start),
            patch.object(browser, "wait_for_json", side_effect=TimeoutError("DevTools unavailable")),
        ):
            profile = Path(root) / "profile"
            profile.mkdir()
            with (
                patch.object(browser.tempfile, "mkdtemp", return_value=str(profile)),
                self.assertRaisesRegex(RuntimeError, "DevTools unavailable.*Chrome startup diagnostic"),
            ):
                browser.launch_chrome("chrome")
            process.terminate.assert_called_once()
            process.wait.assert_called_once()
            self.assertFalse(profile.exists())
