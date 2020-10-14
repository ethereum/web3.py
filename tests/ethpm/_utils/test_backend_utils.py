import os
import pytest

from ethpm._utils.backend import (
    get_resolvable_backends_for_uri,
    get_translatable_backends_for_uri,
)
from ethpm.backends.ipfs import (
    InfuraIPFSBackend,
    LocalIPFSBackend,
)
from ethpm.backends.registry import (
    RegistryURIBackend,
)
from ethpm.exceptions import (
    CannotHandleURI,
)
from ethpm.uri import (
    resolve_uri_contents,
)


@pytest.mark.parametrize(
    "uri,backends",
    (
        (
            "ipfs://QmTKB75Y73zhNbD3Y73xeXGjYrZHmaXXNxoZqGCagu7r8u/",
            (InfuraIPFSBackend, LocalIPFSBackend),
        ),
        ("erc1319://packages.zeppelinos.eth:1/erc20?version=1.0.0", ()),
    ),
)
@pytest.mark.skipif('WEB3_INFURA_PROJECT_ID' not in os.environ, reason='Infura API key unavailable')
def test_get_resolvable_backends_for_supported_uris(dummy_ipfs_backend, uri, backends):
    good_backends = get_resolvable_backends_for_uri(uri)
    assert good_backends == backends


@pytest.mark.parametrize(
    "uri,backends",
    (
        ("erc1319://packages.zeppelinos.eth:1/erc20?version=1.0.0", (RegistryURIBackend,)),
        ("ipfs://QmTKB75Y73zhNbD3Y73xeXGjYrZHmaXXNxoZqGCagu7r8u/", ()),
    ),
)
@pytest.mark.skipif('WEB3_INFURA_PROJECT_ID' not in os.environ, reason='Infura API key unavailable')
def test_get_translatable_backends_for_supported_uris(dummy_ipfs_backend, uri, backends):
    good_backends = get_translatable_backends_for_uri(uri)
    assert good_backends == backends


@pytest.mark.parametrize(
    "uri",
    (
        "xxx",
        # filesystem
        "file:///path_to_erc20.json",
        # invalid registry URI scheme
        "erc1128://packages.zeppelinos.eth:1/erc20/v1.0.0",
        # swarm
        "bzz://da6adeeb4589d8652bbe5679aae6b6409ec85a20e92a8823c7c99e25dba9493d",
        "bzz-immutable:://da6adeeb4589d8652bbe5679aae6b6409ec85a20e92a8823c7c99e25dba9493d",
        "bzz-raw://da6adeeb4589d8652bbe5679aae6b6409ec85a20e92a8823c7c99e25dba9493d",
        # internet
        "http://github.com/ethpm/ethpm-spec/examples/owned/1.0.0.json#content_hash",
        "https://github.com/ethpm/ethpm-spec/examples/owned/1.0.0.json#content_hash",
    ),
)
@pytest.mark.skipif('WEB3_INFURA_PROJECT_ID' not in os.environ, reason='Infura API key unavailable')
def test_resolve_uri_contents_raises_exception_for_unsupported_schemes(uri):
    with pytest.raises(CannotHandleURI):
        resolve_uri_contents(uri)
