import pytest

from web3.utils.abi import (
    filter_by_name,
)

ABI_FUNC_1 = {
    "constant": False,
    "inputs": [],
    "name": "func_1",
    "outputs": [],
    "type": "function",
}
ABI_CONSTRUCTOR = {
    "constant": False,
    "inputs": [],
    "type": "constructor",
}
ABI_FALLBACK = {
    "constant": False,
    "type": "fallback",
}
ABI_FUNC_2_SIG_A = {
    "constant": False,
    "inputs": [
        {"name": "a", "type": "uint256"},
    ],
    "name": "func_2",
    "outputs": [],
    "type": "function",
}
ABI_FUNC_2_SIG_B = {
    "constant": False,
    "inputs": [
        {"name": "a", "type": "uint256"},
        {"name": "b", "type": "uint256"},
    ],
    "name": "func_2",
    "outputs": [],
    "type": "function",
}
ABI_FUNC_3 = {
    "constant": False,
    "inputs": [],
    "name": "func_3",
    "outputs": [],
    "type": "function",
}

ABI = [
    ABI_CONSTRUCTOR,
    ABI_FALLBACK,
    ABI_FUNC_1,
    ABI_FUNC_2_SIG_A,
    ABI_FUNC_2_SIG_B,
    ABI_FUNC_3,
]


@pytest.mark.parametrize(
    'name,expected',
    (
        ('func_1', [ABI_FUNC_1]),
        ('func_2', [ABI_FUNC_2_SIG_A, ABI_FUNC_2_SIG_B]),
        ('func_3', [ABI_FUNC_3]),
        ('does_not_exist', []),
    )
)
def test_filter_by_arguments(name, expected):
    actual_matches = filter_by_name(name, ABI)
    assert actual_matches == expected
