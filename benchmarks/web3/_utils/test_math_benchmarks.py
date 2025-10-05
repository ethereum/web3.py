import pytest
from pytest_codspeed import BenchmarkFixture

import web3._utils.math
import faster_web3._utils.math

def run_100(func, *args, **kwargs):
    for _ in range(100):
        func(*args, **kwargs)

percentile_cases = [
    (list(range(10)), 50),         # 10 elements, median
    (list(range(100)), 90),        # 100 elements, 90th percentile
    (list(range(1000)), 99),       # 1,000 elements, 99th percentile
    (list(range(10000)), 10),      # 10,000 elements, 10th percentile
    (list(range(10000)), 50),      # 10,000 elements, median
    (list(range(10000)), 99),      # 10,000 elements, 99th percentile
    (list(range(100000)), 50),     # 100,000 elements, median
    (list(range(100000)), 99),     # 100,000 elements, 99th percentile
    (list(range(1000000)), 50),    # 1,000,000 elements, median
]
percentile_ids = [
    "10-median", "100-90th", "1k-99th", "10k-10th", "10k-median", "10k-99th", "100k-median", "100k-99th", "1M-median"
]

@pytest.mark.benchmark(group="percentile")
@pytest.mark.parametrize("values,percentile", percentile_cases, ids=percentile_ids)
def test_percentile(benchmark: BenchmarkFixture, values, percentile):
    benchmark(run_100, web3._utils.math.percentile, values, percentile)

@pytest.mark.benchmark(group="percentile")
@pytest.mark.parametrize("values,percentile", percentile_cases, ids=percentile_ids)
def test_faster_percentile(benchmark: BenchmarkFixture, values, percentile):
    benchmark(run_100, faster_web3._utils.math.percentile, values, percentile)
