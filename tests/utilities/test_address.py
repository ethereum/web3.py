from __future__ import unicode_literals

import pytest

from web3.utils.address import (
    is_address,
    is_strict_address,
    is_checksum_address,
    to_checksum_address,
    to_address,
    is_same_address,
)


@pytest.mark.parametrize(
    "value,expected",
    [
        (lambda : None, False),
        ("function", False),
        ({}, False),
        ("0xc6d9d2cd449a754c494264e1809c50e34d64562b", True),
        ("c6d9d2cd449a754c494264e1809c50e34d64562b", True),
        # malformed
        ("c6d9d2cd449a754c494264e1809c50e34d64562", False),  # too short
        ("0xc6d9d2cd449a754c494264e1809c50e34d64562", False),
        ("c6d9d2cd449a754c494264e1809c50e34d64562bb", False),  # too long
        ("0xc6d9d2cd449a754c494264e1809c50e34d64562bb", False),
        ("c6d9d2cd449a754c494264e1809c50e34d64562x", False),  # non-hex-character
        ("0xc6d9d2cd449a754c494264e1809c50e34d6456x", False),
    ]
)
def test_is_address(value, expected):
    assert is_address(value) == expected


@pytest.mark.parametrize(
    "value,expected",
    [
        ('0x52908400098527886E0F7030069857D2E4169EE7', True),
        ('0x8617E340B3D01FA5F11F306F4090FD50E238070D', True),
        ('0xde709f2102306220921060314715629080e2fb77', True),
        ('0x27b1fdb04752bbc536007a920d24acb045561c26', True),
        ('0x5aAeb6053F3E94C9b9A09f33669435E7Ef1BeAed', True),
        ('0xfB6916095ca1df60bB79Ce92cE3Ea74c37c5d359', True),
        ('0xdbF03B407c01E7cD3CBea99509d93f8DDDC8C6FB', True),
        ('0xD1220A0cf47c7B9Be7A2E6BA89F429762e7b9aDb', True),
        ('0XD1220A0CF47C7B9BE7A2E6BA89F429762E7B9ADB', False),
        ('0xd1220a0cf47c7b9be7a2e6ba89f429762e7b9adb', False)
    ]
)
def test_is_checksum_address(value, expected):
    assert is_checksum_address(value) == expected, (value, to_checksum_address(value))


@pytest.mark.parametrize(
    "value,expected",
    [
        (lambda: None, False),
        ("function", False),
        ({}, False),
        ('0xc6d9d2cd449a754c494264e1809c50e34d64562b', True),
        ('c6d9d2cd449a754c494264e1809c50e34d64562b', False)
    ]
)
def test_is_strict_address(value, expected):
    assert is_strict_address(value) == expected


@pytest.mark.parametrize(
    "value,expected",
    (
        (
            b'\xd3\xcd\xa9\x13\xde\xb6\xf6yg\xb9\x9dg\xac\xdf\xa1q,)6\x01',
            '0xd3cda913deb6f67967b99d67acdfa1712c293601',
        ),
        (
            b'0xc6d9d2cd449a754c494264e1809c50e34d64562b',
            '0xc6d9d2cd449a754c494264e1809c50e34d64562b',
        ),
        (
            '0xc6d9d2cd449a754c494264e1809c50e34d64562b',
            '0xc6d9d2cd449a754c494264e1809c50e34d64562b',
        ),
        (
            b'0XC6D9D2CD449A754C494264E1809C50E34D64562B',
            '0xc6d9d2cd449a754c494264e1809c50e34d64562b',
        ),
        (
            '0XC6D9D2CD449A754C494264E1809C50E34D64562B',
            '0xc6d9d2cd449a754c494264e1809c50e34d64562b',
        ),
        (
            'c6d9d2cd449a754c494264e1809c50e34d64562b',
            '0xc6d9d2cd449a754c494264e1809c50e34d64562b',
        ),
        (
            'C6D9D2CD449A754C494264E1809C50E34D64562B',
            '0xc6d9d2cd449a754c494264e1809c50e34d64562b',
        ),
        (
            '0x000000000000000000000000c305c901078781c232a2a521c2af7980f8385ee9',
            '0xc305c901078781c232a2a521c2af7980f8385ee9',
        ),
        (
            b'0x000000000000000000000000c305c901078781c232a2a521c2af7980f8385ee9',
            '0xc305c901078781c232a2a521c2af7980f8385ee9',
        ),
        (
            '000000000000000000000000c305c901078781c232a2a521c2af7980f8385ee9',
            '0xc305c901078781c232a2a521c2af7980f8385ee9',
        ),
    )
)
def test_to_address(value, expected):
    assert to_address(value) == expected


@pytest.mark.parametrize(
    "value,expected",
    (
        (
            '0xc6d9d2cd449a754c494264e1809c50e34d64562b',
            '0xc6d9d2cD449A754c494264e1809c50e34D64562b',
        ),
        (
            'c6d9d2cd449a754c494264e1809c50e34d64562b',
            '0xc6d9d2cD449A754c494264e1809c50e34D64562b',
        ),
    )
)
def test_to_checksum_address(value, expected):
    assert to_checksum_address(value) == expected, (to_checksum_address(value), expected)

@pytest.mark.parametrize(
    "address1,address2,expected",
    (
        (
            '0xc6d9d2cd449a754c494264e1809c50e34d64562b',
            '0xc6d9d2cD449A754c494264e1809c50e34D64562b',
            True,
        ),
        (
            'c6d9d2cd449a754c494264e1809c50e34d64562b',
            '0xc6d9d2cD449A754c494264e1809c50e34D64562b',
            True,
        ),
        (
            b'\xd3\xcd\xa9\x13\xde\xb6\xf6yg\xb9\x9dg\xac\xdf\xa1q,)6\x01',
            '0xd3cda913deb6f67967b99d67acdfa1712c293601',
            True,
        ),
        (
            b'0xc6d9d2cd449a754c494264e1809c50e34d64562b',
            '0xc6d9d2cd449a754c494264e1809c50e34d64562b',
            True,
        ),
        (
            b'0xc6d9d2cd449a754c494264e1809c50e34d64562b',
            '0xc305c901078781c232a2a521c2af7980f8385ee9',
            False,
        ),
        (
            'c6d9d2cd449a754c494264e1809c50e34d64562b',
            '0xc6d9d2cd449a754c494264e1809c50e34d64562b',
            True,
        ),
        (
            'C6D9D2CD449A754C494264E1809C50E34D64562B',
            '0xc6d9d2cd449a754c494264e1809c50e34d64562b',
            True,
        ),
        (
            '0x000000000000000000000000c305c901078781c232a2a521c2af7980f8385ee9',
            '0xc305c901078781c232a2a521c2af7980f8385ee9',
            True,
        ),
        (
            b'0x000000000000000000000000c305c901078781c232a2a521c2af7980f8385ee9',
            '0xc6d9d2cd449a754c494264e1809c50e34d64562b',
            False,
        ),
    )
)

def test_is_same_address(address1, address2, expected):
    assert is_same_address(address1, address2) == expected
