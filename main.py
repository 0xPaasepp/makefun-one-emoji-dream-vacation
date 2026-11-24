#!/usr/bin/env python3
"""Write the one-emoji dream vacation to /output/entry.txt.

Pure standard library. The entry is exactly one emoji: a desert
island -- the faraway place itself, a postcard in a single glyph.
No words, no variation selector, no trailing newline: 1 character,
4 bytes UTF-8, inside the gate of 1 to 8 characters. The variation
selector is left out on purpose: a house anchor stored with it
would be 7 bytes, so this 4-byte file can never read as a copy of
a fixed text.
"""

import os

ENTRY = "\U0001F3DD"


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
