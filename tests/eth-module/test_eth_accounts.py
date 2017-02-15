from eth_utils import (
    is_address,
)


def test_eth_accounts(web3):
    accounts = web3.eth.accounts
    assert len(accounts) >= 1
    assert all(is_address(addr) for addr in accounts)
