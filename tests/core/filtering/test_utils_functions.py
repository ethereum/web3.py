from decimal import (
    Decimal,
)
import pytest

from eth_abi import (
    encode_abi,
)

from web3._utils.filters import (
    match_fn,
)


@pytest.mark.parametrize(
    "data,expected,match_data_and_abi",
    (
        (
            (-12345, 000, 111, Decimal(2) + Decimal(1) / Decimal(10)),
            False,
            (
                ("int", (-12345,)),
                ("uint32", (444,)),
                ("int", (565,)),
                ("ufixed256x4", (Decimal(1.66660),))
            )
        ),
        (
            (-12345, 000, 111, Decimal(2) + Decimal(1) / Decimal(10)),
            True,
            (
                ("int", (-12345,)),
                ("uint32", None),
                ("int", None),
                ("ufixed256x4", None)
            )
        ),
        (
            ("aye", "bee", "sea", b"\xde\xee"),
            False,
            (
                ("string", ("eee",)),
                ("string", ("aye",)),
                ("string", ("sea",)),
                ("bytes", (b"\x00",))
            )
        ),
        (
            ("aye", "bee", "sea", b"\xde\xee"),
            True,
            (
                ("string", ("aye",)),
                ("string", ("bee",)),
                ("string", ("sea",)),
                ("bytes", (b"\xde\xee",))
            )
        ),
        (
            ("aye", "bee", "sea", b"\xde\xee"),
            True,
            (
                ("string", None),
                ("string", None),
                ("string", None),
                ("bytes", None)
            )
        ),
        (
            (("aye", "bee"), ("sea", "dee")),
            True,
            (
                ("string[]", (("aye", "bee"),)),
                ("string[]", (("sea", "dee"),)),
            )
        ),
        (
            (["eee", "eff"], ["gee", "eich"]),
            False,
            (
                ("string[]", (("aye", "bee"),)),
                ("string[]", (("sea", "dee"),)),
            )
        ),
    )
)
def test_match_fn_with_various_data_types(data, expected, match_data_and_abi):
    abi_types, match_data = zip(*match_data_and_abi)
    encoded_data = encode_abi(abi_types, data)
    assert match_fn(match_data_and_abi, encoded_data) == expected


def test_wrong_type_match_data():
    data = ("hello", "goodbye")
    match_data_and_abi = (
        ("string", (50505050,)),
        ("string", (50505050,)),
    )
    abi_types, match_data = zip(*match_data_and_abi)
    encoded_data = encode_abi(abi_types, data)
    with pytest.raises(ValueError):
        match_fn(match_data_and_abi, encoded_data)
