import pytest


@pytest.fixture(autouse=True)
def wait_for_first_block(w3, wait_for_block):
    wait_for_block(w3)


def test_uses_default_account_when_set(w3, extra_accounts, wait_for_transaction):
    w3.eth.default_account = extra_accounts[2]
    assert w3.eth.default_account == extra_accounts[2]

    txn_hash = w3.eth.send_transaction(
        {
            "to": extra_accounts[1],
            "value": 1234,
        }
    )

    wait_for_transaction(w3, txn_hash)

    txn = w3.eth.get_transaction(txn_hash)
    assert txn["from"] == extra_accounts[2]


def test_uses_given_from_address_when_provided(
    w3, extra_accounts, wait_for_transaction
):
    w3.eth.default_account = extra_accounts[2]
    txn_hash = w3.eth.send_transaction(
        {
            "from": extra_accounts[5],
            "to": extra_accounts[1],
            "value": 1234,
        }
    )

    wait_for_transaction(w3, txn_hash)

    txn = w3.eth.get_transaction(txn_hash)
    assert txn["from"] == extra_accounts[5]
