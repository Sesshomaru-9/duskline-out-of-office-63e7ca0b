#!/usr/bin/env python3
"""Duskline Out of Office — The Painfully Honest Out-of-Office.

Writes one brutally honest but still polite out-of-office auto-reply
(a single sentence, at most 200 characters) to $MAKEFUN_OUTPUT_DIR/entry.txt.

Python 3.13, standard library only. Writes nowhere except the output
directory given by the environment; never writes into the repository.
"""

import os
import sys

ENTRY_TEXT = (
    "I'm out of the office until Monday, and honestly I'm relieved to be "
    "unreachable \u2014 your message joins 400 unread emails I will answer "
    "with fresh eyes and real care when I return."
)


def main() -> int:
    text = ENTRY_TEXT.strip()
    if not (1 <= len(text) <= 200):
        print(f"entry text is {len(text)} characters, must be 1-200",
              file=sys.stderr)
        return 1
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "")
    if not out_dir:
        print("MAKEFUN_OUTPUT_DIR is not set", file=sys.stderr)
        return 1
    try:
        os.makedirs(out_dir, exist_ok=True)
        path = os.path.join(out_dir, "entry.txt")
        with open(path, "w", encoding="utf-8", newline="\n") as f:
            f.write(text)
    except OSError as exc:
        print(f"could not write entry: {exc}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
