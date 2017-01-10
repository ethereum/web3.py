import pytest

from web3.providers.manager import RequestManager
from web3.providers.tester import (
    TestRPCProvider,
    is_testrpc_available,
)
from web3.utils.compat import socket


def get_open_port():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(("", 0))
    s.listen(1)
    port = s.getsockname()[1]
    s.close()
    return port


@pytest.mark.skipif(not is_testrpc_available, reason="`eth-testrpc` is not installed")
def test_making_provider_request():
    from testrpc.rpc import RPCMethods
    provider = TestRPCProvider(port=get_open_port())
    rm = RequestManager(provider)

    response = rm.request_blocking(method="web3_clientVersion", params=[])

    assert response == RPCMethods.web3_clientVersion()
