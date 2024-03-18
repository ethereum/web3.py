import pytest

from hypothesis import (
    given,
    strategies as st,
)

from web3._utils.math import (
    percentile,
)
from web3.exceptions import (
    InsufficientData,
    Web3ValueError,
)

values = range(100)


@pytest.mark.parametrize(
    "p,expected",
    ((0, 0), (1, 0), (2, 1), (3, 2), (4, 3), (50, 49), (50.5, 49.5), (100, 99)),
)
def test_percentiles_out_of_one_hundred(p, expected):
    assert percentile(values, p) == expected


def test_percentiles_with_no_values():
    with pytest.raises(InsufficientData):
        percentile([], 1)


def test_percentiles_with_out_of_bounds_fractions():
    assert 1 == percentile([1, 2, 3, 4], percentile=10)
    assert 1 == percentile([1, 2, 3, 4], percentile=15)
    assert 1 == percentile([1, 2, 3, 4], percentile=20)
    assert 1 == percentile([1, 2, 3, 4], percentile=25)
    assert 1 < percentile([1, 2, 3, 4], percentile=30)


@pytest.mark.parametrize(
    "out_of_bounds_percentile", [-2, -1, -0.1, -0.0001, 100.0001, 100.1, 101, 102, 200]
)
def test_percentile_out_of_bounds_values(out_of_bounds_percentile):
    with pytest.raises(Web3ValueError):
        percentile(values, percentile=out_of_bounds_percentile)


@given(
    values=st.lists(elements=st.integers(), min_size=1, max_size=200),
    p=st.integers(max_value=100, min_value=0),
)
def test_fuzz_test_percentiles(values, p):
    if not values:
        with pytest.raises(Web3ValueError):
            percentile(values, p)
    else:
        percentile(values, p)
