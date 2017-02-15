import pytest

from eth_utils import (
    denoms,
    to_normalized_address,
    decode_hex,
)

from web3.providers.manager import (
    PrivateKeySigningManager,
)

from testrpc.client.utils import (
    mk_random_privkey,
    encode_address,
)


@pytest.fixture()
def account_private_key():
    return mk_random_privkey()


@pytest.fixture()
def account_public_key(account_private_key):
    from ethereum.utils import privtoaddr
    return to_normalized_address(encode_address(privtoaddr(account_private_key)))


@pytest.fixture()
def web3_pk_signer(web3,
                   account_public_key,
                   account_private_key,
                   wait_for_block,
                   wait_for_transaction):
    pk_signing_manager = PrivateKeySigningManager(web3._requestManager)
    pk_signing_manager.register_private_key(account_private_key)
    assert account_public_key in pk_signing_manager.keys

    wait_for_block(web3)

    fund_txn_hash = web3.eth.sendTransaction({
        'from': web3.eth.coinbase,
        'to': account_public_key,
        'value': 10 * denoms.ether,
    })
    wait_for_transaction(web3, fund_txn_hash)

    web3._requestManager = pk_signing_manager
    return web3


def test_private_key_signing_manager(web3_pk_signer,
                                     account_private_key,
                                     account_public_key,
                                     wait_for_transaction):
    web3 = web3_pk_signer
    assert account_public_key not in web3_pk_signer.eth.accounts

    with pytest.raises(ValueError):
        web3.eth.sendTransaction({
            'from': account_public_key,
            'to': web3.eth.coinbase,
            'value': 1,
        })

    from ethereum import tester
    tester.keys.append(account_private_key)
    tester.accounts.append(decode_hex(account_public_key))

    txn_hash = web3.eth.sendTransaction({
        'from': account_public_key,
        'to': web3.eth.coinbase,
        'value': 1,
    })
    txn_receipt = wait_for_transaction(web3, txn_hash)
    txn = web3.eth.getTransaction(txn_hash)

    assert txn['from'] == account_public_key
