def test_personal_signAndSendTransaction(web3, password_account,
                                         account_password,
                                         wait_for_transaction,
                                         empty_account):
    txn_hash = web3.personal.signAndSendTransaction({
        'from': password_account,
        'to': empty_account,
        'value': 1234,
    }, account_password)
    wait_for_transaction(web3, txn_hash)

    txn_receipt = web3.eth.getTransactionReceipt(txn_hash)
    assert txn_receipt['transactionHash'] == txn_hash
