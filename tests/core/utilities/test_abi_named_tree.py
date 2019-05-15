from web3._utils.abi import (
    check_if_arguments_can_be_encoded,
    named_data_tree,
)

from .test_abi import (
    TEST_FUNCTION_ABI,
)

abi = TEST_FUNCTION_ABI['inputs']
inputs = (
    (1, [2, 3, 4], [(5, 6), (7, 8), (9, 10)]),  # Value for s
    (11, 12),  # Value for t
    13,  # Value for a
)
expected = [
    {'s': {'a': 1, 'b': [2, 3, 4], 'c': [{'x': 5, 'y': 6}, {'x': 7, 'y': 8}, {'x': 9, 'y': 10}]}},
    {'t': {'x': 11, 'y': 12}},
    {'a': 13},
]


def test_named_data_tree():
    result = [named_data_tree(a, b) for a, b in zip(abi, inputs)]
    assert result == expected

    merged = {key: item[key] for item in result for key in item}
    assert check_if_arguments_can_be_encoded(TEST_FUNCTION_ABI, (), merged)
