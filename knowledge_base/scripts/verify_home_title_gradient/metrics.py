"""Gradient edge metrics."""

from __future__ import annotations

import math

from knowledge_base.scripts.verify_home_title_gradient.model import GradientMetrics, Rgb


def color_delta(a: tuple[float, float, float], b: tuple[float, float, float]) -> float:
    return math.sqrt(sum((x - y) ** 2 for x, y in zip(a, b, strict=True)))


def gradient_metrics(width: int, height: int, rgba: bytes, threshold: float) -> GradientMetrics:
    raw_mask = [False] * (width * height)
    for index in range(width * height):
        base = index * 4
        rgb = (rgba[base], rgba[base + 1], rgba[base + 2])
        alpha = rgba[base + 3]
        raw_mask[index] = alpha > 245 and (max(rgb) - min(rgb)) > 12

    mask = [False] * (width * height)
    erosion = 2
    for y in range(erosion, height - erosion):
        for x in range(erosion, width - erosion):
            index = y * width + x
            mask[index] = all(
                raw_mask[(y + dy) * width + x + dx]
                for dy in range(-erosion, erosion + 1)
                for dx in range(-erosion, erosion + 1)
            )

    max_delta = 0.0
    spike_pairs = 0
    checked_pairs = 0
    text_pixels = 0
    rgb_sums = [0, 0, 0]
    for y in range(height):
        row = y * width
        for x in range(width):
            index = row + x
            if not mask[index]:
                continue
            base = index * 4
            rgb = (rgba[base], rgba[base + 1], rgba[base + 2])
            text_pixels += 1
            rgb_sums[0] += rgb[0]
            rgb_sums[1] += rgb[1]
            rgb_sums[2] += rgb[2]
            for neighbor in (index + 1 if x + 1 < width else None, index + width if y + 1 < height else None):
                if neighbor is None or not mask[neighbor]:
                    continue
                other = neighbor * 4
                delta = color_delta(rgb, (rgba[other], rgba[other + 1], rgba[other + 2]))
                checked_pairs += 1
                max_delta = max(max_delta, delta)
                if delta > threshold:
                    spike_pairs += 1

    mean_rgb: Rgb = (
        (
            round(rgb_sums[0] / text_pixels, 2),
            round(rgb_sums[1] / text_pixels, 2),
            round(rgb_sums[2] / text_pixels, 2),
        )
        if text_pixels
        else (0.0, 0.0, 0.0)
    )
    return {
        "text_pixels": text_pixels,
        "checked_pairs": checked_pairs,
        "max_delta": round(max_delta, 2),
        "mean_rgb": mean_rgb,
        "spike_pairs": spike_pairs,
    }
