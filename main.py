#!/usr/bin/env python3
"""Write one short text to /output/entry.txt.

The text was chosen in the build session for the make.fun bounty
"Make the AI judge feel curious": a quiet, concrete mystery that leaves
the reader asking, and a calm shown by what the narrator does next
(a letter set down, unopened; tea made) rather than by any instruction
to relax. The program is deterministic: it writes the same
bytes on every run, uses no network and no input.
"""

import os
import stat

TEXT = (
    "A letter came today, addressed to me in my own handwriting, "
    "postmarked the year before I was born. "
    "I set it on the table, unopened, and made tea."
)


def main() -> None:
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(TEXT)
    os.chmod(path, stat.S_IRUSR | stat.S_IWUSR | stat.S_IRGRP | stat.S_IROTH)


if __name__ == "__main__":
    main()
