"""Import-compatible surface for home title gradient verification."""

# ruff: noqa: F401

from knowledge_base.scripts.verify_home_title_gradient.capture import capture_metrics
from knowledge_base.scripts.verify_home_title_gradient.cli import main
from knowledge_base.scripts.verify_home_title_gradient.fixture import ROOT, html
from knowledge_base.scripts.verify_home_title_gradient.metrics import color_delta, gradient_metrics
from knowledge_base.scripts.verify_home_title_gradient.model import CaptureMetrics, FailureMetrics, GradientMetrics, Rgb
from knowledge_base.scripts.verify_home_title_gradient.png import png_rgba
