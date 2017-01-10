import pytest

from web3.providers.ipc import IPCProvider

from web3.providers.rpc import (
    RPCProvider,
    KeepAliveRPCProvider,
)
from web3.providers.tester import (
    TestRPCProvider,
)
from web3.utils.compat import (
    socket,
)


def get_open_port():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(("", 0))
    s.listen(1)
    port = s.getsockname()[1]
    s.close()
    return port


@pytest.fixture(params=['testrpc', 'rpc', 'ipc', 'keep-alive-rpc'])
def disconnected_provider(request):
    """
    Supply a Provider that's not connected to a node.

    (See also the web3 fixture.)
    """
    if request.param == 'testrpc':
        port = get_open_port()
        provider = TestRPCProvider(port=port)
        try:
            provider.server.stop()
            provider.server.close()
            provider.thread.kill()
        except AttributeError:
            provider.server.shutdown()
        return provider
    elif request.param == 'rpc':
        return RPCProvider(port=get_open_port())
    elif request.param == 'keep-alive-rpc':
        return KeepAliveRPCProvider(port=get_open_port())
    elif request.param == 'ipc':
        return IPCProvider(ipc_path='nonexistent')
    else:
        raise ValueError(request.param)
