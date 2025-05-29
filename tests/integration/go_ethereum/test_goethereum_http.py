import pytest

from aiohttp import (
    ClientTimeout,
)
import pytest_asyncio

from web3 import (
    AsyncWeb3,
    AutoProvider,
    Web3,
)
from web3._utils.module_testing.go_ethereum_admin_module import (
    GoEthereumAsyncAdminModuleTest,
)
from web3.providers.rpc import (
    AsyncHTTPProvider,
)

from .common import (
    GoEthereumAdminModuleTest,
    GoEthereumAsyncDebugModuleTest,
    GoEthereumAsyncEthModuleTest,
    GoEthereumAsyncNetModuleTest,
    GoEthereumAsyncTxPoolModuleTest,
    GoEthereumAsyncWeb3ModuleTest,
    GoEthereumDebugModuleTest,
    GoEthereumEthModuleTest,
    GoEthereumNetModuleTest,
    GoEthereumTxPoolModuleTest,
    GoEthereumWeb3ModuleTest,
)


def _geth_command_arguments(base_geth_command_arguments, geth_version):
    yield from base_geth_command_arguments
    if geth_version.major == 1:
        yield from (
            "--http",
            "--http.port",
            "0",
            "--http.api",
            "admin,debug,eth,net,web3,txpool",
            "--ipcdisable",
        )
    else:
        raise AssertionError("Unsupported Geth version")


@pytest.fixture
def geth_command_arguments(base_geth_command_arguments, get_geth_version):
    return _geth_command_arguments(base_geth_command_arguments, get_geth_version)


@pytest.fixture
def w3(start_geth_process_and_yield_port):
    port = start_geth_process_and_yield_port
    _w3 = Web3(
        Web3.HTTPProvider(f"http://127.0.0.1:{port}", request_kwargs={"timeout": 10})
    )
    return _w3


@pytest.fixture
def auto_w3(start_geth_process_and_yield_port, monkeypatch):
    from web3.auto import (
        w3,
    )

    port = start_geth_process_and_yield_port
    monkeypatch.setenv("WEB3_PROVIDER_URI", f"http://127.0.0.1:{port}")

    return w3


class TestGoEthereumWeb3ModuleTest(GoEthereumWeb3ModuleTest):
    pass


class TestGoEthereumAdminModuleTest(GoEthereumAdminModuleTest):
    @pytest.mark.xfail(
        reason="running geth with the --nodiscover flag doesn't allow peer addition"
    )
    def test_admin_peers(self, w3: "Web3") -> None:
        super().test_admin_peers(w3)

    def test_admin_start_stop_http(self, w3: "Web3") -> None:
        # This test causes all tests after it to fail on CI if it's allowed to run
        pytest.xfail(
            reason="Only one HTTP endpoint is allowed to be active at any time"
        )
        super().test_admin_start_stop_http(w3)

    def test_admin_start_stop_ws(self, w3: "Web3") -> None:
        # This test causes all tests after it to fail on CI if it's allowed to run
        pytest.xfail(reason="Only one WS endpoint is allowed to be active at any time")
        super().test_admin_start_stop_ws(w3)


class TestGoEthereumDebugModuleTest(GoEthereumDebugModuleTest):
    pass


class TestGoEthereumEthModuleTest(GoEthereumEthModuleTest):
    def test_auto_provider_batching(self, auto_w3: "Web3") -> None:
        with auto_w3.batch_requests() as batch:
            assert isinstance(auto_w3.provider, AutoProvider)
            assert auto_w3.provider._is_batching
            assert auto_w3.provider._batching_context is not None
            batch.add(auto_w3.eth.get_block("latest"))
            batch.add(auto_w3.eth.get_block("earliest"))
            batch.add(auto_w3.eth.get_block("pending"))
            results = batch.execute()

        assert not auto_w3.provider._is_batching
        assert len(results) == 3


class TestGoEthereumNetModuleTest(GoEthereumNetModuleTest):
    pass


class TestGoEthereumTxPoolModuleTest(GoEthereumTxPoolModuleTest):
    pass


# -- async -- #


@pytest_asyncio.fixture
async def async_w3(start_geth_process_and_yield_port):
    port = start_geth_process_and_yield_port
    _w3 = AsyncWeb3(
        AsyncHTTPProvider(
            f"http://127.0.0.1:{port}", request_kwargs={"timeout": ClientTimeout(10)}
        )
    )
    yield _w3
    await _w3.provider.disconnect()


class TestGoEthereumAsyncWeb3ModuleTest(GoEthereumAsyncWeb3ModuleTest):
    pass


class TestGoEthereumAsyncAdminModuleTest(GoEthereumAsyncAdminModuleTest):
    @pytest.mark.asyncio
    @pytest.mark.xfail(
        reason="running geth with the --nodiscover flag doesn't allow peer addition"
    )
    async def test_admin_peers(self, async_w3: "AsyncWeb3") -> None:
        await super().test_admin_peers(async_w3)

    @pytest.mark.asyncio
    async def test_admin_start_stop_http(self, async_w3: "AsyncWeb3") -> None:
        # This test causes all tests after it to fail on CI if it's allowed to run
        pytest.xfail(
            reason="Only one HTTP endpoint is allowed to be active at any time"
        )
        await super().test_admin_start_stop_http(async_w3)

    @pytest.mark.asyncio
    async def test_admin_start_stop_ws(self, async_w3: "AsyncWeb3") -> None:
        # This test causes all tests after it to fail on CI if it's allowed to run
        pytest.xfail(reason="Only one WS endpoint is allowed to be active at any time")
        await super().test_admin_start_stop_ws(async_w3)


class TestGoEthereumAsyncDebugModuleTest(GoEthereumAsyncDebugModuleTest):
    pass


class TestGoEthereumAsyncNetModuleTest(GoEthereumAsyncNetModuleTest):
    pass


class TestGoEthereumAsyncEthModuleTest(GoEthereumAsyncEthModuleTest):
    @pytest.mark.asyncio
    async def test_async_http_provider_disconnects_gracefully(self, async_w3) -> None:
        w3_1 = async_w3

        w3_2 = AsyncWeb3(AsyncHTTPProvider(async_w3.provider.endpoint_uri))
        assert w3_1 != w3_2

        await w3_1.eth.get_block("latest")
        await w3_2.eth.get_block("latest")

        w3_1_session_cache = w3_1.provider._request_session_manager.session_cache
        w3_2_session_cache = w3_2.provider._request_session_manager.session_cache

        for _, session in w3_1_session_cache.items():
            assert not session.closed
        for _, session in w3_2_session_cache.items():
            assert not session.closed
        assert w3_1_session_cache != w3_2_session_cache

        await w3_1.provider.disconnect()
        await w3_2.provider.disconnect()

        assert len(w3_1_session_cache) == 0
        assert len(w3_2_session_cache) == 0

    @pytest.mark.asyncio
    async def test_async_http_provider_reuses_cached_session(self, async_w3) -> None:
        await async_w3.eth.get_block("latest")
        session_cache = async_w3.provider._request_session_manager.session_cache
        assert len(session_cache) == 1
        session = list(session_cache._data.values())[0]

        await async_w3.eth.get_block("latest")
        assert len(session_cache) == 1
        assert session == list(session_cache._data.values())[0]
        await async_w3.provider.disconnect()
        assert len(session_cache) == 0


class TestGoEthereumAsyncTxPoolModuleTest(GoEthereumAsyncTxPoolModuleTest):
    pass
