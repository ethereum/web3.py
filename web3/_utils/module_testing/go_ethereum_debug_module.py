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
    async def test_async_geth_debug_trace_transaction_opcode_logger(
        self, async_w3: "AsyncWeb3", txn_hash_with_log: HexStr
    ) -> None:
        result = await async_w3.geth.debug.trace_transaction(txn_hash_with_log)
        assert "structLogs" in dict(result).keys()
        assert "gas" in dict(result).keys()
        assert "failed" in dict(result).keys()

    @pytest.mark.asyncio
    async def test_async_geth_debug_trace_transaction_call_tracer(
        self, async_w3: "AsyncWeb3", txn_hash_with_log: HexStr
    ) -> None:
        result = await async_w3.geth.debug.trace_transaction(
            txn_hash_with_log, {"tracer": "callTracer"}
        )
        assert result.get("type") == "CALL"

    @pytest.mark.asyncio
    async def test_async_geth_debug_trace_transaction_prestate_tracer(
        self, async_w3: "AsyncWeb3", txn_hash_with_log: HexStr
    ) -> None:
        result = await async_w3.geth.debug.trace_transaction(
            txn_hash_with_log,
            {"tracer": "prestateTracer", "tracerConfig": {"diffMode": True}},
        )
        assert "post" in dict(result).keys()
        assert "pre" in dict(result).keys()


class GoEthereumDebugModuleTest:
    def test_geth_debug_trace_transaction_opcode_logger(
        self, w3: "Web3", txn_hash_with_log: HexStr
    ) -> None:
        result = w3.geth.debug.trace_transaction(txn_hash_with_log)
        assert "structLogs" in dict(result).keys()
        assert "gas" in dict(result).keys()
        assert "failed" in dict(result).keys()

    def test_geth_debug_trace_transaction_call_tracer(
        self, w3: "Web3", txn_hash_with_log: HexStr
    ) -> None:
        result = w3.geth.debug.trace_transaction(
            txn_hash_with_log, {"tracer": "callTracer"}
        )
        assert result.get("type") == "CALL"

    def test_geth_debug_trace_transaction_prestate_tracer(
        self, w3: "Web3", txn_hash_with_log: HexStr
    ) -> None:
        result = w3.geth.debug.trace_transaction(
            txn_hash_with_log,
            {"tracer": "prestateTracer", "tracerConfig": {"diffMode": True}},
        )
        assert "post" in dict(result).keys()
        assert "pre" in dict(result).keys()
