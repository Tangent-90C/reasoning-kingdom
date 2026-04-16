#!/usr/bin/env python3
from __future__ import annotations

import pathlib
import re
import sys


REPO_ROOT = pathlib.Path(__file__).resolve().parent.parent
DOCS_ROOT = REPO_ROOT / "docs"

# Existing raw HTML in the docs should continue to work.
HTML_PREFIXES = (
    "<!--",
    "<!DOCTYPE",
    "</",
    "<=",
    "<div",
    "<br",
    "<figure",
    "<figcaption",
    "<img",
    "<a",
    "<p",
    "<span",
    "<table",
    "<thead",
    "<tbody",
    "<tr",
    "<th",
    "<td",
    "<details",
    "<summary",
    "<sup",
    "<sub",
    "<http",
    "<https",
    "<mailto",
)


def strip_inline_code(line: str) -> str:
    parts = re.split(r"(`+)", line)
    if len(parts) == 1:
        return line

    result: list[str] = []
    active_ticks: str | None = None
    for part in parts:
        if not part:
            continue
        if re.fullmatch(r"`+", part):
            if active_ticks is None:
                active_ticks = part
                result.append(" " * len(part))
            elif active_ticks == part:
                active_ticks = None
                result.append(" " * len(part))
            else:
                result.append(" " * len(part))
        elif active_ticks is None:
            result.append(part)
        else:
            result.append(" " * len(part))
    return "".join(result)


def strip_inline_math(line: str) -> str:
    parts = re.split(r"(\$+)", line)
    if len(parts) == 1:
        return line

    result: list[str] = []
    active_ticks: str | None = None
    for part in parts:
        if not part:
            continue
        if re.fullmatch(r"\$+", part):
            if active_ticks is None:
                active_ticks = part
                result.append(" " * len(part))
            elif active_ticks == part:
                active_ticks = None
                result.append(" " * len(part))
            else:
                result.append(part)
        elif active_ticks is None:
            result.append(part)
        else:
            result.append(" " * len(part))
    return "".join(result)


def find_unsafe_angles(text: str) -> list[int]:
    indices: list[int] = []
    for idx, char in enumerate(text):
        if char != "<":
            continue

        if any(text.startswith(prefix, idx) for prefix in HTML_PREFIXES):
            continue

        if idx == 0 or idx == len(text) - 1:
            continue

        if text[idx - 1] == "\\":
            continue

        indices.append(idx)
    return indices


def main() -> int:
    failures: list[tuple[pathlib.Path, int, str]] = []

    for path in sorted(DOCS_ROOT.rglob("*.md")):
        rel_path = path.relative_to(REPO_ROOT)
        in_fence = False
        fence_marker: str | None = None
        in_math_block = False

        for line_no, raw_line in enumerate(path.read_text(encoding="utf-8").splitlines(), start=1):
            stripped = raw_line.lstrip()
            fence_match = re.match(r"^(```+|~~~+)", stripped)
            if fence_match:
                marker = fence_match.group(1)[0]
                if not in_fence:
                    in_fence = True
                    fence_marker = marker
                elif fence_marker == marker:
                    in_fence = False
                    fence_marker = None
                continue

            if in_fence:
                continue

            if stripped.startswith("$$"):
                in_math_block = not in_math_block
                continue

            if in_math_block:
                continue

            if raw_line.startswith("    ") or raw_line.startswith("\t"):
                continue

            candidate_line = strip_inline_math(strip_inline_code(raw_line))
            if find_unsafe_angles(candidate_line):
                failures.append((rel_path, line_no, raw_line.rstrip()))

    if not failures:
        print("Markdown Vue safety check passed.")
        return 0

    print("Unsafe '<' usage found in Markdown prose. Escape it as '&lt;' or move the expression into code/math syntax.")
    for rel_path, line_no, content in failures:
        print(f"{rel_path}:{line_no}: {content}")
    return 1


if __name__ == "__main__":
    sys.exit(main())
