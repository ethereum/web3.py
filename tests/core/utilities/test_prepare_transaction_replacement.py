import pytest

from web3._utils.transactions import (
    prepare_replacement_transaction,
)
from web3.exceptions import (
    Web3ValueError,
)

SIMPLE_CURRENT_TRANSACTION = {
    "blockHash": None,
    "hash": "0x0",
    "nonce": 2,
    "gasPrice": 10,
}


def test_prepare_transaction_replacement(w3):
    current_transaction = SIMPLE_CURRENT_TRANSACTION
    new_transaction = {
        "value": 1,
        "nonce": 2,
    }
    replacement_transaction = prepare_replacement_transaction(
        w3, current_transaction, new_transaction
    )

    assert replacement_transaction == {
        "value": 1,
        "nonce": 2,
        "gasPrice": 12,
    }


def test_prepare_transaction_replacement_without_nonce_sets_correct_nonce(w3):
    current_transaction = SIMPLE_CURRENT_TRANSACTION
    new_transaction = {
        "value": 1,
    }
    replacement_transaction = prepare_replacement_transaction(
        w3, current_transaction, new_transaction
    )
    assert replacement_transaction == {
        "value": 1,
        "nonce": 2,
        "gasPrice": 12,
    }


def test_prepare_transaction_replacement_already_mined_raises(w3):
    with pytest.raises(Web3ValueError):
        prepare_replacement_transaction(
            w3, {"blockHash": "0xa1a1a1", "hash": "0x0"}, {"value": 2}
        )


def test_prepare_transaction_replacement_nonce_mismatch_raises(w3):
    with pytest.raises(Web3ValueError):
        prepare_replacement_transaction(
            w3,
            {
                "blockHash": None,
                "hash": "0x0",
                "nonce": 1,
            },
            {
                "nonce": 2,
            },
        )


def test_prepare_transaction_replacement_not_higher_gas_price_raises(w3):
    current_transaction = SIMPLE_CURRENT_TRANSACTION
    new_transaction = {
        "value": 1,
        "gasPrice": 5,
    }
    with pytest.raises(Web3ValueError):
        prepare_replacement_transaction(w3, current_transaction, new_transaction)

    # Also raises when equal to the current transaction
    new_transaction["gasPrice"] = 10
    with pytest.raises(Web3ValueError):
        prepare_replacement_transaction(w3, current_transaction, new_transaction)


def test_prepare_transaction_replacement_gas_price_defaulting(w3):
    current_transaction = SIMPLE_CURRENT_TRANSACTION
    new_transaction = {
        "value": 2,
    }
    replacement_transaction = prepare_replacement_transaction(
        w3, current_transaction, new_transaction
    )

    assert replacement_transaction["gasPrice"] == 12


def test_prepare_transaction_replacement_gas_price_defaulting_when_strategy_higher(w3):
    def higher_gas_price_strategy(w3, txn):
        return 20

    w3.eth.set_gas_price_strategy(higher_gas_price_strategy)

    current_transaction = SIMPLE_CURRENT_TRANSACTION
    new_transaction = {
        "value": 2,
    }

    replacement_transaction = prepare_replacement_transaction(
        w3, current_transaction, new_transaction
    )

    assert replacement_transaction["gasPrice"] == 20


def test_prepare_transaction_replacement_gas_price_defaulting_when_strategy_lower(w3):
    def lower_gas_price_strategy(w3, txn):
        return 5

    w3.eth.set_gas_price_strategy(lower_gas_price_strategy)

    current_transaction = SIMPLE_CURRENT_TRANSACTION
    new_transaction = {
        "value": 2,
    }

    replacement_transaction = prepare_replacement_transaction(
        w3, current_transaction, new_transaction
    )

    assert replacement_transaction["gasPrice"] == 12
