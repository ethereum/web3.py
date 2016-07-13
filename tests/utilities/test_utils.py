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
