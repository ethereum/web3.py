import pytest


@pytest.fixture(autouse=True)
def wait_for_first_block(web3, wait_for_block):
    wait_for_block(web3)


def test_personal_unlockAccount(web3, password_account, account_password,
                                wait_for_transaction, empty_account):
    initial_balancee = web3.eth.getBalance(empty_account)

    with pytest.raises(ValueError):
        web3.eth.sendTransaction({
            'from': password_account,
            'to': empty_account,
            'value': 1234,
        })

    assert web3.eth.getBalance(empty_account) == initial_balancee

    assert web3.personal.unlockAccount(password_account, account_password, 30) is True
    txn_hash = web3.eth.sendTransaction({
        'from': password_account,
        'to': empty_account,
        'value': 1234,
    })
    wait_for_transaction(web3, txn_hash)

    after_balance = web3.eth.getBalance(empty_account)

    assert after_balance - initial_balancee == 1234
