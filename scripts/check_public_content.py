#!/usr/bin/env python3
"""Reject private working evidence in public files, history and release payloads."""
from __future__ import annotations

import argparse
import io
import re
import subprocess
import sys
import tarfile
import zipfile
from pathlib import Path, PurePosixPath

ROOT = Path(__file__).resolve().parents[1]
MAX_ARCHIVE_BYTES = 25 * 1024 * 1024
PRIVATE_PARTS = {"private-archives", "private-cleanup", "comparisons", ".product-task", ".local-publication"}
PATTERNS = {
    "local user path": re.compile(r"/(?:Users|home)/(?!example(?:/|\b)|user(?:/|\b)|username(?:/|\b))[^/\s<>\"']+/"),
    "private workspace link": re.compile(r"https://chatgpt\.com/(?:space/|c/)[^\s)\"<>]+"),
    "runtime identifier": re.compile(r'''["'](?:threadId|turnId|requestId|thread_id|session_id|conversation_id|request_id)["']\s*:\s*["'][0-9a-f]{8}-'''),
    "runtime usage measurement": re.compile(r'''["'](?:(?:input|output|total|cached_input|cache_write_input|reasoning_output)_tokens|(?:total|input|output|cachedInput|cacheWriteInput|reasoningOutput)Tokens|modelContextWindow|cost_usd|elapsed_seconds)["']\s*:\s*\d'''),
    "internal token measurement": re.compile(r"(?i)\b\d[\d,.]*\s+(?:o200k_base\s+)?tokens?\b|\b(?:input|output|cached input)\s*\|\s*\d"),
    "credential value": re.compile(r"(?:github_pat_[A-Za-z0-9_]{30,}|gh[pousr]_[A-Za-z0-9]{30,}|sk-(?:proj-|ant-)?[A-Za-z0-9_-]{32,}|AKIA[0-9A-Z]{16}|-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----)"),
    "credential in URL": re.compile(r"https?://[^\s\"<>]+[?&](?:token|key|secret|signature|auth)=[^\s\"<>]+", re.I),
    "personal Git identity": re.compile(r"[\w.+-]+@(?:gmail\.com|[^\s<>\"']+\.local)\b", re.I),
}


def private_path(name: str) -> bool:
    path = PurePosixPath(name)
    lower = path.name.lower()
    return (path.is_absolute() or ".." in path.parts or "\\" in name
            or bool(PRIVATE_PARTS.intersection(path.parts))
            or tuple(path.parts[:2]) == ("docs", "audits")
            or lower.endswith((".jsonl", ".log", ".bundle"))
            or "completed-events" in lower or "token-usage" in lower)


def check_entries(entries: dict[str, bytes], depth: int = 0) -> list[str]:
    failures = []
    for name, data in entries.items():
        if private_path(name):
            failures.append(f"{name}: private working-evidence path")
        if len(data) > MAX_ARCHIVE_BYTES:
            failures.append(f"{name}: oversized publication entry")
            continue
        lower = name.lower()
        if lower.endswith((".zip", ".tar", ".tar.gz", ".tgz")):
            if depth >= 3:
                failures.append(f"{name}: archive nesting limit")
                continue
            try:
                nested = {}
                total = 0
                if lower.endswith(".zip"):
                    with zipfile.ZipFile(io.BytesIO(data)) as archive:
                        for item in archive.infolist():
                            if item.is_dir():
                                continue
                            total += item.file_size
                            if total > MAX_ARCHIVE_BYTES or item.flag_bits & 1:
                                raise ValueError("oversized or encrypted archive")
                            if (item.external_attr >> 16) & 0o170000 == 0o120000:
                                raise ValueError("symlink in publication archive")
                            if item.filename in nested:
                                raise ValueError("duplicate archive entry")
                            nested[item.filename] = archive.read(item)
                else:
                    with tarfile.open(fileobj=io.BytesIO(data)) as archive:
                        for item in archive:
                            if item.isdir():
                                continue
                            total += item.size
                            if not item.isfile() or total > MAX_ARCHIVE_BYTES:
                                raise ValueError("unsupported or oversized archive entry")
                            if item.name in nested:
                                raise ValueError("duplicate archive entry")
                            nested[item.name] = archive.extractfile(item).read()
                failures.extend(f"{name}!{failure}" for failure in check_entries(nested, depth + 1))
            except (ValueError, OSError, RuntimeError, zipfile.BadZipFile, tarfile.TarError):
                failures.append(f"{name}: archive cannot be safely inspected")
            continue
        if b"\0" in data:
            continue
        for number, line in enumerate(data.decode("utf-8", "replace").splitlines(), 1):
            for reason, pattern in PATTERNS.items():
                if pattern.search(line):
                    # Never echo the matching private value into CI/public logs.
                    failures.append(f"{name}:{number}: {reason}")
    return failures


def git(root: Path, *args: str) -> bytes:
    return subprocess.check_output(["git", "-C", str(root), *args])


def blobs(root: Path, objects: dict[str, str]) -> dict[str, bytes]:
    unique = list(dict.fromkeys(objects.values()))
    process = subprocess.run(["git", "-C", str(root), "cat-file", "--batch"],
                             input=("\n".join(unique) + "\n").encode(), stdout=subprocess.PIPE, check=True)
    raw, offset, content = process.stdout, 0, {}
    for oid in unique:
        end = raw.index(b"\n", offset)
        header = raw[offset:end].split()
        size = int(header[2])
        content[oid] = raw[end + 1:end + 1 + size]
        offset = end + size + 2
    return {name: content[oid] for name, oid in objects.items()}


def tree_entries(root: Path, ref: str | None) -> dict[str, bytes]:
    if ref is None:
        raw = git(root, "ls-files", "--stage", "-z")
    else:
        raw = git(root, "ls-tree", "-r", "-z", ref)
    objects = {}
    for entry in raw.split(b"\0"):
        if not entry:
            continue
        meta, path = entry.split(b"\t", 1)
        fields = meta.split()
        objects[path.decode()] = fields[1 if ref is None else 2].decode()
    return blobs(root, objects)


def check_history(root: Path, refs: list[str]) -> list[str]:
    failures = []
    # Check every commit's tree, including paths deleted by later commits.
    objects = {}
    for commit in git(root, "rev-list", *refs).decode().splitlines():
        meta = git(root, "show", "-s", "--format=%ae%n%ce%n%B", commit).decode()
        identities = meta.splitlines()[:2]
        for email in identities:
            if not (email.endswith("@users.noreply.github.com") or email == "noreply@github.com"):
                failures.append(f"commit {commit[:12]}: use a GitHub noreply identity")
        failures.extend(check_entries({f"commit-{commit[:12]}.txt": meta.encode()}))
        for entry in git(root, "ls-tree", "-r", "-z", commit).split(b"\0"):
            if entry:
                fields, name = entry.split(b"\t", 1)
                oid = fields.split()[2].decode()
                # Each path/blob combination matters, even when content is shared.
                objects[(name.decode(), oid)] = oid
    content = blobs(root, {str(i): oid for i, oid in enumerate(dict.fromkeys(objects.values()))})
    by_oid = dict(zip(dict.fromkeys(objects.values()), content.values()))
    for (name, oid) in objects:
        failures.extend(check_entries({name: by_oid[oid]}))
    for ref in refs:
        kind = git(root, "cat-file", "-t", ref).decode().strip()
        if kind == "tag":
            failures.extend(check_entries({"tag-message.txt": git(root, "cat-file", "tag", ref)}))
    return sorted(set(failures))


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    mode = parser.add_mutually_exclusive_group()
    mode.add_argument("--staged", action="store_true", help="inspect the Git index")
    mode.add_argument("--tree", metavar="REF")
    mode.add_argument("--history", nargs="+", metavar="REF", help="inspect all reachable trees and commit metadata")
    mode.add_argument("--archive", type=Path)
    mode.add_argument("--text", type=Path, help="inspect public PR/release/Wiki text before upload")
    parser.add_argument("--root", type=Path, default=ROOT)
    args = parser.parse_args()
    if args.history:
        failures = check_history(args.root, args.history)
    elif args.archive or args.text:
        path = args.archive or args.text
        failures = check_entries({path.name: path.read_bytes()})
    else:
        failures = check_entries(tree_entries(args.root, None if args.staged else args.tree or "HEAD"))
    for failure in failures[:100]:
        print(failure, file=sys.stderr)
    if len(failures) > 100:
        print(f"Additional blocked entries: {len(failures) - 100}", file=sys.stderr)
    if failures:
        raise SystemExit(1)
    print("Public-content guard passed")


if __name__ == "__main__":
    main()
