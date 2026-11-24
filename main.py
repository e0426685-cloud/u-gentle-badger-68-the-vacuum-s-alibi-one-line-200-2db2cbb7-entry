"""The Vacuum's Alibi: one line, 200 characters or fewer.

A robot vacuum's deadpan excuse for the spot it missed.
Writes the line to /output/entry.txt. Python standard library
only, fully deterministic.
"""

import os

LINE = (
    "I did not miss that spot. My sensors logged it as a crime scene: "
    "one sock, zero dust, and a crumb that looked back. "
    "I left it for the mop."
)


def main() -> None:
    assert "\n" not in LINE and "\r" not in LINE, "entry must be a single line"
    assert LINE.strip(), "entry must not be only whitespace"
    assert 1 <= len(LINE) <= 200, f"entry must be 1-200 chars, got {len(LINE)}"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)
    with open("/output/entry.txt", "r", encoding="utf-8") as f:
        written = f.read()
    assert written == LINE, "written entry does not match"
    assert written.count("\n") == 0 and 1 <= len(written) <= 200
    print(f"Wrote /output/entry.txt ({len(written)} characters)")


if __name__ == "__main__":
    main()
