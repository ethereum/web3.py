import pytest

from web3.utils.abi import (
    filter_by_argument_name,
)

ABI = [
    {
        "constant": False,
        "inputs": [],
        "name": "func_1",
        "outputs": [],
        "type": "function",
    },
    {
        "constant": False,
        "inputs": [
            {"name": "a", "type": "uint256"},
        ],
        "name": "func_2",
        "outputs": [],
        "type": "function",
    },
    {
        "constant": False,
        "inputs": [
            {"name": "a", "type": "uint256"},
            {"name": "b", "type": "uint256"},
        ],
        "name": "func_3",
        "outputs": [],
        "type": "function",
    },
    {
        "constant": False,
        "inputs": [
            {"name": "a", "type": "uint256"},
            {"name": "b", "type": "uint256"},
            {"name": "c", "type": "uint256"},
        ],
        "name": "func_4",
        "outputs": [],
        "type": "function",
    },
]


@pytest.mark.parametrize(
    'argument_names,expected',
    (
        ([], ['func_1', 'func_2', 'func_3', 'func_4']),
        (['a'], ['func_2', 'func_3', 'func_4']),
        (['a', 'c'], ['func_4']),
        (['c'], ['func_4']),
        (['b'], ['func_3', 'func_4']),
    )
)
def test_filter_by_arguments_1(argument_names, expected):
    actual_matches = filter_by_argument_name(argument_names, ABI)
    function_names = [match['name'] for match in actual_matches]
    assert set(function_names) == set(expected)
