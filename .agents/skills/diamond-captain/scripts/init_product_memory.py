#!/usr/bin/env python3
"""Create header-only product memory; never invent registry records or overwrite work."""
from __future__ import annotations

import argparse
import hashlib
import json
import re
from datetime import datetime, timezone
from pathlib import Path

TEMPLATE = Path(__file__).resolve().parents[1] / "assets/PRODUCT-MEMORY.md"


def initialize(memory: Path, product: str) -> dict:
    if not product.strip() or any(c in product for c in "\r\n"):
        raise ValueError("A nonempty, single-line product name is required")
    if memory.exists() or memory.is_symlink():
        raise FileExistsError(f"Preserve existing file: {memory}")
    recorded = datetime.now(timezone.utc).isoformat(timespec="seconds")
    content = TEMPLATE.read_text(encoding="utf-8")
    for label, value in (("Product / service", product.strip()),
                         ("Memory path", str(memory)),
                         ("Last reconciled (date/time + timezone)", recorded)):
        pattern = re.compile(r"^- " + re.escape(label) + r":$", re.M)
        if len(pattern.findall(content)) != 1:
            raise ValueError(f"Canonical template field missing or ambiguous: {label}")
        content = pattern.sub(lambda _: f"- {label}: {value}", content)
    data = content.encode("utf-8")
    memory.parent.mkdir(parents=True, exist_ok=True)
    created = False
    try:
        with memory.open("xb") as stream:
            created = True
            stream.write(data)
    except Exception:
        if created:
            memory.unlink()
        raise
    return {"memory": str(memory), "sha256": hashlib.sha256(data).hexdigest(),
            "recorded_at": recorded, "header_only": True}


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--memory", required=True, type=Path)
    parser.add_argument("--product", required=True)
    args = parser.parse_args()
    try:
        receipt = initialize(args.memory, args.product)
    except (ValueError, OSError) as error:
        parser.exit(1, f"{error}\n")
    print(json.dumps(receipt))


if __name__ == "__main__":
    main()
