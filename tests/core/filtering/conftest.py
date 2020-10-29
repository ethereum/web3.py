import functools
import pytest

from eth_utils import (
    apply_key_map,
    encode_hex,
    event_signature_to_log_topic,
)

from web3 import Web3
from web3._utils.module_testing.emitter_contract import (
    CONTRACT_EMITTER_ABI,
    CONTRACT_EMITTER_CODE,
    CONTRACT_EMITTER_RUNTIME,
)
from web3.middleware import (
    local_filter_middleware,
)
from web3.providers.eth_tester import (
    EthereumTesterProvider,
)


@pytest.fixture()
def tester_snapshot(web3):
    return web3.provider.ethereum_tester.take_snapshot()


@pytest.fixture(
    scope='function',
    params=[True, False],
    ids=["local_filter_middleware", "node_based_filter"])
def web3(request):
    use_filter_middleware = request.param
    provider = EthereumTesterProvider()
    w3 = Web3(provider)
    if use_filter_middleware:
        w3.middleware_onion.add(local_filter_middleware)
    return w3


@pytest.fixture(autouse=True)
def wait_for_mining_start(web3, wait_for_block):
    wait_for_block(web3)


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
def EMITTER(EMITTER_CODE,
            EMITTER_RUNTIME,
            EMITTER_ABI):
    return {
        'bytecode': EMITTER_CODE,
        'bytecode_runtime': EMITTER_RUNTIME,
        'abi': EMITTER_ABI,
    }


@pytest.fixture()
def Emitter(web3, EMITTER):
    return web3.eth.contract(**EMITTER)


@pytest.fixture()
def emitter(web3, Emitter, wait_for_transaction, wait_for_block, address_conversion_func):
    wait_for_block(web3)
    deploy_txn_hash = Emitter.constructor().transact({
        'from': web3.eth.coinbase,
        'gas': 1000000,
        'gasPrice': 1})
    deploy_receipt = wait_for_transaction(web3, deploy_txn_hash)
    contract_address = address_conversion_func(deploy_receipt['contractAddress'])

    bytecode = web3.eth.getCode(contract_address)
    assert bytecode == Emitter.bytecode_runtime
    _emitter = Emitter(address=contract_address)
    assert _emitter.address == contract_address
    return _emitter


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
    LogSingleAnonymous = encode_hex(event_signature_to_log_topic("LogSingleAnonymous(uint256)"))
    LogSingleWithIndex = encode_hex(event_signature_to_log_topic("LogSingleWithIndex(uint256)"))
    LogDoubleArg = encode_hex(event_signature_to_log_topic("LogDoubleArg(uint256,uint256)"))
    LogDoubleAnonymous = encode_hex(event_signature_to_log_topic("LogDoubleAnonymous(uint256,uint256)"))  # noqa: E501
    LogDoubleWithIndex = encode_hex(event_signature_to_log_topic("LogDoubleWithIndex(uint256,uint256)"))  # noqa: E501
    LogTripleArg = encode_hex(event_signature_to_log_topic("LogTripleArg(uint256,uint256,uint256)"))
    LogTripleWithIndex = encode_hex(event_signature_to_log_topic("LogTripleWithIndex(uint256,uint256,uint256)"))  # noqa: E501
    LogQuadrupleArg = encode_hex(event_signature_to_log_topic("LogQuadrupleArg(uint256,uint256,uint256,uint256)"))  # noqa: E501
    LogQuadrupleWithIndex = encode_hex(event_signature_to_log_topic("LogQuadrupleWithIndex(uint256,uint256,uint256,uint256)"))  # noqa: E501
    LogBytes = encode_hex(event_signature_to_log_topic("LogBytes(bytes)"))
    LogString = encode_hex(event_signature_to_log_topic("LogString(string)"))
    LogDynamicArgs = encode_hex(event_signature_to_log_topic("LogDynamicArgs(string,string)"))
    LogListArgs = encode_hex(event_signature_to_log_topic("LogListArgs(bytes2[],bytes2[])"))
    LogAddressIndexed = encode_hex(event_signature_to_log_topic(
        "LogAddressIndexed(address,address)"))
    LogAddressNotIndexed = encode_hex(event_signature_to_log_topic(
        "LogAddressNotIndexed(address,address)"))


@pytest.fixture()
def emitter_log_topics():
    return LogTopics


def return_filter(
        contract=None,
        args=[]):
    event_name = args[0]
    kwargs = apply_key_map({'filter': 'argument_filters'}, args[1])
    if 'fromBlock' not in kwargs:
        kwargs['fromBlock'] = 'latest'
    return contract.events[event_name].createFilter(**kwargs)


@pytest.fixture(scope="module")
def create_filter(request):
    return functools.partial(return_filter)
