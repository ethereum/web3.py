import pytest


def test_personal_listAccounts(web3):
    accounts = web3.personal.listAccounts
    assert accounts == web3.eth.accounts


def test_personal_newAccount(web3):
    assert False
