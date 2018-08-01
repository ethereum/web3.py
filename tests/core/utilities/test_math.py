import pytest

from hypothesis import (
    given,
    strategies as st,
)

from web3.exceptions import (
    InsufficientData,
)
from web3.utils.math import (
    percentile,
)

values = range(100)


@pytest.mark.parametrize(
    "p,expected",
    (
        (0, 0),
        (1, 0),
        (2, 1),
        (3, 2),
        (4, 3),
        (50, 49),
        (50.5, 49.5),
        (100, 99)
    )
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


@given(
    values=st.lists(elements=st.integers(), min_size=1, max_size=200),
    p=st.integers(max_value=100, min_value=0))
def test_fuzz_test_percentiles(values, p):
    if not values:
        with pytest.raises(ValueError):
            percentile(values, p)
    else:
        percentile(values, p)
