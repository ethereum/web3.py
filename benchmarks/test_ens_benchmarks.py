import pytest
from pytest_codspeed import BenchmarkFixture
from unittest.mock import patch, MagicMock

import web3._utils.ens as web3_ens
import faster_web3._utils.ens as faster_ens
from faster_ens import ENS

def run_100(func, *args, **kwargs):
    for _ in range(100):
        func(*args, **kwargs)

ens_name_cases = [
    ("vitalik.eth",),
    ("notanens",),
    ("",),
    (123,),
    ("0x1234567890abcdef1234567890abcdef12345678",),
    ("0xdeadbeef",),
]
ens_name_ids = [
    "valid",
    "invalid",
    "empty",
    "int",
    "hex-address",
    "hex-string"
]

class MockResponse:
    def __init__(self, json_data=None, status_code=200):
        self._json_data = json_data or {"jsonrpc": "2.0", "id": 1, "result": "0x0000000000000000000000000000000000000000"}
        self.status_code = status_code
    def json(self):
        return self._json_data

@pytest.mark.benchmark(group="is_ens_name")
@pytest.mark.parametrize("value", ens_name_cases, ids=ens_name_ids)
def test_web3_is_ens_name(benchmark: BenchmarkFixture, value):
    with patch("requests.request", return_value=MockResponse()):
        benchmark(run_100, web3_ens.is_ens_name, *value)

@pytest.mark.benchmark(group="is_ens_name")
@pytest.mark.parametrize("value", ens_name_cases, ids=ens_name_ids)
def test_faster_web3_is_ens_name(benchmark: BenchmarkFixture, value):
    with patch("requests.request", return_value=MockResponse()):
        benchmark(run_100, faster_ens.is_ens_name, *value)

# Benchmark validate_name_has_address with HTTP mocking
@pytest.mark.benchmark(group="validate_name_has_address")
@pytest.mark.parametrize("name,expected_addr", [
    ("vitalik.eth", "0x0000000000000000000000000000000000000000"),
    ("notanens", None),
], ids=["valid", "not-found"])
def test_web3_validate_name_has_address(benchmark: BenchmarkFixture, name, expected_addr):
    ens = ENS()  # Use default provider (will be mocked)
    def mock_request(*args, **kwargs):
        if name == "vitalik.eth":
            return MockResponse({"jsonrpc": "2.0", "id": 1, "result": "0x0000000000000000000000000000000000000000"})
        else:
            return MockResponse({"jsonrpc": "2.0", "id": 1, "result": None})
    with patch("requests.request", side_effect=mock_request):
        benchmark(run_100, web3_ens.validate_name_has_address, ens, name)

@pytest.mark.benchmark(group="validate_name_has_address")
@pytest.mark.parametrize("name,expected_addr", [
    ("vitalik.eth", "0x0000000000000000000000000000000000000000"),
    ("notanens", None),
], ids=["valid", "not-found"])
def test_faster_web3_validate_name_has_address(benchmark: BenchmarkFixture, name, expected_addr):
    ens = ENS()  # Use default provider (will be mocked)
    def mock_request(*args, **kwargs):
        if name == "vitalik.eth":
            return MockResponse({"jsonrpc": "2.0", "id": 1, "result": "0x0000000000000000000000000000000000000000"})
        else:
            return MockResponse({"jsonrpc": "2.0", "id": 1, "result": None})
    with patch("requests.request", side_effect=mock_request):
        benchmark(run_100, faster_ens.validate_name_has_address, ens, name)
