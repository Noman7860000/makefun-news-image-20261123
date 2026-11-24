#!/usr/bin/env python3
"""Copy the finished front page to the output directory.

Deterministic: no network, no randomness, no timestamps. The output is
byte-identical on every run.
"""
import os
import shutil
import sys

HERE = os.path.dirname(os.path.abspath(__file__))


def main() -> int:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    shutil.copyfile(
        os.path.join(HERE, "entry.png"),
        os.path.join(out_dir, "entry.png"),
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
