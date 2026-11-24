"""Funniest out-of-office entry.

Writes one line of an out-of-office auto-reply to
$MAKEFUN_OUTPUT_DIR/entry.txt. Standard library only; the line is
defined here and nowhere else is read.
"""

import os
import sys

REPLY = (
    "I'm out until Tuesday. Dave has my inbox. Dave has never answered "
    "an email in his life, and today will not be the day he starts."
)


def run() -> int:
    text = REPLY.strip()
    if not 1 <= len(text) <= 140 or "\n" in text:
        print("reply fails the 1-140 character single-line gate", file=sys.stderr)
        return 1
    target_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(target_dir, exist_ok=True)
    destination = os.path.join(target_dir, "entry.txt")
    # One line plus a trailing newline, written with an explicit newline
    # so the output is byte-identical wherever the grader runs it.
    with open(destination, "w", encoding="utf-8", newline="\n") as handle:
        handle.write(text + "\n")
    return 0


if __name__ == "__main__":
    sys.exit(run())
