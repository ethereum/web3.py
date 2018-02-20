import pytest

from web3.middleware import (
    construct_fixture_middleware,
    geth_poa_compatibility,
)


# In the spec, a block with extra data longer than 32 bytes is invalid
def test_long_extra_data(web3):
    return_block_with_long_extra_data = construct_fixture_middleware({
        'eth_getBlockByNumber': {'extraData': '0x' + 'ff' * 33},
    })
    web3.middleware_stack.insert(0, return_block_with_long_extra_data)
    with pytest.raises(ValueError):
        web3.eth.getBlock('latest')


def test_full_extra_data(web3):
    return_block_with_long_extra_data = construct_fixture_middleware({
        'eth_getBlockByNumber': {'extraData': '0x' + 'ff' * 32},
    })
    web3.middleware_stack.insert(0, return_block_with_long_extra_data)
    block = web3.eth.getBlock('latest')
    assert block.extraData == b'\xff' * 32


def test_geth_proof_of_authority(web3):
    return_block_with_long_extra_data = construct_fixture_middleware({
        'eth_getBlockByNumber': {'extraData': '0x' + 'ff' * 33},
    })
    web3.middleware_stack.insert(0, geth_poa_compatibility)
    web3.middleware_stack.insert(0, return_block_with_long_extra_data)
    block = web3.eth.getBlock('latest')
    assert 'extraData' not in block
    assert block.proofOfAuthorityData == b'\xff' * 33
