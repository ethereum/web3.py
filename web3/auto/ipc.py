from os import path

from web3 import (
    IPCProvider,
    Web3
)


def ipc():

    home = path.expanduser('~')

    # The following 2 lines are default paths
    parity_path = home + '/.local/share/io.parity.ethereum/jsonrpc.ipc'
    geth_path = home + '/.ethereum/geth.ipc'

    w3 = Web3(IPCProvider(parity_path))
    if w3.isConnected():
        return w3

    w3 = Web3(IPCProvider(geth_path))
    if w3.isConnected():
        return w3

    return False


w3 = ipc()
