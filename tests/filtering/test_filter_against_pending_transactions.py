import random
from flaky import flaky

from web3.utils.compat import (
    Timeout,
)


@flaky(max_runs=3)
def test_filter_against_pending_transactions(web3_empty,
                                             wait_for_transaction,
                                             skip_if_testrpc):
    web3 = web3_empty
    skip_if_testrpc(web3)

    seen_txns = []
    txn_filter = web3.eth.filter("pending")
    txn_filter.watch(seen_txns.append)

    txn_1_hash = web3.eth.sendTransaction({
        'from': web3.eth.coinbase,
        'to': '0xd3cda913deb6f67967b99d67acdfa1712c293601',
        'value': 12345,
    })
    txn_2_hash = web3.eth.sendTransaction({
        'from': web3.eth.coinbase,
        'to': '0xd3cda913deb6f67967b99d67acdfa1712c293601',
        'value': 54321,
    })

    wait_for_transaction(web3, txn_1_hash)
    wait_for_transaction(web3, txn_2_hash)

    with Timeout(5) as timeout:
        while not seen_txns:
            timeout.sleep(random.random())

    txn_filter.stop_watching(30)

    assert txn_1_hash in seen_txns
    assert txn_2_hash in seen_txns
