import pytest


@pytest.fixture(autouse=True)
def wait_for_first_block(w3, wait_for_block):
    wait_for_block(w3)


def test_uses_default_account_when_set(w3, wait_for_transaction):
    current_default = w3.eth.default_account

    w3.eth.default_account = None
    assert w3.eth.default_account is None

    w3.eth.default_account = w3.eth.accounts[3]
    assert w3.eth.default_account == w3.eth.accounts[3]

    txn_hash = w3.eth.send_transaction(
        {
            "to": w3.eth.accounts[3],
            "value": 1234,
        }
    )

    wait_for_transaction(w3, txn_hash)

    txn = w3.eth.get_transaction(txn_hash)
    assert txn["from"] == w3.eth.accounts[3]

    w3.eth.default_account = current_default


def test_uses_given_from_address_when_provided(w3, wait_for_transaction):
    w3.eth.default_account = w3.eth.accounts[3]
    txn_hash = w3.eth.send_transaction(
        {
            "from": w3.eth.accounts[5],
            "to": w3.eth.accounts[1],
            "value": 1234,
        }
    )

    wait_for_transaction(w3, txn_hash)

    txn = w3.eth.get_transaction(txn_hash)
    assert txn["from"] == w3.eth.accounts[5]
