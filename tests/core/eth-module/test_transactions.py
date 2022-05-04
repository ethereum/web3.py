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
    'transaction',
    (
        {
            'gasPrice': 10 ** 9,
            'accessList': (
                {
                    'address': '0xd3CdA913deB6f67967B99D67aCDFa1712C293601',
                    'storageKeys': (
                        '0x0000000000000000000000000000000000000000000000000000000000000003',
                        '0x0000000000000000000000000000000000000000000000000000000000000007',
                    )
                },
                {
                    'address': '0xbb9bc244d798123fde783fcc1c72d3bb8c189413',
                    'storageKeys': ()
                },
            ),
        },
        {
            'maxFeePerGas': 10 ** 9,
            'maxPriorityFeePerGas': 10 ** 9,
            'accessList': (
                {
                    'address': '0xd3CdA913deB6f67967B99D67aCDFa1712C293601',
                    'storageKeys': (
                        '0x0000000000000000000000000000000000000000000000000000000000000003',
                        '0x0000000000000000000000000000000000000000000000000000000000000007',
                    )
                },
                {
                    'address': '0xbb9bc244d798123fde783fcc1c72d3bb8c189413',
                    'storageKeys': ()
                },
            ),
        },
    ),
    ids=[
        'storage_keys_access_list_txn',
        'storage_keys_dynamic_fee_txn',
    ],
)
def test_eth_tester_send_transaction_validation(w3, transaction):
    # Test that eth-tester transaction param validation does not throw for properly formatted
    # transactions. This is especially important because we have key mapping differences
    # (camelCase to snake_case) mitigated by providers/eth-tester/middleware.
    txn_hash = w3.eth.send_transaction(transaction)
    receipt = w3.eth.wait_for_transaction_receipt(txn_hash, timeout=RECEIPT_TIMEOUT)
    assert receipt.get('blockNumber') is not None


@pytest.mark.parametrize(
    'make_chain_id, expect_success',
    (
        (
            lambda w3: w3.eth.chain_id,
            True,
        ),
        pytest.param(
            lambda w3: 999999999999,
            False,
        ),
    ),
)
def test_send_transaction_with_valid_chain_id(w3, make_chain_id, expect_success):
    transaction = {
        'to': w3.eth.accounts[1],
        'chainId': make_chain_id(w3),
    }
    if expect_success:
        txn_hash = w3.eth.send_transaction(transaction)
        receipt = w3.eth.wait_for_transaction_receipt(txn_hash, timeout=RECEIPT_TIMEOUT)
        assert receipt.get('blockNumber') is not None
    else:
        with pytest.raises(ValidationError) as exc_info:
            w3.eth.send_transaction(transaction)

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
def test_send_transaction_with_invalid_ens_names(w3, to, _from):
    with ens_addresses(w3, [
        ('registered-name-1.eth', w3.eth.accounts[1]),
    ]):
        transaction = {
            'to': to,
            'chainId': w3.eth.chain_id,
            'from': _from,
        }

        with pytest.raises(NameNotFound):
            w3.eth.send_transaction(transaction)


def test_send_transaction_with_ens_names(w3):
    with ens_addresses(w3, [
        ('registered-name-1.eth', w3.eth.accounts[1]),
        ('registered-name-2.eth', w3.eth.accounts[0])
    ]):
        transaction = {
            'to': 'registered-name-1.eth',
            'chainId': w3.eth.chain_id,
            'from': 'registered-name-2.eth',
        }

        txn_hash = w3.eth.send_transaction(transaction)
        receipt = w3.eth.wait_for_transaction_receipt(txn_hash, timeout=RECEIPT_TIMEOUT)
        assert receipt.get('blockNumber') is not None


def test_wait_for_missing_receipt(w3):
    with pytest.raises(TimeExhausted):
        w3.eth.wait_for_transaction_receipt(b'\0' * 32, timeout=RECEIPT_TIMEOUT)


def test_passing_string_to_to_hex(w3):
    with pytest.raises(TimeExhausted):
        transaction_hash = '0x5c504ed432cb51138bcf09aa5e8a410dd4a1e204ef84bfed1be16dfba1b22060'
        w3.eth.wait_for_transaction_receipt(transaction_hash, timeout=RECEIPT_TIMEOUT)


def test_unmined_transaction_wait_for_receipt(w3):
    w3.middleware_onion.add(unmined_receipt_simulator_middleware)
    txn_hash = w3.eth.send_transaction({
        'from': w3.eth.coinbase,
        'to': '0xd3CdA913deB6f67967B99D67aCDFa1712C293601',
        'value': 123457
    })
    with pytest.raises(TransactionNotFound):
        w3.eth.get_transaction_receipt(txn_hash)

    txn_receipt = w3.eth.wait_for_transaction_receipt(txn_hash)
    assert txn_receipt['transactionHash'] == txn_hash
    assert txn_receipt['blockHash'] is not None
