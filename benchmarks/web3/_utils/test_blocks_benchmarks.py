import pytest
from pytest_codspeed import BenchmarkFixture

import web3._utils.blocks
import faster_web3._utils.blocks


_object = object()

def run_100(func, *args, **kwargs):
    for _ in range(100):
        func(*args, **kwargs)

def run_100_exc(func, expected_exc, *args, **kwargs):
    for _ in range(100):
        try:
            func(*args, **kwargs)
        except expected_exc:
            pass

# --- is_predefined_block_number ---

predefined_cases = [
    "latest",
    "pending",
    "earliest",
    "safe",
    "finalized",
    "foo",
    b"latest",
    b"pending",
    b"random",
    123,
    None,
    _object,
]
predefined_ids = [
    "str-latest", "str-pending", "str-earliest", "str-safe", "str-finalized",
    "str-foo",
    "bytes-latest", "bytes-pending", "bytes-random",
    "int", "none", "object"
]

@pytest.mark.benchmark(group="is_predefined_block_number")
@pytest.mark.parametrize("value", predefined_cases, ids=predefined_ids)
def test_is_predefined_block_number(benchmark: BenchmarkFixture, value):
    func = web3._utils.blocks.is_predefined_block_number
    if value in (None, _object):
        benchmark(run_100_exc, func, web3.exceptions.Web3TypeError, value)
    else:
        benchmark(run_100, func, value)

@pytest.mark.benchmark(group="is_predefined_block_number")
@pytest.mark.parametrize("value", predefined_cases, ids=predefined_ids)
def test_faster_is_predefined_block_number(benchmark: BenchmarkFixture, value):
    func = faster_web3._utils.blocks.is_predefined_block_number
    if value in (None, _object):
        benchmark(run_100_exc, func, faster_web3.exceptions.Web3TypeError, value)
    else:
        benchmark(run_100, func, value)

# --- is_hex_encoded_block_hash ---

hex_hash_cases = [
    "0x" + "a"*64,
    "0x" + "f"*64,
    "0x" + "g"*64,
    "0x1234",
    "0x" + "a"*63,
    "0x" + "a"*65,
    123,
    None,
]
hex_hash_ids = [
    "valid-a", "valid-f", "invalid-g", "short", "too-short", "too-long", "int", "none"
]

@pytest.mark.benchmark(group="is_hex_encoded_block_hash")
@pytest.mark.parametrize("value", hex_hash_cases, ids=hex_hash_ids)
def test_is_hex_encoded_block_hash(benchmark: BenchmarkFixture, value):
    benchmark(run_100, web3._utils.blocks.is_hex_encoded_block_hash, value)

@pytest.mark.benchmark(group="is_hex_encoded_block_hash")
@pytest.mark.parametrize("value", hex_hash_cases, ids=hex_hash_ids)
def test_faster_is_hex_encoded_block_hash(benchmark: BenchmarkFixture, value):
    benchmark(run_100, faster_web3._utils.blocks.is_hex_encoded_block_hash, value)

# --- is_hex_encoded_block_number ---

hex_number_cases = [
    "0x1",
    "0x" + "f"*64,
    "0x" + "a"*64,
    "0xg",
    "0x" + "1"*65,
    123,
    None,
]
hex_number_ids = [
    "small", "max-64-f", "max-64-a", "invalid-g", "too-long", "int", "none"
]

@pytest.mark.benchmark(group="is_hex_encoded_block_number")
@pytest.mark.parametrize("value", hex_number_cases, ids=hex_number_ids)
def test_is_hex_encoded_block_number(benchmark: BenchmarkFixture, value):
    benchmark(run_100, web3._utils.blocks.is_hex_encoded_block_number, value)

@pytest.mark.benchmark(group="is_hex_encoded_block_number")
@pytest.mark.parametrize("value", hex_number_cases, ids=hex_number_ids)
def test_faster_is_hex_encoded_block_number(benchmark: BenchmarkFixture, value):
    benchmark(run_100, faster_web3._utils.blocks.is_hex_encoded_block_number, value)

# --- select_method_for_block_identifier ---

select_cases = [
    # Predefined
    ("latest", "HASH", "NUMBER", "PREDEFINED"),
    (b"latest", "HASH", "NUMBER", "PREDEFINED"),
    # Hash (bytes)
    (b"\x12"*32, "HASH", "NUMBER", "PREDEFINED"),
    # Hash (hex string)
    ("0x" + "a"*64, "HASH", "NUMBER", "PREDEFINED"),
    # Number (int)
    (123, "HASH", "NUMBER", "PREDEFINED"),
    # Number (hex string)
    ("0x1", "HASH", "NUMBER", "PREDEFINED"),
    # Invalid (should raise)
    (None, "HASH", "NUMBER", "PREDEFINED"),
    (_object, "HASH", "NUMBER", "PREDEFINED"),
]
select_ids = [
    "predefined-str", "predefined-bytes", "hash-bytes", "hash-hexstr",
    "number-int", "number-hexstr", "invalid-none", "invalid-object"
]

@pytest.mark.benchmark(group="select_method_for_block_identifier")
@pytest.mark.parametrize("value,if_hash,if_number,if_predefined", select_cases, ids=select_ids)
def test_select_method_for_block_identifier(benchmark: BenchmarkFixture, value, if_hash, if_number, if_predefined):
    if value in (None, _object):
        expected_exc = web3.exceptions.Web3TypeError
    else:
        expected_exc = web3.exceptions.Web3ValueError,
    benchmark(
        run_100_exc,
        web3._utils.blocks.select_method_for_block_identifier,
        expected_exc,
        value,
        if_hash,
        if_number,
        if_predefined,
    )

@pytest.mark.benchmark(group="select_method_for_block_identifier")
@pytest.mark.parametrize("value,if_hash,if_number,if_predefined", select_cases, ids=select_ids)
def test_faster_select_method_for_block_identifier(benchmark: BenchmarkFixture, value, if_hash, if_number, if_predefined):
    if value in (None, _object):
        expected_exc = faster_web3.exceptions.Web3TypeError
    else:
        expected_exc = faster_web3.exceptions.Web3ValueError,
    benchmark(
        run_100_exc,
        faster_web3._utils.blocks.select_method_for_block_identifier,
        expected_exc,
        value,
        if_hash,
        if_number,
        if_predefined,
    )
