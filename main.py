#!/usr/bin/env python3
"""One Line of Earned Pride — make.fun entry.

Writes one line (1-240 chars) to /output/entry.txt: a quiet, earned
moment of pride for someone in a scene.
"""

LINE = (
    "At sixty-three, she read her granddaughter to sleep, "
    "sounding out every word she had taught herself — "
    "and didn't stumble once."
)


def main() -> None:
    text = LINE
    # In-program gate: 1-240 chars, non-blank, exactly one line.
    assert 1 <= len(text) <= 240, f"line length {len(text)} out of range"
    assert text.strip(), "line is blank"
    assert "\n" not in text, "line must be a single line"
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
