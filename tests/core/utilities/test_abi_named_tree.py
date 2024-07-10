import pytest

from eth_abi.codec import (
    ABICodec,
)
from eth_abi.registry import (
    registry as default_registry,
)

from web3._utils.abi import (
    abi_decoded_namedtuple_factory,
    named_tree,
    recursive_dict_to_namedtuple,
)
from web3.exceptions import (
    MismatchedABI,
)
from web3.utils import (
    check_if_arguments_can_be_encoded,
)

from .test_abi import (
    FUNCTION_ABI,
)

full_abi_inputs = FUNCTION_ABI["inputs"]
full_values = (
    (1, [2, 3, 4], [(5, 6), (7, 8), (9, 10)]),  # Value for s
    (11, 12),  # Value for t
    13,  # Value for a
    [[(14, 15), (16, 17)], [(18, 19)]],  # Value for b
)


def test_named_arguments_decode():
    decoded = named_tree(full_abi_inputs, full_values)
    data = recursive_dict_to_namedtuple(decoded)
    assert data == full_values
    assert data.s.c[2].y == 10
    assert data.t.x == 11
    assert data.a == 13


short_abi_inputs_with_disallowed_names = [
    {
        "components": [
            {"name": "from", "type": "uint256"},
            {"name": "to", "type": "uint256[]"},
            {
                "components": [
                    {"name": "_x", "type": "uint256"},
                    {"name": "_y", "type": "uint256"},
                ],
                "name": "c",
                "type": "tuple[]",
            },
        ],
        "name": "s",
        "type": "tuple",
    },
]

short_values = ((1, [2, 3, 4], [(5, 6), (7, 8), (9, 10)]),)


def test_named_arguments_decode_rename():
    decoded = named_tree(short_abi_inputs_with_disallowed_names, short_values)
    data = recursive_dict_to_namedtuple(decoded)
    assert data == short_values
    assert data._fields == ("s",)

    # python keyword "from" renamed to "_0"
    assert data.s._fields == ("_0", "to", "c")

    # field names starting with "_" - "_x" and "_y" - renamed to "_0" and "_1"
    assert data.s.c[0]._fields == ("_0", "_1")
    assert data.s.c[2]._1 == 10
    assert data.s.to[1] == 3


@pytest.mark.parametrize(
    "values",
    (
        ((1, [2, 3, 4], [(5,), (7, 8), (9, 10)]),),
        ((1, [2, 3, 4], [(5, 6, 11), (7, 8), (9, 10)]),),
        ((1, [(5, 6), (7, 8), (9, 10)]),),
    ),
)
def test_named_arguments_decode_with_misshapen_inputs(values):
    with pytest.raises(MismatchedABI):
        named_tree(short_abi_inputs_with_disallowed_names, values)


def test_namedtuples_encodable():
    registry = default_registry.copy()
    codec = ABICodec(registry)
    kwargs = named_tree(full_abi_inputs, full_values)
    args = recursive_dict_to_namedtuple(kwargs)
    assert check_if_arguments_can_be_encoded(
        FUNCTION_ABI, *(), **kwargs, abi_codec=codec
    )
    assert check_if_arguments_can_be_encoded(FUNCTION_ABI, *args, **{}, abi_codec=codec)


def test_ABIDecodedNamedTuple():
    item = abi_decoded_namedtuple_factory(["a", "b", "c"])([1, 2, 3])
    assert type(item)(item) == item == (1, 2, 3)
    assert item.c == 3

    expected_asdict = {"a": 1, "b": 2, "c": 3}
    assert item._asdict() == expected_asdict
