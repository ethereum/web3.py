import json
import pytest

from web3.exceptions import (
    ValidationError,
)

ABI_A = json.loads('[{"constant":false,"inputs":[],"name":"a","outputs":[],"type":"function"}]')
ABI_B = json.loads('[{"constant":false,"inputs":[{"name":"","type":"uint256"}],"name":"a","outputs":[],"type":"function"}]')  # noqa: E501
ABI_C = json.loads('[{"constant":false,"inputs":[],"name":"a","outputs":[],"type":"function"},{"constant":false,"inputs":[{"name":"","type":"bytes32"}],"name":"a","outputs":[],"type":"function"},{"constant":false,"inputs":[{"name":"","type":"uint256"}],"name":"a","outputs":[],"type":"function"}]')  # noqa: E501
ABI_D = json.loads('[{ "constant": false, "inputs": [ { "name": "b", "type": "bytes32[]" } ], "name": "byte_array", "outputs": [], "payable": false, "type": "function" }]')  # noqa: E501


@pytest.mark.parametrize(
    'abi,method,arguments,data,expected',
    (
        (ABI_A, 'a', [], None, '0x0dbe671f'),
        (ABI_A, 'a', [], '0x12345678', '0x12345678'),
        (
            ABI_B,
            'a',
            [0],
            None,
            '0xf0fdf8340000000000000000000000000000000000000000000000000000000000000000',
        ),
        (
            ABI_B,
            'a',
            [1],
            None,
            '0xf0fdf8340000000000000000000000000000000000000000000000000000000000000001',
        ),
        (
            ABI_C,
            'a',
            [1],
            None,
            '0xf0fdf8340000000000000000000000000000000000000000000000000000000000000001',
        ),
        (
            ABI_C,
            'a',
            [b'a'],
            None,
            '0x9f3fab586100000000000000000000000000000000000000000000000000000000000000',
        ),
        (
            ABI_C,
            'a',
            ['0x61'],
            None,
            '0x9f3fab586100000000000000000000000000000000000000000000000000000000000000',
        ),
    ),
)
def test_contract_abi_encoding(web3, abi, method, arguments, data, expected):
    contract = web3.eth.contract(abi=abi)
    actual = contract.encodeABI(method, arguments, data=data)
    assert actual == expected


def test_contract_abi_encoding_warning(web3):
    contract = web3.eth.contract(abi=ABI_C)

    with pytest.warns(
        DeprecationWarning,
        match='in v6 it will be invalid to pass a hex string without the "0x" prefix'
    ):

        actual = contract.encodeABI('a', ['61'], data=None)
        assert actual == '0x9f3fab586100000000000000000000000000000000000000000000000000000000000000'  # noqa: E501


@pytest.mark.parametrize(
    'abi,method,kwargs,expected',
    (
        (
            ABI_D,
            'byte_array',
            {
                'b': [
                    '0x5595c210956e7721f9b692e702708556aa9aabb14ea163e96afa56ffbe9fa809',
                    '0x6f8d2fa18448afbfe4f82143c384484ad09a0271f3a3c0eb9f629e703f883125',
                ],
            },
            '0xf166d6f8000000000000000000000000000000000000000000000000000000000000002000000000000000000000000000000000000000000000000000000000000000025595c210956e7721f9b692e702708556aa9aabb14ea163e96afa56ffbe9fa8096f8d2fa18448afbfe4f82143c384484ad09a0271f3a3c0eb9f629e703f883125',  # noqa: E501
        ),
    ),
)
def test_contract_abi_encoding_kwargs(web3, abi, method, kwargs, expected):
    contract = web3.eth.contract(abi=abi)
    actual = contract.encodeABI(method, kwargs=kwargs)
    assert actual == expected


@pytest.mark.parametrize(
    'abi,method,arguments,data',
    (
        (
            ABI_C,
            'a',
            [b'a'],
            None,
        ),
        (
            ABI_C,
            'a',
            ['0x61'],
            None,
        ),
        (
            ABI_C,
            'a',
            ['61'],
            None,
        ),
    ),
)
def test_contract_abi_encoding_strict_with_error(web3_strict_types, abi, method, arguments, data):
    contract = web3_strict_types.eth.contract(abi=abi)
    with pytest.raises(ValidationError):
        contract.encodeABI(method, arguments, data=data)


@pytest.mark.parametrize(
    'abi,method,arguments,data,expected',
    (
        (ABI_A, 'a', [], None, '0x0dbe671f'),
        (ABI_A, 'a', [], '0x12345678', '0x12345678'),
        (
            ABI_B,
            'a',
            [0],
            None,
            '0xf0fdf8340000000000000000000000000000000000000000000000000000000000000000',
        ),
        (
            ABI_B,
            'a',
            [1],
            None,
            '0xf0fdf8340000000000000000000000000000000000000000000000000000000000000001',
        ),
        (
            ABI_C,
            'a',
            [1],
            None,
            '0xf0fdf8340000000000000000000000000000000000000000000000000000000000000001',
        ),
        (
            ABI_C,
            'a',
            [b'00000000000000000000000000000000'],
            None,
            '0x9f3fab583030303030303030303030303030303030303030303030303030303030303030',
        ),
        (
            ABI_C,
            'a',
            ['0x0000000000000000000000000000000000000000000000000000000000000000'],
            None,
            '0x9f3fab580000000000000000000000000000000000000000000000000000000000000000',
        ),
    ),
)
def test_contract_abi_encoding_strict(web3_strict_types, abi, method, arguments, data, expected):
    contract = web3_strict_types.eth.contract(abi=abi)
    actual = contract.encodeABI(method, arguments, data=data)
    assert actual == expected
