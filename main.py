"""The Moon Finally Answers Back — make.fun bounty entry.

Writes a single line, in the voice of the Moon replying at last to the
wishes, howls and late-night promises of everyone staring up at it,
to $MAKEFUN_OUTPUT_DIR/entry.txt (or /output/entry.txt by default).
"""

import os

LINE = (
    "Look, I've heard every wish, howl, and 2 a.m. promise for four "
    "billion years \u2014 and not one of you has ever once wished ME a "
    "good night."
)

MAX_CHARS = 240


def main():
    line = LINE
    if not line or not line.strip():
        raise ValueError("entry line must not be empty or only whitespace")
    if "\n" in line or "\r" in line:
        raise ValueError("entry line must be a single line")
    if len(line) > MAX_CHARS - 1:
        raise ValueError(
            "entry line is %d characters, over the 239-character limit"
            % len(line)
        )

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "entry.txt")
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(line + "\n")

    with open(out_path, "r", encoding="utf-8") as f:
        written = f.read()
    if written != line + "\n":
        raise ValueError("verification failed: entry.txt does not match")
    print("Wrote %d characters to %s" % (len(line), out_path))


if __name__ == "__main__":
    main()
