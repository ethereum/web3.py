import pytest

from web3.utils.address import (
    get_create_address,
)


@pytest.mark.parametrize(
    "sender,nonce,expected",
    (
        (
            "0x39fA8c5f2793459D6622857E7D9FbB4BD91766d3",
            8,
            "0xc083e9947Cf02b8FfC7D3090AE9AEA72DF98FD47",
        ),
        (
            "0x39fa8c5f2793459d6622857e7d9fbb4bd91766d3",
            8,
            "0xc083e9947Cf02b8FfC7D3090AE9AEA72DF98FD47",
        ),
        (
            "0x18dd4e0eb8699ea4fee238de41ecfb95e32272f8",
            0,
            "0x3845badAde8e6dFF049820680d1F14bD3903a5d0",
        ),
    ),
)
def test_address_get_create_address(sender, nonce, expected):
    actual = get_create_address(sender, nonce)
    assert actual == expected
