import pytest


def test_putString(web3_tester):
    with pytest.raises(DeprecationWarning):
        web3_tester.db.putString('someDB', 'key', 'value')


def test_getString(web3_tester):
    with pytest.raises(DeprecationWarning):
        web3_tester.db.getString('someDB', 'key')


def test_putHex(web3_tester):
    with pytest.raises(DeprecationWarning):
        web3_tester.db.putHex('someDB', 'key', '0x12345')


def test_getHex(web3_tester):
    with pytest.raises(DeprecationWarning):
        web3_tester.db.getHex('someDB', 'key')
