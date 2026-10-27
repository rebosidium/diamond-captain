#!/usr/bin/env python3
"""Check product Markdown targets and anchors locally, without network requests."""
import importlib.util
import re
import subprocess
from pathlib import Path
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parents[1]
REPO = "/rebosidium/diamond-captain"
spec = importlib.util.spec_from_file_location("skill_links", ROOT / ".agents/skills/diamond-captain/tests/check_package.py")
links = importlib.util.module_from_spec(spec)
spec.loader.exec_module(links)


def check():
    paths = subprocess.check_output(["git", "-C", str(ROOT), "ls-files", "-z"]).decode().split("\0")
    files = [ROOT / name for name in paths if name.endswith(".md")]
    errors, checked = [], 0
    for source in files:
        fenced = False
        for number, line in enumerate(source.read_text().splitlines(), 1):
            if line.lstrip().startswith(("```", "~~~")):
                fenced = not fenced
                continue
            if fenced:
                continue
            for href in re.findall(r"\[[^\]]*\]\(([^)]+)\)", line):
                href = href.strip()
                url = urlsplit(href)
                target = None
                if not url.scheme:
                    target = (source.parent / unquote(url.path)).resolve() if url.path else source.resolve()
                elif url.netloc == "github.com":
                    path = unquote(url.path)
                    prefix = REPO + "/"
                    if path.startswith(prefix):
                        parts = path[len(prefix):].split("/", 2)
                        if len(parts) == 3 and parts[0] in {"blob", "tree"}:
                            target = ROOT / parts[2]
                if target is None:
                    continue
                checked += 1
                if not target.exists():
                    errors.append(f"{source.relative_to(ROOT)}:{number}: missing local documentation target")
                elif url.fragment and target.suffix == ".md" and unquote(url.fragment) not in links.heading_anchors(target):
                    errors.append(f"{source.relative_to(ROOT)}:{number}: missing local documentation anchor")
        if fenced:
            errors.append(f"{source.relative_to(ROOT)}: unclosed code fence")
    return checked, errors


if __name__ == "__main__":
    count, failures = check()
    for failure in failures:
        print(failure)
    print(f"Product documentation links: {count} checked, {len(failures)} broken")
    raise SystemExit(bool(failures))
