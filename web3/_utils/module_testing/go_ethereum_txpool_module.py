import pytest
import random

from eth_typing import (
    ChecksumAddress,
)
from flaky import (
    flaky,
)

from web3._utils.threads import (
    Timeout,
)
from web3.main import (
    Web3,
)
from web3.types import (
    Wei,
)


class GoEthereumTxPoolModuleTest:

    @flaky(max_runs=3)
    def test_txpool_content(self, web3: "Web3", unlocked_account: ChecksumAddress) -> None:

        web3.geth.miner.stop()  # type: ignore

        with Timeout(60) as timeout:
            while web3.eth.hashrate or web3.eth.mining:
                timeout.sleep(random.random())

        txn_1_hash = web3.eth.send_transaction({
            'from': unlocked_account,
            'to': unlocked_account,
            'value': Wei(12345)
        })
        txn_1 = web3.eth.get_transaction(txn_1_hash)
        txn_2_hash = web3.eth.send_transaction({
            'from': unlocked_account,
            'to': unlocked_account,
            'value': Wei(54321)
        })
        txn_2 = web3.eth.get_transaction(txn_2_hash)

        content = web3.geth.txpool.content()  # type: ignore

        assert unlocked_account in content['pending']

        pending_txns = content['pending'][unlocked_account]

        assert str(txn_1['nonce']) in pending_txns
        assert str(txn_2['nonce']) in pending_txns

        assert pending_txns[str(txn_1['nonce'])]['hash'] == Web3.toHex(txn_1_hash)
        assert pending_txns[str(txn_1['nonce'])]['value'] == Web3.toHex(12345)
        assert pending_txns[str(txn_2['nonce'])]['hash'] == Web3.toHex(txn_2_hash)
        assert pending_txns[str(txn_2['nonce'])]['value'] == Web3.toHex(54321)

    @flaky(max_runs=3)
    def test_txpool_inspect(self, web3: "Web3", unlocked_account: ChecksumAddress) -> None:

        web3.geth.miner.stop()  # type: ignore

        with Timeout(60) as timeout:
            while web3.eth.hashrate or web3.eth.mining:
                timeout.sleep(random.random())

        txn_1_hash = web3.eth.send_transaction({
            'from': unlocked_account,
            'to': unlocked_account,
            'value': Wei(12345)
        })
        txn_1 = web3.eth.get_transaction(txn_1_hash)
        txn_2_hash = web3.eth.send_transaction({
            'from': unlocked_account,
            'to': unlocked_account,
            'value': Wei(54321)
        })
        txn_2 = web3.eth.get_transaction(txn_2_hash)

        inspect_content = web3.geth.txpool.inspect()  # type: ignore

        assert unlocked_account in inspect_content['pending']

        pending_txns = inspect_content['pending'][unlocked_account]

        assert str(txn_1['nonce']) in pending_txns
        assert str(txn_2['nonce']) in pending_txns

        txn_1_summary = pending_txns[str(txn_1['nonce'])]
        txn_2_summary = pending_txns[str(txn_2['nonce'])]

        assert unlocked_account in txn_1_summary
        assert '12345 wei' in txn_1_summary

        assert unlocked_account in txn_2_summary
        assert '54321 wei' in txn_2_summary

    def test_geth_txpool_status(self, web3: "Web3") -> None:
        test_data = web3.geth.txpool.status()  # type: ignore
        assert "pending" in test_data


class GoEthereumAsyncTxPoolModuleTest:

    @pytest.mark.asyncio
    async def test_async_geth_txpool_inspect(self, async_w3: "Web3") -> None:
        test_data = await async_w3.geth.txpool.inspect()  # type: ignore
        assert "pending" in test_data

    @pytest.mark.asyncio
    async def test_async_geth_txpool_content(self, async_w3: "Web3") -> None:
        test_data = await async_w3.geth.txpool.content()  # type: ignore
        assert "pending" in test_data

    @pytest.mark.asyncio
    async def test_async_geth_txpool_status(self, async_w3: "Web3") -> None:
        test_data = await async_w3.geth.txpool.status()  # type: ignore
        assert "pending" in test_data
