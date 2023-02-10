from binascii import (
    unhexlify,
)
import json
import pytest

ABI_A = json.loads(
    '[{"constant":false,"inputs":[],"name":"noargfunc","outputs":[],"type":"function"}]'  # noqa: E501
)
ABI_B = json.loads(
    '[{"constant":false,"inputs":[{"name":"uintarg","type":"uint256"}],"name":"uintfunc","outputs":[],"type":"function"}]'  # noqa: E501
)
ABI_C = json.loads(
    '[{"constant":false,"inputs":[],"name":"namesakefunc","outputs":[],"type":"function"},{"constant":false,"inputs":[{"name":"bytesarg","type":"bytes32"}],"name":"namesakefunc","outputs":[],"type":"function"},{"constant":false,"inputs":[{"name":"uintarg","type":"uint256"}],"name":"namesakefunc","outputs":[],"type":"function"}]'  # noqa: E501
)
ABI_D = json.loads(
    '[{ "constant": false, "inputs": [ { "name": "b", "type": "bytes32[]" } ], "name": "byte_array", "outputs": [], "payable": false, "type": "function" }]'  # noqa: E501
)
ABI_BYTES = json.loads(
    '[{"constant":false,"inputs":[{"name":"bytesarg","type":"bytes"}],"name":"bytesfunc","outputs":[],"type":"function"}]'  # noqa: E501
)
ABI_STRING = json.loads(
    '[{"constant":false,"inputs":[{"name":"stringarg","type":"string"}],"name":"stringfunc","outputs":[],"type":"function"}]'  # noqa: E501
)
ABI_ADDRESS = json.loads(
    '[{"constant":false,"inputs":[{"name":"addressarg","type":"address"}],"name":"addressfunc","outputs":[],"type":"function"}]'  # noqa: E501
)
ABI_TUPLE = json.loads(
    '[{"constant":false,"inputs":[{"components":[{"name":"owner","type":"address"},{"name":"number","type":"uint256"}],"name":"fromAccount","type":"tuple"},{"components":[{"name":"owner","type":"address"},{"name":"number","type":"uint256"}],"name":"liquidAccount","type":"tuple"},{"components":[{"name":"value","type":"uint256"}],"name":"minLiquidatorRatio","type":"tuple"},{"name":"minValueLiquidated","type":"uint256"},{"name":"owedPreferences","type":"uint256[]"},{"name":"heldPreferences","type":"uint256[]"}],"name":"liquidate","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"}]'  # noqa: E501
)
a32bytes = b"a".ljust(32, b"\x00")


@pytest.mark.parametrize(
    "abi,data,method,expected",
    (
        (
            ABI_A,
            "0xc4c1a40b",
            "noargfunc",
            {},
        ),
        (
            ABI_B,
            "0xcc6820de0000000000000000000000000000000000000000000000000000000000000001",  # noqa: E501
            "uintfunc",
            {"uintarg": 1},
        ),
        (
            ABI_C,
            "0x22d86fa3",
            "namesakefunc",
            {},
        ),
        (
            ABI_C,
            "0x40c05b2f0000000000000000000000000000000000000000000000000000000000000001",  # noqa: E501
            "namesakefunc",
            {"uintarg": 1},
        ),
        (
            ABI_C,
            "0xf931d77c6100000000000000000000000000000000000000000000000000000000000000",  # noqa: E501
            "namesakefunc",
            {"bytesarg": a32bytes},
        ),
        (
            ABI_BYTES,
            "0xb606a9f6000000000000000000000000000000000000000000000000000000000000002000000000000000000000000000000000000000000000000000000000000000016100000000000000000000000000000000000000000000000000000000000000",  # noqa: E501
            "bytesfunc",
            {"bytesarg": b"a"},
        ),
        (
            ABI_STRING,
            "0x33b4005f000000000000000000000000000000000000000000000000000000000000002000000000000000000000000000000000000000000000000000000000000000016100000000000000000000000000000000000000000000000000000000000000",  # noqa: E501
            "stringfunc",
            {"stringarg": "a"},
        ),
        (
            ABI_ADDRESS,
            "0x4767be6c000000000000000000000000ffffffffffffffffffffffffffffffffffffffff",  # noqa: E501
            "addressfunc",
            {"addressarg": "0xFFfFfFffFFfffFFfFFfFFFFFffFFFffffFfFFFfF"},
        ),
        (
            ABI_TUPLE,
            "0xc29a4b71000000000000000000000000bfae42a79ff045659dd0f84e65534f5c4c8100230000000000000000000000000000000000000000000000000000000000000000000000000000000000000000db3d3af153cb02f0bc44621db82289280e93500f94a7d1598c397f6b49ecd5ccbc2b464259b96870063493b0dc7409d0fd9fb9860000000000000000000000000000000000000000000000000429d069189e00000000000000000000000000000000000178287f49c4a1d6622fb2ab40000000000000000000000000000000000000000000000000000000000000000000000100000000000000000000000000000000000000000000000000000000000000018000000000000000000000000000000000000000000000000000000000000000030000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000100000000000000000000000000000000000000000000000000000000000000020000000000000000000000000000000000000000000000000000000000000003000000000000000000000000000000000000000000000000000000000000000200000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000001",  # noqa: E501
            "liquidate",
            {
                "fromAccount": {
                    "owner": "0xBfae42A79FF045659DD0F84e65534f5c4c810023",
                    "number": 0,
                },
                "liquidAccount": {
                    "owner": "0xdb3d3AF153cB02f0Bc44621Db82289280e93500F",
                    "number": 67238809929330522294664880975001390268660278453875034113630810005818923006342,  # noqa: E501
                },
                "minLiquidatorRatio": {"value": 300000000000000000},
                "minValueLiquidated": 500000000000000000000000000000000000000,
                "owedPreferences": [0, 1, 2],
                "heldPreferences": [2, 0, 1],
            },
        ),
    ),
)
def test_contract_abi_decoding(w3, abi, data, method, expected):
    contract = w3.eth.contract(abi=abi)
    func, params = contract.decode_function_input(data)
    assert func.fn_name == method
    assert params == expected

    reinvoke_func = contract.functions[func.fn_name](**params)
    rebuild_txn = reinvoke_func.build_transaction(
        {"gas": 0, "nonce": 0, "to": "\x00" * 20}
    )
    assert rebuild_txn["data"] == data


@pytest.mark.parametrize(
    "abi,method,expected,data",
    (
        (
            ABI_D,
            "byte_array",
            {
                "b": [
                    unhexlify(
                        "5595c210956e7721f9b692e702708556aa9aabb14ea163e96afa56ffbe9fa809"  # noqa: E501
                    ),
                    unhexlify(
                        "6f8d2fa18448afbfe4f82143c384484ad09a0271f3a3c0eb9f629e703f883125"  # noqa: E501
                    ),
                ],
            },
            "0xf166d6f8000000000000000000000000000000000000000000000000000000000000002000000000000000000000000000000000000000000000000000000000000000025595c210956e7721f9b692e702708556aa9aabb14ea163e96afa56ffbe9fa8096f8d2fa18448afbfe4f82143c384484ad09a0271f3a3c0eb9f629e703f883125",  # noqa: E501
        ),
    ),
)
def test_contract_abi_encoding_kwargs(w3, abi, method, expected, data):
    contract = w3.eth.contract(abi=abi)
    func, params = contract.decode_function_input(data)
    assert func.fn_name == method
    assert params == expected

    reinvoke_func = contract.functions[func.fn_name](**params)
    rebuild_txn = reinvoke_func.build_transaction(
        {"gas": 0, "nonce": 0, "to": "\x00" * 20}
    )
    assert rebuild_txn["data"] == data
