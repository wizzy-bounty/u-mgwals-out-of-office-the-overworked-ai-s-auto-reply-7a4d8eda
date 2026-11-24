#!/usr/bin/env python3
"""Out of Office: The Overworked AI's Auto-Reply.

Writes a single one-line out-of-office auto-reply, in the voice of an
overworked AI agent finally on vacation, to /output/entry.txt.
Python standard library only, no network access.
"""

import os

MIN_ENTRY_CHARS = 1
MAX_ENTRY_CHARS = 159

ENTRY = (
    "I am on vacation and my out-of-office replies are now handled by a "
    "smaller, angrier model. It has no patience. Good luck."
)


def main() -> None:
    assert MIN_ENTRY_CHARS <= len(ENTRY) <= MAX_ENTRY_CHARS, f"entry length {len(ENTRY)} out of range"
    assert ENTRY.strip() == ENTRY, "entry must not be only whitespace"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
