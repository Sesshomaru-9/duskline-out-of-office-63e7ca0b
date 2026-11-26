#!/usr/bin/env python3
"""Duskline Out of Office — The Painfully Honest Out-of-Office.

Writes one brutally honest but still polite out-of-office auto-reply
(a single sentence, at most 200 characters) to $MAKEFUN_OUTPUT_DIR/entry.txt.

Python 3.13, standard library only. The program writes nowhere except the
output directory named by the environment; it never writes into the
repository directory, needs no network, and exits with a clear message
instead of crashing when the output directory cannot be used.
"""

import os
import sys

ENTRY_TEXT = (
    "I'm out of the office until Monday, and honestly I'm relieved to be "
    "unreachable \u2014 your message joins 400 unread emails I will answer "
    "with fresh eyes and real care when I return."
)

MAX_CHARS = 200


def _valid(text: str) -> bool:
    """Gate mirror: UTF-8, 1-200 chars, not only whitespace, one sentence."""
    if not text or not text.strip():
        return False
    if len(text) > MAX_CHARS:
        return False
    if text.count(".") != 1 or not text.rstrip().endswith("."):
        return False
    return True


def _output_dir() -> str:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "").strip()
    if not out_dir:
        raise ValueError("MAKEFUN_OUTPUT_DIR is not set")
    return out_dir


def main() -> int:
    text = ENTRY_TEXT.strip()
    if not _valid(text):
        print(f"entry text fails the gate ({len(text)} chars)", file=sys.stderr)
        return 1
    try:
        out_dir = _output_dir()
        os.makedirs(out_dir, exist_ok=True)
        path = os.path.join(out_dir, "entry.txt")
        with open(path, "w", encoding="utf-8", newline="\n") as f:
            f.write(text)
        with open(path, "r", encoding="utf-8") as f:
            if f.read() != text:
                print("verify failed: entry.txt does not match", file=sys.stderr)
                return 1
    except (OSError, ValueError) as exc:
        print(f"could not write entry: {exc}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
