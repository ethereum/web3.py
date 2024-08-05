import pytest

from eth_tester import (
    EthereumTester,
)

from web3.main import (
    Web3,
)
from web3.providers.eth_tester import (
    EthereumTesterProvider,
)


@pytest.fixture(scope="module")
def w3(backend_class):
    return Web3(EthereumTesterProvider(EthereumTester(backend=backend_class())))
