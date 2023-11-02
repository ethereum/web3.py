import asyncio
import json
import pytest
from typing import (
    TYPE_CHECKING,
    Any,
    Dict,
    Tuple,
    cast,
)

from eth_utils import (
    is_hexstr,
    to_bytes,
)
from hexbytes import (
    HexBytes,
)

from web3.datastructures import (
    AttributeDict,
)
from web3.middleware import (
    async_geth_poa_middleware,
)
from web3.types import (
    FormattedEthSubscriptionResponse,
)

if TYPE_CHECKING:
    from web3.main import (
        _PersistentConnectionWeb3,
    )


def _mocked_recv(sub_id: str, ws_subscription_response: Dict[str, Any]) -> bytes:
    # Must be same subscription id so we can know how to parse the message.
    # We don't have this information when mocking the response.
    ws_subscription_response["params"]["subscription"] = sub_id
    return to_bytes(text=json.dumps(ws_subscription_response))


class PersistentConnectionProviderTest:
    @pytest.mark.asyncio
    @pytest.mark.parametrize(
        "subscription_params,ws_subscription_response,expected_formatted_result",
        (
            (
                ("newHeads",),
                {
                    "jsonrpc": "2.0",
                    "method": "eth_subscription",
                    "params": {
                        "subscription": "THIS_WILL_BE_REPLACED_IN_THE_TEST",
                        "result": {
                            "number": "0x539",
                            "hash": "0xb46b85928f2c2264c2bf7ad5c6d6985664f1527e744193ef990cc0d3da5afc5e",  # noqa: E501
                            "parentHash": "0xb46b85928f2c2264c2bf7ad5c6d6985664f1527e744193ef990cc0d3da5afc5e",  # noqa: E501
                            "sha3Uncles": "0x1dcc4de8dec75d7aab85b567b6ccd41ad312451b948a7413f0a142fd40d49347",  # noqa: E501
                            "logsBloom": "0x00",
                            "transactionsRoot": "0x56260fe8298aff6d360e3a68fa855693f25dcb2708d8a7e509e8519b265d3988",  # noqa: E501
                            "stateRoot": "0x56260fe8298aff6d360e3a68fa855693f25dcb2708d8a7e509e8519b265d3988",  # noqa: E501
                            "receiptsRoot": "0x56260fe8298aff6d360e3a68fa855693f25dcb2708d8a7e509e8519b265d3988",  # noqa: E501
                            "miner": "0x0000000000000000000000000000000000000000",
                            "difficulty": "0x0",
                            "extraData": "0x496c6c756d696e61746520446d6f63726174697a6520447374726962757465",  # noqa: E501
                            "gasLimit": "0x1c9c380",
                            "gasUsed": "0xd1ce44",
                            "timestamp": "0x539",
                            "baseFeePerGas": "0x26f93fef9",
                            "withdrawalsRoot": "0x56260fe8298aff6d360e3a68fa855693f25dcb2708d8a7e509e8519b265d3988",  # noqa: E501
                            "nonce": "0x0000000000000000",
                            "mixHash": "0x73e9e036ec894047f29954571d4b6d9e8717de7304269c263cbf150caa4e0768",  # noqa: E501
                        },
                    },
                },
                AttributeDict(
                    {
                        "number": 1337,
                        "hash": HexBytes(
                            "0xb46b85928f2c2264c2bf7ad5c6d6985664f1527e744193ef990cc0d3da5afc5e"  # noqa: E501
                        ),
                        "parentHash": HexBytes(
                            "0xb46b85928f2c2264c2bf7ad5c6d6985664f1527e744193ef990cc0d3da5afc5e"  # noqa: E501
                        ),
                        "sha3Uncles": HexBytes(
                            "0x1dcc4de8dec75d7aab85b567b6ccd41ad312451b948a7413f0a142fd40d49347"  # noqa: E501
                        ),
                        "logsBloom": HexBytes("0x00"),
                        "transactionsRoot": HexBytes(
                            "0x56260fe8298aff6d360e3a68fa855693f25dcb2708d8a7e509e8519b265d3988"  # noqa: E501
                        ),
                        "stateRoot": HexBytes(
                            "0x56260fe8298aff6d360e3a68fa855693f25dcb2708d8a7e509e8519b265d3988"  # noqa: E501
                        ),
                        "receiptsRoot": HexBytes(
                            "0x56260fe8298aff6d360e3a68fa855693f25dcb2708d8a7e509e8519b265d3988"  # noqa: E501
                        ),
                        "miner": "0x0000000000000000000000000000000000000000",
                        "difficulty": 0,
                        "extraData": HexBytes(
                            "0x496c6c756d696e61746520446d6f63726174697a6520447374726962757465"  # noqa: E501
                        ),
                        "gasLimit": 30000000,
                        "gasUsed": 13749828,
                        "timestamp": 1337,
                        "baseFeePerGas": 10461904633,
                        "withdrawalsRoot": HexBytes(
                            "0x56260fe8298aff6d360e3a68fa855693f25dcb2708d8a7e509e8519b265d3988"  # noqa: E501
                        ),
                        "nonce": HexBytes("0x0000000000000000"),
                        "mixHash": HexBytes(
                            "0x73e9e036ec894047f29954571d4b6d9e8717de7304269c263cbf150caa4e0768"  # noqa: E501
                        ),
                    }
                ),
            ),
            (
                ("newPendingTransactions", True),
                {
                    "jsonrpc": "2.0",
                    "method": "eth_subscription",
                    "params": {
                        "subscription": "THIS_WILL_BE_REPLACED_IN_THE_TEST",
                        "result": {
                            "blockHash": None,
                            "blockNumber": None,
                            "from": "0x0000000000000000000000000000000000000000",
                            "gas": "0xf2f4",
                            "gasPrice": "0x29035f36f",
                            "maxFeePerGas": "0x29035f36f",
                            "maxPriorityFeePerGas": "0x3b9aca00",
                            "hash": "0xb46b85928f2c2264c2bf7ad5c6d6985664f1527e744193ef990cc0d3da5afc5e",  # noqa: E501
                            "input": "0x00",
                            "nonce": "0x2013",
                            "to": "0x0000000000000000000000000000000000000000",
                            "transactionIndex": None,
                            "value": "0x0",
                            "type": "0x2",
                            "accessList": [],
                            "chainId": "0x1",
                            "v": "0x1",
                            "r": "0x3c144a7c00ed3118d55445cd5be2ae4620ca377f7c685e9c5f3687671d4dece1",  # noqa: E501
                            "s": "0x284de67cbf75fec8a9edb368dee3a37cf6faba87f0af4413b2f869ebfa87d002",  # noqa: E501
                            "yParity": "0x1",
                        },
                    },
                },
                AttributeDict(
                    {
                        "blockHash": None,
                        "blockNumber": None,
                        "from": "0x0000000000000000000000000000000000000000",
                        "gas": 62196,
                        "gasPrice": 11009389423,
                        "maxFeePerGas": 11009389423,
                        "maxPriorityFeePerGas": 1000000000,
                        "hash": HexBytes(
                            "0xb46b85928f2c2264c2bf7ad5c6d6985664f1527e744193ef990cc0d3da5afc5e"  # noqa: E501
                        ),
                        "input": HexBytes("0x00"),
                        "nonce": 8211,
                        "to": "0x0000000000000000000000000000000000000000",
                        "transactionIndex": None,
                        "value": 0,
                        "type": 2,
                        "accessList": [],
                        "chainId": 1,
                        "v": 1,
                        "r": HexBytes(
                            "0x3c144a7c00ed3118d55445cd5be2ae4620ca377f7c685e9c5f3687671d4dece1"  # noqa: E501
                        ),
                        "s": HexBytes(
                            "0x284de67cbf75fec8a9edb368dee3a37cf6faba87f0af4413b2f869ebfa87d002"  # noqa: E501
                        ),
                        "yParity": 1,
                    }
                ),
            ),
            (
                ("newPendingTransactions", False),
                {
                    "jsonrpc": "2.0",
                    "method": "eth_subscription",
                    "params": {
                        "subscription": "THIS_WILL_BE_REPLACED_IN_THE_TEST",
                        "result": "0xb46b85928f2c2264c2bf7ad5c6d6985664f1527e744193ef990cc0d3da5afc5e",  # noqa: E501
                    },
                },
                HexBytes(
                    "0xb46b85928f2c2264c2bf7ad5c6d6985664f1527e744193ef990cc0d3da5afc5e"
                ),
            ),
            (
                ("logs", {"address": "0xC02aaA39b223FE8D0A0e5C4F27eAD9083C756Cc2"}),
                {
                    "jsonrpc": "2.0",
                    "method": "eth_subscription",
                    "params": {
                        "subscription": "THIS_WILL_BE_REPLACED_IN_THE_TEST",
                        "result": {
                            "removed": False,
                            "logIndex": "0x0",
                            "transactionIndex": "0x0",
                            "transactionHash": "0x56260fe8298aff6d360e3a68fa855693f25dcb2708d8a7e509e8519b265d3988",  # noqa: E501
                            "blockHash": "0xb46b85928f2c2264c2bf7ad5c6d6985664f1527e744193ef990cc0d3da5afc5e",  # noqa: E501
                            "blockNumber": "0x539",
                            "address": "0xC02aaA39b223FE8D0A0e5C4F27eAD9083C756Cc2",
                            "data": "0x00",
                            "topics": [
                                "0xe1fffdd4923d04f559f4d29e8bfc6cda04eb5b0d3c460751c2402c5c5cc9105c",  # noqa: E501
                                "0x00000000000000000000000016250d5630b4cf539739df2c5dacb4c659f2482d",  # noqa: E501
                            ],
                        },
                    },
                },
                AttributeDict(
                    {
                        "removed": False,
                        "logIndex": 0,
                        "transactionIndex": 0,
                        "transactionHash": HexBytes(
                            "0x56260fe8298aff6d360e3a68fa855693f25dcb2708d8a7e509e8519b265d3988"  # noqa: E501
                        ),
                        "blockHash": HexBytes(
                            "0xb46b85928f2c2264c2bf7ad5c6d6985664f1527e744193ef990cc0d3da5afc5e"  # noqa: E501
                        ),
                        "blockNumber": 1337,
                        "address": "0xC02aaA39b223FE8D0A0e5C4F27eAD9083C756Cc2",
                        "data": HexBytes("0x00"),
                        "topics": [
                            HexBytes(
                                "0xe1fffdd4923d04f559f4d29e8bfc6cda04eb5b0d3c460751c2402c5c5cc9105c"  # noqa: E501
                            ),
                            HexBytes(
                                "0x00000000000000000000000016250d5630b4cf539739df2c5dacb4c659f2482d"  # noqa: E501
                            ),
                        ],
                    }
                ),
            ),
            (
                ("syncing",),
                {
                    "jsonrpc": "2.0",
                    "method": "eth_subscription",
                    "params": {
                        "subscription": "THIS_WILL_BE_REPLACED_IN_THE_TEST",
                        "result": False,
                    },
                },
                False,
            ),
            (
                ("syncing",),
                {
                    "jsonrpc": "2.0",
                    "method": "eth_subscription",
                    "params": {
                        "subscription": "THIS_WILL_BE_REPLACED_IN_THE_TEST",
                        "result": {
                            "isSyncing": True,
                            "startingBlock": "0x0",
                            "currentBlock": "0x4346fe",
                            "highestBlock": "0x434806",
                        },
                    },
                },
                AttributeDict(
                    {
                        "isSyncing": True,
                        "startingBlock": 0,
                        "currentBlock": 4409086,
                        "highestBlock": 4409350,
                    }
                ),
            ),
        ),
        ids=[
            "newHeads",
            "newPendingTransactions-FullTxs",
            "newPendingTransactions-TxHashes",
            "logs",
            "syncing-False",
            "syncing-True",
        ],
    )
    async def test_async_eth_subscribe_mocked(
        self,
        async_w3: "_PersistentConnectionWeb3",
        subscription_params: Tuple[Any, ...],
        ws_subscription_response: Dict[str, Any],
        expected_formatted_result: Any,
    ) -> None:
        sub_id = await async_w3.eth.subscribe(*subscription_params)
        assert is_hexstr(sub_id)

        async def _mocked_recv_coro() -> bytes:
            return _mocked_recv(sub_id, ws_subscription_response)

        actual_recv_fxn = async_w3.provider._ws.recv
        async_w3.provider._ws.__setattr__(
            "recv",
            _mocked_recv_coro,
        )

        async for msg in async_w3.ws.listen_to_websocket():
            response = cast(FormattedEthSubscriptionResponse, msg)
            assert response["subscription"] == sub_id
            assert response["result"] == expected_formatted_result

            # only testing one message, so break here
            break

        # reset the mocked recv
        async_w3.provider._ws.__setattr__("recv", actual_recv_fxn)

    @pytest.mark.asyncio
    async def test_async_geth_poa_middleware_on_eth_subscription(
        self,
        async_w3: "_PersistentConnectionWeb3",
    ) -> None:
        async_w3.middleware_onion.inject(
            async_geth_poa_middleware, "poa_middleware", layer=0
        )

        sub_id = await async_w3.eth.subscribe("newHeads")
        assert is_hexstr(sub_id)

        async def _mocked_recv_coro() -> bytes:
            return _mocked_recv(
                sub_id,
                {
                    "jsonrpc": "2.0",
                    "method": "eth_subscription",
                    "params": {
                        "subscription": sub_id,
                        "result": {
                            "extraData": f"0x{'00' * 100}",
                        },
                    },
                },
            )

        actual_recv_fxn = async_w3.provider._ws.recv
        async_w3.provider._ws.__setattr__(
            "recv",
            _mocked_recv_coro,
        )

        async for msg in async_w3.ws.listen_to_websocket():
            response = cast(FormattedEthSubscriptionResponse, msg)
            assert response.keys() == {"subscription", "result"}
            assert response["subscription"] == sub_id
            assert response["result"]["proofOfAuthorityData"] == HexBytes(  # type: ignore  # noqa: E501
                f"0x{'00' * 100}"
            )

            break

        # reset the mocked recv
        async_w3.provider._ws.__setattr__("recv", actual_recv_fxn)
        async_w3.middleware_onion.remove("poa_middleware")

    @pytest.mark.asyncio
    async def test_asyncio_gather_for_multiple_requests_matches_the_responses(
        self,
        async_w3: "_PersistentConnectionWeb3",
    ) -> None:
        (
            latest,
            chain_id,
            block_num,
            chain_id2,
            pending,
            chain_id3,
        ) = await asyncio.gather(
            async_w3.eth.get_block("latest"),
            async_w3.eth.chain_id,
            async_w3.eth.block_number,
            async_w3.eth.chain_id,
            async_w3.eth.get_block("pending"),
            async_w3.eth.chain_id,
        )

        # assert attrdict middleware was applied appropriately
        assert isinstance(latest, AttributeDict)
        assert isinstance(pending, AttributeDict)

        # assert block values
        some_block_keys = [
            "number",
            "hash",
            "parentHash",
            "transactionsRoot",
            "stateRoot",
            "receiptsRoot",
            "size",
            "gasLimit",
            "gasUsed",
            "timestamp",
            "transactions",
            "baseFeePerGas",
        ]
        assert all(k in latest.keys() for k in some_block_keys)
        assert all(k in pending.keys() for k in some_block_keys)

        assert isinstance(block_num, int)
        assert latest["number"] == block_num

        assert isinstance(chain_id, int)
        assert isinstance(chain_id2, int)
        assert isinstance(chain_id3, int)
