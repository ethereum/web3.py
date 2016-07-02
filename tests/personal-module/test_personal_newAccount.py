def test_personal_newAccount(web3):
    initial_accounts = web3.personal.listAccounts

    new_account = web3.personal.newAccount('a-password')

    assert new_account not in initial_accounts

    assert new_account in web3.personal.listAccounts
