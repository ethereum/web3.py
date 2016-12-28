import pytest


def test_personal_lockAccount(web3, password_account, account_password,
                              wait_for_transaction, empty_account):
    initial_balancee = web3.eth.getBalance(empty_account)

    assert web3.personal.unlockAccount(password_account, account_password) is True
    txn_hash = web3.eth.sendTransaction({
        'from': password_account,
        'to': empty_account,
        'value': 1234,
    })
    wait_for_transaction(web3, txn_hash)

    after_balance = web3.eth.getBalance(empty_account)

    assert after_balance - initial_balancee == 1234

    web3.personal.lockAccount(password_account)

    with pytest.raises(ValueError):
        txn_hash = web3.eth.sendTransaction({
            'from': password_account,
            'to': empty_account,
            'value': 1234,
        })

    assert after_balance - initial_balancee == 1234
