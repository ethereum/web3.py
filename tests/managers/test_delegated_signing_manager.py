import pytest

from web3.providers.manager import (
    DelegatedSigningManager,
)
from web3.utils.currency import denoms


@pytest.fixture()
def web3_signer(web3_rpc_empty, wait_for_block):
    wait_for_block(web3_rpc_empty)
    return web3_rpc_empty


@pytest.fixture()
def web3_sender(web3_signer, web3_ipc_empty, wait_for_transaction, wait_for_block):
    wait_for_block(web3_ipc_empty)

    signer_cb = web3_signer.eth.coinbase
    sender_cb = web3_ipc_empty.eth.coinbase

    assert signer_cb != sender_cb

    # fund the account
    fund_txn_hash = web3_ipc_empty.eth.sendTransaction({
        'from': sender_cb,
        'to': signer_cb,
        'value': 10 * denoms.ether,
    })
    wait_for_transaction(web3_ipc_empty, fund_txn_hash)

    with pytest.raises(ValueError):
        web3_ipc_empty.eth.sendTransaction({
            'from': signer_cb,
            'to': sender_cb,
            'value': 0,
        })

    web3_ipc_empty._requestManager = DelegatedSigningManager(
        wrapped_manager=web3_ipc_empty._requestManager,
        signature_manager=web3_signer._requestManager,
    )

    return web3_ipc_empty


def test_delegated_signing_manager(web3_sender,
                                   web3_signer,
                                   wait_for_transaction):
    sender_cb = web3_sender.eth.coinbase
    signer_cb = web3_signer.eth.coinbase

    assert sender_cb in web3_sender.eth.accounts
    assert signer_cb not in web3_sender.eth.accounts

    txn_hash = web3_sender.eth.sendTransaction({
        'from': signer_cb,
        'to': sender_cb,
        'value': 12345,
    })
    txn_receipt = wait_for_transaction(web3_sender, txn_hash)
    txn = web3_sender.eth.getTransaction(txn_hash)

    assert txn['from'] == signer_cb
    assert txn['to'] == sender_cb
    assert txn['value'] == 12345


def test_delegated_signing_manager_tracks_nonces_correctly(web3_sender,
                                                           web3_signer,
                                                           wait_for_transaction):
    sender_cb = web3_sender.eth.coinbase
    signer_cb = web3_signer.eth.coinbase

    assert sender_cb in web3_sender.eth.accounts
    assert signer_cb not in web3_sender.eth.accounts

    num_to_send = web3_sender.eth.getBlock('latest')['gasLimit'] // 21000 + 10

    all_txn_hashes = []
    for i in range(num_to_send):
        all_txn_hashes.append(web3_sender.eth.sendTransaction({
            'from': signer_cb,
            'to': sender_cb,
            'value': i,
        }))

    all_txn_receipts = [
        wait_for_transaction(web3_sender, txn_hash)
        for txn_hash in all_txn_hashes
    ]
    all_txns = [
        web3_sender.eth.getTransaction(txn_hash)
        for txn_hash in all_txn_hashes
    ]

    assert all([
        idx == txn['nonce']
        for idx, txn in enumerate(all_txns)
    ])
    block_numbers = {
        txn_receipt['blockNumber'] for txn_receipt in all_txn_receipts
    }
    assert len(block_numbers) > 1
