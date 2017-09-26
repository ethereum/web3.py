
import pytest

from eth_abi.abi import (
    process_type,
)

from web3.utils.abi import (
    BASE_RETURN_NORMALIZERS,
    abi_data_tree,
    collapse_type,
    map_abi_data,
)


@pytest.mark.parametrize(
    'original, expected',
    [
        ('address', 'address'),
        ('uint[2][]', 'uint256[2][]'),
        ('uint256[2][]', 'uint256[2][]'),
        ('function', 'bytes24'),
        ('bool', 'bool'),
        ('bytes32', 'bytes32'),
        ('bytes', 'bytes'),
        ('string', 'string'),
    ],
)
def test_collapse_type(original, expected):
    assert collapse_type(*process_type(original)) == expected


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
            '0x5B2063246F2191f18F2675ceDB8b28102e957458',
        ),
        (
            ["address[]"],
            [['0x5b2063246f2191f18f2675cedb8b28102e957458'] * 2],
            BASE_RETURN_NORMALIZERS,
            ['0x5B2063246F2191f18F2675ceDB8b28102e957458'] * 2,
        ),
    ],
)
def test_map_abi_data(types, data, funcs, expected):
    assert map_abi_data(funcs, types, data) == expected
