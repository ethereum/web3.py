import pytest

from gevent import socket

from web3.providers.ipc import IPCProvider
from web3.providers.rpc import TestRPCProvider, RPCProvider


def get_open_port():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(("", 0))
    s.listen(1)
    port = s.getsockname()[1]
    s.close()
    return port


@pytest.fixture(params=['tester', 'rpc', 'ipc'])
def disconnected_provider(request):
    """
    Supply a Provider that's not connected to a node.

    (See also the web3 fixture.)
    """
    if request.param == 'tester':
        port = get_open_port()
        provider = TestRPCProvider(port=port)
        provider.server.stop()
        return provider
    elif request.param == 'rpc':
        return RPCProvider(port=9999)
    elif request.param == 'ipc':
        return IPCProvider(ipc_path='nonexistent')
    else:
        raise ValueError(request.param)
