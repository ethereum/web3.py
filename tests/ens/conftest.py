
import pytest
from unittest.mock import Mock

from web3 import Web3
from web3.providers.tester import EthereumTesterProvider

from ens import ENS


def mkhash(num, digits=40):
    return '0x' + str(num) * digits


@pytest.fixture
def hash_maker():
    return mkhash


@pytest.fixture
def addr1():
    return mkhash(1)


@pytest.fixture
def addr2():
    return mkhash(2)


@pytest.fixture
def addr9():
    return mkhash(9)


@pytest.fixture
def addrbytes1(addr1):
    return Web3.toBytes(hexstr=addr1)


@pytest.fixture
def hash1():
    return mkhash(1, digits=64)


@pytest.fixture
def hash9():
    return mkhash(9, digits=64)


@pytest.fixture
def hashbytes1(hash1):
    return Web3.toBytes(hexstr=hash1)


@pytest.fixture
def hashbytes9(hash9):
    return Web3.toBytes(hexstr=hash9)


@pytest.fixture
def name1():
    return 'dennis.the.peasant.eth'


@pytest.fixture
def name2():
    return 'i.didnt.vote.for.you.eth'


@pytest.fixture
def label1():
    return 'peasant'


@pytest.fixture
def label2():
    return 'dennisthe'


@pytest.fixture
def value1():
    return 1000000000000000000000002


@pytest.fixture
def secret1():
    return 'SUCH_SAFE_MUCH_SECRET'


@pytest.fixture
def ens(mocker):
    ens = ENS(EthereumTesterProvider())
    ens.web3 = Mock(wraps=ens.web3)
    mocker.patch('web3.middleware.stalecheck._isfresh', return_value=True)
    return ens


@pytest.fixture
def registrar(ens, monkeypatch, addr9):
    monkeypatch.setattr(ens, 'owner', lambda namehash: addr9)
    return ens.registrar


@pytest.fixture
def fake_hash_hexout():
    def _fake_hash(tohash):
        assert isinstance(tohash, bytes)
        tohash = b'b' + tohash
        hash_bytes = b'HASH(%s)' % tohash
        return Web3.toHex(hash_bytes)
    return _fake_hash


@pytest.fixture
def fake_hash(fake_hash_hexout):
    return lambda name: Web3.toBytes(hexstr=fake_hash_hexout(name))


@pytest.fixture
def fake_hash_utf8(fake_hash):
    return lambda name: fake_hash(name.encode())
