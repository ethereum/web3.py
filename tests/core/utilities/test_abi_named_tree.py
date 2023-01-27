from eth_abi.codec import (
    ABICodec,
)
from eth_abi.registry import (
    registry as default_registry,
)

from web3._utils.abi import (
    check_if_arguments_can_be_encoded,
    dict_to_namedtuple,
    foldable_namedtuple,
    named_tree,
)

from .test_abi import (
    TEST_FUNCTION_ABI,
)

abi = TEST_FUNCTION_ABI["inputs"]
inputs = (
    (1, [2, 3, 4], [(5, 6), (7, 8), (9, 10)]),  # Value for s
    (11, 12),  # Value for t
    13,  # Value for a
    [[(14, 15), (16, 17)], [(18, 19)]],  # Value for b
)


def test_named_arguments_decode():
    decoded = named_tree(abi, inputs)
    data = dict_to_namedtuple(decoded)
    assert data == inputs
    assert data.s.c[2].y == 10
    assert data.t.x == 11
    assert data.a == 13


def test_namedtuples_encodable():
    registry = default_registry.copy()
    codec = ABICodec(registry)
    kwargs = named_tree(abi, inputs)
    args = dict_to_namedtuple(kwargs)
    assert check_if_arguments_can_be_encoded(TEST_FUNCTION_ABI, codec, (), kwargs)
    assert check_if_arguments_can_be_encoded(TEST_FUNCTION_ABI, codec, args, {})


def test_foldable_namedtuple():
    item = foldable_namedtuple(["a", "b", "c"])([1, 2, 3])
    assert type(item)(item) == item == (1, 2, 3)
    assert item.c == 3
