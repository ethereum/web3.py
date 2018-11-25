import pytest

from web3.exceptions import (
    TimeExhausted,
    ValidationError,
)
from web3.middleware.simulate_unmined_transaction import (
    unmined_receipt_simulator_middleware,
)

RECEIPT_TIMEOUT = 0.2
RECEIPT_POLL_LATENCY = 0.1


@pytest.mark.parametrize("timeout", [0.2, 120])
@pytest.mark.parametrize("poll_latency", [0.1, 0.3, 110, 120, 130])
@pytest.mark.parametrize(
    'make_chain_id, expect_success',
    (
        (
            lambda web3: web3.net.chainId,
            True,
        ),
        pytest.param(
            lambda web3: 999999999999,
            False,
            marks=pytest.mark.xfail,
        ),
    ),
)
def test_send_transaction_with_valid_chain_id(
        web3, make_chain_id, expect_success, timeout, poll_latency):
    transaction = {
        'to': web3.eth.accounts[1],
        'chainId': make_chain_id(web3),
    }
    if expect_success:
        txn_hash = web3.eth.sendTransaction(transaction)
        receipt = web3.eth.waitForTransactionReceipt(txn_hash, timeout, poll_latency)
        assert receipt.get('blockNumber') is not None
    else:
        with pytest.raises(ValidationError) as exc_info:
            web3.eth.sendTransaction(transaction)

        assert 'chain ID' in str(exc_info.value)


@pytest.mark.parametrize("timeout", [0.2])
@pytest.mark.parametrize("poll_latency", [0.1, 0.3])
def test_wait_for_missing_receipt(web3, timeout, poll_latency):
    with pytest.raises(TimeExhausted):
        web3.eth.waitForTransactionReceipt(b'\0' * 32, timeout, poll_latency)


def test_unmined_transaction_wait_for_receipt(web3):
    web3.middleware_stack.add(unmined_receipt_simulator_middleware)
    txn_hash = web3.eth.sendTransaction({
        'from': web3.eth.coinbase,
        'to': '0xd3CdA913deB6f67967B99D67aCDFa1712C293601',
        'value': 123457
    })
    assert web3.eth.getTransactionReceipt(txn_hash) is None

    txn_receipt = web3.eth.waitForTransactionReceipt(txn_hash)
    assert txn_receipt['transactionHash'] == txn_hash
    assert txn_receipt['blockHash'] is not None
