import pytest

from web3.utils.address import (
    parseUnits,
    formatUnits,
    formatEther,
    parseEther
)

@pytest.mark.parametrize(
    "value, decimals, expected",
    [
        ("1.0", 18, 1000000000000000000),
        ("10", 18, 10000000000000000000),
        ("0.11", 18, 110000000000000000),
        ("0.110000222200", 18, 110000222200000000),
        ("42.11", 6, 42110000),
        ("42", 6, 42000000),
        ("0.42004", 6, 420040)
    ]
)
def test_parseUnits(value, decimals, expected):
    assert parseUnits(value, decimals) == expected

@pytest.mark.parametrize(
    "value, decimals, expected",
    [
        (1000000000000000000, 18, "1"),
        (10000000000000000000, 18, "10"),
        (110000000000000000, 18, "0.11"),
        (110000222200000000, 18, "0.1100002222"),
        (42110000, 6, "42.11"),
        (42000000, 6, "42"),
        (420040, 6, "0.42004")
    ]
)
def test_formatUnits(value, decimals, expected):
    assert formatUnits(value, decimals) == expected

@pytest.mark.parametrize(
    "value, expected",
    [
        ("1.0", 1000000000000000000),
        ("10", 10000000000000000000),
        ("0.11", 110000000000000000)
    ]
)
def test_parseEther(value, expected):
    assert parseEther(value) == expected

@pytest.mark.parametrize(
    "value, expected",
    [
        (1000000000000000000, "1"),
        (10000000000000000000, "10"),
        (110000000000000000, "0.11"),
        (110000222200000000, "0.1100002222"),
    ]
)
def test_formatEther(value, expected):
    assert formatEther(value) == expected