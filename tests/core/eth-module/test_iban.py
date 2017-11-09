import pytest

from web3.exceptions import (
    InvalidAddress,
)


@pytest.mark.parametrize(
    'value,expected',
    (
        (
            {"institution": 'XREG', "identifier": 'GAVOFYORK'},
            'XE81ETHXREGGAVOFYORK',
        ),
    )
)
def test_createIndirect(value, expected, web3):
    actual = web3.eth.iban.createIndirect(value).toString()
    assert actual == expected


@pytest.mark.parametrize(
    'value,expected',
    (
        (
            '00c5496aee77c1ba1f0854206a26dda82a81d6d8',
            InvalidAddress,
        ),
        (
            '0x00c5496aee77c1ba1f0854206a26dda82a81d6d8',
            InvalidAddress,
        ),
        (
            '0x00c5496aEe77C1bA1f0854206A26DdA82a81D6D8',
            'XE7338O073KYGTWWZN0F2WZ0R8PX5ZPPZS',
        ),
        (
            '0x11c5496AEE77c1bA1f0854206a26dDa82A81D6D8',
            'XE1222Q908LN1QBBU6XUQSO1OHWJIOS46OO',
        ),
        (
            '0x52Dc504a422f0E2A9e7632A34a50f1a82F8224c7',
            'XE499OG1EH8ZZI0KXC6N83EKGT1BM97P2O7',
        ),
        (
            '0x0000A5327eAB78357CbF2aE8f3d49Fd9d90C7D22',
            'XE0600DQK33XDTYUCRI0KYM5ELAKXDWWF6',
        ),
        (
            '0x606060405261022e806100126000396000f360606040523615610074576000357c01000000000000000000000000000000000000000000000000000000009004806316216f391461007657806361bc221a146100995780637cf5dab0146100bc578063a5f3c23b146100e8578063d09de08a1461011d578063dcf537b11461014057610074565b005b610083600480505061016c565b6040518082815260200191505060405180910390f35b6100a6600480505061017f565b6040518082815260200191505060405180910390f35b6100d26004808035906020019091905050610188565b6040518082815260200191505060405180910390f35b61010760048080359060200190919080359060200190919050506101ea565b6040518082815260200191505060405180910390f35b61012a6004805050610201565b6040518082815260200191505060405180910390f35b6101566004808035906020019091905050610217565b6040518082815260200191505060405180910390f35b6000600d9050805080905061017c565b90565b60006000505481565b6000816000600082828250540192505081905550600060005054905080507f3496c3ede4ec3ab3686712aa1c238593ea6a42df83f98a5ec7df9834cfa577c5816040518082815260200191505060405180910390a18090506101e5565b919050565b6000818301905080508090506101fb565b92915050565b600061020d6001610188565b9050610214565b90565b60006007820290508050809050610229565b91905056',  # noqa: E501
            InvalidAddress,
        ),
        (
            '0xd3CDA913deB6f67967B99D67aCDFa1712C293601',
            InvalidAddress,
        ),
    ),
)
def test_fromAddress(value, expected, web3):

    if isinstance(expected, type) and issubclass(expected, Exception):
        with pytest.raises(expected):
            web3.eth.iban.fromAddress(value).toString()
        return

    actual = web3.eth.iban.fromAddress(value).toString()
    assert actual == expected


@pytest.mark.parametrize(
    'value,expected',
    (
        (
            lambda: None,
            False,
        ),
        (
            'function',
            False,
        ),
        (
            {},
            False,
        ),
        (
            '[]',
            False,
        ),
        (
            '[1, 2]',
            False,
        ),
        (
            '{}',
            False,
        ),
        (
            '{"a": 123, "b" :3,}',
            False,
        ),
        (
            '{"c" : 2}',
            False,
        ),
        (
            'XE81ETHXREGGAVOFYORK',
            True,
        ),
        (
            'XE82ETHXREGGAVOFYORK',
            False,  # control number is invalid
        ),
        (
            'XE81ETCXREGGAVOFYORK',
            False,
        ),
        (
            'XE81ETHXREGGAVOFYORKD',
            False,
        ),
        (
            'XE81ETHXREGGaVOFYORK',
            False,
        ),
        (
            'XE7338O073KYGTWWZN0F2WZ0R8PX5ZPPZS',
            True,
        ),
        (
            'XE7438O073KYGTWWZN0F2WZ0R8PX5ZPPZS',
            False,  # control number is invalid
        ),
        (
            'XD7338O073KYGTWWZN0F2WZ0R8PX5ZPPZS',
            False,
        ),
        (
            'XE1222Q908LN1QBBU6XUQSO1OHWJIOS46OO',
            True,
        ),
    ),
)
def test_isValid(value, expected, web3):
    actual = web3.eth.iban.isValid(value)
    assert actual is expected

    iban = web3.eth.iban(value)
    assert iban.isValid() is expected


@pytest.mark.parametrize(
    "value,expected",
    (
        (
            'XE7338O073KYGTWWZN0F2WZ0R8PX5ZPPZS',
            '0x00c5496aEe77C1bA1f0854206A26DdA82a81D6D8',
        ),
    )
)
def test_toAddress(value, expected, web3):
    actual = web3.eth.iban(value).address()
    assert actual == expected
