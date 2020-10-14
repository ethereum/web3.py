import pytest

from eth_utils import (
    to_bytes,
)

from ethpm import (
    ASSETS_DIR,
)
from ethpm.backends.ipfs import (
    InfuraIPFSBackend,
    LocalIPFSBackend,
    get_ipfs_backend,
)
from ethpm.tools import (
    builder as b,
)

OWNED_MANIFEST_PATH = ASSETS_DIR / "owned" / "1.0.0.json"


def test_local_ipfs_backend_integration_round_trip(monkeypatch, request):
    """
    To run this integration test requires an running IPFS node.
    If you want to run these tests, first start your IPFS node, and
    then run pytest with the arg `--integration`.
    """
    if not request.config.getoption("--integration"):
        pytest.skip("Not asked to run integration tests")

    monkeypatch.setenv(
        "ETHPM_IPFS_BACKEND_CLASS", "ethpm.backends.ipfs.LocalIPFSBackend"
    )
    backend = get_ipfs_backend()
    [asset_data] = backend.pin_assets(OWNED_MANIFEST_PATH)
    assert asset_data["Name"] == "1.0.0.json"
    assert asset_data["Hash"] == "QmbeVyFLSuEUxiXKwSsEjef6icpdTdA4kGG9BcrJXKNKUW"
    local_manifest = to_bytes(text=OWNED_MANIFEST_PATH.read_text())
    ipfs_manifest = backend.fetch_uri_contents(asset_data["Hash"])
    assert ipfs_manifest == local_manifest


@pytest.fixture(params=[LocalIPFSBackend, InfuraIPFSBackend])
def backend(request):
    return request.param()


def test_builder_pins_manifest_to_provided_ipfs_backend(backend, request):
    if not request.config.getoption("--integration"):
        pytest.skip("Not asked to run integration tests")

    minified_manifest_hash = "QmVwwpt2BAkmWQt4eNnswhWd6bYgLbnUQDMHdVMHotwiqz"
    (manifest,) = b.build(
        {},
        b.package_name("package"),
        b.manifest_version("2"),
        b.version("1.0.0"),
        b.pin_to_ipfs(backend=backend),
    )
    assert manifest["Hash"] == minified_manifest_hash
    pinned_manifest = backend.fetch_uri_contents(manifest["Hash"])
    assert (
        pinned_manifest == b'{"manifest_version":"2","package_name":"package","version":"1.0.0"}'
    )
