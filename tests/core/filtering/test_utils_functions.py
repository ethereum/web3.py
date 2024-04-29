from decimal import (
    Decimal,
)
import pytest

from eth_abi.exceptions import (
    ValueOutOfBounds,
)

from web3._utils.filters import (
    match_fn,
)
from web3.exceptions import (
    Web3ValueError,
)


@pytest.mark.parametrize(
    "data,expected,match_data_and_abi",
    (
        (
            pytest.param(
                (-12345, 000, 111, Decimal(2) + Decimal(1) / Decimal(10)),
                False,
                (
                    ("int", (-12345,)),
                    ("uint32", (444,)),
                    ("int", (565,)),
                    ("ufixed256x4", (Decimal(1.66660),)),
                ),
                id="tuple with incorrect numerical return values",
            )
        ),
        (
            pytest.param(
                (-12345, 000, 111, Decimal(2) + Decimal(1) / Decimal(10)),
                True,
                (
                    ("int", (-12345,)),
                    ("uint32", None),
                    ("int", None),
                    ("ufixed256x4", None),
                ),
                id="tuple with correct numerical return values",
            )
        ),
        (
            pytest.param(
                ("aye", "bee", "sea", b"\xde\xee"),
                False,
                (
                    ("string", ("eee",)),
                    ("string", ("aye",)),
                    ("string", ("sea",)),
                    ("bytes", (b"\x00",)),
                ),
                id="tuple with incorrect string and bytes return values",
            )
        ),
        (
            pytest.param(
                ("aye", "bee", "sea", "0x1234"),
                True,
                (
                    ("string", ("aye",)),
                    ("string", ("bee",)),
                    ("string", ("sea",)),
                    ("bytes", (b"\x124",)),
                ),
                id="tuple with valid string and hex values",
            )
        ),
        (
            pytest.param(
                ("aye", "bee", "sea", b"\xde\xee"),
                True,
                (
                    ("string", ("aye",)),
                    ("string", ("bee",)),
                    ("string", ("sea",)),
                    ("bytes", (b"\xde\xee",)),
                ),
                id="tuple with valid string and bytes values",
            )
        ),
        (
            pytest.param(
                ("aye", "bee", "sea", b"\xde\xee"),
                True,
                (("string", None), ("string", None), ("string", None), ("bytes", None)),
                id="tuple with valid string and bytes values",
            )
        ),
        (
            pytest.param(
                ((b"aye", b"bee"), ("sea", "dee")),
                True,
                (
                    ("bytes3[]", ((b"aye", b"bee"),)),
                    ("string[]", (("sea", "dee"),)),
                ),
                id="lists with valid string and bytes values",
            )
        ),
        (
            pytest.param(
                (("aye", "bee"), ("sea", "dee")),
                True,
                (
                    ("string[]", (("aye", "bee"),)),
                    ("string[]", (("sea", "dee"),)),
                ),
                id="lists with valid string values",
            )
        ),
        (
            pytest.param(
                (["eee", "eff"], ["gee", "eich"]),
                False,
                (
                    ("string[]", (("aye", "bee"),)),
                    ("string[]", (("sea", "dee"),)),
                ),
                id="lists with valid string values, incorrect return values",
            )
        ),
    ),
)
def test_match_fn_with_various_data_types(w3, data, expected, match_data_and_abi):
    abi_types, match_data = zip(*match_data_and_abi)
    encoded_data = w3.codec.encode(abi_types, data)
    assert match_fn(w3.codec, match_data_and_abi, encoded_data) == expected


@pytest.mark.parametrize(
    "data,expected,match_data_and_abi",
    (
        (
            pytest.param(
                ((b"1234",)),
                True,
                (("bytes4", (b"1234",)),),
                id="tuple with valid bytes value",
            )
        ),
        (
            pytest.param(
                (("0x12343434",)),
                True,
                (("bytes4", (b"\x12444",)),),
                id="tuple with valid hex string",
            )
        ),
        (
            pytest.param(
                ((b"1234",)),
                False,
                (("bytes4", (b"5678",)),),
                id="tuple with invalid return value",
            )
        ),
        (
            pytest.param(
                (("0x1212", b"34"),),
                True,
                (("bytes2[]", ((b"\x12\x12", b"34"),)),),
                id="list with valid hexstring and byte values",
            )
        ),
        (
            pytest.param(
                (("0x1212", b"34"),),
                False,
                (("bytes2[]", ((b"12", b"34"),)),),
                id="list with incorrect hexstring and byte return values",
            )
        ),
        (
            pytest.param(
                (["aye", "bee"], ["sea", "dee"]),
                True,
                (
                    ("string[]", (("aye", "bee"),)),
                    ("string[]", (("sea", "dee"),)),
                ),
                id="list with valid string values",
            )
        ),
    ),
)
def test_match_fn_with_various_data_types_non_strict(
    w3_non_strict_abi, data, expected, match_data_and_abi
):
    abi_types, match_data = zip(*match_data_and_abi)
    encoded_data = w3_non_strict_abi.codec.encode(abi_types, data)
    assert (
        match_fn(w3_non_strict_abi.codec, match_data_and_abi, encoded_data) == expected
    )


@pytest.mark.parametrize(
    "data,abi_type",
    (
        pytest.param((b"124",), ("bytes4",), id="tuple with invalid bytes input"),
        pytest.param(("0x123434",), ("bytes4",), id="tuple with hex input - too small"),
        pytest.param(
            ("0x1234343232",), ("bytes4",), id="tuple with hex input - too big"
        ),
    ),
)
def test_encode_with_wrong_types_strict(w3, data, abi_type):
    with pytest.raises(ValueOutOfBounds):
        w3.codec.encode(abi_type, data)


def test_wrong_type_match_data(w3):
    data = ("hello", "goodbye")
    match_data_and_abi = (
        ("string", (50505050,)),
        ("string", (50505050,)),
    )
    abi_types, match_data = zip(*match_data_and_abi)
    encoded_data = w3.codec.encode(abi_types, data)
    with pytest.raises(Web3ValueError):
        match_fn(w3.codec, match_data_and_abi, encoded_data)
