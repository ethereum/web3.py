from typing import (
    TYPE_CHECKING,
    Optional,
    cast,
)

from web3.types import (
    BlockIdentifier,
    TxParams,
    Wei,
)

if TYPE_CHECKING:
    from web3 import Web3  # noqa: F401
    from web3.eth import AsyncEth  # noqa: F401


async def get_block_gas_limit(
    web3_eth: "AsyncEth", block_identifier: Optional[BlockIdentifier] = None
) -> Wei:
    if block_identifier is None:
        block_identifier = await web3_eth.block_number
    block = await web3_eth.get_block(block_identifier)
    return block['gasLimit']


async def get_buffered_gas_estimate(
    web3: "Web3", transaction: TxParams, gas_buffer: Wei = Wei(100000)
) -> Wei:
    gas_estimate_transaction = cast(TxParams, dict(**transaction))

    gas_estimate = await web3.eth.estimate_gas(gas_estimate_transaction)  # type: ignore

    gas_limit = await get_block_gas_limit(web3.eth)  # type: ignore

    if gas_estimate > gas_limit:
        raise ValueError(
            "Contract does not appear to be deployable within the "
            "current network gas limits.  Estimated: {0}. Current gas "
            "limit: {1}".format(gas_estimate, gas_limit)
        )

    return Wei(min(gas_limit, gas_estimate + gas_buffer))
