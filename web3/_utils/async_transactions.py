from typing import (
    TYPE_CHECKING,
    Awaitable,
    Optional,
    cast,
)

from eth_utils.toolz import (
    curry,
    merge,
)

from web3._utils.utility_methods import (
    any_in_dict,
)
from web3.constants import (
    DYNAMIC_FEE_TXN_PARAMS,
)
from web3.types import (
    BlockIdentifier,
    TxParams,
    Wei,
)

if TYPE_CHECKING:
    from web3 import Web3  # noqa: F401
    from web3.eth import AsyncEth  # noqa: F401


async def _estimate_gas(w3: 'Web3', tx: TxParams) -> Awaitable[int]:
    return await w3.eth.estimate_gas(tx)  # type: ignore


async def _gas_price(w3: 'Web3', tx: TxParams) -> Awaitable[Optional[Wei]]:
    return await w3.eth.generate_gas_price(tx) or w3.eth.gas_price  # type: ignore


async def _max_fee_per_gas(w3: 'Web3', tx: TxParams) -> Awaitable[Wei]:
    block = await w3.eth.get_block('latest')   # type: ignore
    return await w3.eth.max_priority_fee + (2 * block['baseFeePerGas'])  # type: ignore


async def _max_priority_fee_gas(w3: 'Web3', tx: TxParams) -> Awaitable[Wei]:
    return await w3.eth.max_priority_fee  # type: ignore


async def _chain_id(w3: 'Web3', tx: TxParams) -> Awaitable[int]:
    return await w3.eth.chain_id  # type: ignore

TRANSACTION_DEFAULTS = {
    'value': 0,
    'data': b'',
    'gas': _estimate_gas,
    'gasPrice': _gas_price,
    'maxFeePerGas': _max_fee_per_gas,
    'maxPriorityFeePerGas': _max_priority_fee_gas,
    'chainId': _chain_id,
}


async def get_block_gas_limit(
    web3_eth: "AsyncEth", block_identifier: Optional[BlockIdentifier] = None
) -> int:
    if block_identifier is None:
        block_identifier = await web3_eth.block_number
    block = await web3_eth.get_block(block_identifier)
    return block['gasLimit']


async def get_buffered_gas_estimate(
    w3: "Web3", transaction: TxParams, gas_buffer: int = 100000
) -> int:
    gas_estimate_transaction = cast(TxParams, dict(**transaction))

    gas_estimate = await w3.eth.estimate_gas(gas_estimate_transaction)  # type: ignore

    gas_limit = await get_block_gas_limit(w3.eth)  # type: ignore

    if gas_estimate > gas_limit:
        raise ValueError(
            "Contract does not appear to be deployable within the "
            f"current network gas limits.  Estimated: {gas_estimate}. "
            f"Current gas limit: {gas_limit}"
        )

    return min(gas_limit, gas_estimate + gas_buffer)


@curry
async def fill_transaction_defaults(w3: "Web3", transaction: TxParams) -> TxParams:
    """
    if w3 is None, fill as much as possible while offline
    """
    strategy_based_gas_price = await w3.eth.generate_gas_price(transaction)  # type: ignore
    is_dynamic_fee_transaction = (
        not strategy_based_gas_price
        and (
            'gasPrice' not in transaction  # default to dynamic fee transaction
            or any_in_dict(DYNAMIC_FEE_TXN_PARAMS, transaction)
        )
    )

    defaults = {}
    for key, default_getter in TRANSACTION_DEFAULTS.items():
        if key not in transaction:
            if (
                is_dynamic_fee_transaction and key == 'gasPrice'
                or not is_dynamic_fee_transaction and key in DYNAMIC_FEE_TXN_PARAMS
            ):
                # do not set default max fees if legacy txn or gas price if dynamic fee txn
                continue

            if callable(default_getter):
                if w3 is None:
                    raise ValueError(f"You must specify a '{key}' value in the transaction")
                default_val = await default_getter(w3, transaction)
            else:
                default_val = default_getter

            defaults[key] = default_val
    return merge(defaults, transaction)
