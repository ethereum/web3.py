import pytest

from eth_utils import (
    to_checksum_address,
    to_int,
)
from hexbytes import (
    HexBytes,
)

from web3._utils.ens import (
    ens_addresses,
)
from web3._utils.rpc_abi import (
    RPC,
)
from web3.datastructures import (
    AttributeDict,
)
from web3.exceptions import (
    NameNotFound,
    TimeExhausted,
    TransactionNotFound,
    Web3ValidationError,
)
from web3.middleware import (
    construct_result_generator_middleware,
)
from web3.middleware.simulate_unmined_transaction import (
    unmined_receipt_simulator_middleware,
)

RECEIPT_TIMEOUT = 0.2


@pytest.mark.parametrize(
    "transaction",
    (
        {
            "gasPrice": 10**9,
            "accessList": (
                {
                    "address": "0xd3CdA913deB6f67967B99D67aCDFa1712C293601",
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
        },
        {
            "maxFeePerGas": 10**9,
            "maxPriorityFeePerGas": 10**9,
            "accessList": (
                {
                    "address": "0xd3CdA913deB6f67967B99D67aCDFa1712C293601",
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
        },
    ),
    ids=[
        "storage_keys_access_list_txn",
        "storage_keys_dynamic_fee_txn",
    ],
)
def test_eth_tester_send_transaction_validation(w3, transaction):
    # Test that eth-tester transaction param validation does not
    # throw for properly formatted transactions.
    # This is especially important because we have key mapping differences
    # (camelCase to snake_case) mitigated by providers/eth-tester/middleware.
    txn_hash = w3.eth.send_transaction(transaction)
    receipt = w3.eth.wait_for_transaction_receipt(txn_hash, timeout=RECEIPT_TIMEOUT)
    assert receipt.get("blockNumber") is not None


@pytest.mark.parametrize(
    "make_chain_id, expect_success",
    (
        (
            lambda w3: w3.eth.chain_id,
            True,
        ),
        pytest.param(
            lambda w3: 999999999999,
            False,
        ),
    ),
)
def test_send_transaction_with_valid_chain_id(w3, make_chain_id, expect_success):
    transaction = {
        "to": w3.eth.accounts[1],
        "chainId": make_chain_id(w3),
    }
    if expect_success:
        txn_hash = w3.eth.send_transaction(transaction)
        receipt = w3.eth.wait_for_transaction_receipt(txn_hash, timeout=RECEIPT_TIMEOUT)
        assert receipt.get("blockNumber") is not None
    else:
        with pytest.raises(Web3ValidationError) as exc_info:
            w3.eth.send_transaction(transaction)

        assert "chain ID" in str(exc_info.value)


@pytest.mark.parametrize(
    "to, _from",
    (
        (
            "registered-name-1.eth",
            "not-a-registered-name.eth",
        ),
        (
            "not-a-registered-name.eth",
            "registered-name-1.eth",
        ),
    ),
)
def test_send_transaction_with_invalid_ens_names(w3, to, _from):
    with ens_addresses(
        w3,
        [
            ("registered-name-1.eth", w3.eth.accounts[1]),
        ],
    ):
        transaction = {
            "to": to,
            "chainId": w3.eth.chain_id,
            "from": _from,
        }

        with pytest.raises(NameNotFound):
            w3.eth.send_transaction(transaction)


def test_send_transaction_with_ens_names(w3):
    with ens_addresses(
        w3,
        [
            ("registered-name-1.eth", w3.eth.accounts[1]),
            ("registered-name-2.eth", w3.eth.accounts[0]),
        ],
    ):
        transaction = {
            "to": "registered-name-1.eth",
            "chainId": w3.eth.chain_id,
            "from": "registered-name-2.eth",
        }

        txn_hash = w3.eth.send_transaction(transaction)
        receipt = w3.eth.wait_for_transaction_receipt(txn_hash, timeout=RECEIPT_TIMEOUT)
        assert receipt.get("blockNumber") is not None


def test_wait_for_missing_receipt(w3):
    with pytest.raises(TimeExhausted):
        w3.eth.wait_for_transaction_receipt(b"\0" * 32, timeout=RECEIPT_TIMEOUT)


def test_passing_string_to_to_hex(w3):
    with pytest.raises(TimeExhausted):
        transaction_hash = (
            "0x5c504ed432cb51138bcf09aa5e8a410dd4a1e204ef84bfed1be16dfba1b22060"
        )
        w3.eth.wait_for_transaction_receipt(transaction_hash, timeout=RECEIPT_TIMEOUT)


def test_unmined_transaction_wait_for_receipt(w3):
    w3.middleware_onion.add(unmined_receipt_simulator_middleware)
    txn_hash = w3.eth.send_transaction(
        {
            "from": w3.eth.coinbase,
            "to": "0xd3CdA913deB6f67967B99D67aCDFa1712C293601",
            "value": 123457,
        }
    )
    with pytest.raises(TransactionNotFound):
        w3.eth.get_transaction_receipt(txn_hash)

    txn_receipt = w3.eth.wait_for_transaction_receipt(txn_hash)
    assert txn_receipt["transactionHash"] == txn_hash
    assert txn_receipt["blockHash"] is not None


def test_get_transaction_formatters(w3):
    non_checksummed_addr = "0xB2930B35844A230F00E51431ACAE96FE543A0347"  # all uppercase
    unformatted_transaction = {
        "blockHash": (
            "0x849044202a39ae36888481f90d62c3826bca8269c2716d7a38696b4f45e61d83"
        ),
        "blockNumber": "0x1b4",
        "transactionIndex": "0x0",
        "nonce": "0x0",
        "gas": "0x4c4b40",
        "gasPrice": "0x1",
        "maxFeePerGas": "0x1",
        "maxPriorityFeePerGas": "0x1",
        "value": "0x1",
        "from": non_checksummed_addr,
        "publicKey": "0x",
        "r": "0xd148ae70c8cbef3a038e70e6d1639f0951e60a2965820f33bad19d0a6c2b8116",
        "raw": "0x142ab034696c09dcfb2a8b086b494f3f4c419e67b6c04d95882f87156a3b6f35",
        "s": "0x6f5216fc207221a11efe2e4c3e3a881a0b5ca286ede538fc9dbc403b2009ea76",
        "to": non_checksummed_addr,
        "hash": "0x142ab034696c09dcfb2a8b086b494f3f4c419e67b6c04d95882f87156a3b6f35",
        "v": "0x1",
        "yParity": "0x1",
        "standardV": "0x1",
        "type": "0x2",
        "chainId": "0x539",
        "accessList": [
            {
                "address": non_checksummed_addr,
                "storageKeys": [
                    "0x0000000000000000000000000000000000000000000000000000000000000032",  # noqa: E501
                    "0x0000000000000000000000000000000000000000000000000000000000000036",  # noqa: E501
                ],
            },
            {
                "address": non_checksummed_addr,
                "storageKeys": [],
            },
        ],
        "input": "0x5b34b966",
        "data": "0x5b34b966",
    }

    result_middleware = construct_result_generator_middleware(
        {
            RPC.eth_getTransactionByHash: lambda *_: unformatted_transaction,
        }
    )
    w3.middleware_onion.inject(result_middleware, "result_middleware", layer=0)

    # test against eth_getTransactionByHash
    received_tx = w3.eth.get_transaction("")

    checksummed_addr = to_checksum_address(non_checksummed_addr)
    assert non_checksummed_addr != checksummed_addr

    expected = AttributeDict(
        {
            "blockHash": HexBytes(unformatted_transaction["blockHash"]),
            "blockNumber": to_int(hexstr=unformatted_transaction["blockNumber"]),
            "transactionIndex": 0,
            "nonce": 0,
            "gas": to_int(hexstr=unformatted_transaction["gas"]),
            "gasPrice": 1,
            "maxFeePerGas": 1,
            "maxPriorityFeePerGas": 1,
            "value": 1,
            "from": checksummed_addr,
            "publicKey": HexBytes(unformatted_transaction["publicKey"]),
            "r": HexBytes(unformatted_transaction["r"]),
            "raw": HexBytes(unformatted_transaction["raw"]),
            "s": HexBytes(unformatted_transaction["s"]),
            "to": to_checksum_address(non_checksummed_addr),
            "hash": HexBytes(unformatted_transaction["hash"]),
            "v": 1,
            "yParity": 1,
            "standardV": 1,
            "type": 2,
            "chainId": 1337,
            "accessList": [
                AttributeDict(
                    {
                        "address": checksummed_addr,
                        "storageKeys": [
                            "0x0000000000000000000000000000000000000000000000000000000000000032",  # noqa: E501
                            "0x0000000000000000000000000000000000000000000000000000000000000036",  # noqa: E501
                        ],
                    }
                ),
                AttributeDict(
                    {
                        "address": checksummed_addr,
                        "storageKeys": [],
                    }
                ),
            ],
            "input": HexBytes(unformatted_transaction["input"]),
            "data": HexBytes(unformatted_transaction["data"]),
        }
    )
    assert received_tx == expected
    w3.middleware_onion.remove("result_middleware")
