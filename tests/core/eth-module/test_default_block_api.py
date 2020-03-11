import pytest


@pytest.fixture(autouse=True)
def wait_for_first_block(web3, wait_for_block):
    wait_for_block(web3)


def test_uses_default_block(web3, extra_accounts,
                            wait_for_transaction):
    assert(web3.eth.default_block == 'latest')
    web3.eth.default_block = web3.eth.block_number
    assert(web3.eth.default_block == web3.eth.block_number)


def test_uses_defaultBlock(web3, extra_accounts,
                                         wait_for_transaction):
    with pytest.warns(DeprecationWarning):
        assert(web3.eth.defaultBlock == 'latest')

    with pytest.warns(DeprecationWarning):
        web3.eth.defaultBlock = web3.eth.block_number

    with pytest.warns(DeprecationWarning):
        assert(web3.eth.defaultBlock == web3.eth.block_number)
