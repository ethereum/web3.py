import pytest

import rlp

from eth_utils import (
    encode_hex,
    decode_hex,
    is_same_address,
)

from web3.utils.transactions import (
    Transaction,
    UnsignedTransaction,
    serialize_transaction,
    add_signature_to_transaction,
)


@pytest.fixture()
def wait_for_first_block(web3, wait_for_block):
    wait_for_block(web3)


def test_transaction_serialization():
    transaction = {
        'nonce': hex(0),
        'to': '0xd3cda913deb6f67967b99d67acdfa1712c293601',
        'value': hex(12345),
        'gas': hex(1200300),
        'gasPrice': hex(54321),
        'data': '0x1234567890abcdef',
    }

    serialized_txn = serialize_transaction(transaction)
    unserialized_txn = rlp.decode(serialized_txn, UnsignedTransaction)

    assert is_same_address(unserialized_txn.to, transaction['to'])
    assert unserialized_txn.startgas == int(transaction['gas'], 16)
    assert unserialized_txn.gasprice == int(transaction['gasPrice'], 16)
    assert unserialized_txn.nonce == int(transaction['nonce'], 16)
    assert unserialized_txn.value == int(transaction['value'], 16)
    assert encode_hex(unserialized_txn.data) == transaction['data']


def test_adding_signature_to_transaction(wait_for_first_block,
                                         web3,
                                         skip_if_testrpc):
    skip_if_testrpc(web3)

    transaction = {
        'nonce': hex(0),
        'to': '0xd3cda913deb6f67967b99d67acdfa1712c293601',
        'value': hex(12345),
        'gas': hex(1200300),
        'gasPrice': hex(54321),
        'data': '0x1234567890abcdef',
    }

    serialized_txn = serialize_transaction(transaction)
    signature_hex = web3.eth.sign(web3.eth.coinbase, serialized_txn)

    signed_transaction = add_signature_to_transaction(
        serialized_txn,
        decode_hex(signature_hex),
    )

    assert is_same_address(signed_transaction.to, transaction['to'])
    assert signed_transaction.startgas == int(transaction['gas'], 16)
    assert signed_transaction.gasprice == int(transaction['gasPrice'], 16)
    assert signed_transaction.nonce == int(transaction['nonce'], 16)
    assert signed_transaction.value == int(transaction['value'], 16)
    assert encode_hex(signed_transaction.data) == transaction['data']
    assert signed_transaction.sender == web3.eth.coinbase
