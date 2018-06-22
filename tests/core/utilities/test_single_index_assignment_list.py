import pytest

from hypothesis import (
    given,
    strategies as s,
)

from web3.exceptions import (
    ItemResetException,
)
from web3.utils.datastructures import (
    SingleIndexAssignmentList,
)
from web3.utils.hypothesis import (
    hexstr_strategy,
)

elements = s.one_of(
    s.integers(),
    s.booleans(),
    s.floats(),
    s.tuples(),
    s.lists(),
    s.sets(),
    s.dictionaries(s.integers(), s.integers()),
    s.characters(),
    s.text(),
    s.binary(),
    hexstr_strategy()
)


@s.composite
def values_indexes_resets(draw, elements=elements):
    values = draw(s.lists(elements, min_size=1))
    indexes = draw(
        s.lists(
            max_size=len(values),
            min_size=len(values),
            elements=s.integers(min_value=0, max_value=len(values) - 1), unique=True))

    bools = draw(
        s.lists(
            max_size=len(values),
            min_size=len(values),
            elements=s.booleans()))
    return (values, indexes, bools)


@s.composite
def filled_list_not_prohibited(draw):
    values = draw(s.lists(elements, min_size=1))
    not_prohibited_list = SingleIndexAssignmentList(values)
    return not_prohibited_list


@s.composite
def filled_list_setting_prohibited(draw):
    values = draw(s.lists(elements, min_size=1))
    prohibited_list = SingleIndexAssignmentList(values)
    prohibited_list.set_prohibited = [True for i in range(len(prohibited_list))]
    return prohibited_list


@given(values_indexes_resets())
def test_SingleIndexAssignmentList(values_indexes_resets):
    single_set = SingleIndexAssignmentList()
    values, indexes, bools = values_indexes_resets
    expected = [value for value, index in sorted(zip(values, indexes), key=lambda x: x[1])]
    for value, index, reset in zip(values, indexes, bools):
        single_set[index] = value
        assert len(single_set) == len(single_set.set_prohibited)
        if reset:
            with pytest.raises(ItemResetException):
                single_set[index] = value
    assert single_set == expected


@given(filled_list_not_prohibited())
def test_filled_list_not_prohibited(not_prohibited):
    for i in range(len(not_prohibited)):
        not_prohibited[i] = "0x0"


@given(filled_list_setting_prohibited())
def test_pass_filled_list_to_constructor(prohibited_sets_list):
    with pytest.raises(ItemResetException):
        prohibited_sets_list[0] = "!!!!"
    constructed_from_prohibited_set = SingleIndexAssignmentList(prohibited_sets_list)
    for i in range(len(constructed_from_prohibited_set)):
        constructed_from_prohibited_set[i] = "0x0"
    copied_from_prohibited_set = SingleIndexAssignmentList(prohibited_sets_list)
    for i in range(len(copied_from_prohibited_set)):
        copied_from_prohibited_set[i] = "0x0"
