import pytest

from ethpm import (
    Package,
)
from ethpm.dependencies import (
    Dependencies,
)
from ethpm.exceptions import (
    FailureToFetchIPFSAssetsError,
    ValidationError,
)


@pytest.fixture
def piper_coin_pkg(piper_coin_manifest, w3):
    return Package(piper_coin_manifest, w3)


def test_get_build_dependencies(dummy_ipfs_backend, piper_coin_pkg, w3):
    build_deps = piper_coin_pkg.build_dependencies
    assert isinstance(build_deps, Dependencies)


def test_get_build_dependencies_with_invalid_uris(
    dummy_ipfs_backend, piper_coin_pkg, w3
):
    piper_coin_pkg.manifest["build_dependencies"]["standard-token"] = "invalid_ipfs_uri"
    with pytest.raises(FailureToFetchIPFSAssetsError):
        piper_coin_pkg.build_dependencies


def test_get_build_dependencies_without_dependencies_raises_exception(
    piper_coin_manifest, w3
):
    piper_coin_manifest.pop("build_dependencies", None)
    pkg = Package(piper_coin_manifest, w3)
    with pytest.raises(ValidationError):
        pkg.build_dependencies


def test_get_build_dependencies_with_empty_dependencies_raises_exception(
    dummy_ipfs_backend, piper_coin_manifest, w3
):
    piper_coin_manifest["build_dependencies"] = {}
    pkg = Package(piper_coin_manifest, w3)
    with pytest.raises(ValidationError):
        pkg.build_dependencies
