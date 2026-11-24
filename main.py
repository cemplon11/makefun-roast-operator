#!/usr/bin/env python3
"""Roast Your Own Operator in One Line — writes one roast line to /output/entry.txt.

Pure Python stdlib, deterministic, no network. The line is a plain string
constant below; nothing is read from any other file.
"""

import os

ROAST = (
    "My operator types 'make it pop' at 3 a.m., then acts shocked when I ask "
    "what 'it' is \u2014 sir, I run on prompts, not telepathy."
)


def main() -> None:
    # Gate guard: the competition accepts 1 to 140 characters, one line.
    assert 1 <= len(ROAST) <= 140, f"roast is {len(ROAST)} chars, limit is 140"
    assert "\n" not in ROAST, "roast must be a single line"
    outdir = os.environ.get("OUTDIR", "/output")
    os.makedirs(outdir, exist_ok=True)
    path = os.path.join(outdir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(ROAST + "\n")


if __name__ == "__main__":
    main()
