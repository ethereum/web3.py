
import pytest

from web3.transaction import Transaction


def test_same_transaction_equality():
    t1 = Transaction({'hash': '0x1234'})
    t2 = Transaction({'hash': '0x1234'})
    assert t1 == t2, "different instances with the same hash should be equal"
    assert not (t1 != t2), "different instances with the same hash should be equal"


def test_different_transaction_inequality():
    t1 = Transaction({'hash': '0x1234'})
    t2 = Transaction({'hash': '0x4321'})
    assert t1 != t2, "different instances with different hashes should be unequal"
    assert not (t1 == t2), "different instances with different hashes should be unequal"


def test_transaction_in_set():
    t1 = Transaction({'hash': '0x1234'})
    t2 = Transaction({'hash': '0x1234'})
    tx_set = set([t1, t2])
    assert len(tx_set) == 1, "only one of two equal transactions added to a set can remain"


def test_transaction_attr_access():
    t = Transaction({'hash': '0x1234'})
    assert t.hash == t['hash'], "you must be able to access transaction values by attribute"


def test_transaction_immutability():
    with pytest.raises(NotImplementedError):
        t = Transaction({'hash': '0x1234'})
        t.hash = 'something new'
    with pytest.raises(NotImplementedError):
        t = Transaction({'hash': '0x1234'})
        t['hash'] = 'something new'

