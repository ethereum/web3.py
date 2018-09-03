import pytest

from web3.datastructures import (
    AttributeDict,
)


@pytest.mark.parametrize(
    "dict1,dict2,same_hash",
    [
        ({'b': 2, 'a': 1}, {'a': 1, 'b': 2}, True),
        ({'a': 1, 'b': 2}, {'a': 1, 'b': 0}, False),
    ],
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
    ],
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
    ],
)
def test_attributedict_inequality(dict1, dict2):
    assert AttributeDict(dict1) != dict2
    assert AttributeDict(dict1) != AttributeDict(dict2)
    assert dict1 != AttributeDict(dict2)


def test_attributedict_recursive_dict():
    w = AttributeDict.recursive({'x': {'y': {'z': 8}}})
    assert w.x.y.z == 8


@pytest.mark.parametrize('sequence', [list, tuple])
def test_attributedict_sequence_with_dict(sequence):
    data = sequence(['a', {'found': True}, 'c'])
    dict_in_sequence = AttributeDict.recursive(data)
    assert dict_in_sequence[1].found is True


def test_attributedict_dict_in_list_in_dict():
    data = {'instructions': [
        0,
        1,
        'neither shalt thou count, excepting that thou then proceedeth to three',
        {'if_naughty': 'snuff it'},
        'shalt thou not count',
        'right out',
    ]}
    attrdict = AttributeDict.recursive(data)
    assert attrdict.instructions[3].if_naughty == 'snuff it'


def test_attributedict_set_in_recursive_dict():
    data = {'mydict': {'myset': {'found'}}}
    attrdict = AttributeDict.recursive(data)
    assert 'found' in attrdict.mydict.myset
