import pytest

from eth_typing import (
    HexStr,
)

from web3 import (
    AsyncWeb3,
    Web3,
)


class GoEthereumAsyncDebugModuleTest:
    @pytest.mark.asyncio
    async def test_async_geth_debug_trace_transaction_calltracer(
        self, async_w3: "AsyncWeb3", txn_hash_with_log: HexStr
    ) -> None:
        result = await async_w3.geth.debug.trace_transaction(
            txn_hash_with_log, {"tracer": "callTracer"}
        )
        assert result["type"] in ["CALL", "CREATE"]


class GoEthereumDebugModuleTest:
    def test_geth_debug_trace_transaction_calltracer(
        self, w3: "Web3", txn_hash_with_log: HexStr
    ) -> None:
        result = w3.geth.debug.trace_transaction(
            txn_hash_with_log, {"tracer": "callTracer"}
        )
        assert result["type"] in ["CALL", "CREATE"]
