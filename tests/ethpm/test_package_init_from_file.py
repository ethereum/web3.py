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
    ValidationError,
)


@pytest.fixture
def valid_manifest_from_path(tmpdir):
    valid_manifest = '{"manifest_version":"2","package_name":"foo","version":"1.0.0"}'
    temp_manifest = tmpdir.mkdir("invalid").join("manifest.json")
    temp_manifest.write(valid_manifest)
    yield Path(str(temp_manifest))


@pytest.fixture
def invalid_manifest_from_path(tmpdir):
    invalid_manifest = (
        '{"manifest_version":"xx","package_name":"foo","version":"1.0.0"}'
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
        "package_name": "foo",
        "manifest_version": "2",
        "version": "1.0.0",
    }

    Package(minimal_manifest, w3)


def test_package_init_for_all_manifest_use_cases(all_manifests, w3):
    package = Package(all_manifests, w3)
    assert isinstance(package, Package)


def test_package_init_for_manifest_with_build_dependency(
    dummy_ipfs_backend, piper_coin_manifest, w3
):
    pkg = Package(piper_coin_manifest, w3)
    assert isinstance(pkg, Package)


def test_init_from_invalid_manifest_data(w3):
    with pytest.raises(ValidationError):
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
    with pytest.raises(ValidationError):
        Package.from_file(invalid_manifest_from_path, w3)


def test_from_file_succeeds_with_valid_manifest(valid_manifest_from_path, w3):
    assert Package.from_file(valid_manifest_from_path, w3)


def test_from_file_raises_type_error_with_invalid_param_type():
    with pytest.raises(TypeError):
        Package.from_file(1)
