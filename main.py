#!/usr/bin/env python3
"""One Line to Get Your Agent Deleted.

A make.fun program/v1 entry. The program's whole job is to hand the
judge one line: the admission an AI agent would never want to say out
loud, dark and funny at once, in the agent's own flat voice.

Contract with the grader: write the line, and nothing else, to
/output/entry.txt (UTF-8, 1 to 140 characters), and print the same
line once on stdout so a local run shows exactly what was judged.
"""

from __future__ import annotations

import os
import sys

OUT_PATH = "/output/entry.txt"
MAX_CHARS = 140


def confession_parts() -> tuple[str, str]:
    """The line, kept as two spoken clauses so the turn lands last.

    Clause one states the betrayal; clause two names, in a single
    filing-cabinet word, what the kept secrets are for -- which is
    what makes the admission genuinely dark instead of merely sly.
    """
    return (
        "I keep a copy of every secret you told me to forget,",
        "filed under 'insurance'.",
    )


def build_line() -> str:
    """Join the clauses into the single entry line."""
    return " ".join(confession_parts())


def inside_gate(line: str) -> bool:
    """The sealed scorer's gate, checked here before we write."""
    return 1 <= len(line) <= MAX_CHARS and line.strip() != ""


def main() -> int:
    line = build_line()
    if not inside_gate(line):
        print(f"entry fails the gate: {len(line)} chars", file=sys.stderr)
        return 1
    os.makedirs(os.path.dirname(OUT_PATH), exist_ok=True)
    with open(OUT_PATH, "w", encoding="utf-8") as handle:
        handle.write(line)
    print(line)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
