from web3 import Web3
from web3.types import (
    TxParams,
)


def rpc_gas_price_strategy(web3: Web3, transaction_params: TxParams=None) -> int:
    """
    A simple gas price strategy deriving it's value from the eth_gasPrice JSON-RPC call.
    """
    return web3.manager.request_blocking("eth_gasPrice", [])
