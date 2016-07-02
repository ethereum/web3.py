def test_personal_signAndSendTransaction(web3, password_account,
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
