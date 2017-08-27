import pytest


def test_putString(web3):
    with pytest.raises(DeprecationWarning):
        web3.db.putString('someDB', 'key', 'value')


def test_getString(web3):
    with pytest.raises(DeprecationWarning):
        web3.db.getString('someDB', 'key')


def test_putHex(web3):
    with pytest.raises(DeprecationWarning):
        web3.db.putHex('someDB', 'key', '0x12345')


def test_getHex(web3):
    with pytest.raises(DeprecationWarning):
        web3.db.getHex('someDB', 'key')
