import pytest
from gevent import socket

from web3.providers.manager import RequestManager
from web3.providers.rpc import (
    TestRPCProvider,
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
    from testrpc.testrpc import web3_clientVersion
    provider = TestRPCProvider(port=get_open_port())
    rm = RequestManager(provider)

    response = rm.request_blocking(method="web3_clientVersion", params=[])

    assert response == web3_clientVersion()
