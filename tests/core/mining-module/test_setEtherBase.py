import pytest


def test_miner_set_etherbase(web3_empty):
    web3 = web3_empty
    assert web3.eth.coinbase == web3.eth.accounts[0]
    new_account = web3.personal.newAccount('this-is-a-password')
    web3.geth.miner.set_etherbase(new_account)
    assert web3.eth.coinbase == new_account


def test_miner_setEtherbase(web3_empty):
    web3 = web3_empty
    assert web3.eth.coinbase == web3.eth.accounts[0]
    new_account = web3.personal.newAccount('this-is-a-password')
    with pytest.warns(DeprecationWarning):
        web3.geth.miner.setEtherbase(new_account)
    assert web3.eth.coinbase == new_account
