import pytest
from pytest_codspeed import BenchmarkFixture

import ens.base_ens
import ens.exceptions
import faster_ens.base_ens
import faster_ens.exceptions
from benchmarks.ens.params import LABELS, NAMES, NAMES_VALIDITY, ADDRESSES, PARENT_NAMES

def run_10(func, *args, **kwargs):
    for _ in range(10):
        func(*args, **kwargs)

def run_10_exc(exc, func, *args, **kwargs):
    for _ in range(10):
        try:
            func(*args, **kwargs)
        except exc:
            pass

@pytest.mark.benchmark(group="BaseENS.labelhash")
@pytest.mark.parametrize("label", LABELS)
def test_labelhash(benchmark: BenchmarkFixture, label):
    benchmark(run_10_exc, ens.exceptions.InvalidName, ens.base_ens.BaseENS.labelhash, label)

@pytest.mark.benchmark(group="BaseENS.labelhash")
@pytest.mark.parametrize("label", LABELS)
def test_faster_labelhash(benchmark: BenchmarkFixture, label):
    benchmark(run_10_exc, faster_ens.exceptions.InvalidName, faster_ens.base_ens.BaseENS.labelhash, label)

@pytest.mark.benchmark(group="BaseENS.namehash")
@pytest.mark.parametrize("name", NAMES)
def test_namehash(benchmark: BenchmarkFixture, name):
    benchmark(run_10, ens.base_ens.BaseENS.namehash, name)

@pytest.mark.benchmark(group="BaseENS.namehash")
@pytest.mark.parametrize("name", NAMES)
def test_faster_namehash(benchmark: BenchmarkFixture, name):
    benchmark(run_10, faster_ens.base_ens.BaseENS.namehash, name)

@pytest.mark.benchmark(group="BaseENS.nameprep")
@pytest.mark.parametrize("name", NAMES)
def test_nameprep(benchmark: BenchmarkFixture, name):
    benchmark(run_10, ens.base_ens.BaseENS.nameprep, name)

@pytest.mark.benchmark(group="BaseENS.nameprep")
@pytest.mark.parametrize("name", NAMES)
def test_faster_nameprep(benchmark: BenchmarkFixture, name):
    benchmark(run_10, faster_ens.base_ens.BaseENS.nameprep, name)

@pytest.mark.benchmark(group="BaseENS.is_valid_name")
@pytest.mark.parametrize("name", NAMES_VALIDITY)
def test_is_valid_name(benchmark: BenchmarkFixture, name):
    benchmark(run_10, ens.base_ens.BaseENS.is_valid_name, name)

@pytest.mark.benchmark(group="BaseENS.is_valid_name")
@pytest.mark.parametrize("name", NAMES_VALIDITY)
def test_faster_is_valid_name(benchmark: BenchmarkFixture, name):
    benchmark(run_10, faster_ens.base_ens.BaseENS.is_valid_name, name)

@pytest.mark.benchmark(group="BaseENS.reverse_domain")
@pytest.mark.parametrize("address", ADDRESSES)
def test_reverse_domain(benchmark: BenchmarkFixture, address):
    benchmark(run_10, ens.base_ens.BaseENS.reverse_domain, address)

@pytest.mark.benchmark(group="BaseENS.reverse_domain")
@pytest.mark.parametrize("address", ADDRESSES)
def test_faster_reverse_domain(benchmark: BenchmarkFixture, address):
    benchmark(run_10, faster_ens.base_ens.BaseENS.reverse_domain, address)

@pytest.mark.benchmark(group="BaseENS.parent")
@pytest.mark.parametrize("name", PARENT_NAMES)
def test_parent(benchmark: BenchmarkFixture, name):
    benchmark(run_10, ens.base_ens.BaseENS.parent, name)

@pytest.mark.benchmark(group="BaseENS.parent")
@pytest.mark.parametrize("name", PARENT_NAMES)
def test_faster_parent(benchmark: BenchmarkFixture, name):
    benchmark(run_10, faster_ens.base_ens.BaseENS.parent, name)
