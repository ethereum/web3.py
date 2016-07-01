import pytest

from eth_tester_client.utils import normalize_address


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
            'from': password_account,
            'to': web3.eth.coinbase,
            'value': 1234,
        })

    assert web3.eth.getBalance(web3.eth.coinbase) == initial_balancee

    assert web3.personal.unlockAccount(password_account, account_password, 30) is True
    txn_hash = web3.eth.sendTransaction({
        'from': password_account,
        'to': web3.eth.coinbase,
        'value': 1234,
    })
    wait_for_transaction(txn_hash)

    after_balance = web3.eth.getBalance(web3.eth.coinbase)

    assert after_balance - initial_balancee == 1234


def test_personal_lockAccount(web3, password_account, account_password,
                              wait_for_transaction):
    initial_balancee = web3.eth.getBalance(web3.eth.coinbase)

    assert web3.personal.unlockAccount(password_account, account_password) is True
    txn_hash = web3.eth.sendTransaction({
        'from': password_account,
        'to': web3.eth.coinbase,
        'value': 1234,
    })
    wait_for_transaction(txn_hash)

    after_balance = web3.eth.getBalance(web3.eth.coinbase)

    assert after_balance - initial_balancee == 1234

    web3.personal.lockAccount(password_account)

    with pytest.raises(ValueError):
        txn_hash = web3.eth.sendTransaction({
            'from': password_account,
            'to': web3.eth.coinbase,
            'value': 1234,
        })

    assert after_balance - initial_balancee == 1234


def test_personal_importRawKey(web3, account_private_key, account_password,
                               account_public_key):
    address = web3.personal.importRawKey(account_private_key, account_password)

    # sanity check
    assert normalize_address(address) == normalize_address(account_public_key)

    assert web3.personal.unlockAccount(address, account_password) is True


def test_personal_sendAndSignTransaction(web3, password_account,
                                         account_password,
                                         wait_for_transaction):
    txn_hash = web3.eth.sendTransaction({
        'from': password_account,
        'to': web3.eth.coinbase,
        'value': 1234,
    }, account_password)
    wait_for_transaction(txn_hash)

    txn_receipt = web3.eth.getTransactionReceipt(txn_hash)
    assert txn_receipt['transactionHash'] == txn_hash
