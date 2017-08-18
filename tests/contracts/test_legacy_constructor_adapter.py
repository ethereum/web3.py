import pytest
import warnings
import sys

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

ADDRESS = '0xd3cda913deb6f67967b99d67acdfa1712c293601'
PADDED_ADDRESS = '0x000000000000000000000000d3cda913deb6f67967b99d67acdfa1712c293601'
INVALID_CHECKSUM_ADDRESS = '0xd3CDA913deB6f67967B99D67aCDFa1712C293601'

CODE = "0x606060405261022e806100126000396000f360606040523615610074576000357c01000000000000000000000000000000000000000000000000000000009004806316216f391461007657806361bc221a146100995780637cf5dab0146100bc578063a5f3c23b146100e8578063d09de08a1461011d578063dcf537b11461014057610074565b005b610083600480505061016c565b6040518082815260200191505060405180910390f35b6100a6600480505061017f565b6040518082815260200191505060405180910390f35b6100d26004808035906020019091905050610188565b6040518082815260200191505060405180910390f35b61010760048080359060200190919080359060200190919050506101ea565b6040518082815260200191505060405180910390f35b61012a6004805050610201565b6040518082815260200191505060405180910390f35b6101566004808035906020019091905050610217565b6040518082815260200191505060405180910390f35b6000600d9050805080905061017c565b90565b60006000505481565b6000816000600082828250540192505081905550600060005054905080507f3496c3ede4ec3ab3686712aa1c238593ea6a42df83f98a5ec7df9834cfa577c5816040518082815260200191505060405180910390a18090506101e5565b919050565b6000818301905080508090506101fb565b92915050565b600061020d6001610188565b9050610214565b90565b60006007820290508050809050610229565b91905056"

MALFORMED_ABI_1 = "NON-LIST ABI"
MALFORMED_ABI_2 = [5, {"test": "value"}, True]


class ContactClassForTest(Contract):
    web3 = True


@pytest.mark.parametrize(
    'args,kwargs,expected',
    (
        ((ABI,), {}, {'abi': ABI}),
        ((ABI,), {'abi': ABI}, TypeError),
        ((ABI, ADDRESS), {}, {'abi': ABI, 'address': ADDRESS}),
        (
            (ABI, ADDRESS),
            {'code': '0x1', 'code_runtime': '0x2'},
            {'abi': ABI, 'address': ADDRESS, 'bytecode': '0x1', 'bytecode_runtime': '0x2'}),
        (
            (ABI, ADDRESS, '0x1', '0x2', '0x3'),
            {},
            {'abi': ABI, 'address': ADDRESS, 'bytecode': '0x1', 'bytecode_runtime': '0x2', 'source': '0x3'},
        ),
        (
            tuple(),
            {'abi': ABI, 'address': ADDRESS, 'code': '0x1', 'code_runtime': '0x2', 'source': '0x3'},
            {'abi': ABI, 'address': ADDRESS, 'bytecode': '0x1', 'bytecode_runtime': '0x2', 'source': '0x3'},
        ),
        ((ABI, ADDRESS), {'abi': ABI}, TypeError),
        ((ABI, ADDRESS), {'address': ADDRESS}, TypeError),
        ((ADDRESS,), {}, {'address': ADDRESS}),
        ((), {'abi': MALFORMED_ABI_1, 'address': ADDRESS}, ValueError),
        ((), {'abi': MALFORMED_ABI_2, 'address': ADDRESS}, ValueError),
        ((), {'abi': ABI, 'address': CODE}, ValueError),
        ((ABI, CODE), {}, ValueError),
        ((), {'abi': ABI, 'address': PADDED_ADDRESS}, {'abi': ABI, 'address': ADDRESS}),
        ((), {'abi': ABI, 'address': INVALID_CHECKSUM_ADDRESS}, ValueError),
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


@pytest.mark.skipif(sys.version_info.major == 2, reason="Python2 fails weirdly on this test")
def test_deprecated_properties():
    instance = ContactClassForTest(ABI, ADDRESS, '0x1', '0x2', source='0x3')

    with pytest.warns(DeprecationWarning):
        instance.source

    with pytest.warns(DeprecationWarning):
        instance.code

    with pytest.warns(DeprecationWarning):
        instance.code_runtime


@pytest.mark.skipif(sys.version_info.major == 2, reason="Python2 fails weirdly on this test")
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
