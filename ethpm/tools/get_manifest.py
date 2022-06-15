import json
from typing import (
    Any,
    Dict,
)

from ethpm import (
    ASSETS_DIR,
    get_ethpm_spec_dir,
)


def get_ethpm_spec_manifest(use_case: str, filename: str) -> Dict[str, Any]:
    ethpm_spec_dir = get_ethpm_spec_dir()
    return json.loads((ethpm_spec_dir / "examples" / use_case / filename).read_text())


def get_ethpm_local_manifest(use_case: str, filename: str) -> Dict[str, Any]:
    return json.loads((ASSETS_DIR / use_case / filename).read_text())
