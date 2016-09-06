import pytest

from web3.utils.abi import (
    merge_args_and_kwargs,
)


FUNCTION_ABI = {
    "constant": False
    ,"inputs": [
        {"name":"a", "type":"int256"},
        {"name":"b", "type":"int256"},
        {"name":"c", "type":"int256"},
        {"name":"d", "type":"int256"},
    ],
    "name": "testFn",
    "outputs": [],
    "type":"function",
}


NO_INPUTS_FUNCTION_ABI = {
    "constant": False
    ,"inputs": [],
    "name": "testFn",
    "outputs": [],
    "type":"function",
}


@pytest.mark.parametrize(
    'args,kwargs,expected_args',
    (
        ((1, 4, 2, 3), {}, (1, 4, 2, 3)),
        ((1, 4, 2), {'d': 3}, (1, 4, 2, 3)),
        ((1, 4), {'d': 3, 'c': 2}, (1, 4, 2, 3)),
        ((1,), {'d': 3, 'b': 4, 'c': 2}, (1, 4, 2, 3)),
        (tuple(), {'d': 3, 'b': 4, 'a': 1, 'c': 2}, (1, 4, 2, 3)),
    ),
)
def test_merging_of_args_and_kwargs(args, kwargs, expected_args):
    actual_args = merge_args_and_kwargs(FUNCTION_ABI, args, kwargs)
    assert actual_args == expected_args


def test_merging_of_args_and_kwargs_with_no_inputs():
    actual = merge_args_and_kwargs(NO_INPUTS_FUNCTION_ABI, tuple(), {})
    assert actual == tuple()
