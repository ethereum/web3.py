# coding=utf-8

import pytest
import sys


@pytest.mark.skipif(sys.version_info.major < 3, reason="requires python 3")
@pytest.mark.parametrize(
    'message, expected',
    [
        (
            'Message tö sign. Longer than hash!',
            '0x10c7cb57942998ab214c062e7a57220a174aacd80418cead9f90ec410eacada1',
        ),
        (
            # Intentionally sneaky: message is a hexstr interpreted as text
            '0x4d6573736167652074c3b6207369676e2e204c6f6e676572207468616e206861736821',
            '0x6192785e9ad00100e7332ff585824b65eafa30bc8f1265cf86b5368aa3ab5d56',
        ),
    ]
)
def test_recovery_message_text_hash(web3, message, expected):
    assert web3.eth._recoveryMessageHash(text=message) == expected


@pytest.mark.skipif(sys.version_info.major < 3, reason="requires python 3")
@pytest.mark.parametrize(
    'message, expected',
    [
        (
            '0x4d6573736167652074c3b6207369676e2e204c6f6e676572207468616e206861736821',
            '0x10c7cb57942998ab214c062e7a57220a174aacd80418cead9f90ec410eacada1',
        ),
        (
            '0x29d9f7d6a1d1e62152f314f04e6bd4300ad56fd72102b6b83702869a089f470c',
            '0xe709159ef0e6323c705786fc50e47a8143812e9f82f429e585034777c7bf530b',
        ),
    ]
)
def test_recovery_message_hexstr_hash(web3, message, expected):
    assert web3.eth._recoveryMessageHash(hexstr=message) == expected
