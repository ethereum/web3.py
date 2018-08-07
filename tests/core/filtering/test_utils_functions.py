from decimal import (
    Decimal,
)
import pytest

from eth_abi import (
    encode_abi,
)

from web3.utils.filters import (
    match_fn,
)


def test_static_typed_non_matching_data():
    data = (-12345, 000, 111, Decimal(2) + Decimal(1) / Decimal(10))
    expected = False
    match_data_and_abi = (
        ("int", (-12345,)),
        ("uint32", (444,)),
        ("int", (565,)),
        ("ufixed256x4", (Decimal(1.66660),))
    )
    abi_types, match_data = zip(*match_data_and_abi)
    encoded_data = encode_abi(abi_types, data)
    assert match_fn(match_data_and_abi, encoded_data) == expected


def test_static_typed_matching_data():
    data = (-12345, 000, 111, Decimal(2) + Decimal(1) / Decimal(10))
    expected = True
    match_data_and_abi = (
        ("int", (-12345,)),
        ("uint32", None),
        ("int", None),
        ("ufixed256x4", None)
    )
    abi_types, match_data = zip(*match_data_and_abi)
    encoded_data = encode_abi(abi_types, data)
    assert match_fn(match_data_and_abi, encoded_data) == expected


def test_dynamic_typed_non_matching_data():
    data = ("aye", "bee", "sea", b"\xde\xee")
    expected = False
    match_data_and_abi = (
        ("string", ("eee",)),
        ("string", ("aye",)),
        ("string", ("sea",)),
        ("bytes", (b"\x00",))
    )
    abi_types, match_data = zip(*match_data_and_abi)
    encoded_data = encode_abi(abi_types, data)
    assert match_fn(match_data_and_abi, encoded_data) == expected


def test_dynamic_typed_matching_data():
    data = ("aye", "bee", "sea", b"\xde\xee")
    expected = True
    match_data_and_abi = (
        ("string", ("aye",)),
        ("string", ("bee",)),
        ("string", ("sea",)),
        ("bytes", (b"\xde\xee",))
    )
    abi_types, match_data = zip(*match_data_and_abi)
    encoded_data = encode_abi(abi_types, data)
    assert match_fn(match_data_and_abi, encoded_data) == expected


def test_empty_matching_data():
    data = ("aye", "bee", "sea", b"\xde\xee")
    expected = True
    match_data_and_abi = (("string", None), ("string", None), ("string", None), ("bytes", None))
    abi_types, match_data = zip(*match_data_and_abi)
    encoded_data = encode_abi(abi_types, data)
    assert match_fn(match_data_and_abi, encoded_data) == expected


def test_dynamic_list_typed_matching_data():
    data = (("aye", "bee"), ("sea", "dee"))
    expected = True
    match_data_and_abi = (
        ("string[]", (("aye", "bee"),)),
        ("string[]", (("sea", "dee"),)),
    )
    abi_types, match_data = zip(*match_data_and_abi)
    encoded_data = encode_abi(abi_types, data)
    assert match_fn(match_data_and_abi, encoded_data) == expected


def test_dynamic_list_typed_non_matching_data():
    data = (["eee", "eff"], ["gee", "eich"])
    expected = False
    match_data_and_abi = (
        ("string[]", (("aye", "bee"),)),
        ("string[]", (("sea", "dee"),)),
    )
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
