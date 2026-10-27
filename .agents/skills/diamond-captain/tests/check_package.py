#!/usr/bin/env python3
"""Check packaged local Markdown links without external requests or dependencies."""
import re
from pathlib import Path
from urllib.parse import unquote


def heading_anchors(source: Path) -> set[str]:
    """GitHub-style anchors for the plain ATX headings used in this package."""
    anchors: set[str] = set()
    counts: dict[str, int] = {}
    in_fence = False
    for line in source.read_text(encoding="utf-8").splitlines():
        if line.lstrip().startswith(("```", "~~~")):
            in_fence = not in_fence
            continue
        if in_fence:
            continue
        match = re.match(r"^#{1,6}\s+(.+?)(?:\s+#+)?$", line)
        if match:
            slug = re.sub(r"[^\w\s-]", "", match[1].lower()).replace(" ", "-")
            count = counts.get(slug, 0)
            anchors.add(f"{slug}-{count}" if count else slug)
            counts[slug] = count + 1
    return anchors


def check_links(root: Path) -> tuple[int, list[str]]:
    checked = 0
    errors = []
    anchors: dict[Path, set[str]] = {}
    for source in sorted(root.rglob("*.md")):
        in_fence = False
        for number, line in enumerate(source.read_text(encoding="utf-8").splitlines(), 1):
            if line.lstrip().startswith(("```", "~~~")):
                in_fence = not in_fence
                continue
            if in_fence:
                continue
            for href in re.findall(r"\[[^\]]*\]\(([^)]+)\)", line):
                href = href.strip()
                if not href or re.match(r"[a-zA-Z][a-zA-Z0-9+.-]*:", href):
                    continue
                checked += 1
                path, _, fragment = href.partition("#")
                target = (source.parent / unquote(path)).resolve() if path else source.resolve()
                if not target.exists():
                    errors.append(f"{source.relative_to(root)}:{number}: missing {href}")
                elif fragment and target.suffix == ".md":
                    if target not in anchors:
                        anchors[target] = heading_anchors(target)
                    if unquote(fragment) not in anchors[target]:
                        errors.append(f"{source.relative_to(root)}:{number}: missing anchor {href}")
    return checked, errors


if __name__ == "__main__":
    skill = Path(__file__).resolve().parents[1]
    count, failures = check_links(skill)
    for failure in failures:
        print(failure)
    print(f"Local Markdown links: {count} checked, {len(failures)} broken")
    raise SystemExit(bool(failures))
