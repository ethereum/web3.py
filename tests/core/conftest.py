import pytest

from web3.module import (
    Module,
)


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
