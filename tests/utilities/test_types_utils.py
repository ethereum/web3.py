import pytest

import web3.utils.types import (
    is_integer,
    is_number,
    is_string,
    is_bytes,
    is_text,
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
def test_isString(value, expected):
    assert isString(value) == expected


@pytest.mark.parametrize(
    "value,expected",
    [
    (lambda : None, True),
    (3, False),
    (None, False),
    ("3", False),
    ("0x3", False),
    ]
)
def test_isFunction(value, expected):
    assert isFunction(value) == expected


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
def test_isObject(value, expected):
    assert isObject(value) == expected


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
def test_isBoolean(value, expected):
    assert isBoolean(value) == expected


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
    assert isArray(value) == expected


@pytest.mark.parametrize(
    "value,expected",
    [
    (lambda : None, False),
    (3, False),
    (None, False),
    ("3", True),
    ("0x3", False),
    ("{}", True),
    ('{"test":3}', True),
    ("{3}", False)
    ]
)
def test_isJson(value, expected):
    assert utils.isJson(value) == expected
