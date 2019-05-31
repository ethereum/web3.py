import pytest
import re

from eth_utils import (
    is_same_address,
)
from eth_utils.toolz import (
    dissoc,
)

from web3._utils.events import (
    get_event_data,
)
from web3.exceptions import (
    LogTopicError,
)
from web3.logs import (
    DISCARD,
    IGNORE,
    STRICT,
    WARN,
)


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


@pytest.fixture()
def EventContract(web3, EVENT_CONTRACT):
    return web3.eth.contract(**EVENT_CONTRACT)


@pytest.fixture()
def event_contract(
        web3,
        EventContract,
        wait_for_transaction,
        wait_for_block,
        address_conversion_func):

    wait_for_block(web3)
    deploy_txn_hash = EventContract.constructor().transact({
        'from': web3.eth.coinbase, 'gas': 1000000
    })
    deploy_receipt = wait_for_transaction(web3, deploy_txn_hash)
    contract_address = address_conversion_func(deploy_receipt['contractAddress'])

    bytecode = web3.eth.getCode(contract_address)
    assert bytecode == EventContract.bytecode_runtime
    event_contract = EventContract(address=contract_address)
    assert event_contract.address == contract_address
    return event_contract


@pytest.fixture()
def IndexedEventContract(web3, INDEXED_EVENT_CONTRACT):
    return web3.eth.contract(**INDEXED_EVENT_CONTRACT)


@pytest.fixture()
def indexed_event_contract(
        web3,
        IndexedEventContract,
        wait_for_transaction,
        wait_for_block,
        address_conversion_func):

    wait_for_block(web3)
    deploy_txn_hash = IndexedEventContract.constructor().transact({
        'from': web3.eth.coinbase, 'gas': 1000000
    })
    deploy_receipt = wait_for_transaction(web3, deploy_txn_hash)
    contract_address = address_conversion_func(deploy_receipt['contractAddress'])

    bytecode = web3.eth.getCode(contract_address)
    assert bytecode == IndexedEventContract.bytecode_runtime
    indexed_event_contract = IndexedEventContract(address=contract_address)
    assert indexed_event_contract.address == contract_address
    return indexed_event_contract


@pytest.fixture()
def dup_txn_receipt(
        web3,
        indexed_event_contract,
        wait_for_transaction,
        event_contract):

    emitter_fn = indexed_event_contract.functions.logTwoEvents

    txn_hash = emitter_fn(12345).transact()
    wait_for_transaction(web3, txn_hash)

    event_contract_fn = event_contract.functions.logTwoEvents
    dup_txn_hash = event_contract_fn(12345).transact()
    return wait_for_transaction(web3, dup_txn_hash)


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

    string_0_topic = web3.keccak(text=string_0)
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

    rich_logs = event_instance.processReceipt(txn_receipt)
    quiet_event = emitter.events['LogBytes']
    with pytest.warns(UserWarning,
                      match='The event signature did not match the provided ABI'):
        empty_rich_log = quiet_event().processReceipt(txn_receipt)
        assert empty_rich_log == tuple()


def test_nonanonymous_event_abi_mismatch_warning(
        web3,
        emitter,
        emitter_event_ids,
        wait_for_transaction):
    emitter_fn = emitter.functions.logNoArgs
    event_id = getattr(emitter_event_ids, 'LogAnonymous')
    txn_hash = emitter_fn(event_id).transact()
    txn_receipt = wait_for_transaction(web3, txn_hash)

    event_instance = emitter.events.LogAnonymous()

    event_instance.processReceipt(txn_receipt)
    quiet_event = emitter.events['LogBytes']
    with pytest.warns(UserWarning,
                      match='Expected non-anonymous event to have 1 or more topics'):
        empty_rich_log = quiet_event().processReceipt(txn_receipt)
        assert empty_rich_log == tuple()


def test_event_processing_with_discard_flag(
        web3,
        event_contract,
        indexed_event_contract,
        dup_txn_receipt,
        wait_for_transaction):

    event_instance = indexed_event_contract.events.LogSingleWithIndex()
    returned_logs = event_instance.processReceipt(dup_txn_receipt, errors=DISCARD)

    assert returned_logs == ()


def test_event_processing_with_ignore_flag(
        web3,
        event_contract,
        indexed_event_contract,
        dup_txn_receipt,
        wait_for_transaction):

    event_instance = indexed_event_contract.events.LogSingleWithIndex()
    returned_logs = event_instance.processReceipt(dup_txn_receipt, errors=IGNORE)
    assert len(returned_logs) == 2

    # Check that the correct error is appended to the log
    first_log = returned_logs[0]
    log_error = re.compile("Expected 1 log topics.  Got 0")
    assert log_error.search(str(first_log.errors)) is not None

    # Then, do the same with the other log:
    second_log = returned_logs[1]
    abi_error = re.compile("The event signature did not match the provided ABI")
    assert abi_error.search(str(second_log.errors)) is not None

    for log in returned_logs:
        # Check that the returned log is the same as what got sent in,
        # except for the added errors field
        orig_log = dissoc(dict(log), 'errors')
        assert orig_log in dup_txn_receipt['logs']
        assert is_same_address(log['address'], event_contract.address)


def test_event_processing_with_warn_flag(
        web3,
        indexed_event_contract,
        dup_txn_receipt):

    event_instance = indexed_event_contract.events.LogSingleWithIndex()

    with pytest.warns(UserWarning, match='Expected 1 log topics.  Got 0'):
        returned_log = event_instance.processReceipt(dup_txn_receipt, errors=WARN)
        assert len(returned_log) == 0


def test_event_processing_with_strict_flag(
        web3,
        indexed_event_contract,
        dup_txn_receipt):

    event_instance = indexed_event_contract.events.LogSingleWithIndex()

    with pytest.raises(LogTopicError, match="Expected 1 log topics.  Got 0"):
        event_instance.processReceipt(dup_txn_receipt, errors=STRICT)


def test_event_processing_with_invalid_flag(
        web3,
        indexed_event_contract,
        dup_txn_receipt):

    event_instance = indexed_event_contract.events.LogSingleWithIndex()

    with pytest.raises(AttributeError, match=f"Error flag must be one of: "):
        event_instance.processReceipt(dup_txn_receipt, errors='not-a-flag')


def test_event_processing_with_no_flag(
        web3,
        indexed_event_contract,
        dup_txn_receipt):

    event_instance = indexed_event_contract.events.LogSingleWithIndex()

    with pytest.warns(UserWarning, match='Expected 1 log topics.  Got 0'):
        returned_log = event_instance.processReceipt(dup_txn_receipt)
        assert len(returned_log) == 0
