import pytest

from web3.utils.types import (
    is_integer,
    is_boolean,
    is_string,
    is_array,
    is_object,
)


@pytest.mark.parametrize(
    "value,expected",
    [
    (3, True),
    (None, False),
    ("3", False),
    ("0x3", False),
    ]
)
def test_is_integer(value, expected):
    assert is_integer(value) == expected


@pytest.mark.parametrize(
    "value,expected",
    [
    ("3", True),
    (None, False),
    (3, False),
    ({}, False),
    ]
)
def test_is_string(value, expected):
    assert is_string(value) == expected


@pytest.mark.parametrize(
    "value,expected",
    [
    (lambda : None, False),
    (3, False),
    (None, False),
    ("3", False),
    ("0x3", False),
    ({}, True),
    ({"test": 3}, True)
    ]
)
def test_is_object(value, expected):
    assert is_object(value) == expected


@pytest.mark.parametrize(
    "value,expected",
    [
    (lambda : None, False),
    (3, False),
    (None, False),
    ("3", False),
    ("0x3", False),
    (True, True),
    (False, True)
    ]
)
def test_is_boolean(value, expected):
    assert is_boolean(value) == expected


@pytest.mark.parametrize(
    "value,expected",
    [
    (lambda : None, False),
    (3, False),
    (None, False),
    ("3", False),
    ("0x3", False),
    ([], True),
    ([3], True),
    ([3, 3], True),
    ([None], True)
    ]
)
def test_isArray(value, expected):
    assert is_array(value) == expected
