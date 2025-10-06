import pytest
from pytest_codspeed import BenchmarkFixture

import ens.ens
import ens.exceptions
import faster_ens.ens
import faster_ens.exceptions

import requests
from unittest.mock import patch
from web3 import HTTPProvider as Web3HTTPProvider
from faster_web3 import HTTPProvider as FasterWeb3HTTPProvider

import json
from benchmarks.ens.params import NAMES
from benchmarks.ens.fake_rpc import fake_json_rpc_response, FAKE_ENS_REGISTRY

def run_100(func, exc, *args, **kwargs):
    for _ in range(100):
        try:
            func(*args, **kwargs)
        except exc:
            pass

class FakeResponse:
    def __init__(self, result):
        self.status_code = 200
        self._result = result
        self.headers = {}
        self.content = self.text = ""
    def json(self):
        return self._result

def fake_send(*args, **kwargs):
    request_data = json.loads(args[1].body)
    return FakeResponse(fake_json_rpc_response(request_data))

@pytest.mark.benchmark(group="ENS.address")
@pytest.mark.parametrize("name", NAMES)
def test_address(benchmark: BenchmarkFixture, name):
    with patch("requests.Session.send", side_effect=fake_send):
        provider = Web3HTTPProvider("http://localhost:8545")
        # Patch the ENS registry address to our fake one
        ns = ens.ens.ENS(provider=provider, addr=FAKE_ENS_REGISTRY)
        benchmark(run_100, ens.exceptions.ENSException, ns.address, name)

@pytest.mark.benchmark(group="ENS.address")
@pytest.mark.parametrize("name", NAMES)
def test_faster_address(benchmark: BenchmarkFixture, name):
    with patch("requests.Session.send", side_effect=fake_send):
        provider = FasterWeb3HTTPProvider("http://localhost:8545")
        ns = faster_ens.ens.ENS(provider=provider, addr=FAKE_ENS_REGISTRY)
        benchmark(run_100, faster_ens.exceptions.ENSException, ns.address, name)
