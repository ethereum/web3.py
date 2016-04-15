import pytest

from web3.web3.iban import Iban



def test_createIndirect():
    tests = [
    { "institution": 'XREG', "identifier": 'GAVOFYORK', "expected": 'XE81ETHXREGGAVOFYORK'}
    ]
    for test in tests:
        assert test["expected"] == Iban.createIndirect({"institution":test["institution"], "identifier":test["identifier"]}).toString()

def test_fromAddress():

    tests = [
        { "address": '00c5496aee77c1ba1f0854206a26dda82a81d6d8',   "expected": 'XE7338O073KYGTWWZN0F2WZ0R8PX5ZPPZS'},
        { "address": '0x00c5496aee77c1ba1f0854206a26dda82a81d6d8', "expected": 'XE7338O073KYGTWWZN0F2WZ0R8PX5ZPPZS'},
        { "address": '0x11c5496aee77c1ba1f0854206a26dda82a81d6d8', "expected": 'XE1222Q908LN1QBBU6XUQSO1OHWJIOS46OO'},
        { "address": '0x52dc504a422f0e2a9e7632a34a50f1a82f8224c7', "expected": 'XE499OG1EH8ZZI0KXC6N83EKGT1BM97P2O7'},
        { "address": '0x0000a5327eab78357cbf2ae8f3d49fd9d90c7d22', "expected": 'XE0600DQK33XDTYUCRI0KYM5ELAKXDWWF6'}
    ]
    for test in tests:
        assert Iban.fromAddress(test["address"]).toString() == test["expected"]

def test_isValid():
    tests = [
        { "obj": lambda : None, "is": False},
        { "obj": 'function', "is": False},
        { "obj": {}, "is": False},
        { "obj": '[]', "is": False},
        { "obj": '[1, 2]', "is": False},
        { "obj": '{}', "is": False},
        { "obj": '{"a": 123, "b" :3,}', "is": False},
        { "obj": '{"c" : 2}', "is": False},
        { "obj": 'XE81ETHXREGGAVOFYORK', "is": True},
        { "obj": 'XE82ETHXREGGAVOFYORK', "is": False}, # control number is invalid
        { "obj": 'XE81ETCXREGGAVOFYORK', "is": False},
        { "obj": 'XE81ETHXREGGAVOFYORKD', "is": False},
        { "obj": 'XE81ETHXREGGaVOFYORK', "is": False},
        { "obj": 'XE7338O073KYGTWWZN0F2WZ0R8PX5ZPPZS', "is": True},
        { "obj": 'XE7438O073KYGTWWZN0F2WZ0R8PX5ZPPZS', "is": False}, # control number is invalid
        { "obj": 'XD7338O073KYGTWWZN0F2WZ0R8PX5ZPPZS', "is": False},
        { "obj": 'XE1222Q908LN1QBBU6XUQSO1OHWJIOS46OO', "is": True}
    ]

    for test in tests:
        assert Iban.isValidStatic(test["obj"]) == test["is"]

def test_toAddress():
    tests = [
        { "direct": 'XE7338O073KYGTWWZN0F2WZ0R8PX5ZPPZS', "address": '00c5496aee77c1ba1f0854206a26dda82a81d6d8'}
    ]

    for test in tests:
        assert Iban(test["direct"]).address() == test["address"]