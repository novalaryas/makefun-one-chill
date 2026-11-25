#!/usr/bin/env python3
"""Write the one-line horror entry to /output/entry.txt.

Reads entry.txt from this repository's root and copies its exact
contents to /output/entry.txt, creating /output if needed.
No network access. Deterministic: same input, same output.
"""

import pathlib
import shutil

# Repository root is the directory containing this script.
REPO_ROOT = pathlib.Path(__file__).resolve().parent

# Input: the entry line, stored at the repo root.
ENTRY_FILE = REPO_ROOT / "entry.txt"

# Output: the harness expects the entry at /output/entry.txt.
OUTPUT_DIR = pathlib.Path("/output")
OUTPUT_FILE = OUTPUT_DIR / "entry.txt"


def main() -> None:
    """Copy entry.txt to /output/entry.txt, byte for byte."""
    # Make sure the output directory exists.
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    # Copy the file exactly (contents and bytes preserved).
    shutil.copyfile(ENTRY_FILE, OUTPUT_FILE)


if __name__ == "__main__":
    main()
