import pytest
import warnings

from web3.contract import (
    Contract,
)


ABI = [
    {
        "constant": False,
        "inputs": [],
        "name": "func_1",
        "outputs": [],
        "type": "function",
    },
]

ADDRESS = '0x0000000000000000000000000000000000000000'


class ContactClassForTest(Contract):
    web3 = True


@pytest.mark.parametrize(
    'args,kwargs,expected',
    (
        ((ABI,), {}, {'abi': ABI}),
        ((ABI,), {'abi': ABI}, TypeError),
        ((ABI, ADDRESS), {}, {'abi': ABI, 'address': ADDRESS}),
        (
            (ABI, ADDRESS, '0x1', '0x2', '0x3'),
            {},
            {'abi': ABI, 'address': ADDRESS, 'binary': '0x1', 'binary_runtime': '0x2', 'source': '0x3'},
        ),
        (
            tuple(),
            {'abi': ABI, 'address': ADDRESS, 'code': '0x1', 'code_runtime': '0x2', 'source': '0x3'},
            {'abi': ABI, 'address': ADDRESS, 'binary': '0x1', 'binary_runtime': '0x2', 'source': '0x3'},
        ),
        ((ABI, ADDRESS), {'abi': ABI}, TypeError),
        ((ABI, ADDRESS), {'address': ADDRESS}, TypeError),
        ((ADDRESS,), {}, {'address': ADDRESS}),
    )
)
def test_process_legacy_constructor_signature(args, kwargs, expected):

    if isinstance(expected, type) and issubclass(expected, Exception):
        with pytest.raises(expected):
            ContactClassForTest(*args, **kwargs)
        return

    actual = ContactClassForTest(*args, **kwargs)
    for key, value in expected.items():
        assert getattr(actual, key) == value


def test_deprecated_properties():
    instance = ContactClassForTest(ABI, ADDRESS, '0x1', '0x2', '0x3')

    with pytest.warns(DeprecationWarning):
        instance.code

    with pytest.warns(DeprecationWarning):
        instance.code_runtime

    with pytest.warns(DeprecationWarning):
        instance.source


def test_deprecated_instantiation():
    with pytest.warns(Warning) as record:
        ContactClassForTest(ADDRESS)
        ContactClassForTest(address=ADDRESS)
        warnings.warn(Warning('test'))

    assert len(record) == 1

    with pytest.warns(DeprecationWarning):
        ContactClassForTest()  # no address

    with pytest.warns(DeprecationWarning):
        ContactClassForTest(ABI, ADDRESS)  # no address

    with pytest.warns(DeprecationWarning):
        ContactClassForTest(ABI)  # no address

    with pytest.warns(DeprecationWarning):
        ContactClassForTest(code='0x1')  # no address
