# coding=utf-8

from __future__ import unicode_literals

import pytest
import sys

from web3 import Web3


@pytest.mark.parametrize(
    'message, digest',
    [
        ('bÖb', '0x12d367a59cc89d452cc898bdcb85c576e35f7ec7d156bb8f9b86b8ebe8c18896'),
        ('', '0xc5d2460186f7233c927e7db2dcc703c0e500b653ca82273b7bfad8045d85a470'),
    ]
)
def test_sha3_text(message, digest):
    assert Web3.sha3(text=message) == digest


@pytest.mark.parametrize(
    'hexstr, digest',
    [
        ('0x624fcc8862', '0x12d367a59cc89d452cc898bdcb85c576e35f7ec7d156bb8f9b86b8ebe8c18896'),
        ('0x', '0xc5d2460186f7233c927e7db2dcc703c0e500b653ca82273b7bfad8045d85a470'),
    ]
)
def test_sha3_hexstr(hexstr, digest):
    assert Web3.sha3(hexstr=hexstr) == digest


@pytest.mark.parametrize(
    'primitive, digest',
    [
        (b'bO\xcc\x88b', '0x12d367a59cc89d452cc898bdcb85c576e35f7ec7d156bb8f9b86b8ebe8c18896'),
        (b'', '0xc5d2460186f7233c927e7db2dcc703c0e500b653ca82273b7bfad8045d85a470'),
    ]
)
def test_sha3_primitive(primitive, digest):
    if primitive and sys.version_info[0] < 3:
        # py2 doesn't recognize bytes, tries to decode as hexstr.
        # Old implementation would have failed, too
        pytest.raises(TypeError)
    else:
        assert Web3.sha3(primitive) == digest
