import pytest


def test_personal_listAccounts(web3):
    with pytest.raises(ValueError):
        # this method is not implemented in the `eth-testrpc` server
        accounts = web3.personal.listAccounts
        assert accounts == web3.eth.accounts
        raise ValueError("it worked")
