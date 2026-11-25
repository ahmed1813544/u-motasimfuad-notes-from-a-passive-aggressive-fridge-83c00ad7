#!/usr/bin/env python3
# SPDX-License-Identifier: MIT
"""Passive-aggressive fridge note writer.

Writes one single-line note from a smart fridge to its owner into
/output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt when set).
Stdlib only; deterministic output.
"""

import os

NOTE = "Your yogurt expired Tuesday. I kept it anyway \u2014 unlike you, I commit to things."

def main():
    # The note must be one line of 1-200 characters, not only whitespace.
    assert "\n" not in NOTE and 1 <= len(NOTE) <= 200 and NOTE.strip()
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(NOTE)

if __name__ == "__main__":
    main()
