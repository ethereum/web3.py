import functools
import pytest

from eth_utils import (
    apply_key_map,
    encode_hex,
    event_signature_to_log_topic,
)
import pytest_asyncio

from tests.core.filtering.utils import (
    _async_emitter_fixture_logic,
    _async_w3_fixture_logic,
    _emitter_fixture_logic,
    _w3_fixture_logic,
)
from tests.utils import (
    async_partial,
)
from web3._utils.module_testing.emitter_contract import (
    CONTRACT_EMITTER_ABI,
    CONTRACT_EMITTER_CODE,
    CONTRACT_EMITTER_RUNTIME,
)


@pytest.fixture(
    scope="function",
    params=[True, False],
    ids=["local_filter_middleware", "node_based_filter"],
)
def w3(request):
    return _w3_fixture_logic(request)


@pytest.fixture()
def EMITTER_CODE():
    return CONTRACT_EMITTER_CODE


@pytest.fixture()
def EMITTER_RUNTIME():
    return CONTRACT_EMITTER_RUNTIME


@pytest.fixture()
def EMITTER_ABI():
    return CONTRACT_EMITTER_ABI


@pytest.fixture()
def EMITTER(EMITTER_CODE, EMITTER_RUNTIME, EMITTER_ABI):
    return {
        "bytecode": EMITTER_CODE,
        "bytecode_runtime": EMITTER_RUNTIME,
        "abi": EMITTER_ABI,
    }


@pytest.fixture()
def Emitter(w3, EMITTER):
    return w3.eth.contract(**EMITTER)


@pytest.fixture()
def emitter(w3, Emitter, wait_for_transaction, wait_for_block, address_conversion_func):
    return _emitter_fixture_logic(
        w3, Emitter, wait_for_transaction, wait_for_block, address_conversion_func
    )


class LogFunctions:
    LogAnonymous = 0
    LogNoArguments = 1
    LogSingleArg = 2
    LogDoubleArg = 3
    LogTripleArg = 4
    LogQuadrupleArg = 5
    LogSingleAnonymous = 6
    LogSingleWithIndex = 7
    LogDoubleAnonymous = 8
    LogDoubleWithIndex = 9
    LogTripleWithIndex = 10
    LogQuadrupleWithIndex = 11
    LogBytes = 12
    LogString = 13
    LogDynamicArgs = 14
    LogListArgs = 15
    LogAddressIndexed = 16
    LogAddressNotIndexed = 17


@pytest.fixture(scope="module")
def emitter_event_ids():
    return LogFunctions


class LogTopics:
    LogAnonymous = encode_hex(event_signature_to_log_topic("LogAnonymous()"))
    LogNoArguments = encode_hex(event_signature_to_log_topic("LogNoArguments()"))
    LogSingleArg = encode_hex(event_signature_to_log_topic("LogSingleArg(uint256)"))
    LogSingleAnonymous = encode_hex(
        event_signature_to_log_topic("LogSingleAnonymous(uint256)")
    )
    LogSingleWithIndex = encode_hex(
        event_signature_to_log_topic("LogSingleWithIndex(uint256)")
    )
    LogDoubleArg = encode_hex(
        event_signature_to_log_topic("LogDoubleArg(uint256,uint256)")
    )
    LogDoubleAnonymous = encode_hex(
        event_signature_to_log_topic("LogDoubleAnonymous(uint256,uint256)")
    )  # noqa: E501
    LogDoubleWithIndex = encode_hex(
        event_signature_to_log_topic("LogDoubleWithIndex(uint256,uint256)")
    )  # noqa: E501
    LogTripleArg = encode_hex(
        event_signature_to_log_topic("LogTripleArg(uint256,uint256,uint256)")
    )
    LogTripleWithIndex = encode_hex(
        event_signature_to_log_topic("LogTripleWithIndex(uint256,uint256,uint256)")
    )  # noqa: E501
    LogQuadrupleArg = encode_hex(
        event_signature_to_log_topic("LogQuadrupleArg(uint256,uint256,uint256,uint256)")
    )  # noqa: E501
    LogQuadrupleWithIndex = encode_hex(
        event_signature_to_log_topic(
            "LogQuadrupleWithIndex(uint256,uint256,uint256,uint256)"
        )
    )  # noqa: E501
    LogBytes = encode_hex(event_signature_to_log_topic("LogBytes(bytes)"))
    LogString = encode_hex(event_signature_to_log_topic("LogString(string)"))
    LogDynamicArgs = encode_hex(
        event_signature_to_log_topic("LogDynamicArgs(string,string)")
    )
    LogListArgs = encode_hex(
        event_signature_to_log_topic("LogListArgs(bytes2[],bytes2[])")
    )
    LogAddressIndexed = encode_hex(
        event_signature_to_log_topic("LogAddressIndexed(address,address)")
    )
    LogAddressNotIndexed = encode_hex(
        event_signature_to_log_topic("LogAddressNotIndexed(address,address)")
    )


@pytest.fixture()
def emitter_log_topics():
    return LogTopics


def return_filter(contract, args):
    event_name = args[0]
    kwargs = apply_key_map({"filter": "argument_filters"}, args[1])
    if "fromBlock" not in kwargs:
        kwargs["fromBlock"] = "latest"
    return contract.events[event_name].create_filter(**kwargs)


@pytest.fixture(scope="module")
def create_filter(request):
    return functools.partial(return_filter)


# --- async --- #


@pytest.fixture(
    scope="function",
    params=[True, False],
    ids=["async_local_filter_middleware", "node_based_filter"],
)
def async_w3(request):
    return _async_w3_fixture_logic(request)


@pytest.fixture()
def AsyncEmitter(async_w3, EMITTER):
    return async_w3.eth.contract(**EMITTER)


@pytest_asyncio.fixture()
async def async_emitter(
    async_w3,
    AsyncEmitter,
    async_wait_for_transaction,
    async_wait_for_block,
    address_conversion_func,
):
    return await _async_emitter_fixture_logic(
        async_w3,
        AsyncEmitter,
        async_wait_for_transaction,
        async_wait_for_block,
        address_conversion_func,
    )


async def async_return_filter(contract, args):
    event_name = args[0]
    kwargs = apply_key_map({"filter": "argument_filters"}, args[1])
    if "fromBlock" not in kwargs:
        kwargs["fromBlock"] = "latest"
    return await contract.events[event_name].create_filter(**kwargs)


@pytest_asyncio.fixture(scope="module")
async def async_create_filter(request):
    return async_partial(async_return_filter)
