import json
import os
from pathlib import (
    Path,
)
import pytest

from ethpm import (
    Package,
)
from ethpm.exceptions import (
    CannotHandleURI,
    EthPMValidationError,
)


@pytest.fixture
def valid_manifest_from_path(tmpdir):
    valid_manifest = '{"manifest":"ethpm/3","name":"foo","version":"1.0.0"}'
    temp_manifest = tmpdir.mkdir("invalid").join("manifest.json")
    temp_manifest.write(valid_manifest)
    yield Path(str(temp_manifest))


@pytest.fixture
def invalid_manifest_from_path(tmpdir):
    invalid_manifest = (
        '{"manifest":"xx","name":"foo","version":"1.0.0"}'
    )
    temp_manifest = tmpdir.mkdir("invalid").join("manifest.json")
    temp_manifest.write(invalid_manifest)
    yield Path(str(temp_manifest))


@pytest.fixture
def non_json_manifest(tmpdir):
    temp_manifest = tmpdir.mkdir("invalid").join("manifest.json")
    temp_manifest.write("This is invalid json")
    yield Path(str(temp_manifest))


def test_init_from_minimal_valid_manifest(w3):
    minimal_manifest = {
        "name": "foo",
        "manifest": "ethpm/3",
        "version": "1.0.0",
    }

    Package(minimal_manifest, w3)


def test_init_with_outdated_ethpm_manifest(w3):
    v2_manifest = {
        "package_name": "foo",
        "manifest_version": "2",
        "version": "1.0.0",
    }
    with pytest.raises(EthPMValidationError):
        Package(v2_manifest, w3)


def test_package_init_for_all_manifest_use_cases(all_manifests, w3):
    package = Package(all_manifests, w3)
    assert isinstance(package, Package)


def test_package_init_for_manifest_with_build_dependency(
    piper_coin_manifest, w3
):
    pkg = Package(piper_coin_manifest, w3)
    assert isinstance(pkg, Package)


def test_init_from_invalid_manifest_data(w3):
    with pytest.raises(EthPMValidationError):
        Package({}, w3)


def test_init_from_invalid_argument_type(w3):
    with pytest.raises(TypeError):
        Package("not a manifest", w3)


def test_from_file_fails_with_missing_filepath(tmpdir, w3):
    path = os.path.join(str(tmpdir.mkdir("invalid")), "manifest.json")

    assert not os.path.exists(path)
    with pytest.raises(FileNotFoundError):
        Package.from_file(Path(path), w3)


def test_from_file_fails_with_non_json(non_json_manifest, w3):
    with pytest.raises(json.JSONDecodeError):
        Package.from_file(non_json_manifest, w3)


def test_from_file_fails_with_invalid_manifest(invalid_manifest_from_path, w3):
    with pytest.raises(EthPMValidationError):
        Package.from_file(invalid_manifest_from_path, w3)


def test_from_file_succeeds_with_valid_manifest(valid_manifest_from_path, w3):
    assert Package.from_file(valid_manifest_from_path, w3)


def test_from_file_raises_type_error_with_invalid_param_type():
    with pytest.raises(TypeError):
        Package.from_file(1)


#
# From URI
#

VALID_IPFS_PKG = "ipfs://QmdQfNxmcfGjeVwsXEBLCh5CDYsr2VyZtXoqdVm6F26JJE"


def test_package_from_uri_with_valid_uri(w3):
    package = Package.from_uri(VALID_IPFS_PKG, w3)
    assert package.name == "standard-token"
    assert isinstance(package, Package)


@pytest.mark.parametrize(
    "uri",
    (
        # Invalid
        "123",
        "ipfs://",
        "http://QmTKB75Y73zhNbD3Y73xeXGjYrZHmaXXNxoZqGCagu7r8u/readme",
        "ipfsQmTKB75Y73zhNbD3Y73xeXGjYrZHmaXXNxoZqGCagu7r8u/readme/",
        # Unsupported
        "erc111://packages.zeppelin.os/owned",
        "bzz://da6adeeb4589d8652bbe5679aae6b6409ec85a20e92a8823c7c99e25dba9493d",
    ),
)
@pytest.mark.skipif('WEB3_INFURA_PROJECT_ID' not in os.environ, reason='Infura API key unavailable')
def test_package_from_uri_rejects_invalid_ipfs_uri(uri, w3):
    with pytest.raises(CannotHandleURI):
        Package.from_uri(uri, w3)
