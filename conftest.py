import pytest


@pytest.yield_fixture()
def web3_tester():
    from web3 import Web3
    from web3.web3.rpcprovider import TestRPCProvider

    provider = TestRPCProvider()

    _web3 = Web3(provider)

    yield _web3

    _web3.currentProvider.server.shutdown()
    _web3.currentProvider.server.server_close()
