# -*- coding: utf-8 -*-
import pytest

from web3.utils.datastructures import (
    AttributeDict,
)

@pytest.mark.parametrize(
    "dict1,dict2,same_hash",
    [
    ({'b': 2, 'a': 1}, {'a': 1, 'b': 2}, True),
    ({'a': 1, 'b': 2}, {'a': 1, 'b': 0}, False),
    ]
)
def test_attributedict_hashable(dict1, dict2, same_hash):
    dicts = map(AttributeDict, (dict1, dict2))
    dicts = set(dicts)
    assert len(dicts) == (1 if same_hash else 2)

def test_attributedict_access():
    container = AttributeDict({'a': 1})
    assert container.a == 1

def test_attributedict_repr():
    dict1 = AttributeDict({'a': 1})
    dict2 = eval(repr(dict1))
    assert dict1 == dict2

def test_attributedict_setitem_invalid():
    container = AttributeDict({'a': 1})
    with pytest.raises(TypeError):
        container['a'] = 0
    assert container['a'] == 1

def test_attributedict_setattr_invalid():
    container = AttributeDict({'a': 1})
    with pytest.raises(TypeError):
        container.a = 0
    assert container.a == 1

def test_attributedict_delitem_invalid():
    container = AttributeDict({'a': 1})
    with pytest.raises(TypeError):
        del container['a']
    assert container['a'] == 1

@pytest.mark.parametrize(
    "dict1,dict2",
    [
    ({'b': 2, 'a': 1}, {'a': 1, 'b': 2}),
    ({}, {}),
    ]
)
def test_attributedict_equality(dict1, dict2):
    assert AttributeDict(dict1) == dict2
    assert AttributeDict(dict1) == AttributeDict(dict2)
    assert dict1 == AttributeDict(dict2)

@pytest.mark.parametrize(
    "dict1,dict2",
    [
    ({'a': 1, 'b': 2}, {'a': 1, 'b': 0}),
    ({'a': 1, 'b': 2}, {'a': 1}),
    ]
)
def test_attributedict_inequality(dict1, dict2):
    assert AttributeDict(dict1) != dict2
    assert AttributeDict(dict1) != AttributeDict(dict2)
    assert dict1 != AttributeDict(dict2)

