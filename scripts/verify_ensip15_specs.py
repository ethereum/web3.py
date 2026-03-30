"""
Verify local ENSIP-15 spec and test files match the upstream sources.

Run this script manually when updating ENSIP-15 files or to check if
upstream has published new versions.

Upstream links are referenced in the ENSIP-15 specification:
https://docs.ens.domains/ensip/15

Usage:
    python scripts/verify_ensip15_specs.py
"""

import json
import os
import sys

import requests

REPO_ROOT = os.path.join(os.path.dirname(__file__), "..")
ENSIP15_BASE = "https://raw.githubusercontent.com/adraffy/ens-normalize.js/main"

FILES = {
    "spec.json": {
        "local": os.path.join(REPO_ROOT, "ens", "specs", "normalization_spec.json"),
        "upstream": f"{ENSIP15_BASE}/derive/output/spec.json",
    },
    "nf.json": {
        "local": os.path.join(REPO_ROOT, "ens", "specs", "nf.json"),
        "upstream": f"{ENSIP15_BASE}/derive/output/nf.json",
    },
    "tests.json": {
        "local": os.path.join(
            REPO_ROOT, "tests", "ens", "normalization", "normalization_tests.json"
        ),
        "upstream": f"{ENSIP15_BASE}/validate/tests.json",
    },
}

all_match = True
for name, paths in FILES.items():
    with open(paths["local"]) as f:
        local_data = json.load(f)

    response = requests.get(paths["upstream"], timeout=30)
    response.raise_for_status()
    upstream_data = response.json()

    if local_data == upstream_data:
        print(f"  {name}: up to date")
    else:
        print(f"  {name}: OUT OF DATE — update from {paths['upstream']}")
        all_match = False

if all_match:
    print("\nAll ENSIP-15 files match upstream.")
else:
    print("\nOne or more files need updating.")
    sys.exit(1)
