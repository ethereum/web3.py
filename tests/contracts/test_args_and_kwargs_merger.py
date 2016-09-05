import pytest

from web3.contract import (
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


@pytest.mark.parametrize(
    'args,kwargs,expected_args',
    (
        ([1, 4, 2, 3], {}, [1, 4, 2, 3]),
    ),
)
def test_merging_of_args_and_kwargs(args, kwargs, expected_args):
    actual_args = merge_args_and_kwargs(FUNCTION_ABI, args, kwargs)
    assert actual_args == expected_args
