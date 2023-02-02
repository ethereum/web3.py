import pytest


@pytest.fixture
def account_password():
    return "this-is-not-a-secure-password"


@pytest.fixture
def extra_accounts(w3, account_password):
    num_accounts_to_create = 10 - len(w3.eth.accounts)

    for i in range(num_accounts_to_create):
        w3.personal.new_account(account_password)

    return w3.eth.accounts
