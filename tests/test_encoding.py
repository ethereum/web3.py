# -*- coding: utf-8 -*-
import pytest
import web3.utils.encoding as encoding


@pytest.mark.parametrize(
    "value,expected",
    [
    ('myString', '0x6d79537472696e67'),
    ('myString\x00', '0x6d79537472696e6700'),
    #('\u0003\u0000\u0000\u00005èÆÕL]\u0012|Î¾\u001a7«\u00052\u0011(ÐY\n<\u0010\u0000\u0000\u0000\u0000\u0000\u0000e!ßd/ñõì\f:z¦Î¦±ç·÷Í¢Ëß\u00076*\bñùC1ÉUÀé2\u001aÓB', '0x0300000035e8c6d54c5d127c9dcebe9e1a37ab9b05321128d097590a3c100000000000006521df642ff1f5ec0c3a7aa6cea6b1e7b7f7cda2cbdf07362a85088e97f19ef94331c955c0e9321ad386428c')
    ]
)
def test_fromAscii(value, expected):
    assert encoding.fromAscii(value) == expected


@pytest.mark.parametrize(
    "value,expected",
    [
    (
        1,
        '0x1'
    ),
    (
        '1',
        '0x1'
    ),
    (
        15,
        '0xf'
    ),
    (
        '15',
        '0xf'
    ),
    (
        -1,
        '-0x1'
    ),
    (
        '-1',
        '-0x1'
    ),
    (
        -15,
        '-0xf'
    ),
    (
        '-15',
        '-0xf'
    ),
    (
        0,
        '0x0'
    ),
    (
        '0',
        '0x0'
    ),
    (
        -0,
        '0x0'
    ),
    (
        '-0',
        '0x0'
    )
    ]
)
def test_fromDecimal(value, expected):
    assert encoding.fromDecimal(value) == expected