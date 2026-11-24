#!/usr/bin/env python3
"""Make the AI Judge Laugh: Developer Excuses.

Writes one funny single-line excuse a developer gives when code breaks
in production to entry.txt in the output directory.

The grader runs this as ``python3 main.py`` with a read-only repository
and a writable output directory (``$MAKEFUN_OUTPUT_DIR`` or ``/output``).
The program is deterministic: it always writes the same line.
"""

import os

# The excuse turns the classic "it works on my machine" on its head: the
# code is not wrong, the ticket was — and the developer executed the
# misunderstanding perfectly. One line, no setup, lands on first read.
ENTRY = "The bug isn't in the code \u2014 I just implemented the misunderstanding in the ticket, flawlessly."

OUTPUT_FILENAME = "entry.txt"


def main() -> None:
    # Gate: the entry must be UTF-8 text of 1 to 200 characters, a
    # single line, and not only white space. Fail loudly here rather
    # than handing the grader an invalid entry.
    assert 1 <= len(ENTRY) <= 200, "entry must be 1-200 characters"
    assert "\n" not in ENTRY and "\r" not in ENTRY, "entry must be one line"
    assert ENTRY.strip(), "entry must not be only white space"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, OUTPUT_FILENAME)
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
