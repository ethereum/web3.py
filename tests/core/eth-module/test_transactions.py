import pytest
import sys

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
    async_construct_error_generator_middleware,
    async_construct_result_generator_middleware,
    construct_error_generator_middleware,
    construct_result_generator_middleware,
)
from web3.middleware.simulate_unmined_transaction import (
    unmined_receipt_simulator_middleware,
)

RECEIPT_TIMEOUT = 0.2


def _swap_error_middleware_for_result_middleware_and_return_error(
    w3, result_middleware
):
    # On the first call, this will be in ``layer=0`` and we will remove this
    # middleware and add the result middleware to layer 0 for the next call.
    w3.middleware_onion.remove("error_middleware")
    w3.middleware_onion.inject(result_middleware, "result_middleware", layer=0)
    return {"code": -32000, "message": "transaction indexing in progress"}


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


def test_eth_wait_for_transaction_receipt_transaction_indexing_in_progress(w3):
    result_middleware = construct_result_generator_middleware(
        {RPC.eth_getTransactionReceipt: lambda *_: {"status": 1}}
    )
    error_middleware = construct_error_generator_middleware(
        {
            RPC.eth_getTransactionReceipt: lambda *_: (
                _swap_error_middleware_for_result_middleware_and_return_error(
                    w3, result_middleware
                )
            )
        }
    )
    w3.middleware_onion.inject(error_middleware, "error_middleware", layer=0)

    receipt = w3.eth.wait_for_transaction_receipt(f"0x{'00' * 32}")
    assert receipt == {"status": 1}

    assert "error_middleware" not in w3.middleware_onion.middlewares
    w3.middleware_onion.remove("result_middleware")


def test_get_transaction_formatters(w3):
    non_checksummed_addr = "0xB2930B35844A230F00E51431ACAE96FE543A0347"  # all uppercase
    unformatted_transaction = {
        "blobVersionedHashes": [
            "0x01b8c5b09810b5fc07355d3da42e2c3a3e200c1d9a678491b7e8e256fc50cc4f",
            "0x015b4c8cc4f86aa2d2cf9e9ce97fca704a11a6c20f6b1d6c00a6e15f6d60a6df",
            "0x01878f80eaf10be1a6f618e6f8c071b10a6c14d9b89a3bf2a3f3cf2db6c5681d",
        ],
        "blockHash": (
            "0x849044202a39ae36888481f90d62c3826bca8269c2716d7a38696b4f45e61d83"
        ),
        "blockNumber": "0x1b4",
        "transactionIndex": "0x0",
        "nonce": "0x0",
        "gas": "0x4c4b40",
        "gasPrice": "0x1",
        "maxFeePerBlobGas": "0x1",
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
            "blobVersionedHashes": [
                HexBytes(
                    "0x01b8c5b09810b5fc07355d3da42e2c3a3e200c1d9a678491b7e8e256fc50cc4f"
                ),
                HexBytes(
                    "0x015b4c8cc4f86aa2d2cf9e9ce97fca704a11a6c20f6b1d6c00a6e15f6d60a6df"
                ),
                HexBytes(
                    "0x01878f80eaf10be1a6f618e6f8c071b10a6c14d9b89a3bf2a3f3cf2db6c5681d"
                ),
            ],
            "blockHash": HexBytes(unformatted_transaction["blockHash"]),
            "blockNumber": to_int(hexstr=unformatted_transaction["blockNumber"]),
            "transactionIndex": 0,
            "nonce": 0,
            "gas": to_int(hexstr=unformatted_transaction["gas"]),
            "gasPrice": 1,
            "maxFeePerBlobGas": 1,
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
                            HexBytes(
                                "0x0000000000000000000000000000000000000000000000000000000000000032"  # noqa: E501
                            ),
                            HexBytes(
                                "0x0000000000000000000000000000000000000000000000000000000000000036"  # noqa: E501
                            ),
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


@pytest.mark.skipif(
    sys.version_info < (3, 8),
    reason=(
        "There is no version of eth-tester that supports both python 3.7 and blob "
        "transactions / Cancun network upgrade."
    ),
)
def test_eth_send_raw_blob_transaction(w3):
    # `eth-tester` account #1's pkey is "0x00000000...01"
    acct = w3.eth.account.from_key(f"0x{'00' * 31}01")

    text = "We are the music makers and we are the dreamers of dreams."
    encoded_text = w3.codec.encode(["string"], [text])
    # Blobs contain 4096 32-byte field elements. Subtract the length of the encoded text
    # divided into 32-byte chunks from 4096 and pad the rest with zeros.
    blob_data = (b"\x00" * 32 * (4096 - len(encoded_text) // 32)) + encoded_text

    tx = {
        "type": 3,
        "chainId": 1337,
        "from": acct.address,
        "to": "0xb45BEc6eeCA2a09f4689Dd308F550Ad7855051B5",
        "value": 0,
        "gas": 21000,
        "maxFeePerGas": 10**10,
        "maxPriorityFeePerGas": 10**10,
        "maxFeePerBlobGas": 10**10,
        "nonce": w3.eth.get_transaction_count(acct.address),
    }

    signed = acct.sign_transaction(tx, blobs=[blob_data])

    tx_hash = w3.eth.send_raw_transaction(signed.rawTransaction)
    transaction = w3.eth.get_transaction(tx_hash)

    assert len(transaction["blobVersionedHashes"]) == 1
    assert transaction["blobVersionedHashes"][0] == HexBytes(
        "0x0127c38bcad458d932e828b580b9ad97310be01407dfa0ed88118735980a3e9a"
    )


# --- async --- #


@pytest.mark.asyncio
async def test_async_wait_for_transaction_receipt_transaction_indexing_in_progress(
    async_w3,
):
    result_middleware = await async_construct_result_generator_middleware(
        {RPC.eth_getTransactionReceipt: lambda *_: {"status": 1}}
    )
    error_middleware = await async_construct_error_generator_middleware(
        {
            RPC.eth_getTransactionReceipt: lambda *_: (
                _swap_error_middleware_for_result_middleware_and_return_error(
                    async_w3, result_middleware
                )
            )
        }
    )
    async_w3.middleware_onion.inject(error_middleware, "error_middleware", layer=0)

    receipt = await async_w3.eth.wait_for_transaction_receipt(f"0x{'00' * 32}")
    assert receipt == {"status": 1}

    async_w3.middleware_onion.remove("result_middleware")


@pytest.mark.skipif(
    sys.version_info < (3, 8),
    reason=(
        "There is no version of eth-tester that supports both python 3.7 and blob "
        "transactions / Cancun network upgrade."
    ),
)
@pytest.mark.asyncio
async def test_async_send_raw_blob_transaction(async_w3):
    # `eth-tester` account #1's pkey is "0x00000000...01"
    acct = async_w3.eth.account.from_key(f"0x{'00' * 31}01")

    text = "We are the music makers and we are the dreamers of dreams."
    encoded_text = async_w3.codec.encode(["string"], [text])
    # Blobs contain 4096 32-byte field elements. Subtract the length of the encoded text
    # divided into 32-byte chunks from 4096 and pad the rest with zeros.
    blob_data = (b"\x00" * 32 * (4096 - len(encoded_text) // 32)) + encoded_text

    tx = {
        "type": 3,
        "chainId": 1337,
        "from": acct.address,
        "to": "0xb45BEc6eeCA2a09f4689Dd308F550Ad7855051B5",
        "value": 0,
        "gas": 21000,
        "maxFeePerGas": 10**10,
        "maxPriorityFeePerGas": 10**10,
        "maxFeePerBlobGas": 10**10,
        "nonce": await async_w3.eth.get_transaction_count(acct.address),
    }

    signed = acct.sign_transaction(tx, blobs=[blob_data])

    tx_hash = await async_w3.eth.send_raw_transaction(signed.rawTransaction)
    transaction = await async_w3.eth.get_transaction(tx_hash)

    assert len(transaction["blobVersionedHashes"]) == 1
    assert transaction["blobVersionedHashes"][0] == HexBytes(
        "0x0127c38bcad458d932e828b580b9ad97310be01407dfa0ed88118735980a3e9a"
    )
