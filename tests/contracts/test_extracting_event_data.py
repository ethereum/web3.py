import pytest

from web3.utils.events import (
    get_event_data,
)


@pytest.fixture()
def Emitter(web3_tester_empty, EMITTER):
    web3 = web3_tester_empty
    return web3.eth.contract(**EMITTER)


@pytest.fixture()
def emitter(web3_tester_empty, Emitter, wait_for_transaction, wait_for_block):
    web3 = web3_tester_empty

    wait_for_block(web3)
    deploy_txn_hash = Emitter.deploy({'from': web3.eth.coinbase, 'gas': 1000000})
    deploy_receipt = wait_for_transaction(web3, deploy_txn_hash)
    contract_address = deploy_receipt['contractAddress']

    code = web3.eth.getCode(contract_address)
    assert code == Emitter.code_runtime
    return Emitter(address=contract_address)


#def test_event_data_extraction_with_no_data(web3_tester_empty,
#                                            emitter,
#                                            wait_for_transaction,
#                                            emitter_log_topics,
#                                            emitter_event_ids):
#    web3 = web3_tester_empty
#
#    txn_hash = emitter.transact().logNoArgs(emitter_event_ids.LogNoArguments)
#    txn_receipt = wait_for_transaction(web3, txn_hash)
#
#    assert len(txn_receipt['logs']) == 1
#    log_entry = txn_receipt['logs'][0]
#
#    event_abi = emitter.find_matching_event_abi('LogNoArguments')
#
#    event_data = get_event_data(event_abi, log_entry)
#
#    assert event_data['args'] == {}
#    assert event_data['blockHash'] == txn_receipt['blockHash']
#    assert event_data['blockNumber'] == txn_receipt['blockNumber']
#    assert event_data['transactionIndex'] == txn_receipt['transactionIndex']
#    assert event_data['address'] == emitter.address
#    assert event_data['event'] == 'LogNoArguments'


@pytest.mark.parametrize(
    'contract_fn,event_name,call_args,expected_args',
    (
        ('logNoArgs', 'LogNoArguments', [], {}),
    )
)
def test_event_data_extraction(web3_tester_empty,
                               emitter,
                               wait_for_transaction,
                               emitter_log_topics,
                               emitter_event_ids,
                               contract_fn,
                               event_name,
                               call_args,
                               expected_args):
    web3 = web3_tester_empty

    transact_fn = getattr(emitter.transact(), contract_fn)
    event_id = getattr(emitter_event_ids, event_name)
    txn_hash = transact_fn(event_id, *call_args)
    txn_receipt = wait_for_transaction(web3, txn_hash)

    assert len(txn_receipt['logs']) == 1
    log_entry = txn_receipt['logs'][0]

    event_abi = emitter.find_matching_event_abi('LogNoArguments')

    event_data = get_event_data(event_abi, log_entry)

    assert event_data['args'] == expected_args
    assert event_data['blockHash'] == txn_receipt['blockHash']
    assert event_data['blockNumber'] == txn_receipt['blockNumber']
    assert event_data['transactionIndex'] == txn_receipt['transactionIndex']
    assert event_data['address'] == emitter.address
    assert event_data['event'] == 'LogNoArguments'
