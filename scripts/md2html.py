#!/usr/bin/env python3
"""Convert the apply page's Markdown detail source into embeddable HTML data."""

from __future__ import annotations

import argparse
import html
import json
import re
from pathlib import Path


SECTION_RE = re.compile(r"^##\s+([A-Za-z0-9][A-Za-z0-9_-]*)\s*$")
HEADING_RE = re.compile(r"^(#{1,6})\s+(.+?)\s*$")
IMAGE_RE = re.compile(r"^!\[([^]]*)\]\(([^)]+)\)\s*$")
LINK_RE = re.compile(r"\[([^]]+)\]\(([^)]+)\)")


def inline_markdown(value: str) -> str:
    escaped = html.escape(value, quote=False)
    escaped = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", escaped)
    escaped = re.sub(r"`(.+?)`", r"<code>\1</code>", escaped)
    escaped = LINK_RE.sub(
        lambda match: f'<a href="{html.escape(match.group(2), quote=True)}">{match.group(1)}</a>',
        escaped,
    )
    return escaped


def render_blocks(lines: list[str]) -> str:
    blocks: list[str] = []
    paragraph: list[str] = []
    list_items: list[str] = []

    def flush_paragraph() -> None:
        if paragraph:
            blocks.append(f"<p>{inline_markdown(' '.join(paragraph))}</p>")
            paragraph.clear()

    def flush_list() -> None:
        if list_items:
            items = "".join(f"<li>{inline_markdown(item)}</li>" for item in list_items)
            blocks.append(f"<ul>{items}</ul>")
            list_items.clear()

    for raw_line in lines:
        line = raw_line.strip()
        if not line:
            flush_paragraph()
            flush_list()
            continue

        image_match = IMAGE_RE.match(line)
        if image_match:
            flush_paragraph()
            flush_list()
            alt, source = image_match.groups()
            image_source = source if re.match(r"^(?:https?:)?/", source) else f"./{source.lstrip('./')}"
            blocks.append(
                '<div class="detail-image">'
                f'<img src="{html.escape(image_source, quote=True)}" alt="{html.escape(alt, quote=True)}">'
                "</div>"
            )
            continue

        if line.startswith("- "):
            flush_paragraph()
            list_items.append(line[2:].strip())
            continue

        heading_match = HEADING_RE.match(line)
        if heading_match:
            flush_paragraph()
            flush_list()
            level = len(heading_match.group(1))
            tag = "h3" if level == 1 else "h4"
            blocks.append(f"<{tag}>{inline_markdown(heading_match.group(2))}</{tag}>")
            continue

        flush_list()
        paragraph.append(line)

    flush_paragraph()
    flush_list()
    return "".join(blocks)


def parse_details(source: str) -> dict[str, str]:
    details: dict[str, str] = {}
    current_key: str | None = None
    current_lines: list[str] = []

    def flush() -> None:
        if current_key is not None:
            details[current_key] = render_blocks(current_lines)

    for line in source.splitlines():
        match = SECTION_RE.match(line.strip())
        if match:
            flush()
            current_key = match.group(1)
            current_lines = []
        elif current_key is not None:
            current_lines.append(line)

    flush()
    if not details:
        raise ValueError("Markdown source must contain at least one `## detail-key` section")
    return details


def render_js(details: dict[str, str]) -> str:
    payload = json.dumps(details, ensure_ascii=False, indent=2)
    return f"window.applyDetails = {payload};\n"


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("source", type=Path)
    parser.add_argument("output", type=Path)
    args = parser.parse_args()

    details = parse_details(args.source.read_text(encoding="utf-8"))
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(render_js(details), encoding="utf-8")


if __name__ == "__main__":
    main()
