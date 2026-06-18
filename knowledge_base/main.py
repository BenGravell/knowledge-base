import itertools
from typing import Any

from knowledge_base.utils.site_links import site_icon_svg

TIMELINE_PREVIEW_PROFILES = (
    {
        "class": "one",
        "center": 15.5,
        "points": ((6, 1.0), (18, 3.9), (31, 3.0), (46, 5.3), (63, 4.0), (80, 5.1), (96, 2.6), (106, 1.0)),
        "dots": (17, 25, 43, 48, 54, 61, 75, 82, 90),
    },
    {
        "class": "two",
        "center": 37.0,
        "points": ((6, 1.1), (18, 6.0), (30, 7.5), (44, 4.6), (58, 8.5), (72, 7.2), (88, 8.3), (106, 1.2)),
        "dots": (16, 22, 27, 31, 39, 53, 58, 62, 69, 75, 84, 88, 93),
    },
    {
        "class": "three",
        "center": 58.0,
        "points": ((6, 0.9), (20, 3.0), (34, 1.8), (50, 5.0), (65, 4.4), (80, 3.8), (96, 3.2), (106, 0.9)),
        "dots": (21, 47, 52, 57, 64, 71, 80, 94),
    },
)

TIMELINE_PREVIEW_DOT_OFFSETS = (-0.26, 0.18, -0.12, 0.34, -0.3, 0.08, 0.28, -0.2)


def _catmull_rom_path(points: list[tuple[float, float]]) -> str:
    """Return a smooth cubic path through the given SVG points."""
    if len(points) < 2:
        return ""

    commands = [f"M {points[0][0]:.1f} {points[0][1]:.1f}"]
    for index in range(len(points) - 1):
        p0 = points[max(0, index - 1)]
        p1 = points[index]
        p2 = points[index + 1]
        p3 = points[min(len(points) - 1, index + 2)]
        c1x = p1[0] + (p2[0] - p0[0]) / 6
        c1y = p1[1] + (p2[1] - p0[1]) / 6
        c2x = p2[0] - (p3[0] - p1[0]) / 6
        c2y = p2[1] - (p3[1] - p1[1]) / 6
        commands.append(f"C {c1x:.1f} {c1y:.1f} {c2x:.1f} {c2y:.1f} {p2[0]:.1f} {p2[1]:.1f}")
    return " ".join(commands)


def _profile_width(points: tuple[tuple[float, float], ...], x: float) -> float:
    for left, right in itertools.pairwise(points):
        if left[0] <= x <= right[0]:
            t = (x - left[0]) / (right[0] - left[0])
            return left[1] + (right[1] - left[1]) * t
    return points[-1][1]


def _timeline_preview_stream(profile: dict[str, Any]) -> str:
    center = profile["center"]
    points = profile["points"]
    top = [(x, center - width) for x, width in points]
    bottom = [(x, center + width) for x, width in reversed(points)]
    return f"{_catmull_rom_path(top)} L {bottom[0][0]:.1f} {bottom[0][1]:.1f} {_catmull_rom_path(bottom)[2:]} Z"


def _timeline_preview_dots(profile: dict[str, Any]) -> list[tuple[float, float]]:
    dots = []
    center = profile["center"]
    points = profile["points"]
    for index, x in enumerate(profile["dots"]):
        width = _profile_width(points, x)
        offset = TIMELINE_PREVIEW_DOT_OFFSETS[index % len(TIMELINE_PREVIEW_DOT_OFFSETS)]
        y = center + offset * max(0.0, width - 2.6)
        dots.append((x, y))
    return dots


def define_env(env: Any) -> None:
    @env.macro
    def site_icon(icon_name: str) -> str:
        return site_icon_svg(icon_name)

    @env.macro
    def timeline_preview():
        streams = []
        dots = []
        for profile in TIMELINE_PREVIEW_PROFILES:
            class_name = profile["class"]
            streams.append(
                f'<path class="kb-time-stream-shape kb-time-stream-shape--{class_name}" '
                f'd="{_timeline_preview_stream(profile)}" />'
            )
            for x, y in _timeline_preview_dots(profile):
                dots.append(
                    f'<circle class="kb-time-swarm-dot kb-time-swarm-dot--{class_name}" '
                    f'cx="{x:.1f}" cy="{y:.1f}" r="2.0" />'
                )

        return (
            '<svg class="kb-time-streams" viewBox="0 0 112 71" focusable="false" aria-hidden="true">'
            + "".join(streams)
            + "".join(dots)
            + "</svg>"
        )
