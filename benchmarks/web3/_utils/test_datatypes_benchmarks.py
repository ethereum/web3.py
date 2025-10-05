import pytest
from pytest_codspeed import BenchmarkFixture

import web3._utils.datatypes
import web3.exceptions
import faster_web3._utils.datatypes
import faster_web3.exceptions

Web3AttributeError = (web3.exceptions.Web3AttributeError, faster_web3.exceptions.Web3AttributeError)

def run_100(func, *args, **kwargs):
    for _ in range(100):
        try:
            func(*args, **kwargs)
        except Web3AttributeError:
            pass  # ignore expected attribute errors for invalid cases

verify_attr_cases = [
    ("MyClass", "foo", ["foo", "bar", "baz"]),                # found at start
    ("OtherClass", "baz", ["foo", "bar", "baz"]),             # found at end
    ("TestClass", "notfound", ["foo", "bar", "baz"]),         # not found
    ("BigClass", "x99", [f"x{i}" for i in range(100)]),       # large namespace, found
    ("BigClass", "notfound", [f"x{i}" for i in range(100)]),  # large namespace, not found
    ("EmptyClass", "foo", []),                                # empty namespace
]
verify_attr_ids = [
    "found-start", "found-end", "notfound", "large-found", "large-notfound", "empty"
]

@pytest.mark.benchmark(group="verify_attr")
@pytest.mark.parametrize("class_name,key,namespace", verify_attr_cases, ids=verify_attr_ids)
def test_verify_attr(benchmark: BenchmarkFixture, class_name, key, namespace):
    benchmark(run_100, web3._utils.datatypes.verify_attr, class_name, key, namespace)

@pytest.mark.benchmark(group="verify_attr")
@pytest.mark.parametrize("class_name,key,namespace", verify_attr_cases, ids=verify_attr_ids)
def test_faster_verify_attr(benchmark: BenchmarkFixture, class_name, key, namespace):
    benchmark(run_100, faster_web3._utils.datatypes.verify_attr, class_name, key, namespace)

# More varied parameterization for PropertyCheckingFactory
def make_class_with_factory(name, bases, namespace, normalizers=None):
    metaclass = web3._utils.datatypes.PropertyCheckingFactory
    return metaclass(name, bases, namespace, normalizers=normalizers)

def faster_make_class_with_factory(name, bases, namespace, normalizers=None):
    metaclass = faster_web3._utils.datatypes.PropertyCheckingFactory
    return metaclass(name, bases, namespace, normalizers=normalizers)

property_factory_cases = [
    # Valid: property exists in base
    ("ValidClass", (type,), {"__doc__": "A valid class."}, None),
    # Valid: property with normalizer
    ("NormalizedClass", (type,), {"foo": "bar"}, {"foo": lambda v: v.upper()}),
    # Invalid: property not in base
    ("InvalidClass", (type,), {"notfound": 123}, None),
    # Multiple properties, all valid
    ("MultiPropClass", (type,), {"foo": 1, "bar": 2, "baz": 3}, None),
    # Large namespace, valid
    ("BigClass", (type,), {f"x{i}": i for i in range(100)}, None),
    # Large namespace, invalid property
    ("BigClassInvalid", (type,), {**{f"x{i}": i for i in range(100)}, "notfound": 1}, None),
    # Inheritance: property in base
    ("ChildClass", (type("Base", (), {"foo": 1}),), {"foo": 2}, None),
    # Normalizers on multiple fields
    ("MultiNormClass", (type,), {"foo": "bar", "baz": "qux"}, {"foo": str.upper, "baz": str.lower}),
]
property_factory_ids = [
    "valid", "normalized", "invalid", "multi-prop", "big-valid", "big-invalid", "inheritance", "multi-normalizer"
]

@pytest.mark.benchmark(group="PropertyCheckingFactory")
@pytest.mark.parametrize("name,bases,namespace,normalizers", property_factory_cases, ids=property_factory_ids)
def test_PropertyCheckingFactory(benchmark: BenchmarkFixture, name, bases, namespace, normalizers):
    benchmark(run_100, make_class_with_factory, name, bases, namespace, normalizers)

@pytest.mark.benchmark(group="PropertyCheckingFactory")
@pytest.mark.parametrize("name,bases,namespace,normalizers", property_factory_cases, ids=property_factory_ids)
def test_faster_PropertyCheckingFactory(benchmark: BenchmarkFixture, name, bases, namespace, normalizers):
    benchmark(run_100, faster_make_class_with_factory, name, bases, namespace, normalizers)
