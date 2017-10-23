# coding=utf-8

from __future__ import unicode_literals

import pytest
import sys

from web3 import Web3


@pytest.mark.parametrize(
    'message, digest',
    [
        ('cowmö', '0x0f355f04c0a06eebac1d219b34c598f85a1169badee164be8a30345944885fe8'),
        ('', '0xc5d2460186f7233c927e7db2dcc703c0e500b653ca82273b7bfad8045d85a470'),
    ]
)
def test_sha3_text(message, digest):
    assert Web3.sha3(text=message) == digest


@pytest.mark.parametrize(
    'hexstr, digest',
    [
        ('0x636f776dc3b6', '0x0f355f04c0a06eebac1d219b34c598f85a1169badee164be8a30345944885fe8'),
        ('0x', '0xc5d2460186f7233c927e7db2dcc703c0e500b653ca82273b7bfad8045d85a470'),
    ]
)
def test_sha3_hexstr(hexstr, digest):
    assert Web3.sha3(hexstr=hexstr) == digest


@pytest.mark.parametrize(
    'primitive, digest',
    [
        (b'cowm\xc3\xb6', '0x0f355f04c0a06eebac1d219b34c598f85a1169badee164be8a30345944885fe8'),
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


@pytest.mark.parametrize(
    'kwargs',
    [
        {'text': ''},
        {'hexstr': '0x'},
        {'text': '', 'hexstr': '0x'},
    ]
)
def test_sha3_raise_if_primitive_and(kwargs):
    # must not set more than one input
    with pytest.raises(TypeError):
        Web3.sha3('', **kwargs)


def test_sha3_raise_if_hexstr_and_text():
    with pytest.raises(TypeError):
        Web3.sha3(hexstr='0x', text='')


def test_sha3_raise_if_no_args():
    with pytest.raises(TypeError):
        Web3.sha3()
