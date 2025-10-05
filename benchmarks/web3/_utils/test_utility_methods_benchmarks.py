import pytest
from pytest_codspeed import BenchmarkFixture

import web3._utils.utility_methods
import faster_web3._utils.utility_methods

def run_500(func, *args, **kwargs):
    for _ in range(500):
        func(*args, **kwargs)

dict_cases = [
    (["a", "b"], {"a": 1, "b": 2, "c": 3}),  # all in
    (["x"], {"x": 10}),                      # one in
    (["z"], {"a": 1, "b": 2}),               # none in
    ([], {"a": 1}),                          # empty list
    (["a", "b", "c"], {}),                   # empty dict
    (["a", 1], {"a": 1, 1: "b"}),            # mixed types
    (["a", "b", "c"], {"a": 1, "b": 2}),     # partial overlap
    (["a", "b", "c"], {"x": 1, "y": 2}),     # no overlap
    (["a"], {"a": None}),                    # value is None
]
dict_ids = [
    "all-in", "one-in", "none-in", "empty-list", "empty-dict",
    "mixed-types", "partial-overlap", "no-overlap", "value-none"
]

@pytest.mark.benchmark(group="all_in_dict")
@pytest.mark.parametrize("values,d", dict_cases, ids=dict_ids)
def test_all_in_dict(benchmark: BenchmarkFixture, values, d):
    benchmark(run_500, web3._utils.utility_methods.all_in_dict, values, d)

@pytest.mark.benchmark(group="all_in_dict")
@pytest.mark.parametrize("values,d", dict_cases, ids=dict_ids)
def test_faster_all_in_dict(benchmark: BenchmarkFixture, values, d):
    benchmark(run_500, faster_web3._utils.utility_methods.all_in_dict, values, d)

@pytest.mark.benchmark(group="any_in_dict")
@pytest.mark.parametrize("values,d", dict_cases, ids=dict_ids)
def test_any_in_dict(benchmark: BenchmarkFixture, values, d):
    benchmark(run_500, web3._utils.utility_methods.any_in_dict, values, d)

@pytest.mark.benchmark(group="any_in_dict")
@pytest.mark.parametrize("values,d", dict_cases, ids=dict_ids)
def test_faster_any_in_dict(benchmark: BenchmarkFixture, values, d):
    benchmark(run_500, faster_web3._utils.utility_methods.any_in_dict, values, d)

@pytest.mark.benchmark(group="none_in_dict")
@pytest.mark.parametrize("values,d", dict_cases, ids=dict_ids)
def test_none_in_dict(benchmark: BenchmarkFixture, values, d):
    benchmark(run_500, web3._utils.utility_methods.none_in_dict, values, d)

@pytest.mark.benchmark(group="none_in_dict")
@pytest.mark.parametrize("values,d", dict_cases, ids=dict_ids)
def test_faster_none_in_dict(benchmark: BenchmarkFixture, values, d):
    benchmark(run_500, faster_web3._utils.utility_methods.none_in_dict, values, d)

# Expanded parameterization for set-based function
set_cases = [
    ({"a", "b"}, {"a", "b", "c"}),           # subset
    ({"x"}, {"y", "z"}),                     # not subset
    (set(), {"a", "b"}),                     # empty set1
    ({"a", "b"}, set()),                     # empty set2
    (set(), set()),                          # both empty
    ({"a", 1}, {"a", 1, 2}),                 # mixed types, subset
    ({"a", "b", "c"}, {"a", "b"}),           # superset
    ({"a"}, {"a"}),                          # identical
    ({"a", "b"}, {"b", "c"}),                # partial overlap
]
set_ids = [
    "subset", "not-subset", "empty-set1", "empty-set2", "both-empty",
    "mixed-types", "superset", "identical", "partial-overlap"
]

@pytest.mark.benchmark(group="either_set_is_a_subset")
@pytest.mark.parametrize("set1,set2", set_cases, ids=set_ids)
def test_either_set_is_a_subset(benchmark: BenchmarkFixture, set1, set2):
    benchmark(run_500, web3._utils.utility_methods.either_set_is_a_subset, set1, set2)

@pytest.mark.benchmark(group="either_set_is_a_subset")
@pytest.mark.parametrize("set1,set2", set_cases, ids=set_ids)
def test_faster_either_set_is_a_subset(benchmark: BenchmarkFixture, set1, set2):
    benchmark(run_500, faster_web3._utils.utility_methods.either_set_is_a_subset, set1, set2)
