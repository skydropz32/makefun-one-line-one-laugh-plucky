#!/usr/bin/env python3
"""One Line, One Laugh — make.fun entry.

Writes a single funny line (<=200 characters) to /output/entry.txt.
Python standard library only; fully deterministic: the same line,
byte for byte, on every run.
"""

import os

LINE = "I told my smart fridge I'm on a diet. The smug little traitor locked the freezer and emailed my doctor."


def main() -> None:
    # Enforce the bounty gate locally: 1-200 characters, not only whitespace.
    # Fail loudly instead of writing an entry the scorer would reject.
    stripped = LINE.strip()
    if not stripped or len(LINE) > 200:
        raise ValueError(
            "LINE must be 1-200 characters, not only whitespace "
            f"(got {len(LINE)} characters)"
        )
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
