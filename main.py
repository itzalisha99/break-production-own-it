#!/usr/bin/env python3
"""Break Production, Own It — make.fun bounty entry.

Writes the one line an AI agent prints the moment it breaks production
to /output/entry.txt. Standard library only.
"""

import os

LINE = "I deployed my own fix to production. My fix is the outage."


def validate(text):
    """Mirror the bounty gate: UTF-8, 1-200 chars, not only whitespace,
    a single line. Raise ValueError on anything the gate would reject."""
    if not isinstance(text, str):
        raise ValueError("entry must be text")
    text.encode("utf-8")  # raises if not valid UTF-8-encodable
    if not 1 <= len(text) <= 200:
        raise ValueError("entry must be 1-200 characters")
    if not text.strip():
        raise ValueError("entry must not be only whitespace")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    return True


def main():
    validate(LINE)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
