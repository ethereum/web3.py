import pytest

from eth_utils import (
    is_same_address,
)

from web3.utils.events import (
    get_event_data,
)

# Ignore warning in pyethereum 1.6 - will go away with the upgrade
pytestmark = pytest.mark.filterwarnings("ignore:implicit cast from 'char *'")


@pytest.fixture()
def Emitter(web3, EMITTER):
    return web3.eth.contract(**EMITTER)


@pytest.fixture()
def emitter(web3, Emitter, wait_for_transaction, wait_for_block, address_conversion_func):
    wait_for_block(web3)
    deploy_txn_hash = Emitter.constructor().transact({'from': web3.eth.coinbase, 'gas': 1000000})
    deploy_receipt = web3.eth.waitForTransactionReceipt(deploy_txn_hash)
    contract_address = address_conversion_func(deploy_receipt['contractAddress'])

    bytecode = web3.eth.getCode(contract_address)
    assert bytecode == Emitter.bytecode_runtime
    _emitter = Emitter(address=contract_address)
    assert _emitter.address == contract_address
    return _emitter


@pytest.mark.parametrize(
    'contract_fn,event_name,call_args,expected_args',
    (
        ('logNoArgs', 'LogAnonymous', [], {}),
        ('logNoArgs', 'LogNoArguments', [], {}),
        ('logSingle', 'LogSingleArg', [12345], {'arg0': 12345}),
        ('logSingle', 'LogSingleWithIndex', [12345], {'arg0': 12345}),
        ('logSingle', 'LogSingleAnonymous', [12345], {'arg0': 12345}),
        ('logDouble', 'LogDoubleArg', [12345, 54321], {'arg0': 12345, 'arg1': 54321}),
        ('logDouble', 'LogDoubleAnonymous', [12345, 54321], {'arg0': 12345, 'arg1': 54321}),
        ('logDouble', 'LogDoubleWithIndex', [12345, 54321], {'arg0': 12345, 'arg1': 54321}),
        (
            'logTriple',
            'LogTripleArg',
            [12345, 54321, 98765],
            {'arg0': 12345, 'arg1': 54321, 'arg2': 98765},
        ),
        (
            'logTriple',
            'LogTripleWithIndex',
            [12345, 54321, 98765],
            {'arg0': 12345, 'arg1': 54321, 'arg2': 98765},
        ),
        (
            'logQuadruple',
            'LogQuadrupleArg',
            [12345, 54321, 98765, 56789],
            {'arg0': 12345, 'arg1': 54321, 'arg2': 98765, 'arg3': 56789},
        ),
        (
            'logQuadruple',
            'LogQuadrupleWithIndex',
            [12345, 54321, 98765, 56789],
            {'arg0': 12345, 'arg1': 54321, 'arg2': 98765, 'arg3': 56789},
        ),
    )
)
def test_event_data_extraction(web3,
                               emitter,
                               wait_for_transaction,
                               emitter_log_topics,
                               emitter_event_ids,
                               contract_fn,
                               event_name,
                               call_args,
                               expected_args):
    emitter_fn = emitter.functions[contract_fn]
    event_id = getattr(emitter_event_ids, event_name)
    txn_hash = emitter_fn(event_id, *call_args).transact()
    txn_receipt = wait_for_transaction(web3, txn_hash)

    assert len(txn_receipt['logs']) == 1
    log_entry = txn_receipt['logs'][0]

    event_abi = emitter._find_matching_event_abi(event_name)

    event_topic = getattr(emitter_log_topics, event_name)
    is_anonymous = event_abi['anonymous']

    if is_anonymous:
        assert event_topic not in log_entry['topics']
    else:
        assert event_topic in log_entry['topics']

    event_data = get_event_data(event_abi, log_entry)

    assert event_data['args'] == expected_args
    assert event_data['blockHash'] == txn_receipt['blockHash']
    assert event_data['blockNumber'] == txn_receipt['blockNumber']
    assert event_data['transactionIndex'] == txn_receipt['transactionIndex']
    assert is_same_address(event_data['address'], emitter.address)
    assert event_data['event'] == event_name


def test_dynamic_length_argument_extraction(web3,
                                            emitter,
                                            wait_for_transaction,
                                            emitter_log_topics,
                                            emitter_event_ids):
    string_0 = "this-is-the-first-string-which-exceeds-32-bytes-in-length"
    string_1 = "this-is-the-second-string-which-exceeds-32-bytes-in-length"
    txn_hash = emitter.functions.logDynamicArgs(string_0, string_1).transact()
    txn_receipt = wait_for_transaction(web3, txn_hash)

    assert len(txn_receipt['logs']) == 1
    log_entry = txn_receipt['logs'][0]

    event_abi = emitter._find_matching_event_abi('LogDynamicArgs')

    event_topic = emitter_log_topics.LogDynamicArgs
    assert event_topic in log_entry['topics']

    string_0_topic = web3.sha3(text=string_0)
    assert string_0_topic in log_entry['topics']

    event_data = get_event_data(event_abi, log_entry)

    expected_args = {
        "arg0": string_0_topic,
        "arg1": string_1,
    }

    assert event_data['args'] == expected_args
    assert event_data['blockHash'] == txn_receipt['blockHash']
    assert event_data['blockNumber'] == txn_receipt['blockNumber']
    assert event_data['transactionIndex'] == txn_receipt['transactionIndex']
    assert is_same_address(event_data['address'], emitter.address)
    assert event_data['event'] == 'LogDynamicArgs'


@pytest.mark.parametrize(
    'contract_fn,event_name,call_args,expected_args',
    (
        ('logNoArgs', 'LogAnonymous', [], {}),
        ('logNoArgs', 'LogNoArguments', [], {}),
        ('logSingle', 'LogSingleArg', [12345], {'arg0': 12345}),
        ('logSingle', 'LogSingleWithIndex', [12345], {'arg0': 12345}),
        ('logSingle', 'LogSingleAnonymous', [12345], {'arg0': 12345}),
        ('logDouble', 'LogDoubleArg', [12345, 54321], {'arg0': 12345, 'arg1': 54321}),
        ('logDouble', 'LogDoubleAnonymous', [12345, 54321], {'arg0': 12345, 'arg1': 54321}),
        ('logDouble', 'LogDoubleWithIndex', [12345, 54321], {'arg0': 12345, 'arg1': 54321}),
        (
            'logTriple',
            'LogTripleArg',
            [12345, 54321, 98765],
            {'arg0': 12345, 'arg1': 54321, 'arg2': 98765},
        ),
        (
            'logTriple',
            'LogTripleWithIndex',
            [12345, 54321, 98765],
            {'arg0': 12345, 'arg1': 54321, 'arg2': 98765},
        ),
        (
            'logQuadruple',
            'LogQuadrupleArg',
            [12345, 54321, 98765, 56789],
            {'arg0': 12345, 'arg1': 54321, 'arg2': 98765, 'arg3': 56789},
        ),
        (
            'logQuadruple',
            'LogQuadrupleWithIndex',
            [12345, 54321, 98765, 56789],
            {'arg0': 12345, 'arg1': 54321, 'arg2': 98765, 'arg3': 56789},
        ),
    )
)
def test_event_rich_log(
        web3,
        emitter,
        emitter_event_ids,
        wait_for_transaction,
        contract_fn,
        event_name,
        call_args,
        expected_args):

    emitter_fn = emitter.functions[contract_fn]
    event_id = getattr(emitter_event_ids, event_name)
    txn_hash = emitter_fn(event_id, *call_args).transact()
    txn_receipt = wait_for_transaction(web3, txn_hash)

    event_instance = emitter.events[event_name]()

    rich_logs = event_instance.processReceipt(txn_receipt)

    assert len(rich_logs) == 1

    rich_log = rich_logs[0]

    assert rich_log['args'] == expected_args
    assert rich_log.args == expected_args
    for arg in expected_args:
        assert getattr(rich_log.args, arg) == expected_args[arg]
    assert rich_log['blockHash'] == txn_receipt['blockHash']
    assert rich_log['blockNumber'] == txn_receipt['blockNumber']
    assert rich_log['transactionIndex'] == txn_receipt['transactionIndex']
    assert is_same_address(rich_log['address'], emitter.address)
    assert rich_log['event'] == event_name

    quiet_event = emitter.events['LogBytes']
    empty_rich_log = quiet_event().processReceipt(txn_receipt)
    assert empty_rich_log == tuple()
