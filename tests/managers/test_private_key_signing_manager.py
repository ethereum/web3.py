import pytest

from web3.providers.manager import (
    PrivateKeySigningManager,
)
from web3.utils.address import to_address
from web3.utils.currency import denoms


@pytest.fixture()
def account_private_key():
    from eth_tester_client.utils import mk_random_privkey
    return mk_random_privkey()


@pytest.fixture()
def account_public_key(account_private_key):
    from ethereum.utils import privtoaddr
    from eth_tester_client.utils import encode_address
    return to_address(encode_address(privtoaddr(account_private_key)))


@pytest.fixture()
def web3_pk_signer(web3_ipc_persistent,
                   account_public_key,
                   account_private_key,
                   wait_for_block,
                   wait_for_transaction):
    pk_signing_manager = PrivateKeySigningManager(web3_ipc_persistent._requestManager)
    pk_signing_manager.register_private_key(account_private_key)
    assert account_public_key in pk_signing_manager.keys

    wait_for_block(web3_ipc_persistent)

    fund_txn_hash = web3_ipc_persistent.eth.sendTransaction({
        'from': web3_ipc_persistent.eth.coinbase,
        'to': account_public_key,
        'value': 10 * denoms.ether,
    })
    wait_for_transaction(web3_ipc_persistent, fund_txn_hash)

    with pytest.raises(ValueError):
        web3_ipc_persistent.eth.sendTransaction({
            'from': account_public_key,
            'to': web3_ipc_persistent.eth.coinbase,
            'value': 1,
        })

    web3_ipc_persistent._requestManager = pk_signing_manager
    return web3_ipc_persistent


def test_private_key_signing_manager(web3_pk_signer, account_public_key, wait_for_transaction):
    assert account_public_key not in web3_pk_signer.eth.accounts
    txn_hash = web3_pk_signer.eth.sendTransaction({
        'from': account_public_key,
        'to': web3_pk_signer.eth.coinbase,
        'value': 12345,
    })
    txn_receipt = wait_for_transaction(web3_pk_signer, txn_hash)
    txn = web3_pk_signer.eth.getTransaction(txn_hash)

    assert txn['from'] == account_public_key
