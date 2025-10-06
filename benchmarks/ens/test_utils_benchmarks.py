import pytest
from pytest_codspeed import BenchmarkFixture

import ens.utils
import faster_ens.utils
from benchmarks.ens.params import NAMES, LABELS, ADDRESSES, LABEL_LISTS

def run_10(func, *args, **kwargs):
    for _ in range(10):
        func(*args, **kwargs)

def run_10_exc(exc, func, *args, **kwargs):
    for _ in range(10):
        try:
            func(*args, **kwargs)
        except exc:
            pass

@pytest.mark.benchmark(group="normalize_name")
@pytest.mark.parametrize("name", NAMES)
def test_normalize_name(benchmark: BenchmarkFixture, name):
    benchmark(run_10, ens.utils.normalize_name, name)

@pytest.mark.benchmark(group="normalize_name")
@pytest.mark.parametrize("name", NAMES)
def test_faster_normalize_name(benchmark: BenchmarkFixture, name):
    benchmark(run_10, faster_ens.utils.normalize_name, name)

@pytest.mark.benchmark(group="dns_encode_name")
@pytest.mark.parametrize("name", NAMES)
def test_dns_encode_name(benchmark: BenchmarkFixture, name):
    benchmark(run_10, ens.utils.dns_encode_name, name)

@pytest.mark.benchmark(group="dns_encode_name")
@pytest.mark.parametrize("name", NAMES)
def test_faster_dns_encode_name(benchmark: BenchmarkFixture, name):
    benchmark(run_10, faster_ens.utils.dns_encode_name, name)

@pytest.mark.benchmark(group="is_valid_name")
@pytest.mark.parametrize("name", NAMES)
def test_is_valid_name(benchmark: BenchmarkFixture, name):
    benchmark(run_10, ens.utils.is_valid_name, name)

@pytest.mark.benchmark(group="is_valid_name")
@pytest.mark.parametrize("name", NAMES)
def test_faster_is_valid_name(benchmark: BenchmarkFixture, name):
    benchmark(run_10, faster_ens.utils.is_valid_name, name)

@pytest.mark.benchmark(group="sha3_text")
@pytest.mark.parametrize("val", NAMES + LABELS)
def test_sha3_text(benchmark: BenchmarkFixture, val):
    benchmark(run_10, ens.utils.sha3_text, val)

@pytest.mark.benchmark(group="sha3_text")
@pytest.mark.parametrize("val", NAMES + LABELS)
def test_faster_sha3_text(benchmark: BenchmarkFixture, val):
    benchmark(run_10, faster_ens.utils.sha3_text, val)

@pytest.mark.benchmark(group="label_to_hash")
@pytest.mark.parametrize("label", LABELS)
def test_label_to_hash(benchmark: BenchmarkFixture, label):
    benchmark(run_10_exc, ens.exceptions.InvalidName, ens.utils.label_to_hash, label)

@pytest.mark.benchmark(group="label_to_hash")
@pytest.mark.parametrize("label", LABELS)
def test_faster_label_to_hash(benchmark: BenchmarkFixture, label):
    benchmark(run_10_exc, faster_ens.exceptions.InvalidName, faster_ens.utils.label_to_hash, label)

@pytest.mark.benchmark(group="normal_name_to_hash")
@pytest.mark.parametrize("name", NAMES)
def test_normal_name_to_hash(benchmark: BenchmarkFixture, name):
    benchmark(run_10, ens.utils.normal_name_to_hash, name)

@pytest.mark.benchmark(group="normal_name_to_hash")
@pytest.mark.parametrize("name", NAMES)
def test_faster_normal_name_to_hash(benchmark: BenchmarkFixture, name):
    benchmark(run_10, faster_ens.utils.normal_name_to_hash, name)

@pytest.mark.benchmark(group="raw_name_to_hash")
@pytest.mark.parametrize("name", NAMES)
def test_raw_name_to_hash(benchmark: BenchmarkFixture, name):
    benchmark(run_10, ens.utils.raw_name_to_hash, name)

@pytest.mark.benchmark(group="raw_name_to_hash")
@pytest.mark.parametrize("name", NAMES)
def test_faster_raw_name_to_hash(benchmark: BenchmarkFixture, name):
    benchmark(run_10, faster_ens.utils.raw_name_to_hash, name)

@pytest.mark.benchmark(group="address_to_reverse_domain")
@pytest.mark.parametrize("address", ADDRESSES)
def test_address_to_reverse_domain(benchmark: BenchmarkFixture, address):
    benchmark(run_10, ens.utils.address_to_reverse_domain, address)

@pytest.mark.benchmark(group="address_to_reverse_domain")
@pytest.mark.parametrize("address", ADDRESSES)
def test_faster_address_to_reverse_domain(benchmark: BenchmarkFixture, address):
    benchmark(run_10, faster_ens.utils.address_to_reverse_domain, address)

@pytest.mark.benchmark(group="estimate_auction_start_gas")
@pytest.mark.parametrize("labels", LABEL_LISTS)
def test_estimate_auction_start_gas(benchmark: BenchmarkFixture, labels):
    benchmark(run_10, ens.utils.estimate_auction_start_gas, labels)

@pytest.mark.benchmark(group="estimate_auction_start_gas")
@pytest.mark.parametrize("labels", LABEL_LISTS)
def test_faster_estimate_auction_start_gas(benchmark: BenchmarkFixture, labels):
    benchmark(run_10, faster_ens.utils.estimate_auction_start_gas, labels)

@pytest.mark.benchmark(group="is_none_or_zero_address")
@pytest.mark.parametrize("address", ADDRESSES + [""])
def test_is_none_or_zero_address(benchmark: BenchmarkFixture, address):
    benchmark(run_10, ens.utils.is_none_or_zero_address, address)

@pytest.mark.benchmark(group="is_none_or_zero_address")
@pytest.mark.parametrize("address", ADDRESSES + [""])
def test_faster_is_none_or_zero_address(benchmark: BenchmarkFixture, address):
    benchmark(run_10, faster_ens.utils.is_none_or_zero_address, address)

@pytest.mark.benchmark(group="is_empty_name")
@pytest.mark.parametrize("name", NAMES + ["", ".", " "])
def test_is_empty_name(benchmark: BenchmarkFixture, name):
    benchmark(run_10, ens.utils.is_empty_name, name)

@pytest.mark.benchmark(group="is_empty_name")
@pytest.mark.parametrize("name", NAMES + ["", ".", " "])
def test_faster_is_empty_name(benchmark: BenchmarkFixture, name):
    benchmark(run_10, faster_ens.utils.is_empty_name, name)

@pytest.mark.benchmark(group="is_valid_ens_name")
@pytest.mark.parametrize("ens_name", NAMES + ["foo", "bar", "baz"])
def test_is_valid_ens_name(benchmark: BenchmarkFixture, ens_name):
    benchmark(run_10, ens.utils.is_valid_ens_name, ens_name)

@pytest.mark.benchmark(group="is_valid_ens_name")
@pytest.mark.parametrize("ens_name", NAMES + ["foo", "bar", "baz"])
def test_faster_is_valid_ens_name(benchmark: BenchmarkFixture, ens_name):
    benchmark(run_10, faster_ens.utils.is_valid_ens_name, ens_name)
