import pytest
import re

from web3.datastructures import (
    AttributeDict,
    tupleize_lists_nested,
)


@pytest.mark.parametrize(
    "input,expected",
    (
        (
            {
                "mylst": [1, 2, 3, [4, 5, [6, 7], 8], 9, 10],
                "nested": {"mylst": [1, 2, 3, [1], [2, 3]]},
            },
            AttributeDict(
                {
                    "mylst": (1, 2, 3, (4, 5, (6, 7), 8), 9, 10),
                    "nested": AttributeDict({"mylst": (1, 2, 3, (1,), (2, 3))}),
                }
            ),
        ),
        (
            {
                "mylst": [1, 2, 3, [5, 4, [6, 7], 8], 9, 10],
                "nested": {"mylst": [1, 2, 3, [1], [2, 3]]},
            },
            AttributeDict(
                {
                    "nested": AttributeDict({"mylst": (1, 2, 3, (1,), (2, 3))}),
                    "mylst": (1, 2, 3, (5, 4, (6, 7), 8), 9, 10),
                }
            ),
        ),
        (
            AttributeDict(
                {
                    "mylst": [1, 2, 3, [4, 5, [6, 7], 8], 9, 10],
                    "nested": AttributeDict({"mylst": [1, 2, 3, [1], [2, 3]]}),
                }
            ),
            AttributeDict(
                {
                    "mylst": (1, 2, 3, (4, 5, (6, 7), 8), 9, 10),
                    "nested": AttributeDict({"mylst": (1, 2, 3, (1,), (2, 3))}),
                }
            ),
        ),
    ),
)
def test_tupleization_and_hashing(input, expected):
    assert tupleize_lists_nested(input) == expected
    assert hash(AttributeDict(input)) == hash(expected)


@pytest.mark.parametrize(
    "input, error",
    (
        (
            AttributeDict(
                {
                    "myset": set({1, 2, 3}),
                    "nested": AttributeDict({"mylst": (1, 2, 3, (1,), (2, 3))}),
                }
            ),
            {
                "expected_exception": TypeError,
                "match": "Found unhashable type 'set': {(1, 2, 3)}",
            },
        ),
        (
            AttributeDict(
                {
                    "mybytearray": bytearray((1, 2, 3)),
                    "nested": AttributeDict({"mylst": [1, 2, 3, [1], [2, 3]]}),
                }
            ),
            {
                "expected_exception": TypeError,
                "match": re.escape(
                    "Found unhashable type 'bytearray': bytearray(b'\\x01\\x02\\x03')"
                ),
            },
        ),
    ),
)
def test_tupleization_and_hashing_error(input, error):
    with pytest.raises(**error):
        assert hash(input)


@pytest.mark.parametrize(
    "input, error",
    (
        (
            AttributeDict(
                {
                    "mylst": (1, 2, 3, (4, 5, (6, 7), 8), 9, 10),
                    "nested": AttributeDict({"mylst": (1, 2, 3, (1,), (2, 3))}),
                }
            ),
            None,
        ),
        (
            AttributeDict(
                {
                    "mylst": [1, 2, 3, [4, 5, [6, 7], 8], 9, 10],
                    "nested": AttributeDict({"mylst": [1, 2, 3, [1], [2, 3]]}),
                }
            ),
            {"expected_exception": TypeError, "match": "unhashable type: 'list'"},
        ),
    ),
)
def test_AttributeDict_hashing_backwards_compatibility(input, error):
    if error:
        with pytest.raises(**error):
            assert hash(tuple(sorted(input.items()))) == hash(input)
    else:
        assert hash(tuple(sorted(input.items()))) == hash(input)
