from decimal import Decimal
import pytest
from web3 import Web3


def test_to_wei_with_decimals_int_default_18():
    assert Web3.to_wei_with_decimals(1, 18) == 10 ** 18


def test_to_wei_with_decimals_str_and_decimal_inputs():
    assert Web3.to_wei_with_decimals("1.5", 6) == 1_500_000
    assert Web3.to_wei_with_decimals(Decimal("0.000001"), 6) == 1


def test_to_wei_with_non_18_decimals():
    assert Web3.to_wei_with_decimals("2.345678", 8) == 234_567_800


def test_to_wei_fractional_wei_raises():
    # 0.0000001 * 10**6 == 0.1 -> fractional wei -> error
    with pytest.raises(ValueError):
        Web3.to_wei_with_decimals("0.0000001", 6)


def test_from_wei_with_decimals_returns_decimal():
    assert Web3.from_wei_with_decimals(1_500_000, 6) == Decimal("1.5")
    assert Web3.from_wei_with_decimals("234567800", 8) == Decimal("2.345678")


def test_invalid_decimals_raise():
    with pytest.raises(ValueError):
        Web3.to_wei_with_decimals(1, -1)
    with pytest.raises(ValueError):
        Web3.from_wei_with_decimals(1, -5)
    with pytest.raises(ValueError):
        Web3.to_wei_with_decimals(1, 2.5)  # non-int decimals
    with pytest.raises(ValueError):
        Web3.from_wei_with_decimals(1, "6")  # non-int decimals


def test_invalid_value_types_raise():
    with pytest.raises(ValueError):
        Web3.to_wei_with_decimals("not-a-number", 18)
    with pytest.raises(ValueError):
        Web3.from_wei_with_decimals("not-a-number", 6)
