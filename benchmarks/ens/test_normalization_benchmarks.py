import pytest
from pytest_codspeed import BenchmarkFixture

import ens._normalization
import ens.exceptions

import faster_ens._normalization
import faster_ens.exceptions

from benchmarks.ens.params import NAMES

def run_1000(func, exc, *args, **kwargs):
    for _ in range(1000):
        try:
            func(*args, **kwargs)
        except exc:
            # Some cases are expected to raise (invalid names)
            pass

@pytest.mark.benchmark(group="normalize_name_ensip15")
@pytest.mark.parametrize("name", NAMES)
def test_normalize_name_ensip15(benchmark: BenchmarkFixture, name):
    benchmark(run_1000, ens.exceptions.InvalidName, ens._normalization.normalize_name_ensip15, name)

@pytest.mark.benchmark(group="faster_normalize_name_ensip15")
@pytest.mark.parametrize("name", NAMES)
def test_faster_normalize_name_ensip15(benchmark: BenchmarkFixture, name):
    benchmark(run_1000, faster_ens.exceptions.InvalidName, faster_ens._normalization.normalize_name_ensip15, name)
