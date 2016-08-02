import pytest


reset_chain = True


@pytest.fixture()
def account_password():
    return "a-password"


@pytest.fixture()
def account_private_key():
    from eth_tester_client.utils import mk_random_privkey, force_bytes
    return mk_random_privkey()


@pytest.fixture()
def account_public_key(account_private_key):
    from ethereum.utils import privtoaddr
    from eth_tester_client.utils import encode_address
    return encode_address(privtoaddr(account_private_key))


@pytest.fixture()
def password_account(web3, account_password,
                     account_private_key, account_public_key,
                     wait_for_transaction):
    from eth_tester_client.utils import normalize_address
    address = web3.personal.importRawKey(account_private_key, account_password)

    # sanity check
    assert normalize_address(address) == normalize_address(account_public_key)

    initial_balance = 1000000000000000000000  # 1,000 ether

    funding_txn_hash = web3.personal.signAndSendTransaction({
        'from': web3.eth.coinbase,
        'to': address,
        'value': initial_balance,
    }, 'this-is-not-a-secure-password')
    wait_for_transaction(funding_txn_hash)

    assert web3.eth.getBalance(address) == initial_balance
    return address
