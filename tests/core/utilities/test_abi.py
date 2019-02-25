import json
import pytest

from web3._utils.abi import (
    abi_data_tree,
    get_aligned_abi_inputs,
    get_tuple_type_str_parts,
    map_abi_data,
)
from web3._utils.normalizers import (
    BASE_RETURN_NORMALIZERS,
    abi_string_to_text,
    addresses_checksummed,
)


@pytest.mark.parametrize(
    'input, expected',
    (
        # Well-formed tuple type strings
        ('tuple', ('tuple', None)),
        ('tuple[]', ('tuple', '[]')),
        ('tuple[1]', ('tuple', '[1]')),
        ('tuple[10]', ('tuple', '[10]')),
        ('tuple[19]', ('tuple', '[19]')),
        ('tuple[195]', ('tuple', '[195]')),

        # Malformed tuple type strings
        ('tuple[][]', None),
        ('tuple[1][1]', None),
        ('tuple[0]', None),
        ('tuple[01]', None),
        ('tupleasfasdf', None),
        ('uint256', None),
        ('bool', None),
        ('', None),
        ('tupletuple', None),
    ),
)
def test_get_tuple_type_str_parts(input, expected):
    assert get_tuple_type_str_parts(input) == expected


TEST_FUNCTION_ABI_JSON = """
{
  "constant": false,
  "inputs": [
    {
      "components": [
        {
          "name": "a",
          "type": "uint256"
        },
        {
          "name": "b",
          "type": "uint256[]"
        },
        {
          "components": [
            {
              "name": "x",
              "type": "uint256"
            },
            {
              "name": "y",
              "type": "uint256"
            }
          ],
          "name": "c",
          "type": "tuple[]"
        }
      ],
      "name": "s",
      "type": "tuple"
    },
    {
      "components": [
        {
          "name": "x",
          "type": "uint256"
        },
        {
          "name": "y",
          "type": "uint256"
        }
      ],
      "name": "t",
      "type": "tuple"
    },
    {
      "name": "a",
      "type": "uint256"
    }
  ],
  "name": "f",
  "outputs": [],
  "payable": false,
  "stateMutability": "nonpayable",
  "type": "function"
}
"""
TEST_FUNCTION_ABI = json.loads(TEST_FUNCTION_ABI_JSON)


GET_ABI_INPUTS_OUTPUT = (
    (
        '(uint256,uint256[],(uint256,uint256)[])',  # Type of s
        '(uint256,uint256)',                        # Type of t
        'uint256',                                  # Type of a
    ),
    (
        (1, [2, 3, 4], [(5, 6), (7, 8), (9, 10)]),  # Value for s
        (11, 12),                                   # Value for t
        13,                                         # Value for a
    ),
)

GET_ABI_INPUTS_TESTS = (
    (
        TEST_FUNCTION_ABI,
        {
            's': {
                'a': 1,
                'b': [2, 3, 4],
                'c': [{'x': 5, 'y': 6}, {'x': 7, 'y': 8}, {'x': 9, 'y': 10}],
            },
            't': {'x': 11, 'y': 12},
            'a': 13,
        },
        GET_ABI_INPUTS_OUTPUT,
    ),
    (
        TEST_FUNCTION_ABI,
        {
            's': {'a': 1, 'b': [2, 3, 4], 'c': [(5, 6), (7, 8), {'x': 9, 'y': 10}]},
            't': {'x': 11, 'y': 12},
            'a': 13,
        },
        GET_ABI_INPUTS_OUTPUT,
    ),
    (
        TEST_FUNCTION_ABI,
        {
            's': {'a': 1, 'b': [2, 3, 4], 'c': [(5, 6), (7, 8), (9, 10)]},
            't': (11, 12),
            'a': 13,
        },
        GET_ABI_INPUTS_OUTPUT,
    ),
    (
        TEST_FUNCTION_ABI,
        {
            's': (1, [2, 3, 4], [(5, 6), (7, 8), (9, 10)]),
            't': (11, 12),
            'a': 13,
        },
        GET_ABI_INPUTS_OUTPUT,
    ),
    (
        TEST_FUNCTION_ABI,
        (
            (1, [2, 3, 4], [(5, 6), (7, 8), (9, 10)]),
            (11, 12),
            13,
        ),
        GET_ABI_INPUTS_OUTPUT,
    ),
    (
        {},
        (),
        ((), ()),
    ),
)


@pytest.mark.parametrize(
    'abi, args, expected',
    GET_ABI_INPUTS_TESTS,
)
def test_get_aligned_abi_inputs(abi, args, expected):
    assert get_aligned_abi_inputs(abi, args) == expected


GET_ABI_INPUTS_RAISING_TESTS = (
    (
        TEST_FUNCTION_ABI,
        {
            's': {'a': 1, 'b': [2, 3, 4], 'c': ['56', (7, 8), (9, 10)]},
            't': (11, 12),
            'a': 13,
        },
    ),
    (
        TEST_FUNCTION_ABI,
        {
            's': {'a': 1, 'b': [2, 3, 4], 'c': {(5, 6), (7, 8), (9, 10)}},
            't': (11, 12),
            'a': 13,
        },
    ),
)


@pytest.mark.parametrize(
    'abi, args',
    GET_ABI_INPUTS_RAISING_TESTS,
)
def test_get_aligned_abi_inputs_raises_type_error(abi, args):
    with pytest.raises(TypeError):
        get_aligned_abi_inputs(abi, args)


@pytest.mark.parametrize(
    'types, data, expected',
    [
        (
            ["bool[2]", "bytes"],
            [[True, False], b'\x00\xFF'],
            [("bool[2]", [("bool", True), ("bool", False)]), ("bytes", b'\x00\xFF')],
        ),
        (
            ["uint256[]"],
            [[0, 2**256 - 1]],
            [("uint256[]", [("uint256", 0), ("uint256", 2**256 - 1)])],
        ),
    ],
)
def test_abi_data_tree(types, data, expected):
    assert abi_data_tree(types, data) == expected


@pytest.mark.parametrize(
    'types, data, funcs, expected',
    [
        (
            ["bool[2]", "int256"],
            [[True, False], 9876543210],
            [
                lambda typ, dat: (typ, 'Tru-dat') if typ == 'bool' and dat else (typ, dat),
                lambda typ, dat: (typ, hex(dat)) if typ == 'int256' else (typ, dat),
            ],
            [['Tru-dat', False], '0x24cb016ea'],
        ),
        (
            ["address"],
            ['0x5b2063246f2191f18f2675cedb8b28102e957458'],
            BASE_RETURN_NORMALIZERS,
            ['0x5B2063246F2191f18F2675ceDB8b28102e957458'],
        ),
        (
            ["address[]"],
            [['0x5b2063246f2191f18f2675cedb8b28102e957458'] * 2],
            BASE_RETURN_NORMALIZERS,
            [['0x5B2063246F2191f18F2675ceDB8b28102e957458'] * 2],
        ),
        (
            ["(address,address)[]"],
            [[(
                '0x5b2063246f2191f18f2675cedb8b28102e957458',
                '0xebe0da78ecb266c7ea605dc889c64849f860383f',
            )] * 2],
            BASE_RETURN_NORMALIZERS,
            [[(
                '0x5B2063246F2191f18F2675ceDB8b28102e957458',
                '0xeBe0DA78ecb266C7EA605DC889c64849F860383F',
            )] * 2],
        ),
        (
            ['(string,address[])'],
            [(b'a string', [b'\xf2\xe2F\xbbv\xdf\x87l\xef\x8b8\xae\x84\x13\x0fOU\xde9['])],
            [addresses_checksummed, abi_string_to_text],
            [('a string', ['0xF2E246BB76DF876Cef8b38ae84130F4F55De395b'])],
        ),
    ],
)
def test_map_abi_data(types, data, funcs, expected):
    assert map_abi_data(funcs, types, data) == expected
