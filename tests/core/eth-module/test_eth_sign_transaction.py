import pytest
from eth_account import Account
from eth_account.messages import encode_defunct
from eth_utils import to_bytes, to_hex
from hexbytes import HexBytes

from web3._utils.transactions import serialize_transaction
from web3.exceptions import InvalidAddress


def test_eth_sign_transaction_legacy(w3, keyfile_account_address):
    """
    Test signing a legacy (pre-EIP-1559) transaction.
    """
    transaction = {
        'nonce': w3.eth.get_transaction_count(keyfile_account_address),
        'gasPrice': w3.eth.gas_price,
        'gas': 21000,
        'to': '0x0000000000000000000000000000000000000000',
        'value': 1000000000000000000,  # 1 ETH
        'data': '0x',
        'chainId': w3.eth.chain_id
    }
    
    signed = w3.eth.sign_transaction(transaction)
    
    # Verify the signature
    assert isinstance(signed.rawTransaction, (bytes, bytearray))
    assert isinstance(signed.hash, HexBytes)
    assert isinstance(signed.r, int)
    assert isinstance(signed.s, int)
    assert isinstance(signed.v, int)
    
    # Verify the transaction can be sent
    tx_hash = w3.eth.send_raw_transaction(signed.rawTransaction)
    assert isinstance(tx_hash, HexBytes)


def test_eth_sign_transaction(w3, keyfile_account_address):
    """
    Test signing an EIP-1559 transaction with maxFeePerGas and maxPriorityFeePerGas.
    """
    transaction = {
        'nonce': w3.eth.get_transaction_count(keyfile_account_address),
        'maxFeePerGas': 2000000000,  # 2 Gwei
        'maxPriorityFeePerGas': 1000000000,  # 1 Gwei
        'gas': 21000,
        'to': '0x0000000000000000000000000000000000000000',
        'value': 1000000000000000000,  # 1 ETH
        'data': '0x',
        'chainId': w3.eth.chain_id,
        'type': '0x2'  # EIP-1559 transaction type
    }
    
    signed = w3.eth.sign_transaction(transaction)
    
    # Verify the signature
    assert isinstance(signed.rawTransaction, (bytes, bytearray))
    assert isinstance(signed.hash, HexBytes)
    assert isinstance(signed.r, int)
    assert isinstance(signed.s, int)
    assert isinstance(signed.v, int)
    
    # Verify transaction type
    decoded = w3.eth.account.decode_transaction(signed.rawTransaction)
    assert decoded['type'] == 2
    
    # Verify the transaction can be sent
    tx_hash = w3.eth.send_raw_transaction(signed.rawTransaction)
    assert isinstance(tx_hash, HexBytes)


def test_eth_sign_transaction_hex_fees(w3, keyfile_account_address):
    """
    Test signing a transaction with hexadecimal fee values.
    """
    transaction = {
        'nonce': hex(w3.eth.get_transaction_count(keyfile_account_address)),
        'maxFeePerGas': '0x77359400',  # 2 Gwei in hex
        'maxPriorityFeePerGas': '0x3B9ACA00',  # 1 Gwei in hex
        'gas': '0x5208',  # 21000 in hex
        'to': '0x0000000000000000000000000000000000000000',
        'value': '0xDE0B6B3A7640000',  # 1 ETH in hex
        'data': '0x',
        'chainId': hex(w3.eth.chain_id),
        'type': '0x2'
    }
    
    signed = w3.eth.sign_transaction(transaction)
    
    # Verify the signature
    assert isinstance(signed.rawTransaction, (bytes, bytearray))
    assert isinstance(signed.hash, HexBytes)
    
    # Verify values are properly encoded
    decoded = w3.eth.account.decode_transaction(signed.rawTransaction)
    assert decoded['gas'] == 21000
    assert decoded['value'] == 1000000000000000000
    assert decoded['maxFeePerGas'] == 2000000000
    assert decoded['maxPriorityFeePerGas'] == 1000000000
    
    # Verify the transaction can be sent
    tx_hash = w3.eth.send_raw_transaction(signed.rawTransaction)
    assert isinstance(tx_hash, HexBytes)