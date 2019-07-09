import json
from typing import Any, Dict

from ethpm import ASSETS_DIR


def get_manifest(use_case: str, filename: str) -> Dict[str, Any]:
    return json.loads((ASSETS_DIR / use_case / filename).read_text())
