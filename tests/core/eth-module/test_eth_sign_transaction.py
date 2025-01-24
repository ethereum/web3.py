"""Test the eth_tester sign transaction implementations."""

import pytest
from eth_utils import (
    is_bytes,
    is_checksum_address,
    is_hex,
)
from hexbytes import (
    HexBytes,
)

from web3.exceptions import (
    MethodUnavailable,
)


def test_eth_sign_transaction_legacy(w3, unlocked_account):
    """
    Test eth_signTransaction with legacy (pre-EIP1559) transaction parameters.
    Expect MethodUnavailable as this is not implemented in eth_tester.
    """
    transaction = {
        "from": unlocked_account,
        "to": "0x" + "00" * 20,  # Zero address
        "value": 100,
        "gas": 21000,
        "gasPrice": w3.eth.gas_price,
        "nonce": w3.eth.get_transaction_count(unlocked_account),
        "chainId": w3.eth.chain_id,
    }

    with pytest.raises(MethodUnavailable):
        w3.eth.sign_transaction(transaction)


def test_eth_sign_transaction(w3, unlocked_account):
    """
    Test eth_signTransaction with EIP1559 transaction parameters.
    Expect MethodUnavailable as this is not implemented in eth_tester.
    """
    transaction = {
        "from": unlocked_account,
        "to": "0x" + "00" * 20,  # Zero address
        "value": 100,
        "gas": 21000,
        "maxFeePerGas": 2000000000,
        "maxPriorityFeePerGas": 1000000000,
        "nonce": w3.eth.get_transaction_count(unlocked_account),
        "chainId": w3.eth.chain_id,
        "type": "0x2",
    }

    with pytest.raises(MethodUnavailable):
        w3.eth.sign_transaction(transaction)


def test_eth_sign_transaction_hex_fees(w3, unlocked_account):
    """
    Test eth_signTransaction with hex values for EIP1559 fee parameters.
    Expect MethodUnavailable as this is not implemented in eth_tester.
    """
    transaction = {
        "from": unlocked_account,
        "to": "0x" + "00" * 20,  # Zero address
        "value": "0x64",  # 100 in hex
        "gas": "0x5208",  # 21000 in hex
        "maxFeePerGas": "0x77359400",  # 2 Gwei in hex
        "maxPriorityFeePerGas": "0x3B9ACA00",  # 1 Gwei in hex
        "nonce": hex(w3.eth.get_transaction_count(unlocked_account)),
        "chainId": hex(w3.eth.chain_id),
        "type": "0x2",
    }

    with pytest.raises(MethodUnavailable):
        w3.eth.sign_transaction(transaction)