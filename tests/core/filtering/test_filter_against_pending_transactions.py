import pytest
import random

from flaky import (
    flaky,
)

from web3._utils.threads import (
    Timeout,
)


@pytest.mark.skip(reason="fixture 'w3_empty' not found")
@flaky(max_runs=3)
def test_sync_filter_against_pending_transactions(w3_empty,
                                                  wait_for_transaction,
                                                  skip_if_testrpc
                                                  ):
    w3 = w3_empty
    skip_if_testrpc(w3)

    txn_filter = w3.eth.filter("pending")

    txn_1_hash = w3.eth.send_transaction({
        'from': w3.eth.coinbase,
        'to': '0xd3CdA913deB6f67967B99D67aCDFa1712C293601',
        'value': 12345,
    })
    txn_2_hash = w3.eth.send_transaction({
        'from': w3.eth.coinbase,
        'to': '0xd3CdA913deB6f67967B99D67aCDFa1712C293601',
        'value': 54321,
    })

    wait_for_transaction(w3, txn_1_hash)
    wait_for_transaction(w3, txn_2_hash)

    with Timeout(5) as timeout:
        while not txn_filter.get_new_entries():
            timeout.sleep(random.random())

    seen_txns = txn_filter.get_new_entries()

    assert txn_1_hash in seen_txns
    assert txn_2_hash in seen_txns


@pytest.mark.skip(reason="fixture 'w3_empty' not found")
@flaky(max_runs=3)
def test_async_filter_against_pending_transactions(w3_empty,
                                                   wait_for_transaction,
                                                   skip_if_testrpc
                                                   ):
    w3 = w3_empty
    skip_if_testrpc(w3)

    seen_txns = []
    txn_filter = w3.eth.filter("pending")
    txn_filter.watch(seen_txns.append)

    txn_1_hash = w3.eth.send_transaction({
        'from': w3.eth.coinbase,
        'to': '0xd3CdA913deB6f67967B99D67aCDFa1712C293601',
        'value': 12345,
    })
    txn_2_hash = w3.eth.send_transaction({
        'from': w3.eth.coinbase,
        'to': '0xd3CdA913deB6f67967B99D67aCDFa1712C293601',
        'value': 54321,
    })

    wait_for_transaction(w3, txn_1_hash)
    wait_for_transaction(w3, txn_2_hash)

    with Timeout(5) as timeout:
        while not seen_txns:
            timeout.sleep(random.random())

    txn_filter.stop_watching(30)

    assert txn_1_hash in seen_txns
    assert txn_2_hash in seen_txns
