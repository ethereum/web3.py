import pytest

from ethpm import Package
from ethpm.exceptions import CannotHandleURI

VALID_IPFS_PKG = "ipfs://QmeD2s7KaBUoGYTP1eutHBmBkMMMoycdfiyGMx2DKrWXyV"


def test_package_from_uri_with_valid_uri(dummy_ipfs_backend, w3):
    package = Package.from_uri(VALID_IPFS_PKG, w3)
    assert package.name == "safe-math-lib"
    assert isinstance(package, Package)


@pytest.mark.parametrize(
    "invalid",
    (
        "123",
        b"123",
        "ipfs://",
        "http://QmTKB75Y73zhNbD3Y73xeXGjYrZHmaXXNxoZqGCagu7r8u/readme",
        "ipfsQmTKB75Y73zhNbD3Y73xeXGjYrZHmaXXNxoZqGCagu7r8u/readme/",
    ),
)
def test_package_from_uri_rejects_invalid_ipfs_uri(invalid, w3):
    with pytest.raises(CannotHandleURI):
        Package.from_uri(invalid, w3)
