#!/usr/bin/env python3
"""One Letter: Coffee or Tea — make.fun entry.

Writes exactly one letter to /output/entry.txt: A for coffee.
No word, no explanation, no punctuation — just the letter.
"""

import os


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write("A")  # letter A for coffee


if __name__ == "__main__":
    main()
