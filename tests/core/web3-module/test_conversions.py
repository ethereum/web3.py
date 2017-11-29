# coding=utf-8

import pytest

from web3 import Web3


@pytest.mark.parametrize(
    'val, expected',
    (
        (b'\x01', b'\x01'),
        (b'\xff', b'\xff'),
        (b'\x00', b'\x00'),
        (0x1, b'\x01'),
        (0x0001, b'\x01'),
        (0xFF, b'\xff'),
        (0, b'\x00'),
        (256, b'\x01\x00'),
        (True, b'\x01'),
        (False, b'\x00'),
    ),
)
def test_to_bytes_primitive(val, expected):
    assert Web3.toBytes(val) == expected


@pytest.mark.parametrize(
    'val, expected',
    (
        ('0x', b''),
        ('0x0', b'\x00'),
        ('0x1', b'\x01'),
        ('0', b'\x00'),
        ('1', b'\x01'),
        ('0xFF', b'\xff'),
        ('0x100', b'\x01\x00'),
        ('0x0000', b'\x00\x00'),
        ('0000', b'\x00\x00'),
    ),
)
def test_to_bytes_hexstr(val, expected):
    assert Web3.toBytes(hexstr=val) == expected


@pytest.mark.parametrize(
    'val, expected',
    (
        ('cowmö', b'cowm\xc3\xb6'),
        ('', b''),
    ),
)
def test_to_bytes_text(val, expected):
    assert Web3.toBytes(text=val) == expected


def test_to_text_identity():
    assert Web3.toText(text='pass-through') == 'pass-through'


@pytest.mark.parametrize(
    'val, expected',
    (
        (b'', ''),
        ('0x', ''),
        (b'cowm\xc3\xb6', 'cowmö'),
        ('0x636f776dc3b6', 'cowmö'),
        (0x636f776dc3b6, 'cowmö'),
        ('0xa', '\n'),
    ),
)
def test_to_text(val, expected):
    assert Web3.toText(val) == expected


@pytest.mark.parametrize(
    'val, expected',
    (
        ('0x', ''),
        ('0xa', '\n'),
        ('0x636f776dc3b6', 'cowmö'),
        ('636f776dc3b6', 'cowmö'),
    ),
)
def test_to_text_hexstr(val, expected):
    assert Web3.toText(hexstr=val) == expected


@pytest.mark.parametrize(
    'val, expected',
    (
        (b'\x00', 0),
        (b'\x01', 1),
        (b'\x00\x01', 1),
        (b'\x01\x00', 256),
        (True, 1),
        (False, 0),
        ('255', TypeError),
        ('-1', TypeError),
        ('0x0', TypeError),
        ('0x1', TypeError),
    ),
)
def test_to_int(val, expected):
    if isinstance(expected, type):
        with pytest.raises(expected):
            Web3.toInt(val)
    else:
        assert Web3.toInt(val) == expected


@pytest.mark.parametrize(
    'val, expected',
    (
        ('0', 0),
        ('-1', -1),
        ('255', 255),
        ('0x0', ValueError),
        ('0x1', ValueError),
        ('1.1', ValueError),
        ('a', ValueError),
    ),
)
def test_to_int_text(val, expected):
    if isinstance(expected, type):
        with pytest.raises(expected):
            Web3.toInt(text=val)
    else:
        assert Web3.toInt(text=val) == expected


@pytest.mark.parametrize(
    'val, expected',
    (
        ('0x0', 0),
        ('0x1', 1),
        ('0x01', 1),
        ('0x10', 16),
        ('0', 0),
        ('1', 1),
        ('01', 1),
        ('10', 16),
    ),
)
def test_to_int_hexstr(val, expected):
    assert Web3.toInt(hexstr=val) == expected


@pytest.mark.parametrize(
    'val, expected',
    (
        (b'\x00', '0x00'),
        (b'\x01', '0x01'),
        (b'\x10', '0x10'),
        (b'\x01\x00', '0x0100'),
        (b'\x00\x0F', '0x000f'),
        (b'', '0x'),
        (0, '0x0'),
        (1, '0x1'),
        (16, '0x10'),
        (256, '0x100'),
        (0x0, '0x0'),
        (0x0F, '0xf'),
        (False, '0x0'),
        (True, '0x1'),
    ),
)
def test_to_hex(val, expected):
    assert Web3.toHex(val) == expected


@pytest.mark.parametrize(
    'val, expected',
    (
        ('', '0x'),
        ('cowmö', '0x636f776dc3b6'),
    ),
)
def test_to_hex_text(val, expected):
    assert Web3.toHex(text=val) == expected


@pytest.mark.parametrize(
    'val, expected',
    (
        ('0x0', '0x0'),
        ('0x1', '0x1'),
        ('0x0001', '0x0001'),
        ('0x10', '0x10'),
        ('0xF', '0xf'),
        ('F', '0xf'),
    ),
)
def test_to_hex_cleanup_only(val, expected):
    assert Web3.toHex(hexstr=val) == expected
