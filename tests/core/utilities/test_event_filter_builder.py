import pytest

from eth_abi.exceptions import (
    ValueOutOfBounds,
)
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
            ("0x1", "0x2", "0x3", None, "0x4"),
        ),
        (
            (None, ["0x2", "0x2a"], "0x3", None, "0x4", None, [None], None),
            (None, ["0x2", "0x2a"], "0x3", None, "0x4"),
        ),
        ((None, None, [None]), tuple()),
    ),
)
def test_normalize_topic_list(topic_list, expected):
    assert normalize_topic_list(topic_list) == expected


@given(st.text())
def test_match_single_string_type_properties_data_arg(value):
    data_filter = DataArgumentFilter(arg_type="string")
    data_filter.match_single(value)


@given(st.text())
def test_match_single_string_type_properties_topic_arg(w3, value):
    topic_filter = TopicArgumentFilter(arg_type="string", abi_codec=w3.codec)
    topic_filter.match_single(value)


@given(st.lists(elements=st.text(), max_size=10, min_size=0))
def test_match_any_string_type_properties(w3, values):
    topic_filter = TopicArgumentFilter(arg_type="string", abi_codec=w3.codec)
    topic_filter.match_any(*values)
    assert len(topic_filter.match_values) == len(values)


@given(st.lists(elements=st.binary(), max_size=10, min_size=0))
def test_match_any_bytes_type_properties(w3, values):
    topic_filter = TopicArgumentFilter(arg_type="bytes", abi_codec=w3.codec)
    topic_filter.match_any(*values)
    assert len(topic_filter.match_values) == len(values)


@given(st.lists(elements=st.binary(), max_size=10, min_size=1))
def test_match_any_bytes_type_properties_strict(w3, values):
    topic_filter = TopicArgumentFilter(arg_type="bytes", abi_codec=w3.codec)
    topic_filter.match_any(*values)
    assert len(topic_filter.match_values) == len(values)


def test_match_hex_type_properties_strict(w3):
    topic_filter = TopicArgumentFilter(arg_type="bytes2", abi_codec=w3.codec)
    topic_filter.match_any("0x1233")
    assert len(topic_filter.match_values) == 1


@pytest.mark.parametrize("values", (b"123", b"1", "0x12", "0x", "0x121212"))
def test_match_any_bytes_type_properties_strict_errors(w3, values):
    topic_filter = TopicArgumentFilter(arg_type="bytes2", abi_codec=w3.codec)
    topic_filter.match_any(values)
    with pytest.raises(ValueOutOfBounds):
        topic_filter.match_values
