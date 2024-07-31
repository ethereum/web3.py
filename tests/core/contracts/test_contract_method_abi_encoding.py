import json
import pytest

from web3 import (
    constants,
)
from web3.exceptions import (
    MismatchedABI,
)

ABI_A = json.loads(
    '[{"constant":false,"inputs":[],"name":"a","outputs":[],"type":"function"}]'
)
ABI_B = json.loads(
    '[{"constant":false,"inputs":[{"name":"","type":"uint256"}],"name":"a","outputs":[],"type":"function"}]'  # noqa: E501
)
ABI_C = json.loads(
    '[{"constant":false,"inputs":[],"name":"a","outputs":[],"type":"function"},{"constant":false,"inputs":[{"name":"","type":"bytes32"}],"name":"a","outputs":[],"type":"function"},{"constant":false,"inputs":[{"name":"","type":"uint256"}],"name":"a","outputs":[],"type":"function"}]'  # noqa: E501
)
ABI_D = json.loads(
    '[{ "constant": false, "inputs": [ { "name": "b", "type": "bytes32[]" } ], "name": "byte_array", "outputs": [], "payable": false, "type": "function" }]'  # noqa: E501
)


@pytest.mark.parametrize(
    "abi,arguments,data,expected",
    (
        pytest.param(
            ABI_B,
            [0],
            None,
            "0xf0fdf8340000000000000000000000000000000000000000000000000000000000000000",  # noqa: E501
            id="ABI_B, valid int args, no data",
        ),
        pytest.param(
            ABI_B,
            [1],
            None,
            "0xf0fdf8340000000000000000000000000000000000000000000000000000000000000001",  # noqa: E501
            id="ABI_B, valid int args, no data",
        ),
        pytest.param(
            ABI_C,
            [1],
            None,
            "0xf0fdf8340000000000000000000000000000000000000000000000000000000000000001",  # noqa: E501
            id="ABI_B, valid int args, no data",
        ),
        pytest.param(
            ABI_C,
            [b"a" + (b"\x00" * 31)],
            None,
            "0x9f3fab586100000000000000000000000000000000000000000000000000000000000000",  # noqa: E501
            id="ABI_C, valid byte args, no data",
        ),
        pytest.param(
            ABI_C,
            [f"0x61{'00' * 31}"],
            None,
            "0x9f3fab586100000000000000000000000000000000000000000000000000000000000000",  # noqa: E501
            id="ABI_C, valid hex args, no data",
        ),
    ),
)
def test_contract_abi_encoding(w3, abi, arguments, data, expected):
    contract = w3.eth.contract(abi=abi)
    actual = contract.encode_abi("a", arguments, data=data)
    assert actual == expected


@pytest.mark.parametrize(
    "abi,arguments,data,expected",
    (
        pytest.param(ABI_A, [], None, "0x0dbe671f", id="ABI_A, no args, no data"),
        pytest.param(
            ABI_A, [], "0x12345678", "0x12345678", id="ABI_A, no args, some data"
        ),
        pytest.param(
            ABI_B,
            [0],
            None,
            "0xf0fdf8340000000000000000000000000000000000000000000000000000000000000000",  # noqa: E501
            id="ABI_B, valid int args, no data",
        ),
        pytest.param(
            ABI_B,
            [1],
            None,
            "0xf0fdf8340000000000000000000000000000000000000000000000000000000000000001",  # noqa: E501
            id="ABI_B, valid int args, no data",
        ),
        pytest.param(
            ABI_C,
            [1],
            None,
            "0xf0fdf8340000000000000000000000000000000000000000000000000000000000000001",  # noqa: E501
            id="ABI_B, valid int args, no data",
        ),
        pytest.param(
            ABI_C,
            [b"a"],
            None,
            "0x9f3fab586100000000000000000000000000000000000000000000000000000000000000",  # noqa: E501
            id="ABI_C, valid byte args, no data",
        ),
        pytest.param(
            ABI_C,
            ["0x61"],
            None,
            "0x9f3fab586100000000000000000000000000000000000000000000000000000000000000",  # noqa: E501
            id="ABI_C, valid hex args, no data",
        ),
    ),
)
def test_contract_abi_encoding_non_strict(
    w3_non_strict_abi, abi, arguments, data, expected
):
    contract = w3_non_strict_abi.eth.contract(abi=abi)
    actual = contract.encode_abi("a", arguments, data=data)
    assert actual == expected


def test_contract_abi_encoding_kwargs(w3):
    contract = w3.eth.contract(abi=ABI_D)
    kwargs = {
        "b": [
            "0x5595c210956e7721f9b692e702708556aa9aabb14ea163e96afa56ffbe9fa809",
            "0x6f8d2fa18448afbfe4f82143c384484ad09a0271f3a3c0eb9f629e703f883125",
        ],
    }
    actual = contract.encode_abi("byte_array", kwargs=kwargs)
    assert (
        actual
        == "0xf166d6f8000000000000000000000000000000000000000000000000000000000000002000000000000000000000000000000000000000000000000000000000000000025595c210956e7721f9b692e702708556aa9aabb14ea163e96afa56ffbe9fa8096f8d2fa18448afbfe4f82143c384484ad09a0271f3a3c0eb9f629e703f883125"  # noqa: E501
    )


@pytest.mark.parametrize(
    "arguments",
    (
        [b"a"],
        ["0x61"],
        ["61"],
    ),
)
def test_contract_abi_encoding_strict_with_error(w3, arguments):
    contract = w3.eth.contract(abi=ABI_C)
    with pytest.raises(MismatchedABI):
        contract.encode_abi("a", arguments, data=None)


@pytest.mark.parametrize(
    "abi,arguments,data,expected",
    (
        pytest.param(ABI_A, [], None, "0x0dbe671f", id="ABI_A, no args, no data"),
        pytest.param(
            ABI_A, [], "0x12345678", "0x12345678", id="ABI_A, no args, some data"
        ),
        pytest.param(
            ABI_B,
            [0],
            None,
            "0xf0fdf8340000000000000000000000000000000000000000000000000000000000000000",  # noqa: E501
            id="ABI_B, valid int args, no data",
        ),
        pytest.param(
            ABI_B,
            [1],
            None,
            "0xf0fdf8340000000000000000000000000000000000000000000000000000000000000001",  # noqa: E501
            id="ABI_B, valid int args, no data",
        ),
        pytest.param(
            ABI_C,
            [1],
            None,
            "0xf0fdf8340000000000000000000000000000000000000000000000000000000000000001",  # noqa: E501
            id="ABI_C, valid int args, no data",
        ),
        pytest.param(
            ABI_C,
            [b"00000000000000000000000000000000"],
            None,
            "0x9f3fab583030303030303030303030303030303030303030303030303030303030303030",  # noqa: E501
            id="ABI_C, valid bytestring args, no data",
        ),
        pytest.param(
            ABI_C,
            [constants.HASH_ZERO],
            None,
            "0x9f3fab580000000000000000000000000000000000000000000000000000000000000000",  # noqa: E501
            id="ABI_C, valid hexstring args, no data",
        ),
    ),
)
def test_contract_abi_encoding_strict(w3, abi, arguments, data, expected):
    contract = w3.eth.contract(abi=abi)
    actual = contract.encode_abi("a", arguments, data=data)
    assert actual == expected
