import pytest

from hypothesis import (
    given,
    strategies as st,
)

from web3.utils.events import (
    DataArgumentFilter,
    TopicArgumentFilter,
    normalize_topic_list,
)


@pytest.mark.parametrize(
    "topic_list,expected",
    (
        (
            ("0x1", "0x2", ["0x3"], None, "0x4", None, None, None),
            ("0x1", "0x2", "0x3", None, "0x4")
        ),
        (
            (None, ["0x2", "0x2a"], "0x3", None, "0x4", None, [None], None),
            (None, ["0x2", "0x2a"], "0x3", None, "0x4")
        ),
        (
            (None, None, [None]),
            tuple()
        )
    )
)
def test_normalize_topic_list(topic_list, expected):
    assert normalize_topic_list(topic_list) == expected


@given(st.text())
def test_match_single_string_type_properties_data_arg(value):
    ea = DataArgumentFilter(arg_type="string")
    ea.match_single(value)


@given(st.text())
def test_match_single_string_type_properties_topic_arg(value):
    ea = TopicArgumentFilter(arg_type="string")
    ea.match_single(value)


@given(st.lists(elements=st.text(), max_size=10, min_size=0))
def test_match_any_string_type_properties(values):
    ea = TopicArgumentFilter(arg_type="string")
    ea.match_any(*values)
    assert len(ea.match_values) == len(values)
