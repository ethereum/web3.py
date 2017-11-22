import pytest
import socket

from web3.manager import (
    RequestManager,
)
from web3.providers.tester import (
    TestRPCProvider as TheTestRPCProvider,
    is_testrpc_available,
)


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
    provider = TheTestRPCProvider(port=get_open_port())
    rm = RequestManager(None, provider)

    response = rm.request_blocking(method="web3_clientVersion", params=[])

    assert response == RPCMethods.web3_clientVersion()
