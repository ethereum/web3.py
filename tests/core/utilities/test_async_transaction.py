import pytest

from web3._utils.async_transactions import (
    fill_transaction_defaults,
)


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
