import json
import pytest
from eth_abi import encode_single
from binascii import unhexlify

ABI_A = json.loads('[{"constant":false,"inputs":[],"name":"a","outputs":[],"type":"function"}]')
ABI_B = json.loads('[{"constant":false,"inputs":[{"name":"","type":"uint256"}],"name":"a","outputs":[],"type":"function"}]')  # noqa: E501
ABI_C = json.loads('[{"constant":false,"inputs":[],"name":"a","outputs":[],"type":"function"},{"constant":false,"inputs":[{"name":"","type":"bytes32"}],"name":"a","outputs":[],"type":"function"},{"constant":false,"inputs":[{"name":"","type":"uint256"}],"name":"a","outputs":[],"type":"function"}]')  # noqa: E501
ABI_D = json.loads('[{ "constant": false, "inputs": [ { "name": "b", "type": "bytes32[]" } ], "name": "byte_array", "outputs": [], "payable": false, "type": "function" }]')  # noqa: E501
A = encode_single('bytes32', b'a')


@pytest.mark.parametrize(
    'abi,data,method,arguments,expected',
    (
        (
            ABI_A,
            '0x0dbe671f',
            'a',
            [],
            {},
        ),
        (
            ABI_B,
            '0xf0fdf8340000000000000000000000000000000000000000000000000000000000000001',
            'a',
            [1],
            {'': 1},
        ),
        (
            ABI_C,
            '0xf0fdf8340000000000000000000000000000000000000000000000000000000000000001',
            'a',
            [1],
            {'': 1},
        ),
        (
            ABI_C,
            '0x9f3fab586100000000000000000000000000000000000000000000000000000000000000',
            'a',
            [b'a'],
            {'': A},
        ),
        (
            ABI_C,
            '0x9f3fab586100000000000000000000000000000000000000000000000000000000000000',
            'a',
            ['0x61'],
            {'': A},
        ),
        (
            ABI_C,
            '0x9f3fab586100000000000000000000000000000000000000000000000000000000000000',
            'a',
            ['61'],
            {'': A},
        ),
        (
            ABI_C,
            '0xf0fdf834000000000000000000000000000000000000000000000000000000000000007f',
            'a',
            [127],
            {'': 127},
        ),
    ),
)
def test_contract_abi_decoding(web3, abi, data, method, arguments, expected):
    contract = web3.eth.contract(abi=abi)
    func, params = contract.decode_function_input(data)
    assert func.fn_name == method
    assert params == expected


@pytest.mark.parametrize(
    'abi,method,expected,data',
    (
        (
            ABI_D,
            'byte_array',
            {
                'b': (
                    unhexlify('5595c210956e7721f9b692e702708556aa9aabb14ea163e96afa56ffbe9fa809'),
                    unhexlify('6f8d2fa18448afbfe4f82143c384484ad09a0271f3a3c0eb9f629e703f883125'),
                ),
            },
            '0xf166d6f8000000000000000000000000000000000000000000000000000000000000002000000000000000000000000000000000000000000000000000000000000000025595c210956e7721f9b692e702708556aa9aabb14ea163e96afa56ffbe9fa8096f8d2fa18448afbfe4f82143c384484ad09a0271f3a3c0eb9f629e703f883125',  # noqa: E501
        ),
    ),
)
def test_contract_abi_encoding_kwargs(web3, abi, method, expected, data):
    contract = web3.eth.contract(abi=abi)
    func, params = contract.decode_function_input(data)
    assert func.fn_name == method
    assert params == expected
