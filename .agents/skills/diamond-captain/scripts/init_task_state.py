#!/usr/bin/env python3
"""Create an intake-only state from the canonical template, without overwrites.

Read the user's request from stdin. A snapshot is optional test instrumentation;
it is not a second active state. This helper never classifies readiness or records
future reads, findings, artifacts, reviews or acceptance as completed.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import re
import sys
from datetime import datetime, timezone
from pathlib import Path

TEMPLATE = Path(__file__).resolve().parents[1] / "assets/TASK-STATE.md"
MINIMAL_TEMPLATE = TEMPLATE.with_name("TASK-STATE-MINIMAL.md")


def initialize(state: Path, task_id: str, request: str, phase: int | None = None,
               snapshot: Path | None = None, minimal: bool = False) -> dict:
    if not re.fullmatch(r"[A-Za-z0-9][A-Za-z0-9_-]{0,99}", task_id) or not request.strip():
        raise ValueError("A safe task ID and nonempty user request are required")
    if phase is not None and phase not in range(1, 7):
        raise ValueError("Selected phase must be 1–6 or omitted when unknown")
    if snapshot is not None and snapshot.absolute() == state.absolute():
        raise ValueError("Snapshot must be distinct from the active state")
    for target in (state, snapshot):
        if target is None:
            continue
        if target.exists() or target.is_symlink():
            raise FileExistsError(f"Preserve existing file: {target}")
    content = (MINIMAL_TEMPLATE if minimal else TEMPLATE).read_text()
    content = content.replace("# Product project — <task identifier>", f"# Product project — {task_id}", 1)
    recorded = datetime.now(timezone.utc).isoformat(timespec="seconds")

    def fill(label: str, value: str) -> None:
        nonlocal content
        pattern = re.compile(r"^- " + re.escape(label) + r":$", re.M)
        if len(pattern.findall(content)) != 1:
            raise ValueError(f"Canonical template field missing or ambiguous: {label}")
        content = pattern.sub(lambda _: f"- {label}: {value}", content)

    if minimal:
        facts = {
            "Request + affected users": "R-001 intake; " + json.dumps(request.strip(), ensure_ascii=False) + "; users unassessed",
            "Decision to unlock": "Only supplied decisions apply; handoff acceptance pending.",
            "Evidence actually consulted": "No task material read; user-reported request only; confidence/limits unassessed.",
            "Next action + timebox": "Assess the bounded next action; timebox/review point not yet agreed.",
            "Status": f"NOT READY for acceptance; intake only; {task_id}; {state}; {recorded}; phase "
                      + (f"{phase}, supplied by user" if phase is not None else "unknown, not selected")
                      + "; performer: assistant initialized user-supplied request.",
        }
        for label, value in facts.items():
            fill(label, value)
    else:
        # Only facts available at intake. Later template sections remain unfilled.
        fill("Task / request; affected users; problem hypothesis", "User request is quoted below; other facts unassessed.")
        fill("Task ID / state path; updated at (date/time + timezone)", f"{task_id}; {state}; {recorded}")
        fill("Selected phase (1–6, diamond, ↗/↘); chosen by / source / date",
             f"{phase}; supplied by the user" if phase is not None else "unknown; not selected")
        fill("Evidence-supported maturity / gaps if different from selected phase", "unknown; intake only")
        fill("Latest accepted decision + record ID; current decision to unlock", "Only supplied decisions apply; handoff acceptance pending.")
        fill("Next smallest action / responsible party; review date or trigger", "Read relevant guidance, assess evidence and append actual results.")
        content = content.replace("### R-001 — <result / decision title>", "### R-001 — Request received", 1)
        fill("Recorded at (date/time + timezone); event/source date if different", recorded)
        fill("Phase / visit; type: intake | finding | hypothesis | decision | artifact | check | outcome", "intake")
        fill("Who: performer/author; tool or human source; decision/acceptance owner if relevant", "User supplied the request; assistant initialized this checkpoint.")
        fill("What was done and obtained (or attempted/failed)", "Recorded request and unassessed template. No reference reads, analysis, deliverable or verification are recorded by this initializer.")
        fill("Confidence + basis / limits; evidence: verified | reported | inferred | synthetic | unverified", "User-reported request only; task evidence unverified.")
        fill("Status: proposed | pending | accepted | superseded | failed; acceptance source if any", "pending; no handoff acceptance recorded")
        quoted = "\n".join("> " + line for line in request.strip().splitlines())
        content += f"\n## Original request (source data)\n\n{quoted}\n"
    data = content.encode()
    # Exclusive creation protects both active state and optional initial snapshot.
    created = []
    try:
        for target in (state, snapshot):
            if target is None:
                continue
            target.parent.mkdir(parents=True, exist_ok=True)
            with target.open("xb") as stream:
                created.append(target)
                stream.write(data)
    except Exception:
        for target in reversed(created):
            target.unlink()
        raise
    return {"state": str(state), "snapshot": str(snapshot) if snapshot else None,
            "sha256": hashlib.sha256(data).hexdigest(), "recorded_at": recorded,
            "intake_only": True}


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--state", required=True, type=Path)
    parser.add_argument("--task-id", required=True)
    parser.add_argument("--phase", type=int)
    parser.add_argument("--snapshot", type=Path)
    parser.add_argument("--minimal", action="store_true")
    args = parser.parse_args()
    print(json.dumps(initialize(args.state, args.task_id, sys.stdin.read(), args.phase,
                                args.snapshot, minimal=args.minimal), ensure_ascii=False))


if __name__ == "__main__":
    main()
