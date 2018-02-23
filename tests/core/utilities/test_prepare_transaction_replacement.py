import pytest

from web3.utils.transactions import (
    prepare_replacement_transaction,
)

SIMPLE_CURRENT_TRANSACTION = {
    'blockHash': None,
    'hash': '0x0',
    'nonce': 2,
    'gasPrice': 10,
}


def test_prepare_transaction_replacement(web3):
    current_transaction = SIMPLE_CURRENT_TRANSACTION
    new_transaction = {
        'value': 1,
        'nonce': 2,
    }
    replacement_transaction = prepare_replacement_transaction(
        web3, current_transaction, new_transaction)

    assert replacement_transaction == {
        'value': 1,
        'nonce': 2,
        'gasPrice': 11,
    }


def test_prepare_transaction_replacement_without_nonce_sets_correct_nonce(web3):
    current_transaction = SIMPLE_CURRENT_TRANSACTION
    new_transaction = {
        'value': 1,
    }
    replacement_transaction = prepare_replacement_transaction(
        web3, current_transaction, new_transaction)
    assert replacement_transaction == {
        'value': 1,
        'nonce': 2,
        'gasPrice': 11,
    }


def test_prepare_transaction_replacement_already_mined_raises(web3):
    with pytest.raises(ValueError):
        prepare_replacement_transaction(
            web3, {'blockHash': '0xa1a1a1', 'hash': '0x0'}, {'value': 2})


def test_prepare_transaction_replacement_nonce_mismatch_raises(web3):
    with pytest.raises(ValueError):
        prepare_replacement_transaction(web3, {
            'blockHash': None,
            'hash': '0x0',
            'nonce': 1,
        }, {
            'nonce': 2,
        })


def test_prepare_transaction_replacement_not_higher_gas_price_raises(web3):
    current_transaction = SIMPLE_CURRENT_TRANSACTION
    new_transaction = {
        'value': 1,
        'gasPrice': 5,
    }
    with pytest.raises(ValueError):
        prepare_replacement_transaction(
            web3, current_transaction, new_transaction)

    # Also raises when equal to the current transaction
    new_transaction['gasPrice'] = 10
    with pytest.raises(ValueError):
        prepare_replacement_transaction(web3, current_transaction, new_transaction)


def test_prepare_transaction_replacement_gas_price_defaulting(web3):
    current_transaction = SIMPLE_CURRENT_TRANSACTION
    new_transaction = {
        'value': 2,
    }
    replacement_transaction = prepare_replacement_transaction(
        web3, current_transaction, new_transaction)

    assert replacement_transaction['gasPrice'] == 11


def test_prepare_transaction_replacement_gas_price_defaulting_when_strategy_higer(web3):

    def higher_gas_price_strategy(web3, txn):
        return 20

    web3.eth.setGasPriceStrategy(higher_gas_price_strategy)

    current_transaction = SIMPLE_CURRENT_TRANSACTION
    new_transaction = {
        'value': 2,
    }

    replacement_transaction = prepare_replacement_transaction(
        web3, current_transaction, new_transaction)

    assert replacement_transaction['gasPrice'] == 20


def test_prepare_transaction_replacement_gas_price_defaulting_when_strategy_lower(web3):

    def lower_gas_price_strategy(web3, txn):
        return 5

    web3.eth.setGasPriceStrategy(lower_gas_price_strategy)

    current_transaction = SIMPLE_CURRENT_TRANSACTION
    new_transaction = {
        'value': 2,
    }

    replacement_transaction = prepare_replacement_transaction(
        web3, current_transaction, new_transaction)

    assert replacement_transaction['gasPrice'] == 11
