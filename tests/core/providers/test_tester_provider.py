import pytest

from web3.manager import (
    RequestManager,
)
from web3.providers.tester import (
    EthereumTesterProvider,
    is_testrpc_available,
)


@pytest.mark.skipif(not is_testrpc_available, reason="`eth-testrpc` is not installed")
def test_making_provider_request():
    from testrpc.rpc import RPCMethods
    provider = EthereumTesterProvider()
    rm = RequestManager(None, provider)

    response = rm.request_blocking(method="web3_clientVersion", params=[])

    assert response == RPCMethods.web3_clientVersion()
