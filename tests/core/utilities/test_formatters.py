
import pytest

from web3.utils.formatters import (
    apply_formatters_to_dict,
    map_collection,
    recursive_map,
)


def square_int(x):
    if isinstance(x, int):
        return x * x
    else:
        return x


@pytest.mark.parametrize('non_collection', [1, 'abc', u'def', True, None])
def test_map_collection_on_non_collection(non_collection):
    assert map_collection(lambda x: x + 2, non_collection) == non_collection


@pytest.mark.parametrize('coll', [set, list, tuple])
def test_collection_apply(coll):
    vals = coll([1, 2])
    assert map_collection(lambda x: x + 2, vals) == coll([3, 4])


def test_collection_apply_to_mapping():
    vals = {'a': 1, 'b': 2}
    assert map_collection(lambda x: x + 2, vals) == {'a': 3, 'b': 4}


def test_recursive_collection_apply():
    assert recursive_map(square_int, [[3]]) == [[9]]


def test_recursive_collection_cycle():
    data = [3]
    data.append(data)
    with pytest.raises(ValueError):
        recursive_map(square_int, data)


def test_format_dict_error():
    with pytest.raises(ValueError) as exc_info:
        apply_formatters_to_dict(
            {'myfield': int},
            {'myfield': 'a'},
        )
    assert 'myfield' in str(exc_info.value)
