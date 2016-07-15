import decimal

import pytest
from hypothesis import (
    given,
    strategies as st,
)

from web3.utils.currency import (
    units,
    to_wei,
    from_wei,
    MIN_WEI,
    MAX_WEI,
)


@given(
    amount_in_wei=st.integers(min_value=MIN_WEI, max_value=MAX_WEI),
    intermediate_unit=st.sampled_from(tuple(units.keys())),
)
def test_conversion_rount_trip(amount_in_wei, intermediate_unit):
    intermediate_amount = from_wei(amount_in_wei, intermediate_unit)
    result_amount = to_wei(intermediate_amount, intermediate_unit)
    assert result_amount == amount_in_wei


@pytest.mark.parametrize(
    "value,expected",
    [
        ([1000000000000000000, 'wei'], '1000000000000000000'),
        ([1000000000000000000, 'kwei'], '1000000000000000'),
        ([1000000000000000000, 'mwei'], '1000000000000'),
        ([1000000000000000000, 'gwei'], '1000000000'),
        ([1000000000000000000, 'szabo'], '1000000'),
        ([1000000000000000000, 'finney'], '1000'),
        ([1000000000000000000, 'ether'], '1'),
        ([1000000000000000000, 'kether'], '0.001'),
        ([1000000000000000000, 'grand'], '0.001'),
        ([1000000000000000000, 'mether'], '0.000001'),
        ([1000000000000000000, 'gether'], '0.000000001'),
        ([1000000000000000000, 'tether'], '0.000000000001'),
    ]
)
def test_from_wei(value, expected):
    assert from_wei(*value) == decimal.Decimal(expected)


@pytest.mark.parametrize(
    "value,expected",
    [
        ([1, 'wei'], '1'),
        ([1, 'kwei'], '1000'),
        ([1, 'Kwei'], '1000'),
        ([1, 'babbage'], '1000'),
        ([1, 'mwei'], '1000000'),
        ([1, 'Mwei'], '1000000'),
        ([1, 'lovelace'], '1000000'),
        ([1, 'gwei'], '1000000000'),
        ([1, 'Gwei'], '1000000000'),
        ([1, 'shannon'], '1000000000'),
        ([1, 'szabo'], '1000000000000'),
        ([1, 'finney'], '1000000000000000'),
        ([1, 'ether'], '1000000000000000000'),
        ([1, 'kether'], '1000000000000000000000'),
        ([1, 'grand'], '1000000000000000000000'),
        ([1, 'mether'], '1000000000000000000000000'),
        ([1, 'gether'], '1000000000000000000000000000'),
        ([1, 'tether'], '1000000000000000000000000000000')
    ]
)
def test_to_wei(value, expected):
    assert to_wei(*value) == decimal.Decimal(expected)


@pytest.mark.parametrize(
    'value,unit',
    (
        (1, 'wei1'),
        (1, 'not-a-unit'),
        (-1, 'ether'),
    )
)
def test_invalid_to_wei_values(value, unit):
    with pytest.raises(ValueError):
        to_wei(value, unit)

    with pytest.raises(ValueError):
        from_wei(value, unit)
