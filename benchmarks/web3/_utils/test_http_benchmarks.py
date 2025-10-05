import pytest
from pytest_codspeed import BenchmarkFixture

import web3._utils.http
import faster_web3._utils.http

def run_1000(func, *args, **kwargs):
    for _ in range(1000):
        func(*args, **kwargs)

MODULE = "some_module"
CLASS_NAME = "SomeClass"

@pytest.mark.benchmark(group="construct_user_agent")
def test_web3_construct_user_agent(benchmark: BenchmarkFixture):
    benchmark(run_1000, web3._utils.http.construct_user_agent, MODULE, CLASS_NAME)

@pytest.mark.benchmark(group="construct_user_agent")
def test_faster_web3_construct_user_agent(benchmark: BenchmarkFixture):
    benchmark(run_1000, faster_web3._utils.http.construct_user_agent, MODULE, CLASS_NAME)
