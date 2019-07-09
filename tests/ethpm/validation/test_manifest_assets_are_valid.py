import json
import pytest

from ethpm import (
    ASSETS_DIR,
)
from ethpm.exceptions import (
    InsufficientAssetsError,
)
from ethpm.validation.manifest import (
    validate_manifest_against_schema,
)

SOURCES_GLOB = "**/*.json"


def get_all_manifest_paths():
    # Expects all json in ethpm/assets to be either compiler_output or a manifest
    all_use_case_json = set(ASSETS_DIR.glob(SOURCES_GLOB)) - set(
        (ASSETS_DIR / "spec").glob(SOURCES_GLOB)
    )
    solc_outputs = ("solc", "output")
    all_manifests = [
        json
        for json in all_use_case_json
        if all(known not in json.name for known in solc_outputs)
    ]
    if not all_manifests:
        raise InsufficientAssetsError(
            "Error importing manifests for validation, found no manifests in `ethpm/assets/`"
        )
    return all_manifests


@pytest.fixture(params=get_all_manifest_paths())
def manifest(request):
    return json.loads(request.param.read_text())


def test_manifest_assets_are_valid(manifest):
    result = validate_manifest_against_schema(manifest)
    assert result is None
