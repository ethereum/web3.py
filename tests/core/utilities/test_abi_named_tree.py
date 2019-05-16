from web3._utils.abi import (
    check_if_arguments_can_be_encoded,
    foldable_namedtuple,
    named_arguments_tuple,
)

from .test_abi import TEST_FUNCTION_ABI

abi = TEST_FUNCTION_ABI['inputs']

# s = (a=1, b=[2, 3, 4], c=[(x=5, y=6), (x=7, y=8), (x=9, y=10)])
# t = (x=11, y=12)
# a = 13
inputs = (
    (1, [2, 3, 4], [(5, 6), (7, 8), (9, 10)]),
    (11, 12),
    13,
)


def test_named_arguments_decode():
    data = named_arguments_tuple(abi, inputs)
    s, t, a = data
    assert data == inputs
    assert data.s.c[2].y == 10
    assert data.t.x == 11
    assert data.a == 13


def test_namedtuples_encodable():
    args = named_arguments_tuple(abi, inputs)
    assert check_if_arguments_can_be_encoded(TEST_FUNCTION_ABI, args, {})


def test_foldable_namedtuple():
    item = foldable_namedtuple('a b c')([1, 2, 3])
    assert type(item)(item) == item == (1, 2, 3)
    assert item.c == 3
