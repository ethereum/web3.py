import os
import pytest

from ethpm.backends.registry import (
    RegistryURIBackend,
    parse_registry_uri,
)
from ethpm.exceptions import (
    CannotHandleURI,
)


@pytest.fixture
def backend():
    return RegistryURIBackend()


@pytest.mark.skipif('WEB3_INFURA_PROJECT_ID' not in os.environ, reason='Infura API key unavailable')
def test_registry_uri_backend(backend):
    valid_uri = "erc1319://0x1457890158DECD360e6d4d979edBcDD59c35feeB:1/owned@1.0.0"
    expected_uri = 'ipfs://QmbeVyFLSuEUxiXKwSsEjef6icpdTdA4kGG9BcrJXKNKUW'
    assert backend.can_translate_uri(valid_uri) is True
    assert backend.can_resolve_uri(valid_uri) is False
    assert backend.fetch_uri_contents(valid_uri) == expected_uri


@pytest.mark.skipif('WEB3_INFURA_PROJECT_ID' not in os.environ, reason='Infura API key unavailable')
def test_registry_uri_supports_ens_domains(backend):
    valid_uri = "erc1319://defi.snakecharmers.eth:1/compound@1.0.0"
    parsed = parse_registry_uri(valid_uri)
    expected_uri = 'ipfs://QmYvsyuxjj9mKmCvn3jrdfnaHYwFsyHXUu7kETrN4dBhE6'
    assert backend.can_translate_uri(valid_uri) is True
    assert backend.can_resolve_uri(valid_uri) is False
    assert backend.fetch_uri_contents(valid_uri) == expected_uri
    assert parsed.address == "0xA635F17288187daE5b424D343E21FF44a79ce922"
    assert parsed.ens == "defi.snakecharmers.eth"
    assert parsed.chain_id == '1'
    assert parsed.name == "compound"
    assert parsed.version == "1.0.0"


@pytest.mark.skipif('WEB3_INFURA_PROJECT_ID' not in os.environ, reason='Infura API key unavailable')
def test_registry_uri_backend_raises_exception_for_non_mainnet_chains(backend):
    ropsten_uri = "erc1319://snakecharmers.eth:3/owned@1.0.0"
    with pytest.raises(CannotHandleURI, match="Currently only mainnet"):
        backend.fetch_uri_contents(ropsten_uri)
