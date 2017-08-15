import pytest
from web3 import Web3, IPCProvider


@pytest.fixture(scope="session")
def web3():
    return Web3(IPCProvider())
