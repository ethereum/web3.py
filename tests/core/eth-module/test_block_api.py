import pytest

from web3._utils.rpc_abi import (
    RPC,
)
from web3.middleware import (
    construct_result_generator_middleware,
)


@pytest.fixture(autouse=True)
def wait_for_first_block(w3, wait_for_block):
    wait_for_block(w3)


def test_uses_default_block(w3, extra_accounts,
                            wait_for_transaction):
    assert(w3.eth.default_block == 'latest')
    w3.eth.default_block = w3.eth.block_number
    assert(w3.eth.default_block == w3.eth.block_number)


def test_uses_defaultBlock_with_warning(w3, extra_accounts,
                                        wait_for_transaction):
    with pytest.warns(DeprecationWarning):
        assert w3.eth.defaultBlock == 'latest'

    with pytest.warns(DeprecationWarning):
        w3.eth.defaultBlock = w3.eth.block_number

    with pytest.warns(DeprecationWarning):
        assert(w3.eth.defaultBlock == w3.eth.block_number)


def test_get_block_formatters_with_null_values(w3):
    null_values_block = {
        'baseFeePerGas': None,
        'extraData': None,
        'gasLimit': None,
        'gasUsed': None,
        'size': None,
        'timestamp': None,
        'hash': None,
        'logsBloom': None,
        'miner': None,
        'mixHash': None,
        'nonce': None,
        'number': None,
        'parentHash': None,
        'sha3Uncles': None,
        'difficulty': None,
        'receiptsRoot': None,
        'statesRoot': None,
        'totalDifficulty': None,
        'transactionsRoot': None,
    }
    result_middleware = construct_result_generator_middleware({
        RPC.eth_getBlockByNumber: lambda *_: null_values_block,
    })

    w3.middleware_onion.inject(result_middleware, 'result_middleware', layer=0)

    received_block = w3.eth.get_block('pending')
    assert received_block == null_values_block
