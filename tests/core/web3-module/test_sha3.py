# coding=utf-8

import pytest

from hexbytes import (
    HexBytes,
)

from web3 import Web3


@pytest.mark.parametrize(
    'message, digest',
    [
        ('cowmö', HexBytes('0x0f355f04c0a06eebac1d219b34c598f85a1169badee164be8a30345944885fe8')),
        ('', HexBytes('0xc5d2460186f7233c927e7db2dcc703c0e500b653ca82273b7bfad8045d85a470')),
    ],
)
def test_sha3_text(message, digest):
    assert Web3.sha3(text=message) == digest


@pytest.mark.parametrize(
    'hexstr, digest',
    [
        (
            '0x636f776dc3b6',
            HexBytes('0x0f355f04c0a06eebac1d219b34c598f85a1169badee164be8a30345944885fe8')
        ),
        (
            '636f776dc3b6',
            HexBytes('0x0f355f04c0a06eebac1d219b34c598f85a1169badee164be8a30345944885fe8')
        ),
        (
            '0x',
            HexBytes('0xc5d2460186f7233c927e7db2dcc703c0e500b653ca82273b7bfad8045d85a470')
        ),
        (
            '',
            HexBytes('0xc5d2460186f7233c927e7db2dcc703c0e500b653ca82273b7bfad8045d85a470')
        ),
    ],
)
def test_sha3_hexstr(hexstr, digest):
    assert Web3.sha3(hexstr=hexstr) == digest


@pytest.mark.parametrize(
    'primitive, exception',
    [
        ('0x0', TypeError),
        ('', TypeError),
        (-1, ValueError),
    ],
)
def test_sha3_primitive_invalid(primitive, exception):
    with pytest.raises(exception):
        Web3.sha3(primitive)


@pytest.mark.parametrize(
    'primitive, digest',
    [
        (
            b'cowm\xc3\xb6',
            HexBytes('0x0f355f04c0a06eebac1d219b34c598f85a1169badee164be8a30345944885fe8')
        ),
        (
            b'',
            HexBytes('0xc5d2460186f7233c927e7db2dcc703c0e500b653ca82273b7bfad8045d85a470')
        ),
    ],
)
def test_sha3_primitive(primitive, digest):
    assert Web3.sha3(primitive) == digest


@pytest.mark.parametrize(
    'kwargs',
    [
        {'text': ''},
        {'hexstr': '0x'},
        {'text': '', 'hexstr': '0x'},
    ],
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
