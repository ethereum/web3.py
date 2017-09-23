import pytest

from eth_utils import (
    is_address,
)


@pytest.fixture
def PRIVATE_BYTES():
    return b'unicorns' * 4


@pytest.fixture
def PRIVATE_BYTES_INVERT(PRIVATE_BYTES):
    return b'rainbows' * 4


def test_eth_account_create_variation(web3):
    account1 = web3.eth.account.create()
    account2 = web3.eth.account.create()
    assert account1 != account2


def test_eth_account_privateKeyToAccount_reproducible(web3, PRIVATE_BYTES):
    account1 = web3.eth.account.privateKeyToAccount(PRIVATE_BYTES)
    account2 = web3.eth.account.privateKeyToAccount(PRIVATE_BYTES)
    assert account1 == PRIVATE_BYTES
    assert account1 == account2


def test_eth_account_privateKeyToAccount_diverge(web3, PRIVATE_BYTES, PRIVATE_BYTES_INVERT):
    account1 = web3.eth.account.privateKeyToAccount(PRIVATE_BYTES)
    account2 = web3.eth.account.privateKeyToAccount(PRIVATE_BYTES_INVERT)
    assert account2 == PRIVATE_BYTES_INVERT
    assert account1 != account2


def test_eth_account_privateKeyToAccount_seed_restrictions(web3):
    with pytest.raises(ValueError):
        web3.eth.account.privateKeyToAccount(b'')
    with pytest.raises(ValueError):
        web3.eth.account.privateKeyToAccount(b'\xff' * 31)
    with pytest.raises(ValueError):
        web3.eth.account.privateKeyToAccount(b'\xff' * 33)


def test_eth_account_privateKeyToAccount_properties(web3, PRIVATE_BYTES):
    account = web3.eth.account.privateKeyToAccount(PRIVATE_BYTES)
    assert callable(account.sign)
    assert callable(account.signTransaction)
    assert is_address(account.address)
    assert bytes(account.privateKey) == bytes(account)


def test_eth_account_create_properties(web3):
    account = web3.eth.account.create()
    assert callable(account.sign)
    assert callable(account.signTransaction)
    assert is_address(account.address)
    assert bytes(account.privateKey) == bytes(account)
