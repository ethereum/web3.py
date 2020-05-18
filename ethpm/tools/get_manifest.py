import json
from typing import (
    Any,
    Dict,
)

from ethpm import (
    ETHPM_SPEC_DIR,
)


def get_manifest(use_case: str, filename: str) -> Dict[str, Any]:
    return json.loads((ETHPM_SPEC_DIR / 'examples' / use_case / filename).read_text())
