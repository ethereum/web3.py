import pytest


def get_open_port():
    import socket
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(("", 0))
    s.listen(1)
    port = s.getsockname()[1]
    s.close()
    return port


@pytest.yield_fixture()
def web3_tester():
    from web3 import Web3
    from web3.web3.rpcprovider import TestRPCProvider

    provider = TestRPCProvider(port=get_open_port())

    _web3 = Web3(provider)

    yield _web3

    _web3.currentProvider.server.shutdown()
    _web3.currentProvider.server.server_close()
