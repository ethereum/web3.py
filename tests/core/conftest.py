import pytest

from web3.module import (
    Module,
)

# --- inherit from `web3.module.Module` class --- #


@pytest.fixture(scope='module')
def module1():
    class Module1(Module):
        a = 'a'

        @property
        def b(self):
            return 'b'
    return Module1


@pytest.fixture(scope='module')
def module2():
    class Module2(Module):
        c = 'c'

        @staticmethod
        def d():
            return 'd'
    return Module2


@pytest.fixture(scope='module')
def module3():
    class Module3(Module):
        e = 'e'
    return Module3


@pytest.fixture(scope='module')
def module4():
    class Module4(Module):
        f = 'f'
    return Module4


# --- do not inherit from `web3.module.Module` class --- #


@pytest.fixture(scope='module')
def module1_unique():
    class Module1:
        a = 'a'
    return Module1


@pytest.fixture(scope='module')
def module2_unique():
    class Module2:
        b = 'b'

        @staticmethod
        def c():
            return 'c'
    return Module2


@pytest.fixture(scope='module')
def module3_unique():
    class Module3:
        d = 'd'
    return Module3


@pytest.fixture(scope='module')
def module4_unique():
    class Module4:
        e = 'e'
    return Module4
