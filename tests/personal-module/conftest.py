import pytest

from testrpc.client.utils import (
    mk_random_privkey,
)

from eth_utils import (
    force_bytes,
    is_same_address,
    to_normalized_address,
)


@pytest.fixture()
def account_password():
    return "a-password"


@pytest.fixture()
def account_private_key():
    return mk_random_privkey()


@pytest.fixture()
def account_public_key(account_private_key):
    from ethereum.utils import privtoaddr
    return to_normalized_address(privtoaddr(account_private_key))


@pytest.fixture()
def password_account(web3,
                     account_password,
                     account_private_key,
                     account_public_key,
                     wait_for_transaction):
    address = web3.personal.importRawKey(account_private_key, account_password)

    # sanity check
    assert is_same_address(address, account_public_key)

    initial_balance = 1000000000000000000000  # 1,000 ether

    funding_txn_hash = web3.personal.signAndSendTransaction({
        'from': web3.eth.coinbase,
        'to': address,
        'value': initial_balance,
    }, 'this-is-not-a-secure-password')
    wait_for_transaction(web3, funding_txn_hash)

    assert web3.eth.getBalance(address) == initial_balance
    return address


@pytest.fixture()
def empty_account(web3):
    address = web3.personal.importRawKey(mk_random_privkey(), "a-password")

    assert web3.eth.getBalance(address) == 0
    return address
