import pytest
import random
import re

from web3.datastructures import (
    AttributeDict,
    tupleize_lists_nested,
)


def generate_random_value(depth=0, max_depth=3, key_type=None):
    if depth > max_depth:
        return None

    choice = random.choice(["str", "int", "bool", "list", "tuple", "dict"])

    if choice == "str":
        return "".join(random.choices("abcdefghijklmnopqrstuvwxyz", k=5))
    elif choice == "int":
        return random.randint(0, 100)
    elif choice == "bool":
        return random.choice([True, False])
    elif choice == "list":
        return [
            generate_random_value(depth + 1, key_type=key_type)
            for _ in range(random.randint(1, 5))
        ]
    elif choice == "tuple":
        return tuple(
            generate_random_value(depth + 1, key_type=key_type)
            for _ in range(random.randint(1, 5))
        )
    elif choice == "dict":
        return generate_random_dict(depth + 1, key_type=key_type)


def generate_random_dict(depth=0, max_depth=3, max_keys=5, key_type=None):
    if not key_type:
        key_type = random.choice(["str", "int", "float"])

    if depth > max_depth:
        return {}

    result = {}
    for _ in range(random.randint(1, max_keys)):
        if key_type == "str":
            key = "".join(random.choices("abcdefghijklmnopqrstuvwxyz", k=5))
        elif key_type == "int":
            key = random.randint(0, 100)
        elif key_type == "float":
            key = round(random.uniform(0, 100), 2)

        value = generate_random_value(depth, max_depth, key_type)
        result[key] = value

    return AttributeDict.recursive(result)


def test_attribute_dict_raises_when_mutated():
    test_attr_dict = AttributeDict(
        {"address": "0x4CB06C43fcdABeA22541fcF1F856A6a296448B6c"}
    )
    with pytest.raises(TypeError):
        # should raise when trying to edit an attribute with dict syntax
        test_attr_dict["address"] = "0x6C8f2A135f6ed072DE4503Bd7C4999a1a17F824B"

    with pytest.raises(TypeError):
        # should raise when trying to edit an attribute with dot syntax
        test_attr_dict.address = "0x6C8f2A135f6ed072DE4503Bd7C4999a1a17F824B"

    with pytest.raises(TypeError):
        # should raise when trying to add an attribute with dict syntax
        test_attr_dict["cats"] = "0x6C8f2A135f6ed072DE4503Bd7C4999a1a17F824B"

    with pytest.raises(TypeError):
        # should raise when trying to add an attribute with dot syntax
        test_attr_dict.cats = "0x6C8f2A135f6ed072DE4503Bd7C4999a1a17F824B"

    with pytest.raises(TypeError):
        # should raise when trying to delete an attribute with dict syntax
        del test_attr_dict["address"]

    with pytest.raises(TypeError):
        # should raise when trying to delete an attribute with dot syntax
        del test_attr_dict.address


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
def test_tupleization_and_hashing_passing_defined(input, expected):
    assert tupleize_lists_nested(input) == expected
    assert hash(AttributeDict(input)) == hash(expected)
    assert AttributeDict(input) == expected


def test_tupleization_and_hashing_passing_random():
    for _ in range(1000):
        random_dict = generate_random_dict()
        tupleized_random_dict = tupleize_lists_nested(random_dict)
        assert hash(random_dict) == hash(tupleized_random_dict)
        assert random_dict == tupleized_random_dict


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
