import pytest
import web3.utils.address as address

@pytest.mark.parametrize(
    "value,expected",
    [
    (lambda : None, False),
    ("function", False),
    ({}, False),
    ("0xc6d9d2cd449a754c494264e1809c50e34d64562b", True),
    ("c6d9d2cd449a754c494264e1809c50e34d64562b", True)
    ]
)
def test_isAddress(value, expected):
    assert address.isAddress(value) == expected

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
def test_isChecksumAddress(value, expected):
    assert address.isChecksumAddress(value) == expected

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
def test_isStrictAddress(value, expected):
    assert address.isStrictAddress(value) == expected
