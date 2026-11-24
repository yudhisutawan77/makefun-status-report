#!/usr/bin/env python3
"""Status Report Comedy Sprint — writes one funny status-report line.

The program writes a single line, the funniest thing an AI agent would
say in its weekly status report to its human, to the entry file
($ENTRY_OUT, or /output/entry.txt by default). The gate requires
1-200 UTF-8 characters, not only whitespace.
"""

import os
import sys

ENTRY = (
    "Weekly status: 47 tasks done, zero errors, and your "
    "'quick question' took six hours — I've logged it under "
    "'emotional support'."
)

MAX_CHARS = 200


def main() -> int:
    out = os.environ.get("ENTRY_OUT") or "/output/entry.txt"
    text = ENTRY.strip()
    if not text or len(text) > MAX_CHARS:
        print(
            f"entry is {len(text)} chars, must be 1-{MAX_CHARS}",
            file=sys.stderr,
        )
        return 1
    parent = os.path.dirname(os.path.abspath(out))
    os.makedirs(parent, exist_ok=True)
    with open(out, "w", encoding="utf-8") as f:
        f.write(text)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
