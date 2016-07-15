# -*- coding: utf-8 -*-
import pytest

from web3.utils.formatting import (
    pad_left,
    pad_right,
)


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
    assert pad_left(*value) == expected


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
    assert pad_right(*value) == expected
