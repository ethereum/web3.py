import pytest
from typing import (
    Type,
)

from eth_utils import (
    event_signature_to_log_topic,
    to_bytes,
)
from eth_utils.toolz import (
    identity,
)
import pytest_asyncio

from web3._utils.contract_sources.contract_data.emitter_contract import (
    EMITTER_CONTRACT_DATA,
)
from web3._utils.module_testing.utils import (
    RequestMocker,
)

from .utils import (
    get_open_port,
)


@pytest.fixture(scope="module", params=[lambda x: to_bytes(hexstr=x), identity])
def address_conversion_func(request):
    return request.param


@pytest.fixture()
def open_port():
    return get_open_port()


# --- session-scoped constants --- #


@pytest.fixture(scope="session")
def emitter_contract_data():
    return EMITTER_CONTRACT_DATA


# This class defines events for the EmitterContract and are used to construct
# a fixture for contract event logs. Parameterized tests that utilize an `emitter`
# contract fixture will use this data.
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


@pytest.fixture(scope="session")
def emitter_contract_event_ids():
    return LogFunctions


# This class defines topics for the EmitterContract and are used to construct
# a fixture for contract event log topics. Parameterized tests that utilize
# an `emitter` contract fixture will use this data.
class LogTopics:
    LogAnonymous = event_signature_to_log_topic("LogAnonymous()")
    LogNoArguments = event_signature_to_log_topic("LogNoArguments()")
    LogSingleArg = event_signature_to_log_topic("LogSingleArg(uint256)")
    LogSingleAnonymous = event_signature_to_log_topic("LogSingleAnonymous(uint256)")
    LogSingleWithIndex = event_signature_to_log_topic("LogSingleWithIndex(uint256)")
    LogDoubleArg = event_signature_to_log_topic("LogDoubleArg(uint256,uint256)")
    LogDoubleAnonymous = event_signature_to_log_topic(
        "LogDoubleAnonymous(uint256,uint256)"
    )
    LogDoubleWithIndex = event_signature_to_log_topic(
        "LogDoubleWithIndex(uint256,uint256)"
    )
    LogTripleArg = event_signature_to_log_topic("LogTripleArg(uint256,uint256,uint256)")
    LogTripleWithIndex = event_signature_to_log_topic(
        "LogTripleWithIndex(uint256,uint256,uint256)"
    )
    LogQuadrupleArg = event_signature_to_log_topic(
        "LogQuadrupleArg(uint256,uint256,uint256,uint256)"
    )
    LogQuadrupleWithIndex = event_signature_to_log_topic(
        "LogQuadrupleWithIndex(uint256,uint256,uint256,uint256)",
    )
    LogBytes = event_signature_to_log_topic("LogBytes(bytes)")
    LogString = event_signature_to_log_topic("LogString(string)")
    LogDynamicArgs = event_signature_to_log_topic("LogDynamicArgs(string,string)")
    LogListArgs = event_signature_to_log_topic("LogListArgs(bytes2[],bytes2[])")
    LogAddressIndexed = event_signature_to_log_topic(
        "LogAddressIndexed(address,address)"
    )
    LogAddressNotIndexed = event_signature_to_log_topic(
        "LogAddressNotIndexed(address,address)"
    )
    LogStructArgs = event_signature_to_log_topic("LogStructArgs(uint256,tuple)")
    LogIndexedAndNotIndexed = event_signature_to_log_topic("LogIndexedAndNotIndexed()")


@pytest.fixture(scope="session")
def emitter_contract_log_topics():
    return LogTopics


# -- mock requests -- #


@pytest_asyncio.fixture(scope="function")
def request_mocker() -> Type[RequestMocker]:
    return RequestMocker
