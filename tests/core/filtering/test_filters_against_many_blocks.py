import pytest
import random

from eth_utils import (
    to_tuple,
)


@to_tuple
def deploy_contracts(web3, contract, wait_for_transaction):
    for i in range(25):
        tx_hash = contract.constructor().transact()
        wait_for_transaction(web3, tx_hash)
        yield web3.eth.getTransactionReceipt(tx_hash)['contractAddress']


def pad_with_transactions(w3):
    accounts = w3.eth.accounts
    for tx_count in range(random.randint(0, 10)):
        _from = accounts[random.randint(0, len(accounts) - 1)]
        _to = accounts[random.randint(0, len(accounts) - 1)]
        value = 50 + tx_count
        w3.eth.sendTransaction({'from': _from, 'to': _to, 'value': value})


def single_transaction(w3):
    accounts = w3.eth.accounts
    _from = accounts[random.randint(0, len(accounts) - 1)]
    _to = accounts[random.randint(0, len(accounts) - 1)]
    value = 50
    tx_hash = w3.eth.sendTransaction({'from': _from, 'to': _to, 'value': value})
    return tx_hash


def test_event_filter_new_events(
        web3,
        emitter,
        Emitter,
        wait_for_transaction,
        emitter_event_ids,
        create_filter):

    matching_transact = emitter.functions.logNoArgs(
        which=1).transact
    non_matching_transact = emitter.functions.logNoArgs(
        which=0).transact

    event_filter = emitter.events.LogNoArguments().createFilter(fromBlock='latest')

    expected_match_counter = 0

    while web3.eth.blockNumber < 50:
        is_match = bool(random.randint(0, 1))
        if is_match:
            expected_match_counter += 1
            matching_transact()
            pad_with_transactions(web3)
            continue
        non_matching_transact()
        pad_with_transactions(web3)

    assert len(event_filter.get_new_entries()) == expected_match_counter


@pytest.mark.xfail(reason="Suspected eth-tester bug")
def test_block_filter(web3):
    block_filter = web3.eth.filter("latest")

    while web3.eth.blockNumber < 50:
        pad_with_transactions(web3)

    assert len(block_filter.get_new_entries()) == web3.eth.blockNumber


def test_transaction_filter_with_mining(
        web3):

    transaction_filter = web3.eth.filter("pending")

    transaction_counter = 0

    while transaction_counter < 100:
        single_transaction(web3)
        transaction_counter += 1

    assert len(transaction_filter.get_new_entries()) == transaction_counter


@pytest.mark.xfail(reason="Suspected eth-tester bug")
def test_transaction_filter_without_mining(
        web3):

    web3.providers[0].ethereum_tester.auto_mine_transactions = False
    transaction_filter = web3.eth.filter("pending")

    transaction_counter = 0

    transact_once = single_transaction(web3)
    while transaction_counter < 100:
        next(transact_once)
        transaction_counter += 1

    assert len(transaction_filter.get_new_entries()) == transaction_counter


def test_event_filter_new_events_many_deployed_contracts(
        web3,
        emitter,
        Emitter,
        wait_for_transaction,
        emitter_event_ids,
        create_filter):

    matching_transact = emitter.functions.logNoArgs(
        which=1).transact

    deployed_contract_addresses = deploy_contracts(web3, Emitter, wait_for_transaction)

    def gen_non_matching_transact():
        while True:
            contract_address = deployed_contract_addresses[
                random.randint(0, len(deployed_contract_addresses) - 1)]
            yield web3.eth.contract(
                address=contract_address, abi=Emitter.abi).functions.logNoArgs(which=1).transact

    non_matching_transact = gen_non_matching_transact()

    event_filter = emitter.events.LogNoArguments().createFilter(fromBlock='latest')

    expected_match_counter = 0

    while web3.eth.blockNumber < 50:
        is_match = bool(random.randint(0, 1))
        if is_match:
            expected_match_counter += 1
            matching_transact()
            pad_with_transactions(web3)
            continue
        next(non_matching_transact)()
        pad_with_transactions(web3)

    assert len(event_filter.get_new_entries()) == expected_match_counter
