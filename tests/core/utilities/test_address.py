import pytest

from web3.utils.address import (
    get_create2_address,
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


@pytest.mark.parametrize(
    "sender,salt,init_code,expected",
    (
        (
            "0x0000000000000000000000000000000000000000",
            "0x0000000000000000000000000000000000000000000000000000000000000000",
            "0x00",
            "0x4D1A2e2bB4F88F0250f26Ffff098B0b30B26BF38",
        ),
        (
            "0xdeadbeef00000000000000000000000000000000",
            "0x0000000000000000000000000000000000000000000000000000000000000000",
            "0x00",
            "0xB928f69Bb1D91Cd65274e3c79d8986362984fDA3",
        ),
        (
            "0xdeadbeef00000000000000000000000000000000",
            "0x000000000000000000000000feed000000000000000000000000000000000000",
            "0x00",
            "0xD04116cDd17beBE565EB2422F2497E06cC1C9833",
        ),
        (
            "0xDEADBEEF00000000000000000000000000000000",
            "0x000000000000000000000000feed000000000000000000000000000000000000",
            "0x00",
            "0xD04116cDd17beBE565EB2422F2497E06cC1C9833",
        ),
        (
            "0x0000000000000000000000000000000000000000",
            "0x0000000000000000000000000000000000000000000000000000000000000000",
            "0xdeadbeef",
            "0x70f2b2914A2a4b783FaEFb75f459A580616Fcb5e",
        ),
    ),
)
def test_address_get_create2_address(sender, salt, init_code, expected):
    actual = get_create2_address(sender, salt, init_code)
    assert actual == expected
