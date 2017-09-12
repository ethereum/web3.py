# coding=utf-8

from __future__ import unicode_literals

import pytest
import sys

from web3 import Web3


@pytest.mark.parametrize(
    'val, expected',
    (
        (0x01, b'\x01'),
        (0xFF, b'\xff'),
        (0, b'\x00'),
        (256, b'\x01\x00'),
    )
)
def test_to_bytes_primitive(val, expected):
    if sys.version_info.major < 3:
        with pytest.raises(NotImplementedError):
            Web3.toBytes(val)
    else:
        assert Web3.toBytes(val) == expected


@pytest.mark.parametrize(
    'val, expected',
    (
        ('0x', b''),
        ('0x0', b'\x00'),
        ('0x1', b'\x01'),
        ('0xFF', b'\xff'),
        ('0x100', b'\x01\x00'),
        ('0x0000', b'\x00\x00'),
    )
)
def test_to_bytes_hexstr(val, expected):
    if sys.version_info.major < 3:
        with pytest.raises(NotImplementedError):
            Web3.toBytes(hexstr=val)
    else:
        assert Web3.toBytes(hexstr=val) == expected


@pytest.mark.parametrize(
    'val, expected',
    (
        ('cowmö', b'cowm\xc3\xb6'),
        ('', b''),
    )
)
def test_to_bytes_text(val, expected):
    if sys.version_info.major < 3:
        with pytest.raises(NotImplementedError):
            Web3.toBytes(text=val)
    else:
        assert Web3.toBytes(text=val) == expected


@pytest.mark.parametrize(
    'val, expected',
    (
        (b'', ''),
        ('0x', ''),
        (b'cowm\xc3\xb6', 'cowmö'),
        ('0x636f776dc3b6', 'cowmö'),
        (0x636f776dc3b6, 'cowmö'),
    )
)
def test_to_text(val, expected):
    if sys.version_info.major < 3:
        with pytest.raises(NotImplementedError):
            Web3.toText(val)
    else:
        assert Web3.toText(val) == expected
