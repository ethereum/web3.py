import pytest

from ethpm.backends.registry import (
    RegistryURIBackend,
)
from ethpm.exceptions import (
    CannotHandleURI,
)


@pytest.fixture
def backend():
    return RegistryURIBackend()


def test_registry_uri_backend(backend):
    valid_uri = "erc1319://snakecharmers.eth:1/owned?version=1.0.0"
    expected_uri = 'ipfs://QmbeVyFLSuEUxiXKwSsEjef6icpdTdA4kGG9BcrJXKNKUW'
    assert backend.can_translate_uri(valid_uri) is True
    assert backend.can_resolve_uri(valid_uri) is False
    assert backend.fetch_uri_contents(valid_uri) == expected_uri


def test_registry_uri_backend_raises_exception_for_non_mainnet_chains(backend):
    ropsten_uri = "erc1319://snakecharmers.eth:3/owned?version=1.0.0"
    with pytest.raises(CannotHandleURI, match="Currently only mainnet"):
        backend.fetch_uri_contents(ropsten_uri)
