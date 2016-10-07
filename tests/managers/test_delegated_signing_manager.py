import pytest

from web3.providers.manager import (
    DelegatedSigningManager,
)
from web3.utils.currency import denoms


def test_delegated_signing_manager(web3_ipc_empty,
                                   web3_rpc_empty,
                                   wait_for_block,
                                   wait_for_transaction):
    web3_signer = web3_ipc_empty
    web3_sender = web3_rpc_empty
    wait_for_block(web3_signer)
    wait_for_block(web3_sender)

    signer_cb = web3_signer.eth.coinbase
    sender_cb = web3_sender.eth.coinbase

    # fund the account
    fund_txn_hash = web3_sender.eth.sendTransaction({
        'from': sender_cb,
        'to': signer_cb,
        'value': 10 * denoms.ether,
    })
    wait_for_transaction(web3_sender, fund_txn_hash)

    assert signer_cb != sender_cb

    with pytest.raises(ValueError):
        web3_sender.eth.sendTransaction({
            'from': signer_cb,
            'to': sender_cb,
            'value': 0,
        })

    web3_sender._requestManager = DelegatedSigningManager(
        wrapped_manager=web3_sender._requestManager,
        signature_manager=web3_signer._requestManager,
    )

    assert sender_cb in web3_sender.eth.accounts
    assert signer_cb not in web3_sender.eth.accounts

    txn_hash = web3_sender.eth.sendTransaction({
        'from': signer_cb,
        'to': sender_cb,
        'value': 0,
    })
    txn_receipt = wait_for_transaction(web3_sender, txn_hash)
    txn = web3_sender.eth.getTransaction(txn_hash)

    assert txn['from'] == signer_cb
