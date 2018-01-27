import pytest

from web3.utils.abi import (
    merge_args_and_kwargs,
)

FUNCTION_ABI = {
    "constant": False,
    "inputs": [
        {"name": "a", "type": "int256"},
        {"name": "b", "type": "int256"},
        {"name": "c", "type": "int256"},
        {"name": "d", "type": "int256"},
    ],
    "name": "testFn",
    "outputs": [],
    "type": "function",
}


def test_error_when_invalid_args_kwargs_combo_provided():
    with pytest.raises(TypeError):
        merge_args_and_kwargs(GENERATED_FUNCTION_ABI, (1, 2,), {'a': 1, 'b': 2})


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


NO_INPUTS_FUNCTION_ABI = {
    "constant": False,
    "inputs": [],
    "name": "testFn",
    "outputs": [],
    "type": "function",
}


def test_merging_of_args_and_kwargs_with_no_inputs():
    actual = merge_args_and_kwargs(NO_INPUTS_FUNCTION_ABI, tuple(), {})
    assert actual == tuple()


GENERATED_FUNCTION_ABI = {
    "constant": False,
    "inputs": [
        {"name": "", "type": "int256"},
        {"name": "", "type": "int256"},
    ],
    "name": "testFn",
    "outputs": [],
    "type": "function",
}


def test_kwargs_is_disallowed_when_merging_with_unnamed_inputs():
    with pytest.raises(TypeError):
        merge_args_and_kwargs(GENERATED_FUNCTION_ABI, tuple(), {'x': 1, 'y': 2})


def test_args_works_when_merging_with_unnamed_inputs():
    actual = merge_args_and_kwargs(GENERATED_FUNCTION_ABI, (1, 2), {})
    assert actual == (1, 2)


DUPLICATE_NAMES_FUNCTION_ABI = {
    "constant": False,
    "inputs": [
        {"name": "b", "type": "int256"},
        {"name": "b", "type": "int256"},
        {"name": "a", "type": "int256"},
    ],
    "name": "testFn",
    "outputs": [],
    "type": "function",
}


def test_args_allowed_when_duplicate_named_inputs():
    actual = merge_args_and_kwargs(DUPLICATE_NAMES_FUNCTION_ABI, (1, 2, 3), {})
    assert actual == (1, 2, 3)


def test_kwargs_not_allowed_for_duplicate_input_names():
    with pytest.raises(TypeError):
        merge_args_and_kwargs(DUPLICATE_NAMES_FUNCTION_ABI, (1,), {'a': 2, 'b': 3})


def test_kwargs_allowed_if_no_intersections_with_duplicate_input_names():
    with pytest.raises(TypeError):
        merge_args_and_kwargs(DUPLICATE_NAMES_FUNCTION_ABI, (1,), {'a': 2, 'b': 3})
