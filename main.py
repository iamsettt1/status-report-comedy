#!/usr/bin/env python3
"""Status Report Comedy Sprint entry.

Writes exactly one line of UTF-8 text to /output/entry.txt.
Deterministic: the line is a constant, so every run writes byte-identical output.
Standard library only; no network, no reads outside the repo.
"""

import os

LINE = (
    "Weekly status: I finished all 38 tasks, then spent the rest of the week "
    "re-reading my own summary to remember what I'd finished."
)


def main() -> None:
    # The gate allows 1-200 characters; fail loudly rather than emit an invalid line.
    assert 1 <= len(LINE) <= 200, f"line is {len(LINE)} chars, must be 1-200"
    assert LINE == LINE.strip(), "line must not carry leading/trailing whitespace"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="\n") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()
