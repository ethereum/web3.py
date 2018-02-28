import random

from eth_utils import (
    to_dict,
)
from hypothesis import (
    given,
    strategies as st,
)

from web3.utils.caching import (
    generate_cache_key,
)


@to_dict
def shuffle_dict(_dict):
    keys = list(_dict.keys())
    random.shuffle(keys)
    for key in keys:
        yield key, _dict[key]


def extend_fn(children):
    lists_st = st.lists(children)
    dicts_st = st.dictionaries(st.text(), children)
    return lists_st | dicts_st


all_st = st.recursive(
    st.none() | st.integers() | st.booleans() | st.floats() | st.text() | st.binary(),
    extend_fn,
)


def recursive_shuffle_dict(v):
    if isinstance(v, dict):
        return shuffle_dict(v)
    elif isinstance(v, (list, tuple)):
        return type(v)((recursive_shuffle_dict(_v) for _v in v))
    else:
        return v


@given(value=all_st)
def test_key_generation_is_deterministic(value):
    left = recursive_shuffle_dict(value)
    right = recursive_shuffle_dict(value)
    left_key = generate_cache_key(left)
    right_key = generate_cache_key(right)
    assert left_key == right_key
