from os import path

from web3 import (
    IPCProvider,
    Web3
)

def ipc():
    home = path.expanduser('~')
    
    #The following 2 lines are default paths
    parity_path = home+'/.local/share/io.parity.ethereum/jsonrpc.ipc'
    geth_path = home+'/.ethereum/geth.ipc'

    web3 =  Web3(IPCProvider(parity_path))
    if web3.isConnected():
        return web3

    web3 = Web3(IPCProvider(geth_path))
    if web3.isConnected():
        return web3

    return False



web3 = ipc()

