import pytest

from hypothesis import (
    given,
    strategies as st,
)

from web3._utils.events import (
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
    data_filter = DataArgumentFilter(arg_type="string")
    data_filter.match_single(value)


@given(st.text())
def test_match_single_string_type_properties_topic_arg(value):
    topic_filter = TopicArgumentFilter(arg_type="string")
    topic_filter.match_single(value)


@given(st.lists(elements=st.text(), max_size=10, min_size=0))
def test_match_any_string_type_properties(values):
    topic_filter = TopicArgumentFilter(arg_type="string")
    topic_filter.match_any(*values)
    assert len(topic_filter.match_values) == len(values)
