import pytest

from web3.web3.requestmanager import RequestManager
from web3.web3.rpcprovider import TestRPCProvider, is_testrpc_available


@pytest.mark.skipif(not is_testrpc_available, reason="`eth-testrpc` is not installed")
def test_making_provider_request():
    from testrpc.testrpc import web3_clientVersion
    provider = TestRPCProvider()
    rm = RequestManager(provider)

    req_id = rm.forward({"method": "web3_clientVersion", "params": []})
    response = rm.receive(req_id, timeout=1)

    assert response == web3_clientVersion()
