import pytest

from eth_typing import (
    BlockNumber,
)

from web3._utils.async_transactions import (
    fill_transaction_defaults,
    get_block_gas_limit,
    get_buffered_gas_estimate,
)
from web3._utils.utility_methods import (
    none_in_dict,
)
from web3.constants import (
    DYNAMIC_FEE_TXN_PARAMS,
)

SIMPLE_CURRENT_TRANSACTION = {
    'blockHash': None,
    'hash': '0x0',
    'nonce': 2,
    'gasPrice': 10,
}


@pytest.mark.asyncio()
async def test_get_block_gas_limit_with_block_number(async_w3):
    gas_limit = await get_block_gas_limit(async_w3.eth, BlockNumber(0))
    assert isinstance(gas_limit, int)


@pytest.mark.asyncio()
async def test_get_block_gas_limit_without_block_number(async_w3):
    gas_limit = await get_block_gas_limit(async_w3.eth)
    assert isinstance(gas_limit, int)


@pytest.mark.asyncio()
async def test_get_buffered_gas_estimate(async_w3):

    txn_params = {
        'data': b'0x1',
    }
    gas_estimate = await async_w3.eth.estimate_gas(txn_params)
    gas_buffer = 100000
    gas_limit = await get_block_gas_limit(async_w3.eth)  # type: ignore

    buffered_gas_estimate = await get_buffered_gas_estimate(async_w3, txn_params)
    assert isinstance(buffered_gas_estimate, int)
    assert buffered_gas_estimate == min(gas_estimate + gas_buffer, gas_limit)


@pytest.mark.asyncio()
async def test_fill_transaction_defaults_for_all_params(async_w3):
    default_transaction = await fill_transaction_defaults(async_w3, {})

    block = await async_w3.eth.get_block('latest')
    assert default_transaction == {
        'chainId': await async_w3.eth.chain_id,
        'data': b'',
        'gas': await async_w3.eth.estimate_gas({}),
        'maxFeePerGas': (
            await async_w3.eth.max_priority_fee + (2 * block['baseFeePerGas'])
        ),
        'maxPriorityFeePerGas': await async_w3.eth.max_priority_fee,
        'value': 0,
    }


@pytest.mark.asyncio()
async def test_fill_transaction_defaults_nondynamic_tranaction_fee(async_w3):
    gasPrice_transaction = {
        'gasPrice': 10,
    }
    default_transaction = await fill_transaction_defaults(async_w3, gasPrice_transaction)

    assert none_in_dict(DYNAMIC_FEE_TXN_PARAMS, default_transaction)
