"""
TODO: Provide explanation of gas price engines
"""


def rpc_gas_pricing_strategy(web3, transaction_params=None):  # TODO: call eth.gasPrice
    """
    This is the default gas pricing strategy. It derives it's value from the eth_gasPrice
    JSON-RPC call.
    """
    return web3.eth.gasPrice
