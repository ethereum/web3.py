import json
from typing import (
    Any,
    Dict,
)

from ethpm import (
    ASSETS_DIR,
    ETHPM_SPEC_DIR,
)


def get_ethpm_spec_manifest(use_case: str, filename: str) -> Dict[str, Any]:
    return json.loads((ETHPM_SPEC_DIR / 'examples' / use_case / filename).read_text())


def get_ethpm_local_manifest(use_case: str, filename: str) -> Dict[str, Any]:
    return json.loads((ASSETS_DIR / use_case / filename).read_text())
