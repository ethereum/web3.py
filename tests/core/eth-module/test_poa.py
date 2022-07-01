import pytest

from web3.exceptions import (
    BlockNotFound,
    ExtraDataLengthError,
)
from web3.middleware import (
    construct_fixture_middleware,
    geth_poa_middleware,
)


# In the spec, a block with extra data longer than 32 bytes is invalid
def test_long_extra_data(w3):
    return_block_with_long_extra_data = construct_fixture_middleware(
        {
            "eth_getBlockByNumber": {"extraData": "0x" + "ff" * 33},
        }
    )
    w3.middleware_onion.inject(return_block_with_long_extra_data, layer=0)
    with pytest.raises(ExtraDataLengthError):
        w3.eth.get_block("latest")


def test_full_extra_data(w3):
    return_block_with_long_extra_data = construct_fixture_middleware(
        {
            "eth_getBlockByNumber": {"extraData": "0x" + "ff" * 32},
        }
    )
    w3.middleware_onion.inject(return_block_with_long_extra_data, layer=0)
    block = w3.eth.get_block("latest")
    assert block.extraData == b"\xff" * 32


def test_geth_proof_of_authority(w3):
    return_block_with_long_extra_data = construct_fixture_middleware(
        {
            "eth_getBlockByNumber": {"extraData": "0x" + "ff" * 33},
        }
    )
    w3.middleware_onion.inject(geth_poa_middleware, layer=0)
    w3.middleware_onion.inject(return_block_with_long_extra_data, layer=0)
    block = w3.eth.get_block("latest")
    assert "extraData" not in block
    assert block.proofOfAuthorityData == b"\xff" * 33


def test_returns_none_response(w3):
    return_none_response = construct_fixture_middleware(
        {
            "eth_getBlockByNumber": None,
        }
    )
    w3.middleware_onion.inject(geth_poa_middleware, layer=0)
    w3.middleware_onion.inject(return_none_response, layer=0)
    with pytest.raises(BlockNotFound):
        w3.eth.get_block(100000000000)
