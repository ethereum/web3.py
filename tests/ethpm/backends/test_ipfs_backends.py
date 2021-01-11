import json
from pathlib import (
    Path,
)
import pytest

from eth_utils import (
    to_text,
)
from ipfshttpclient.exceptions import (
    TimeoutError,
)

from ethpm.backends.ipfs import (
    DummyIPFSBackend,
    InfuraIPFSBackend,
    LocalIPFSBackend,
    get_ipfs_backend,
    get_ipfs_backend_class,
)
from ethpm.constants import (
    INFURA_GATEWAY_MULTIADDR,
)


@pytest.fixture
def owned_manifest_path(ethpm_spec_dir):
    return ethpm_spec_dir / "examples" / "owned" / "v3.json"


@pytest.fixture
def fake_client(owned_manifest_path):
    class FakeClient:
        def cat(self, ipfs_hash):
            return ipfs_hash

        def add(self, file_or_dir_path, recursive):
            if Path(file_or_dir_path) == owned_manifest_path:
                return {
                    "Hash": "QmbeVyFLSuEUxiXKwSsEjef6icpdTdA4kGG9BcrJXKNKUW",
                    "Name": "1.0.0.json",
                    "Size": "454",
                }

    return FakeClient()


@pytest.mark.parametrize(
    "base_uri,backend", ((INFURA_GATEWAY_MULTIADDR, InfuraIPFSBackend()),)
)
def test_ipfs_and_infura_gateway_backends_fetch_uri_contents(base_uri, backend):
    uri = "ipfs://Qme4otpS88NV8yQi8TfTP89EsQC5bko3F5N1yhRoi6cwGV"
    assert backend.base_uri == base_uri
    contents = backend.fetch_uri_contents(uri)
    assert contents.startswith(b"pragma solidity")


@pytest.mark.xfail(strict=False, raises=TimeoutError)
def test_local_ipfs_backend(owned_manifest_path):
    uri = "ipfs://Qme4otpS88NV8yQi8TfTP89EsQC5bko3F5N1yhRoi6cwGV"
    backend = LocalIPFSBackend()
    backend.pin_assets(owned_manifest_path.parent / "contracts" / "Owned.sol")
    contents = backend.fetch_uri_contents(uri)
    assert contents.startswith(b"pragma solidity")


@pytest.mark.parametrize(
    "uri,expected",
    (
        ("ipfs:QmTKB75Y73zhNbD3Y73xeXGjYrZHmaXXNxoZqGCagu7r8u", True),
        ("ipfs:/QmTKB75Y73zhNbD3Y73xeXGjYrZHmaXXNxoZqGCagu7r8u", True),
        ("ipfs://QmTKB75Y73zhNbD3Y73xeXGjYrZHmaXXNxoZqGCagu7r8u", True),
        ("http://raw.githubusercontent.com/ethpm/py-ethpm#0x123", False),
        ("https://raw.githubusercontent.com/ethpm/py-ethpm#0x123", False),
        (
            "bzz://679bde3ccb6fb911db96a0ea1586c04899c6c0cc6d3426e9ee361137b270a463",
            False,
        ),
        ("ercxxx://packages.eth/owned?version=1.0.0", False),
    ),
)
def test_base_ipfs_gateway_backend_correctly_handles_uri_schemes(uri, expected):
    backend = InfuraIPFSBackend()
    assert backend.can_resolve_uri(uri) is expected


def test_dummy_ipfs_backend():
    pkg = DummyIPFSBackend().fetch_uri_contents(
        "ipfs://QmQNffBrmbB3TuBCtYfYsJWJVLssatWXa3H6CkGeyNUySA"
    )
    manifest = json.loads(to_text(pkg))
    assert manifest["name"] == "standard-token"


def test_get_ipfs_backend_class_with_default_backend():
    backend = get_ipfs_backend_class()
    assert issubclass(backend, InfuraIPFSBackend)


def test_get_ipfs_backend_with_default_backend():
    backend = get_ipfs_backend()
    assert isinstance(backend, InfuraIPFSBackend)


def test_get_uri_backend_with_env_variable(dummy_ipfs_backend, monkeypatch):
    monkeypatch.setenv(
        "ETHPM_IPFS_BACKEND_CLASS", "ethpm.backends.ipfs.LocalIPFSBackend"
    )
    backend = get_ipfs_backend()
    assert isinstance(backend, LocalIPFSBackend)


def test_pin_assets_to_dummy_backend(dummy_ipfs_backend, ethpm_spec_dir, owned_manifest_path):
    # Test pinning a file
    backend = get_ipfs_backend()
    hashes = backend.pin_assets(owned_manifest_path)
    asset_data = hashes[0]
    assert asset_data["Name"] == "v3.json"
    assert asset_data["Hash"] == "QmcxvhkJJVpbxEAa6cgW3B6XwPJb79w9GpNUv2P2THUzZR"
    assert asset_data["Size"] == "478"
    # Test pinning a directory
    dir_data = backend.pin_assets(ethpm_spec_dir / "examples" / "standard-token" / "contracts")
    dir_names = [result["Name"] for result in dir_data]
    dir_hashes = [result["Hash"] for result in dir_data]
    dir_sizes = [result["Size"] for result in dir_data]
    assert len(dir_data) == 2
    assert "StandardToken.sol" in dir_names
    assert "QmUofKBtNJVaqoSAtnHfrarJyyLm1oMUTAK4yCtnmYMJVy" in dir_hashes
    assert "2949" in dir_sizes
