import pytest

from web3._utils.ens import (
    ens_addresses,
)
from web3.exceptions import (
    NameNotFound,
    TimeExhausted,
    TransactionNotFound,
    ValidationError,
)
from web3.middleware.simulate_unmined_transaction import (
    unmined_receipt_simulator_middleware,
)

RECEIPT_TIMEOUT = 0.2


@pytest.mark.parametrize(
    'make_chain_id, expect_success',
    (
        (
            lambda web3: web3.eth.chainId,
            True,
        ),
        pytest.param(
            lambda web3: 999999999999,
            False,
        ),
    ),
)
def test_send_transaction_with_valid_chain_id(web3, make_chain_id, expect_success):
    transaction = {
        'to': web3.eth.accounts[1],
        'chainId': make_chain_id(web3),
    }
    if expect_success:
        txn_hash = web3.eth.sendTransaction(transaction)
        receipt = web3.eth.waitForTransactionReceipt(txn_hash, timeout=RECEIPT_TIMEOUT)
        assert receipt.get('blockNumber') is not None
    else:
        with pytest.raises(ValidationError) as exc_info:
            web3.eth.sendTransaction(transaction)

        assert 'chain ID' in str(exc_info.value)


@pytest.mark.parametrize(
    'to, _from',
    (
        (
            'registered-name-1.eth',
            'not-a-registered-name.eth',
        ),
        (
            'not-a-registered-name.eth',
            'registered-name-1.eth',
        ),
    )
)
def test_send_transaction_with_invalid_ens_names(web3, to, _from):
    with ens_addresses(web3, [
        ('registered-name-1.eth', web3.eth.accounts[1]),
    ]):
        transaction = {
            'to': to,
            'chainId': web3.eth.chainId,
            'from': _from,
        }

        with pytest.raises(NameNotFound):
            web3.eth.sendTransaction(transaction)


def test_send_transaction_with_ens_names(web3):
    with ens_addresses(web3, [
        ('registered-name-1.eth', web3.eth.accounts[1]),
        ('registered-name-2.eth', web3.eth.accounts[0])
    ]):
        transaction = {
            'to': 'registered-name-1.eth',
            'chainId': web3.eth.chainId,
            'from': 'registered-name-2.eth',
        }

        txn_hash = web3.eth.sendTransaction(transaction)
        receipt = web3.eth.waitForTransactionReceipt(txn_hash, timeout=RECEIPT_TIMEOUT)
        assert receipt.get('blockNumber') is not None


def test_wait_for_missing_receipt(web3):
    with pytest.raises(TimeExhausted):
        web3.eth.waitForTransactionReceipt(b'\0' * 32, timeout=RECEIPT_TIMEOUT)


def test_unmined_transaction_wait_for_receipt(web3):
    web3.middleware_onion.add(unmined_receipt_simulator_middleware)
    txn_hash = web3.eth.sendTransaction({
        'from': web3.eth.coinbase,
        'to': '0xd3CdA913deB6f67967B99D67aCDFa1712C293601',
        'value': 123457
    })
    with pytest.raises(TransactionNotFound):
        web3.eth.getTransactionReceipt(txn_hash)

    txn_receipt = web3.eth.waitForTransactionReceipt(txn_hash)
    assert txn_receipt['transactionHash'] == txn_hash
    assert txn_receipt['blockHash'] is not None
