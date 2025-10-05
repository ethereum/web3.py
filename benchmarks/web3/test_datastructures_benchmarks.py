import pytest
from pytest_codspeed import BenchmarkFixture

from web3.datastructures import (
    ReadableAttributeDict,
    MutableAttributeDict,
    AttributeDict,
    tupleize_lists_nested,
    NamedElementOnion,
)
from faster_web3.datastructures import (
    ReadableAttributeDict as FasterReadableAttributeDict,
    MutableAttributeDict as FasterMutableAttributeDict,
    AttributeDict as FasterAttributeDict,
    tupleize_lists_nested as faster_tupleize_lists_nested,
    NamedElementOnion as FasterNamedElementOnion,
)

# --- Shared parameter sets ---
init_dicts = [
    {},
    {"a": 1, "b": 2, "c": 3, "d": 4, "e": 5},
    {str(i): i for i in range(100)},
]
init_dict_ids = ["empty", "small", "large"]

getitem_cases = [
    ({"a": 1, "b": 2, "c": 3, "d": 4, "e": 5}, "a"),
    ({str(i): i for i in range(100)}, "50"),
]
getitem_ids = ["small", "large"]

recursive_vals = [
    {"a": {"b": [1, 2, {"c": 3}]}},
    [1, 2, {"a": [3, 4]}],
    set([1, 2, 3]),
]
recursive_ids = ["nested-dict", "list-in-dict", "set"]

hash_dicts = [
    {"a": 1, "b": 2, "c": 3, "d": 4, "e": 5},
    {"a": [1, 2], "b": {"c": 3}},
]
hash_ids = ["flat", "nested"]

tupleize_dicts = [
    {"a": [1, 2, 3], "b": {"c": [4, 5]}},
    {"x": (1, 2, [3, 4]), "y": {"z": [5, 6]}},
]
tupleize_ids = ["list-in-dict", "tuple-in-dict"]

# Use unique callables for onion_elements to avoid duplicate un-named instances
def make_callable(val):
    return lambda: val

onion_elements = [
    [],
    [make_callable(1), make_callable(2)],
    [make_callable(3), make_callable(4), make_callable(5)],
]
onion_ids = ["empty", "callables2", "callables3"]

# --- Helpers ---
def run_100(func, *args, **kwargs):
    for _ in range(100):
        func(*args, **kwargs)

def run_500(func, *args, **kwargs):
    for _ in range(500):
        func(*args, **kwargs)

# --- Benchmarks for ReadableAttributeDict ---

@pytest.mark.benchmark(group="ReadableAttributeDict-init")
@pytest.mark.parametrize("d", init_dicts, ids=init_dict_ids)
def test_readableattributedict_init(benchmark: BenchmarkFixture, d):
    benchmark(run_100, ReadableAttributeDict, d)

@pytest.mark.benchmark(group="ReadableAttributeDict-init")
@pytest.mark.parametrize("d", init_dicts, ids=init_dict_ids)
def test_faster_readableattributedict_init(benchmark: BenchmarkFixture, d):
    benchmark(run_100, FasterReadableAttributeDict, d)

@pytest.mark.benchmark(group="ReadableAttributeDict-getitem")
@pytest.mark.parametrize("d,key", getitem_cases, ids=getitem_ids)
def test_readableattributedict_getitem(benchmark: BenchmarkFixture, d, key):
    rad = ReadableAttributeDict(d)
    benchmark(run_100, lambda: rad[key])

@pytest.mark.benchmark(group="ReadableAttributeDict-getitem")
@pytest.mark.parametrize("d,key", getitem_cases, ids=getitem_ids)
def test_faster_readableattributedict_getitem(benchmark: BenchmarkFixture, d, key):
    rad = FasterReadableAttributeDict(d)
    benchmark(run_100, lambda: rad[key])

@pytest.mark.benchmark(group="ReadableAttributeDict-recursive")
@pytest.mark.parametrize("val", recursive_vals, ids=recursive_ids)
def test_readableattributedict_recursive(benchmark: BenchmarkFixture, val):
    benchmark(run_100, ReadableAttributeDict.recursive, val)

@pytest.mark.benchmark(group="ReadableAttributeDict-recursive")
@pytest.mark.parametrize("val", recursive_vals, ids=recursive_ids)
def test_faster_readableattributedict_recursive(benchmark: BenchmarkFixture, val):
    benchmark(run_100, FasterReadableAttributeDict.recursive, val)

# --- Benchmarks for MutableAttributeDict ---

@pytest.mark.benchmark(group="MutableAttributeDict-setitem")
def test_mutableattributedict_setitem(benchmark: BenchmarkFixture):
    def setitem():
        mad = MutableAttributeDict({})
        for i in range(20):
            mad[i] = i
    benchmark(run_100, setitem)

@pytest.mark.benchmark(group="MutableAttributeDict-setitem")
def test_faster_mutableattributedict_setitem(benchmark: BenchmarkFixture):
    def setitem():
        mad = FasterMutableAttributeDict({})
        for i in range(20):
            mad[i] = i
    benchmark(run_100, setitem)

@pytest.mark.benchmark(group="MutableAttributeDict-delitem")
def test_mutableattributedict_delitem(benchmark: BenchmarkFixture):
    def delitem():
        mad = MutableAttributeDict({i: i for i in range(20)})
        for i in range(20):
            del mad[i]
    benchmark(run_100, delitem)

@pytest.mark.benchmark(group="MutableAttributeDict-delitem")
def test_faster_mutableattributedict_delitem(benchmark: BenchmarkFixture):
    def delitem():
        mad = FasterMutableAttributeDict({i: i for i in range(20)})
        for i in range(20):
            del mad[i]
    benchmark(run_100, delitem)

# --- Benchmarks for AttributeDict ---

@pytest.mark.benchmark(group="AttributeDict-init")
@pytest.mark.parametrize("d", init_dicts, ids=init_dict_ids)
def test_attributedict_init(benchmark: BenchmarkFixture, d):
    benchmark(run_100, AttributeDict, d)

@pytest.mark.benchmark(group="AttributeDict-init")
@pytest.mark.parametrize("d", init_dicts, ids=init_dict_ids)
def test_faster_attributedict_init(benchmark: BenchmarkFixture, d):
    benchmark(run_100, FasterAttributeDict, d)

@pytest.mark.benchmark(group="AttributeDict-hash")
@pytest.mark.parametrize("d", hash_dicts, ids=hash_ids)
def test_attributedict_hash(benchmark: BenchmarkFixture, d):
    ad = AttributeDict(d)
    benchmark(run_100, hash, ad)

@pytest.mark.benchmark(group="AttributeDict-hash")
@pytest.mark.parametrize("d", hash_dicts, ids=hash_ids)
def test_faster_attributedict_hash(benchmark: BenchmarkFixture, d):
    ad = FasterAttributeDict(d)
    benchmark(run_100, hash, ad)

@pytest.mark.benchmark(group="AttributeDict-eq")
def test_attributedict_eq(benchmark: BenchmarkFixture):
    d1 = {"a": 1, "b": 2}
    d2 = {"b": 2, "a": 1}
    ad1 = AttributeDict(d1)
    ad2 = AttributeDict(d2)
    benchmark(run_100, lambda: ad1 == ad2)

@pytest.mark.benchmark(group="AttributeDict-eq")
def test_faster_attributedict_eq(benchmark: BenchmarkFixture):
    d1 = {"a": 1, "b": 2}
    d2 = {"b": 2, "a": 1}
    ad1 = FasterAttributeDict(d1)
    ad2 = FasterAttributeDict(d2)
    benchmark(run_100, lambda: ad1 == ad2)

# --- Benchmarks for tupleize_lists_nested ---

@pytest.mark.benchmark(group="tupleize_lists_nested")
@pytest.mark.parametrize("d", tupleize_dicts, ids=tupleize_ids)
def test_tupleize_lists_nested(benchmark: BenchmarkFixture, d):
    benchmark(run_100, tupleize_lists_nested, d)

@pytest.mark.benchmark(group="tupleize_lists_nested")
@pytest.mark.parametrize("d", tupleize_dicts, ids=tupleize_ids)
def test_faster_tupleize_lists_nested(benchmark: BenchmarkFixture, d):
    benchmark(run_100, faster_tupleize_lists_nested, d)

# --- Benchmarks for NamedElementOnion ---

@pytest.mark.benchmark(group="NamedElementOnion-init")
@pytest.mark.parametrize("elements", onion_elements, ids=onion_ids)
def test_namedelementonion_init(benchmark: BenchmarkFixture, elements):
    benchmark(run_100, NamedElementOnion, elements)

@pytest.mark.benchmark(group="NamedElementOnion-init")
@pytest.mark.parametrize("elements", onion_elements, ids=onion_ids)
def test_faster_namedelementonion_init(benchmark: BenchmarkFixture, elements):
    benchmark(run_100, FasterNamedElementOnion, elements)

@pytest.mark.benchmark(group="NamedElementOnion-add")
def test_namedelementonion_add(benchmark: BenchmarkFixture):
    onion = NamedElementOnion([make_callable(i) for i in range(10)])
    def add():
        for i in range(100, 200):
            onion.add(make_callable(i))
    benchmark(run_100, add)

@pytest.mark.benchmark(group="NamedElementOnion-add")
def test_faster_namedelementonion_add(benchmark: BenchmarkFixture):
    onion = FasterNamedElementOnion([make_callable(i) for i in range(10)])
    def add():
        for i in range(100, 200):
            onion.add(make_callable(i))
    benchmark(run_100, add)

@pytest.mark.benchmark(group="NamedElementOnion-inject")
def test_namedelementonion_inject(benchmark: BenchmarkFixture):
    onion = NamedElementOnion([make_callable(i) for i in range(10)])
    def inject():
        for i in range(100, 200):
            onion.inject(make_callable(i), layer=0)
    benchmark(run_100, inject)

@pytest.mark.benchmark(group="NamedElementOnion-inject")
def test_faster_namedelementonion_inject(benchmark: BenchmarkFixture):
    onion = FasterNamedElementOnion([make_callable(i) for i in range(10)])
    def inject():
        for i in range(100, 200):
            onion.inject(make_callable(i), layer=0)
    benchmark(run_100, inject)

@pytest.mark.benchmark(group="NamedElementOnion-replace")
def test_namedelementonion_replace(benchmark: BenchmarkFixture):
    middlewares = [make_callable(i) for i in range(10)]
    def replace():
        onion = NamedElementOnion(middlewares)
        for i in range(10):
            onion.replace(middlewares[i], make_callable(i + 10))
    benchmark(run_100, replace)

@pytest.mark.benchmark(group="NamedElementOnion-replace")
def test_faster_namedelementonion_replace(benchmark: BenchmarkFixture):
    middlewares = [make_callable(i) for i in range(10)]
    def replace():
        onion = FasterNamedElementOnion(middlewares)
        for i in range(10):
            onion.replace(middlewares[i], make_callable(i + 10))
    benchmark(run_100, replace)

@pytest.mark.benchmark(group="NamedElementOnion-remove")
def test_namedelementonion_remove(benchmark: BenchmarkFixture):
    middlewares = [make_callable(i) for i in range(10)]
    def remove():
        onion = NamedElementOnion(middlewares)
        for mw in middlewares:
            onion.remove(mw)
    benchmark(run_100, remove)

@pytest.mark.benchmark(group="NamedElementOnion-remove")
def test_faster_namedelementonion_remove(benchmark: BenchmarkFixture):
    middlewares = [make_callable(i) for i in range(10)]
    def remove():
        onion = FasterNamedElementOnion(middlewares)
        for mw in middlewares:
            onion.remove(mw)
    benchmark(run_100, remove)

@pytest.mark.benchmark(group="NamedElementOnion-contains")
def test_namedelementonion_contains(benchmark: BenchmarkFixture):
    middlewares = [make_callable(i) for i in range(10)]
    onion = NamedElementOnion(middlewares)
    middleware = middlewares[4]
    benchmark(run_100, lambda: middleware in onion)

@pytest.mark.benchmark(group="NamedElementOnion-contains")
def test_faster_namedelementonion_contains(benchmark: BenchmarkFixture):
    middlewares = [make_callable(i) for i in range(10)]
    onion = FasterNamedElementOnion(middlewares)
    middleware = middlewares[4]
    benchmark(run_100, lambda: middleware in onion)

@pytest.mark.benchmark(group="NamedElementOnion-getitem")
def test_namedelementonion_getitem(benchmark: BenchmarkFixture):
    middlewares = [make_callable(i) for i in range(10)]
    onion = NamedElementOnion(middlewares)
    middleware = middlewares[4]
    benchmark(run_100, lambda: onion[middleware])

@pytest.mark.benchmark(group="NamedElementOnion-getitem")
def test_faster_namedelementonion_getitem(benchmark: BenchmarkFixture):
    middlewares = [make_callable(i) for i in range(10)]
    onion = FasterNamedElementOnion(middlewares)
    middleware = middlewares[4]
    benchmark(run_100, lambda: onion[middleware])

@pytest.mark.benchmark(group="NamedElementOnion-iter")
def test_namedelementonion_iter(benchmark: BenchmarkFixture):
    onion = NamedElementOnion([make_callable(i) for i in range(10)])
    benchmark(run_100, list, onion)

@pytest.mark.benchmark(group="NamedElementOnion-iter")
def test_faster_namedelementonion_iter(benchmark: BenchmarkFixture):
    onion = FasterNamedElementOnion([make_callable(i) for i in range(10)])
    benchmark(run_100, list, onion)

@pytest.mark.benchmark(group="NamedElementOnion-as_tuple_of_middleware")
def test_namedelementonion_as_tuple_of_middleware(benchmark: BenchmarkFixture):
    onion = NamedElementOnion([make_callable(i) for i in range(10)])
    benchmark(run_100, onion.as_tuple_of_middleware)

@pytest.mark.benchmark(group="NamedElementOnion-as_tuple_of_middleware")
def test_faster_namedelementonion_as_tuple_of_middleware(benchmark: BenchmarkFixture):
    onion = FasterNamedElementOnion([make_callable(i) for i in range(10)])
    benchmark(run_100, onion.as_tuple_of_middleware)
