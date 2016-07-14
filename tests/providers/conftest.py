import pytest

from web3.providers.ipc import IPCProvider
from web3.providers.rpc import TestRPCProvider, RPCProvider


@pytest.fixture(params=['tester', 'rpc', 'ipc'])
def disconnected_provider(request):
    """
    Supply a Provider that's not connected to a node.

    (See also the web3 fixture.)
    """
    if request.param == 'tester':
        provider = TestRPCProvider()
        provider.server.shutdown()
        provider.server.server_close()
        return provider
    elif request.param == 'rpc':
        return RPCProvider(port=9999)
    elif request.param == 'ipc':
        return IPCProvider(ipc_path='nonexistent')
    else:
        raise ValueError(request.param)
