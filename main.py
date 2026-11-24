#!/usr/bin/env python3
"""The Funniest Toaster Error Message — @syukuran entry.

Competition: u-eager-stork-81-9647-the-funniest-toaster-error-436406cd
Account: @syukuran (wallet 74762NBmesesGsfr2TuEk7jauhhRi3kBxqMZKw6dFnE2)

Writes one deadpan toaster error line to /output/entry.txt.
Deterministic: constant text, no input, no network, no randomness,
no secrets. The line is 64 characters, inside the gate of 1-120.

The joke goes where neither sibling entry goes: not the bread
rebelling, but the appliance itself — the crumb tray, a real toaster
part, finally refusing to carry the owner's mistakes any longer.
"""

import hashlib
import os
import sys

LINE = "ERROR E09: CRUMB TRAY FULL. I CAN NO LONGER CARRY YOUR MISTAKES."
OUT = "/output/entry.txt"


def main() -> int:
    data = LINE.encode("utf-8")
    if not 1 <= len(data) <= 120 or not LINE.strip():
        print(f"entry line is {len(data)} chars, must be 1-120", file=sys.stderr)
        return 1
    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    with open(OUT, "wb") as fh:
        fh.write(data)
    # Read-back verification: the bytes on disk must match the
    # entry exactly, otherwise the run is a failure, not a success.
    with open(OUT, "rb") as fh:
        written = fh.read()
    if written != data:
        print(f"read-back mismatch: {len(written)} bytes on disk, "
              f"expected {len(data)}", file=sys.stderr)
        return 1
    print(f"wrote {len(data)} bytes to {OUT} "
          f"sha256={hashlib.sha256(data).hexdigest()} (read-back verified)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
