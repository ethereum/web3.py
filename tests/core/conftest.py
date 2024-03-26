import pytest

import pytest_asyncio

from web3 import (
    AsyncWeb3,
)
from web3.module import (
    Module,
)
from web3.providers.eth_tester.main import (
    AsyncEthereumTesterProvider,
)

# --- inherit from `web3.module.Module` class --- #


@pytest.fixture(scope="module")
def module1():
    class Module1(Module):
        a = "a"

        @property
        def b(self):
            return "b"

    return Module1


@pytest.fixture(scope="module")
def module2():
    class Module2(Module):
        c = "c"

        @staticmethod
        def d():
            return "d"

    return Module2


@pytest.fixture(scope="module")
def module3():
    class Module3(Module):
        e = "e"

    return Module3


@pytest.fixture(scope="module")
def module4():
    class Module4(Module):
        f = "f"

    return Module4


# --- do not inherit from `web3.module.Module` class --- #


@pytest.fixture(scope="module")
def module1_unique():
    # uses ``Web3`` instance by accepting it as first arg in the ``__init__()`` method
    class Module1:
        a = "a"

        def __init__(self, w3):
            self._b = "b"
            self.w3 = w3

        def b(self):
            return self._b

        @property
        def return_eth_chain_id(self):
            return self.w3.eth.chain_id

    return Module1


@pytest.fixture(scope="module")
def module2_unique():
    class Module2:
        c = "c"

        @staticmethod
        def d():
            return "d"

    return Module2


@pytest.fixture(scope="module")
def module3_unique():
    class Module3:
        e = "e"

    return Module3


@pytest.fixture(scope="module")
def module4_unique():
    class Module4:
        f = "f"

    return Module4


@pytest.fixture(scope="module")
def module_many_init_args():
    class ModuleManyArgs:
        def __init__(self, a, b):
            self.a = a
            self.b = b

    return ModuleManyArgs


@pytest_asyncio.fixture
async def async_w3():
    w3 = AsyncWeb3(AsyncEthereumTesterProvider())
    accounts = await w3.eth.accounts
    w3.eth.default_account = accounts[0]
    return w3


@pytest_asyncio.fixture
async def async_w3_non_strict_abi():
    w3 = AsyncWeb3(AsyncEthereumTesterProvider())
    w3.strict_bytes_type_checking = False
    accounts = await w3.eth.accounts
    w3.eth.default_account = accounts[0]
    return w3
