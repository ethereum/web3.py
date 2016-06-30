import pytest


def test_personal_listAccounts(web3):
    accounts = web3.personal.listAccounts
    assert accounts == web3.eth.accounts


def test_personal_newAccount(web3):
    initial_accounts = web3.personal.listAccounts

    new_account = web3.personal.newAccount('a-password')

    assert new_account not in initial_accounts

    assert new_account in web3.personal.listAccounts


def test_personal_unlockAccount(web3, password_account, account_password,
                                wait_for_transaction):
    initial_balancee = web3.eth.getBalance(web3.eth.coinbase)

    with pytest.raises(ValueError):
        web3.eth.sendTransaction({
            'from': address,
            'to': web3.eth.coinbase,
            'value': 1234,
        })

    assert web3.eth.getBalance(web3.eth.coinbase) == initial_balancee

    assert web3.personal.unlockAccount(password_account, account_password, 30) is True
    txn_hash = web3.eth.sendTransaction({
        'from': address,
        'to': web3.eth.coinbase,
        'value': 1234,
    })
    wait_for_transaction(txn_hash)

    after_balance = web3.eth.getBalance(web3.eth.coinbase)

    assert after_balance - initial_balancee == 1234
