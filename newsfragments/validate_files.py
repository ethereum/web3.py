#!/usr/bin/env python3

# Towncrier silently ignores files that do not match the expected ending.
# We use this script to ensure we catch these as errors in CI.

import pathlib
import sys

ALLOWED_EXTENSIONS = {
    ".breaking.rst",
    ".bugfix.rst",
    ".deprecation.rst",
    ".docs.rst",
    ".feature.rst",
    ".internal.rst",
    ".misc.rst",
    ".performance.rst",
    ".removal.rst",
}

ALLOWED_FILES = {
    "validate_files.py",
    "README.md",
}

THIS_DIR = pathlib.Path(__file__).parent

num_args = len(sys.argv) - 1
assert num_args in {0, 1}
if num_args == 1:
    assert sys.argv[1] in ("is-empty",)

for fragment_file in THIS_DIR.iterdir():
    if fragment_file.name in ALLOWED_FILES:
        continue
    elif num_args == 0:
        full_extension = "".join(fragment_file.suffixes)
        if full_extension not in ALLOWED_EXTENSIONS:
            raise Exception(f"Unexpected file: {fragment_file}")
    elif sys.argv[1] == "is-empty":
        raise Exception(f"Unexpected file: {fragment_file}")
    else:
        raise RuntimeError(
            f"Strange: arguments {sys.argv} were validated, but not found"
        )
