import pytest


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
            'XE7338O073KYGTWWZN0F2WZ0R8PX5ZPPZS',
        ),
        (
            '0x00c5496aee77c1ba1f0854206a26dda82a81d6d8',
            'XE7338O073KYGTWWZN0F2WZ0R8PX5ZPPZS',
        ),
        (
            '0x11c5496aee77c1ba1f0854206a26dda82a81d6d8',
            'XE1222Q908LN1QBBU6XUQSO1OHWJIOS46OO',
        ),
        (
            '0x52dc504a422f0e2a9e7632a34a50f1a82f8224c7',
            'XE499OG1EH8ZZI0KXC6N83EKGT1BM97P2O7',
        ),
        (
            '0x0000a5327eab78357cbf2ae8f3d49fd9d90c7d22',
            'XE0600DQK33XDTYUCRI0KYM5ELAKXDWWF6',
        ),
    ),
)
def test_fromAddress(value, expected, web3):
    actual = web3.eth.iban.fromAddress(value).toString()
    assert actual == expected


@pytest.mark.parametrize(
    'value,expected',
    (
        (
            lambda : None,
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
            '0x00c5496aee77c1ba1f0854206a26dda82a81d6d8',
        ),
    )
)
def test_toAddress(value, expected, web3):
    actual = web3.eth.iban(value).address()
    assert actual == expected
