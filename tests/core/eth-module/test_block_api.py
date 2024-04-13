import pytest

from eth_utils import (
    to_checksum_address,
)
from hexbytes import (
    HexBytes,
)


@pytest.fixture(autouse=True)
def wait_for_first_block(w3, wait_for_block):
    wait_for_block(w3)


def test_uses_default_block(w3, wait_for_transaction):
    assert w3.eth.default_block == "latest"
    w3.eth.default_block = w3.eth.block_number
    assert w3.eth.default_block == w3.eth.block_number


def test_get_block_formatters_with_null_values(w3, request_mocker):
    null_values_block = {
        "baseFeePerGas": None,
        "extraData": None,
        "gasLimit": None,
        "gasUsed": None,
        "size": None,
        "timestamp": None,
        "hash": None,
        "logsBloom": None,
        "miner": None,
        "mixHash": None,
        "nonce": None,
        "number": None,
        "parentHash": None,
        "sha3Uncles": None,
        "difficulty": None,
        "receiptsRoot": None,
        "stateRoot": None,
        "totalDifficulty": None,
        "transactionsRoot": None,
        "transactions": [],
        "withdrawalsRoot": None,
        "withdrawals": [],
        "blobGasUsed": None,
        "excessBlobGas": None,
        "parentBeaconBlockRoot": None,
    }
    with request_mocker(w3, mock_results={"eth_getBlockByNumber": null_values_block}):
        received_block = w3.eth.get_block("pending")
    assert received_block == null_values_block


def test_get_block_formatters_with_pre_formatted_values(w3, request_mocker):
    unformatted_values_block = {
        "baseFeePerGas": "0x3b9aca00",
        "extraData": "0x",
        "gasLimit": "0x1c9c380",
        "gasUsed": "0x1ec30",
        "size": "0x734",
        "timestamp": "0x2dfdc1c3e",
        "hash": "0x759bc3c1221beb27a7074dbf33faded2276b04df6aaf225d51c426b8c481e935",
        "logsBloom": "0x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000",  # noqa: E501
        "miner": "0x0deadbeefdeadbeef72211ad2C21deadbeeffeed",
        "mixHash": "0xfa167946892d77a2fe116fa81c53c18cfd163889cb08f74c23415c8d13762e1b",
        "nonce": "0x0",
        "number": "0x2dfdc1c3e",
        "parentHash": (
            "0xfe7bde5fac0a5b023504e4abba1165101ca7fe724e6ad29d0c5f122e6bb656fe"
        ),
        "sha3Uncles": (
            "0x1dcc4de8dec75d7aab85b567b6ccd41ad312451b948a7413f0a142fd40d49347"
        ),
        "difficulty": "0x0",
        "receiptsRoot": (
            "0x5ffefe7b059459dd6e1bdecba354eafa33fa0ae619383658bac39b817fdebeef"
        ),
        "stateRoot": (
            "0xfeed54faf6bb151112970b460118ed790197d69df7fcdd79801d120851723c88"
        ),
        "totalDifficulty": "0x9bf9a3",
        "transactionsRoot": (
            "0xafeedbeef5f30efc9baf28e49271302e9b569cfa1e8e9d9512360eb8e7c667a7"
        ),
        "transactions": [
            "0xfcdabb5af17478051493039875221e21282d64b4ed4cf9ba38dff222ecde2f88",
            "0x2636dba09e226a39ad90df7cc43c6a3b353ef6f3ba754f33507a3c29e47467eb",
        ],
        "withdrawalsRoot": (
            "0xfeed23dfefd5340fddc3b23bd6c84a32b8ea964ba16dc4c961ed7caa494cfefe"
        ),
        "withdrawals": [
            {
                "index": "0x3090f7",
                "validatorIndex": "0xbfe1",
                "address": "0xfe102287c050e5ba072211ad2C213eb5dae4feed",
                "amount": "0x3f695",
            },
            {
                "index": "0x309103",
                "validatorIndex": "0xbfed",
                "address": "0xf22E180C050E5AB072211AD2C213EB5AEE4DF123",
                "amount": "0x3f695",
            },
        ],
        "blobGasUsed": "0x7ffff",
        "excessBlobGas": "0x12c00000",
        "parentBeaconBlockRoot": (
            "0x6470e77f1b8a55a49a57b3f74c2a10a76185636d65122053752ea5e4bb4dac59"
        ),
    }

    with request_mocker(
        w3, mock_results={"eth_getBlockByNumber": unformatted_values_block}
    ):
        received_block = w3.eth.get_block("pending")

    assert received_block == {
        "baseFeePerGas": int(unformatted_values_block["baseFeePerGas"], 16),
        "extraData": HexBytes(unformatted_values_block["extraData"]),
        "gasLimit": int(unformatted_values_block["gasLimit"], 16),
        "gasUsed": int(unformatted_values_block["gasUsed"], 16),
        "size": int(unformatted_values_block["size"], 16),
        "timestamp": int(unformatted_values_block["timestamp"], 16),
        "hash": HexBytes(unformatted_values_block["hash"]),
        "logsBloom": HexBytes(unformatted_values_block["logsBloom"]),
        "miner": to_checksum_address(unformatted_values_block["miner"]),
        "mixHash": HexBytes(unformatted_values_block["mixHash"]),
        "nonce": HexBytes(unformatted_values_block["nonce"]),
        "number": int(unformatted_values_block["number"], 16),
        "parentHash": HexBytes(unformatted_values_block["parentHash"]),
        "sha3Uncles": HexBytes(unformatted_values_block["sha3Uncles"]),
        "difficulty": int(unformatted_values_block["difficulty"], 16),
        "receiptsRoot": HexBytes(unformatted_values_block["receiptsRoot"]),
        "stateRoot": HexBytes(unformatted_values_block["stateRoot"]),
        "totalDifficulty": int(unformatted_values_block["totalDifficulty"], 16),
        "transactionsRoot": HexBytes(unformatted_values_block["transactionsRoot"]),
        "transactions": [
            HexBytes(unformatted_values_block["transactions"][0]),
            HexBytes(unformatted_values_block["transactions"][1]),
        ],
        "withdrawalsRoot": HexBytes(unformatted_values_block["withdrawalsRoot"]),
        "withdrawals": [
            {
                "index": int(unformatted_values_block["withdrawals"][0]["index"], 16),
                "validatorIndex": int(
                    unformatted_values_block["withdrawals"][0]["validatorIndex"],
                    16,
                ),
                "address": to_checksum_address(
                    unformatted_values_block["withdrawals"][0]["address"]
                ),
                "amount": int(unformatted_values_block["withdrawals"][0]["amount"], 16),
            },
            {
                "index": int(unformatted_values_block["withdrawals"][1]["index"], 16),
                "validatorIndex": int(
                    unformatted_values_block["withdrawals"][1]["validatorIndex"],
                    16,
                ),
                "address": to_checksum_address(
                    unformatted_values_block["withdrawals"][1]["address"]
                ),
                "amount": int(unformatted_values_block["withdrawals"][1]["amount"], 16),
            },
        ],
        "blobGasUsed": int(unformatted_values_block["blobGasUsed"], 16),
        "excessBlobGas": int(unformatted_values_block["excessBlobGas"], 16),
        "parentBeaconBlockRoot": HexBytes(
            unformatted_values_block["parentBeaconBlockRoot"]
        ),
    }
