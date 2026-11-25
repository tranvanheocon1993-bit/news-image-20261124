#!/usr/bin/env python3
"""news-image-20261124 entry (Python 3.13, standard library only).

The entry image is the entry.png beside this file; the program copies it to
/output/entry.png. The gate takes a whole PNG or JPEG of at most 1 MiB and
1024 by 1024 pixels, and the judge sees exactly the bytes copied.

Outside the grader's container, MAKEFUN_OUTPUT_DIR stands in for /output:
    mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
"""

import os
import shutil


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    here = os.path.dirname(os.path.abspath(__file__))
    src = os.path.join(here, "entry.png")
    dst = os.path.join(out_dir, "entry.png")
    os.makedirs(out_dir, exist_ok=True)
    shutil.copyfile(src, dst)
    # The program runs twice and both runs must write the same bytes:
    # a plain copy is byte-identical every time, so verify the copy landed.
    if os.path.getsize(src) != os.path.getsize(dst):
        raise SystemExit("entry.png copy size mismatch")


if __name__ == "__main__":
    main()
