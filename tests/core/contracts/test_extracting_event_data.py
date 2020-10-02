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
    ValidationError,
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

    event_data = get_event_data(web3.codec, event_abi, log_entry)

    assert event_data['args'] == expected_args
    assert event_data['blockHash'] == txn_receipt['blockHash']
    assert event_data['blockNumber'] == txn_receipt['blockNumber']
    assert event_data['transactionIndex'] == txn_receipt['transactionIndex']
    assert is_same_address(event_data['address'], emitter.address)
    assert event_data['event'] == event_name


@pytest.mark.parametrize(
    'call_args,expected_args',
    (
        (
            [[b'13'], [b'54']],
            {
                'arg0': b'H\x7f\xad\xb3\x16zAS7\xa5\x0c\xfe\xe2%T\xb7\x17\x81p\xf04~\x8d(\x93\x8e\x19\x97k\xd9"1',  # noqa: E501
                'arg1': [b'54']
            }
        ),
        (
            [[b'1'], [b'5']],
            {
                'arg0': b' F=9\n\x03\xb6\xe1\x00\xc5\xb7\xce\xf5\xa5\xac\x08\x08\xb8\xaf\xc4d=\xdb\xda\xf1\x05|a\x0f.\xa1!',  # noqa: E501
                'arg1': [b'5\x00']}
        ),
    )
)
def test_event_data_extraction_bytes(web3,
                                     emitter,
                                     wait_for_transaction,
                                     emitter_log_topics,
                                     emitter_event_ids,
                                     call_args,
                                     expected_args):
    emitter_fn = emitter.functions.logListArgs
    txn_hash = emitter_fn(*call_args).transact()
    txn_receipt = wait_for_transaction(web3, txn_hash)

    assert len(txn_receipt['logs']) == 1
    log_entry = txn_receipt['logs'][0]

    event_name = 'LogListArgs'
    event_abi = emitter._find_matching_event_abi(event_name)

    event_topic = getattr(emitter_log_topics, event_name)

    assert event_topic in log_entry['topics']

    event_data = get_event_data(web3.codec, event_abi, log_entry)

    assert event_data['args'] == expected_args
    assert event_data['blockHash'] == txn_receipt['blockHash']
    assert event_data['blockNumber'] == txn_receipt['blockNumber']
    assert event_data['transactionIndex'] == txn_receipt['transactionIndex']
    assert is_same_address(event_data['address'], emitter.address)
    assert event_data['event'] == event_name


def test_event_data_extraction_bytes_with_warning(web3,
                                                  emitter,
                                                  wait_for_transaction,
                                                  emitter_log_topics):
    with pytest.warns(
        DeprecationWarning,
        match='in v6 it will be invalid to pass a hex string without the "0x" prefix'
    ):
        txn_hash = emitter.functions.logListArgs(['13'], ['54']).transact()
        txn_receipt = wait_for_transaction(web3, txn_hash)

        assert len(txn_receipt['logs']) == 1
        log_entry = txn_receipt['logs'][0]

        event_name = 'LogListArgs'
        event_abi = emitter._find_matching_event_abi(event_name)

        event_topic = getattr(emitter_log_topics, event_name)

        assert event_topic in log_entry['topics']

        event_data = get_event_data(web3.codec, event_abi, log_entry)
        expected_args = {
            'arg0': b']\x0b\xf6sp\xbe\xa2L\xa9is\xe4\xab\xb7\xfa+nVJpgt\xa7\x8f:\xa4\x9f\xdb\x93\xf0\x8f\xae',  # noqa: E501
            'arg1': [b'T\x00']
        }

        assert event_data['args'] == expected_args
        assert event_data['blockHash'] == txn_receipt['blockHash']
        assert event_data['blockNumber'] == txn_receipt['blockNumber']
        assert event_data['transactionIndex'] == txn_receipt['transactionIndex']
        assert is_same_address(event_data['address'], emitter.address)
        assert event_data['event'] == event_name


@pytest.mark.parametrize(
    'call_args',
    (
        (
            [[b'1312'], [b'4354']],
        ),
        (
            [[b'1'], [b'5']],
        ),
    )
)
def test_event_data_extraction_bytes_strict_with_errors(strict_emitter,
                                                        call_args):
    emitter_fn = strict_emitter.functions.logListArgs
    with pytest.raises(ValidationError):
        emitter_fn(*call_args).transact()


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

    event_data = get_event_data(web3.codec, event_abi, log_entry)

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


def test_argument_extraction_strict_bytes_types(w3_strict_abi,
                                                strict_emitter,
                                                wait_for_transaction,
                                                emitter_log_topics):
    arg_0 = [b'12']
    arg_1 = [b'12']
    txn_hash = strict_emitter.functions.logListArgs(arg_0, arg_1).transact()
    txn_receipt = wait_for_transaction(w3_strict_abi, txn_hash)

    assert len(txn_receipt['logs']) == 1
    log_entry = txn_receipt['logs'][0]
    assert len(log_entry['topics']) == 2

    event_abi = strict_emitter._find_matching_event_abi('LogListArgs')

    event_topic = emitter_log_topics.LogListArgs
    assert event_topic in log_entry['topics']

    encoded_arg_0 = w3_strict_abi.codec.encode_abi(['bytes2'], arg_0)
    padded_arg_0 = encoded_arg_0.ljust(32, b'\x00')
    arg_0_topic = w3_strict_abi.keccak(padded_arg_0)
    assert arg_0_topic in log_entry['topics']

    event_data = get_event_data(w3_strict_abi.codec, event_abi, log_entry)

    expected_args = {
        "arg0": arg_0_topic,
        "arg1": arg_1
    }

    assert event_data['args'] == expected_args
    assert event_data['blockHash'] == txn_receipt['blockHash']
    assert event_data['blockNumber'] == txn_receipt['blockNumber']
    assert event_data['transactionIndex'] == txn_receipt['transactionIndex']
    assert is_same_address(event_data['address'], strict_emitter.address)
    assert event_data['event'] == 'LogListArgs'


@pytest.mark.parametrize(
    'contract_fn,event_name,call_args,expected_args,warning_msg,process_receipt',
    (
        (
            'logNoArgs',
            'LogAnonymous',
            [],
            {},
            'Expected non-anonymous event to have 1 or more topics',
            True
        ),
        (
            'logNoArgs',
            'LogAnonymous',
            [],
            {},
            'Expected non-anonymous event to have 1 or more topics',
            False
        ),
        (
            'logNoArgs',
            'LogNoArguments',
            [],
            {},
            'The event signature did not match the provided ABI',
            True
        ),
        (
            'logNoArgs',
            'LogNoArguments',
            [],
            {},
            'The event signature did not match the provided ABI',
            False
        ),
        (
            'logSingle',
            'LogSingleArg',
            [12345],
            {'arg0': 12345},
            'The event signature did not match the provided ABI',
            True
        ),
        (
            'logSingle',
            'LogSingleArg',
            [12345],
            {'arg0': 12345},
            'The event signature did not match the provided ABI',
            False
        ),
        (
            'logSingle',
            'LogSingleWithIndex',
            [12345],
            {'arg0': 12345},
            'The event signature did not match the provided ABI',
            True
        ),
        (
            'logSingle',
            'LogSingleWithIndex',
            [12345],
            {'arg0': 12345},
            'The event signature did not match the provided ABI',
            False
        ),
        (
            'logSingle',
            'LogSingleAnonymous',
            [12345],
            {'arg0': 12345},
            'The event signature did not match the provided ABI',
            True
        ),
        (
            'logSingle',
            'LogSingleAnonymous',
            [12345],
            {'arg0': 12345},
            'The event signature did not match the provided ABI',
            False
        ),
        (
            'logDouble',
            'LogDoubleArg',
            [12345, 54321],
            {'arg0': 12345, 'arg1': 54321},
            'The event signature did not match the provided ABI',
            True
        ),
        (
            'logDouble',
            'LogDoubleArg',
            [12345, 54321],
            {'arg0': 12345, 'arg1': 54321},
            'The event signature did not match the provided ABI',
            False
        ),
        (
            'logDouble',
            'LogDoubleAnonymous',
            [12345, 54321],
            {'arg0': 12345, 'arg1': 54321},
            'The event signature did not match the provided ABI',
            True
        ),
        (
            'logDouble',
            'LogDoubleAnonymous',
            [12345, 54321],
            {'arg0': 12345, 'arg1': 54321},
            'The event signature did not match the provided ABI',
            False
        ),
        (
            'logDouble',
            'LogDoubleWithIndex',
            [12345, 54321],
            {'arg0': 12345, 'arg1': 54321},
            'The event signature did not match the provided ABI',
            True
        ),
        (
            'logDouble',
            'LogDoubleWithIndex',
            [12345, 54321],
            {'arg0': 12345, 'arg1': 54321},
            'The event signature did not match the provided ABI',
            False
        ),
        (
            'logTriple',
            'LogTripleArg',
            [12345, 54321, 98765],
            {'arg0': 12345, 'arg1': 54321, 'arg2': 98765},
            'The event signature did not match the provided ABI',
            True,
        ),
        (
            'logTriple',
            'LogTripleArg',
            [12345, 54321, 98765],
            {'arg0': 12345, 'arg1': 54321, 'arg2': 98765},
            'The event signature did not match the provided ABI',
            False,
        ),
        (
            'logTriple',
            'LogTripleWithIndex',
            [12345, 54321, 98765],
            {'arg0': 12345, 'arg1': 54321, 'arg2': 98765},
            'The event signature did not match the provided ABI',
            True,
        ),
        (
            'logTriple',
            'LogTripleWithIndex',
            [12345, 54321, 98765],
            {'arg0': 12345, 'arg1': 54321, 'arg2': 98765},
            'The event signature did not match the provided ABI',
            False,
        ),
        (
            'logQuadruple',
            'LogQuadrupleArg',
            [12345, 54321, 98765, 56789],
            {'arg0': 12345, 'arg1': 54321, 'arg2': 98765, 'arg3': 56789},
            'The event signature did not match the provided ABI',
            True,
        ),
        (
            'logQuadruple',
            'LogQuadrupleArg',
            [12345, 54321, 98765, 56789],
            {'arg0': 12345, 'arg1': 54321, 'arg2': 98765, 'arg3': 56789},
            'The event signature did not match the provided ABI',
            False,
        ),
        (
            'logQuadruple',
            'LogQuadrupleWithIndex',
            [12345, 54321, 98765, 56789],
            {'arg0': 12345, 'arg1': 54321, 'arg2': 98765, 'arg3': 56789},
            'The event signature did not match the provided ABI',
            True,
        ),
        (
            'logQuadruple',
            'LogQuadrupleWithIndex',
            [12345, 54321, 98765, 56789],
            {'arg0': 12345, 'arg1': 54321, 'arg2': 98765, 'arg3': 56789},
            'The event signature did not match the provided ABI',
            False,
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
        warning_msg,
        call_args,
        process_receipt,
        expected_args):

    emitter_fn = emitter.functions[contract_fn]
    event_id = getattr(emitter_event_ids, event_name)
    txn_hash = emitter_fn(event_id, *call_args).transact()
    txn_receipt = wait_for_transaction(web3, txn_hash)

    event_instance = emitter.events[event_name]()

    if process_receipt:
        processed_logs = event_instance.processReceipt(txn_receipt)
        assert len(processed_logs) == 1
        rich_log = processed_logs[0]
    elif not process_receipt:
        rich_log = event_instance.processLog(txn_receipt['logs'][0])
    else:
        raise Exception('Unreachable!')

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
    with pytest.warns(UserWarning, match=warning_msg):
        empty_rich_log = quiet_event().processReceipt(txn_receipt)
        assert empty_rich_log == tuple()


@pytest.mark.parametrize('process_receipt', (True, False))
def test_event_rich_log_with_byte_args(
        web3,
        emitter,
        emitter_event_ids,
        wait_for_transaction,
        process_receipt):

    txn_hash = emitter.functions.logListArgs([b'13'], [b'54']).transact()
    txn_receipt = wait_for_transaction(web3, txn_hash)

    event_instance = emitter.events.LogListArgs()

    if process_receipt:
        processed_logs = event_instance.processReceipt(txn_receipt)
        assert len(processed_logs) == 1
        rich_log = processed_logs[0]
    elif not process_receipt:
        rich_log = event_instance.processLog(txn_receipt['logs'][0])
    else:
        raise Exception('Unreachable!')

    expected_args = {
        'arg0': b'H\x7f\xad\xb3\x16zAS7\xa5\x0c\xfe\xe2%T\xb7\x17\x81p\xf04~\x8d(\x93\x8e\x19\x97k\xd9"1',  # noqa: E501
        'arg1': [b'54']
    }
    assert rich_log['args'] == expected_args
    assert rich_log.args == expected_args
    for arg in expected_args:
        assert getattr(rich_log.args, arg) == expected_args[arg]
    assert rich_log['blockHash'] == txn_receipt['blockHash']
    assert rich_log['blockNumber'] == txn_receipt['blockNumber']
    assert rich_log['transactionIndex'] == txn_receipt['transactionIndex']
    assert is_same_address(rich_log['address'], emitter.address)
    assert rich_log['event'] == 'LogListArgs'


def test_receipt_processing_with_discard_flag(
        web3,
        event_contract,
        indexed_event_contract,
        dup_txn_receipt,
        wait_for_transaction):

    event_instance = indexed_event_contract.events.LogSingleWithIndex()

    returned_logs = event_instance.processReceipt(dup_txn_receipt, errors=DISCARD)
    assert returned_logs == ()


def test_receipt_processing_with_ignore_flag(
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


def test_receipt_processing_with_warn_flag(
        web3,
        indexed_event_contract,
        dup_txn_receipt):

    event_instance = indexed_event_contract.events.LogSingleWithIndex()

    with pytest.warns(UserWarning, match='Expected 1 log topics.  Got 0'):
        returned_logs = event_instance.processReceipt(dup_txn_receipt, errors=WARN)
        assert len(returned_logs) == 0


def test_receipt_processing_with_strict_flag(
        web3,
        indexed_event_contract,
        dup_txn_receipt):

    event_instance = indexed_event_contract.events.LogSingleWithIndex()

    with pytest.raises(LogTopicError, match="Expected 1 log topics.  Got 0"):
        event_instance.processReceipt(dup_txn_receipt, errors=STRICT)


def test_receipt_processing_with_invalid_flag(
        web3,
        indexed_event_contract,
        dup_txn_receipt):

    event_instance = indexed_event_contract.events.LogSingleWithIndex()

    with pytest.raises(AttributeError, match="Error flag must be one of: "):
        event_instance.processReceipt(dup_txn_receipt, errors='not-a-flag')


def test_receipt_processing_with_no_flag(
        web3,
        indexed_event_contract,
        dup_txn_receipt):

    event_instance = indexed_event_contract.events.LogSingleWithIndex()

    with pytest.warns(UserWarning, match='Expected 1 log topics.  Got 0'):
        returned_log = event_instance.processReceipt(dup_txn_receipt)
        assert len(returned_log) == 0


def test_single_log_processing_with_errors(
        web3,
        indexed_event_contract,
        dup_txn_receipt):
    event_instance = indexed_event_contract.events.LogSingleWithIndex()

    with pytest.raises(LogTopicError, match="Expected 1 log topics.  Got 0"):
        event_instance.processLog(dup_txn_receipt['logs'][0])
