from web3.providers.ipc import get_default_ipc_path
from web3 import (
    IPCProvider,
    Web3
)


def connect():
    w3 = Web3(IPCProvider(get_default_ipc_path()))
    if w3.isConnected():
        return w3

    return False


w3 = connect()
