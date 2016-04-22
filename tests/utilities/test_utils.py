# -*- coding: utf-8 -*-
import pytest
import web3.utils.utils as utils


@pytest.mark.parametrize(
    "value,expected",
    [
    (["test", 3, ""], "test"),
    (["test", 5, ""], "test"),
    (["test", 8, ""], "test"),
    (["test", 8, "0"], "0000test"),
    ]
)
def test_padLeft(value, expected):
    assert utils.padLeft(*value) == expected


@pytest.mark.parametrize(
    "value,expected",
    [
    (["test", 3, ""], "test"),
    (["test", 5, ""], "test"),
    (["test", 8, ""], "test"),
    (["test", 8, "0"], "test0000"),
    ]
)
def test_padRight(value, expected):
    assert utils.padRight(*value) == expected


@pytest.mark.parametrize(
    "value,expected",
    [
    (3, True),
    (None, False),
    ("3", False),
    ("0x3", False),
    ]
)
def test_isInteger(value, expected):
    assert utils.isInteger(value) == expected


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
    assert utils.isString(value) == expected


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
    assert utils.isFunction(value) == expected


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
    assert utils.isObject(value) == expected


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
    assert utils.isBoolean(value) == expected


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
    assert utils.isArray(value) == expected


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