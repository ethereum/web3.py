import decimal

import pytest

from web3.utils.currency import (
    to_wei,
    from_wei,
)

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
def test_toWei(value, expected):
    assert to_wei(*value) == decimal.Decimal(expected)


@pytest.mark.parametrize(
    "value,expected",
    [
    ([1, 'kwei'], [1, 'femtoether']),
    ([1, 'szabo'], [1, 'microether']),
    ([1, 'finney'], [1, 'milliether']),
    ([1, 'milli'], [1, 'milliether']),
    ([1, 'milli'], [1000, 'micro']),
    ]
)
def test_toWei2(value, expected):
    assert to_wei(*value) == to_wei(*expected)


def test_toWei3():
    with pytest.raises(Exception):
        currency.toWei(1, 'wei1')
