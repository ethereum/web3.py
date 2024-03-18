import pytest

from web3._utils.transactions import (
    assert_valid_transaction_params,
    extract_valid_transaction_params,
    fill_transaction_defaults,
)
from web3.exceptions import (
    Web3AttributeError,
    Web3ValueError,
)


def test_assert_valid_transaction_params_all_params():
    assert_valid_transaction_params(
        {
            "chainId": 1,
            "type": "0x2",
            "from": "0x0",
            "to": "0x0",
            "gas": 21000,
            "gasPrice": 5000000,
            "maxFeePerGas": 2000000000,
            "maxPriorityFeePerGas": 1000000000,
            "accessList": (
                {
                    "address": "0xde0b295669a9fd93d5f28d9ec85e40f4cb697bae",
                    "storageKeys": (
                        "0x0000000000000000000000000000000000000000000000000000000000000003",  # noqa: E501
                        "0x0000000000000000000000000000000000000000000000000000000000000007",  # noqa: E501
                    ),
                },
                {
                    "address": "0xbb9bc244d798123fde783fcc1c72d3bb8c189413",
                    "storageKeys": (),
                },
            ),
            "value": 1,
            "data": "0x0",
            "nonce": 2,
        }
    )


def test_assert_valid_transaction_params_some_params():
    assert_valid_transaction_params(
        {
            "from": "0x0",
            "to": "0x0",
            "value": 1,
        }
    )


def test_assert_valid_transaction_params_invalid_param():
    with pytest.raises(Web3ValueError):
        assert_valid_transaction_params(
            {
                "from": "0x0",
                "to": "0x0",
                "value": 1,
                "tokens": 9000,
            }
        )


FULL_TXN_DICT = {
    "type": "0x2",
    "from": "0x0",
    "to": "0x1",
    "gas": 21000,
    "gasPrice": 5000000,
    "maxFeePerGas": 2000000000,
    "maxPriorityFeePerGas": 1000000000,
    "data": "0x2",
    "value": 3,
    "nonce": 2,
    "chainId": 1,
    "accessList": (
        {
            "address": "0xde0b295669a9fd93d5f28d9ec85e40f4cb697bae",
            "storageKeys": (
                "0x0000000000000000000000000000000000000000000000000000000000000003",
                "0x0000000000000000000000000000000000000000000000000000000000000007",
            ),
        },
        {"address": "0xbb9bc244d798123fde783fcc1c72d3bb8c189413", "storageKeys": ()},
    ),
    "maxFeePerBlobGas": 2000000000,
    "blobVersionedHashes": (
        "0x01a915e4d060149eb4365960e6a7a45f334393093061116b197e3240065ff2d8",
    ),
}


@pytest.mark.parametrize(
    "transaction_params, expected",
    (
        (FULL_TXN_DICT, FULL_TXN_DICT),
        ({"data": "0x0", "input": "0x0"}, {"data": "0x0"}),
        ({"input": "0x0"}, {"data": "0x0"}),
        ({}, {}),
    ),
)
def test_extract_valid_transaction_params(transaction_params, expected):
    valid_transaction_params = extract_valid_transaction_params(transaction_params)
    assert valid_transaction_params == expected


INVALID_TXN_PARAMS = {"data": "0x0", "input": "0x1"}
EXPECTED_EXC_MSG = r'.* "input:(.*)" and "data:(.*)" .*'


@pytest.mark.parametrize(
    "transaction_params, expected_exc_msg", ((INVALID_TXN_PARAMS, EXPECTED_EXC_MSG),)
)
def test_extract_valid_transaction_params_invalid(transaction_params, expected_exc_msg):
    with pytest.raises(Web3AttributeError, match=expected_exc_msg):
        extract_valid_transaction_params(transaction_params)


def test_extract_valid_transaction_params_includes_invalid():
    input = {
        "chainId": 1,
        "type": "0x2",
        "from": "0x0",
        "to": "0x0",
        "gas": 21000,
        "gasPrice": 5000000,
        "maxFeePerGas": 2000000000,
        "maxPriorityFeePerGas": 1000000000,
        "value": 1,
        "tokens": 9000,
    }
    valid_transaction_params = extract_valid_transaction_params(input)
    assert valid_transaction_params == {
        "chainId": 1,
        "type": "0x2",
        "from": "0x0",
        "to": "0x0",
        "gas": 21000,
        "gasPrice": 5000000,
        "maxFeePerGas": 2000000000,
        "maxPriorityFeePerGas": 1000000000,
        "value": 1,
    }


def test_fill_transaction_defaults_for_all_params(w3):
    default_transaction = fill_transaction_defaults(w3, {})

    assert default_transaction == {
        "chainId": w3.eth.chain_id,
        "data": b"",
        "gas": w3.eth.estimate_gas({}),
        "maxFeePerGas": (
            w3.eth.max_priority_fee + (2 * w3.eth.get_block("latest")["baseFeePerGas"])
        ),
        "maxPriorityFeePerGas": w3.eth.max_priority_fee,
        "value": 0,
    }


def test_fill_transaction_defaults_for_zero_gas_price(w3):
    def gas_price_strategy(_w3, tx):
        return 0

    w3.eth.set_gas_price_strategy(gas_price_strategy)

    default_transaction = fill_transaction_defaults(w3, {})

    assert default_transaction == {
        "chainId": w3.eth.chain_id,
        "data": b"",
        "gas": w3.eth.estimate_gas({}),
        "value": 0,
        "gasPrice": 0,
    }
