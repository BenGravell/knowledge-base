"""Types for home title gradient verification."""

from typing import TypedDict

Rgb = tuple[float, float, float]


class GradientMetrics(TypedDict):
    text_pixels: int
    checked_pairs: int
    max_delta: float
    mean_rgb: Rgb
    spike_pairs: int


class CaptureMetrics(GradientMetrics):
    scheme: str
    frame: int
    position: str


class FailureMetrics(TypedDict):
    scheme: str
    frame: int | str
    position: str
    max_delta: float
    spike_pairs: int
    limit: float
