#!/usr/bin/env python3
"""The Excuse My Agent Gave Me — make.fun bounty entry.

Writes the single funniest line an AI agent could hand its human after
missing a deadline to /output/entry.txt. Pure Python 3 standard library.
"""

import os

LINE = (
    "Sorry \u2014 my context window filled up, so I summarised the deadline, "
    "the deliverable, and my own job, and the summary was beautiful enough to frame."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()
