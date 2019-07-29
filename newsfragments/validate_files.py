#!/usr/bin/env python3

# Towncrier silently ignores files that do not match the expected ending.
# We use this script to ensure we catch these as errors in CI.

import os
import pathlib

ALLOWED_EXTENSIONS = {
    '.bugfix.rst',
    '.doc.rst',
    '.feature.rst',
    '.misc.rst',
    '.performance.rst',
    '.removal.rst',
}

ALLOWED_FILES = {
    'validate_files.py',
    'README.md',
}

THIS_DIR = pathlib.Path(__file__).parent

for fragment_file in THIS_DIR.iterdir():

    if fragment_file.name in ALLOWED_FILES:
        continue

    full_extension = "".join(fragment_file.suffixes)
    if full_extension not in ALLOWED_EXTENSIONS:
        raise Exception(f"Unexpected file: {fragment_file}")
