import pytest

import sys


@pytest.fixture(autouse=True)
def wait_for_first_block(web3, wait_for_block):
    wait_for_block(web3)


def test_uses_defaultAccount_when_set(web3, extra_accounts,
                                      wait_for_transaction):
    web3.eth.defaultAccount = extra_accounts[2]

    txn_hash = web3.eth.sendTransaction({
        "to": extra_accounts[1],
        "value": 1234,
    })

    wait_for_transaction(web3, txn_hash)

    txn = web3.eth.getTransaction(txn_hash)
    assert txn['from'] == extra_accounts[2]


@pytest.mark.skipif(sys.version_info.major == 2, reason="Doesn't seem to work on py27")
def test_raises_warning_and_defaults_to_coinbase_when_not_set(web3, extra_accounts,
                                                              wait_for_transaction):
    with pytest.warns(DeprecationWarning):
        txn_hash = web3.eth.sendTransaction({
            "to": extra_accounts[1],
            "value": 1234,
        })

    wait_for_transaction(web3, txn_hash)

    txn = web3.eth.getTransaction(txn_hash)
    assert txn['from'] == web3.eth.coinbase


def test_uses_given_from_address_when_provided(web3, extra_accounts,
                                               wait_for_transaction):
    web3.eth.defaultAccount = extra_accounts[2]
    txn_hash = web3.eth.sendTransaction({
        "from": extra_accounts[5],
        "to": extra_accounts[1],
        "value": 1234,
    })

    wait_for_transaction(web3, txn_hash)

    txn = web3.eth.getTransaction(txn_hash)
    assert txn['from'] == extra_accounts[5]
