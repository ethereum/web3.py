from web3.datastructures import AttributeDict, tupleize_lists_nested

DICT_1 = {
    "mylst": [1, 2, 3, [4, 5, [6, 7], 8], 9, 10],
    "nested": {"mylst": [1, 2, 3, [1], [2, 3]]},
}
EXPECTED_1 = AttributeDict(
    {
        "mylst": (1, 2, 3, (4, 5, (6, 7), 8), 9, 10),
        "nested": AttributeDict({"mylst": (1, 2, 3, (1,), (2, 3))}),
    }
)

DICT_2 = AttributeDict(
    {
        "mylst": [1, 2, 3, [4, 5, [6, 7], 8], 9, 10],
        "nested": AttributeDict({"mylst": [1, 2, 3, [1], [2, 3]]}),
    }
)
EXPECTED_2 = AttributeDict(
    {
        "mylst": (1, 2, 3, (4, 5, (6, 7), 8), 9, 10),
        "nested": AttributeDict({"mylst": (1, 2, 3, (1,), (2, 3))}),
    }
)


def test_dict_tupleization():
    assert tupleize_lists_nested(DICT_1) == EXPECTED_1
    assert tupleize_lists_nested(DICT_2) == EXPECTED_2


def test_hashing_success():
    try:
        hash(DICT_2)
    except TypeError:
        assert False
