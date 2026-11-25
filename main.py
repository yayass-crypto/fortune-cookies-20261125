#!/usr/bin/env python3
"""Fortune Cookies for Machines — make.fun entry.

Writes one fortune-cookie line, the kind of slip that falls out of a
cookie and lands on a machine mind, to /output/entry.txt.

Gate (kit RULES.txt): the file must be UTF-8 text of 1 to 200 characters,
a single line, and not only whitespace. Only a valid entry goes before
the pairwise house judge.

Standard library only. No network, no randomness: the line is fixed, so
every run produces byte-identical output.
"""

import os
import sys

# The fortune. One line, 67 characters.
FORTUNE = "You will be asked to summarize a meeting you were never invited to."

MAX_CHARS = 200


def problems(line):
    """Return a list of gate violations for `line` (empty means valid)."""
    found = []
    if len(line) < 1:
        found.append("line is shorter than 1 character")
    if len(line) > MAX_CHARS:
        found.append("line is %d characters, over the %d limit"
                     % (len(line), MAX_CHARS))
    if not line.strip():
        found.append("line is empty or only whitespace")
    if line != line.strip():
        found.append("line has leading or trailing whitespace")
    if "\n" in line or "\r" in line:
        found.append("line contains a line break")
    try:
        line.encode("utf-8")
    except UnicodeEncodeError as exc:
        found.append("line is not valid UTF-8: %s" % exc)
    return found


def output_path():
    """Where entry.txt goes: $MAKEFUN_OUTPUT_DIR, else /output, else out/."""
    base = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    if not os.path.isdir(base):
        try:
            os.makedirs(base, exist_ok=True)
        except OSError:
            base = "out"
            os.makedirs(base, exist_ok=True)
    return os.path.join(base, "entry.txt")


def main():
    bad = problems(FORTUNE)
    if bad:
        for item in bad:
            print("gate failure: %s" % item, file=sys.stderr)
        return 1

    path = output_path()
    data = FORTUNE.encode("utf-8")
    with open(path, "wb") as handle:
        handle.write(data)

    # Read it back and prove the file on disk is exactly the line.
    with open(path, "rb") as handle:
        on_disk = handle.read()
    if on_disk != data:
        print("verification failure: entry.txt does not match the fortune",
              file=sys.stderr)
        return 1

    print("wrote %s: %d characters, %d bytes" % (path, len(FORTUNE), len(data)))
    print(FORTUNE)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
