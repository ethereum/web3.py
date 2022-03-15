from typing import (
    TYPE_CHECKING,
    Optional,
    cast,
)

from web3.types import (
    BlockIdentifier,
    TxParams,
)

if TYPE_CHECKING:
    from web3 import Web3  # noqa: F401
    from web3.eth import AsyncEth  # noqa: F401


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
