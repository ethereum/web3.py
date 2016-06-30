import pytest


@pytest.fixture
def account_password():
    return "this-is-not-a-secure-password"


@pytest.fixture
def extra_accounts(web3, account_password):
    num_accounts_to_create = 10 - len(web3.eth.accounts)

    for i in range(num_accounts_to_create):
        web3.personal.newAccount(account_password)

    return web3.eth.accounts
