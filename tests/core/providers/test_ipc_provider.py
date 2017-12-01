from web3.providers.ipc import (
    IPCProvider,
)


def test_ipc_no_path():
    """
    IPCProvider.isConnected() returns False when no path is supplied
    """
    ipc = IPCProvider(None)
    assert ipc.isConnected() is False
