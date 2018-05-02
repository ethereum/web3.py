import pytest

from web3.exceptions import (
    ValidationError,
)
from web3.middleware import (
    construct_fixture_middleware,
    geth_poa_middleware,
)


# In the spec, a block with extra data longer than 32 bytes is invalid
def test_long_extra_data(web3):
    return_block_with_long_extra_data = construct_fixture_middleware({
        'eth_getBlockByNumber': {'extraData': '0x' + 'ff' * 33},
    })
    web3.middleware_stack.inject(return_block_with_long_extra_data, layer=0)
    with pytest.raises(ValidationError):
        web3.eth.getBlock('latest')


def test_full_extra_data(web3):
    return_block_with_long_extra_data = construct_fixture_middleware({
        'eth_getBlockByNumber': {'extraData': '0x' + 'ff' * 32},
    })
    web3.middleware_stack.inject(return_block_with_long_extra_data, layer=0)
    block = web3.eth.getBlock('latest')
    assert block.extraData == b'\xff' * 32


def test_geth_proof_of_authority(web3):
    return_block_with_long_extra_data = construct_fixture_middleware({
        'eth_getBlockByNumber': {'extraData': '0x' + 'ff' * 33},
    })
    web3.middleware_stack.inject(geth_poa_middleware, layer=0)
    web3.middleware_stack.inject(return_block_with_long_extra_data, layer=0)
    block = web3.eth.getBlock('latest')
    assert 'extraData' not in block
    assert block.proofOfAuthorityData == b'\xff' * 33
