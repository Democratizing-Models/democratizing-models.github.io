"""Build gallery navigation and cards from the case studies present in a branch."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


CATALOG_PATH = Path(__file__).parents[1] / "docs" / "gallery" / "catalog.json"
MARKER = "<!-- GALLERY_CASES -->"


def _catalog() -> list[dict[str, Any]]:
    return json.loads(CATALOG_PATH.read_text(encoding="utf-8"))


def _source_exists(docs_dir: Path, path: str) -> bool:
    source = docs_dir / "gallery" / path
    localized_source = source.with_name(f"{source.stem}.en{source.suffix}")
    return source.exists() or localized_source.exists()


def _published_sections(config: Any) -> list[dict[str, Any]]:
    docs_dir = Path(config["docs_dir"])
    sections: list[dict[str, Any]] = []
    for section in _catalog():
        entries = [
            entry
            for entry in section["entries"]
            if _source_exists(docs_dir, entry["path"])
        ]
        if entries:
            sections.append({"section": section["section"], "entries": entries})
    return sections


def on_config(config: Any) -> Any:
    """Expose only case studies whose Markdown source is present."""
    gallery_nav: list[Any] = ["gallery/index.md"]
    for section in _published_sections(config):
        pages = [
            {entry["title_plain"]: f"gallery/{entry['path']}"}
            for entry in section["entries"]
        ]
        gallery_nav.append({section["section"]: pages})

    for nav_item in config["nav"]:
        if isinstance(nav_item, dict) and "Gallery" in nav_item:
            nav_item["Gallery"] = gallery_nav
            break
    return config


def on_page_markdown(markdown: str, page: Any, config: Any, **_: Any) -> str:
    """Generate gallery cards while keeping absent branch content unpublished."""
    if MARKER not in markdown:
        return markdown

    rendered_sections: list[str] = []
    for section in _published_sections(config):
        cards: list[str] = []
        for entry in section["entries"]:
            cards.append(
                "\n".join(
                    [
                        '<div class="project-card" markdown>',
                        "",
                        f"### {entry['title_latex']} {{ data-toc-label=\"{entry['title_plain']}\" }}",
                        "",
                        entry["summary"],
                        "",
                        f"[Open gallery entry]({entry['path']})",
                        "",
                        "</div>",
                    ]
                )
            )
        rendered_sections.append(
            "\n".join(
                [
                    f"## {section['section']}",
                    "",
                    '<div class="project-grid" markdown>',
                    "",
                    "\n\n".join(cards),
                    "",
                    "</div>",
                ]
            )
        )
    return markdown.replace(MARKER, "\n\n".join(rendered_sections))
