import pytest

from aiohttp import (
    ClientTimeout,
)
import pytest_asyncio

from tests.utils import (
    get_open_port,
)
from web3 import (
    AsyncWeb3,
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
from .utils import (
    wait_for_aiohttp,
    wait_for_http,
)


@pytest.fixture(scope="module")
def rpc_port():
    return get_open_port()


@pytest.fixture(scope="module")
def endpoint_uri(rpc_port):
    return f"http://localhost:{rpc_port}"


def _geth_command_arguments(rpc_port, base_geth_command_arguments, geth_version):
    yield from base_geth_command_arguments
    if geth_version.major == 1:
        yield from (
            "--http",
            "--http.port",
            rpc_port,
            "--http.api",
            "admin,debug,eth,net,web3,txpool",
            "--ipcdisable",
        )
    else:
        raise AssertionError("Unsupported Geth version")


@pytest.fixture(scope="module")
def geth_command_arguments(rpc_port, base_geth_command_arguments, get_geth_version):
    return _geth_command_arguments(
        rpc_port, base_geth_command_arguments, get_geth_version
    )


@pytest.fixture(scope="module")
def w3(geth_process, endpoint_uri):
    wait_for_http(endpoint_uri)
    return Web3(Web3.HTTPProvider(endpoint_uri, request_kwargs={"timeout": 10}))


@pytest.fixture(scope="module")
def auto_w3(geth_process, endpoint_uri):
    wait_for_http(endpoint_uri)

    from web3.auto import (
        w3,
    )

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
    def test_auto_provider_batching(
        self,
        auto_w3: "Web3",
        monkeypatch,
        endpoint_uri,
    ) -> None:
        monkeypatch.setenv("WEB3_PROVIDER_URI", endpoint_uri)
        # test that batch_requests doesn't error out when using the auto provider
        auto_w3.batch_requests()


class TestGoEthereumNetModuleTest(GoEthereumNetModuleTest):
    pass


class TestGoEthereumTxPoolModuleTest(GoEthereumTxPoolModuleTest):
    pass


# -- async -- #


@pytest_asyncio.fixture(scope="module")
async def async_w3(geth_process, endpoint_uri):
    await wait_for_aiohttp(endpoint_uri)
    _w3 = AsyncWeb3(
        AsyncHTTPProvider(endpoint_uri, request_kwargs={"timeout": ClientTimeout(10)})
    )
    return _w3


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
    async def test_async_http_provider_disconnects_gracefully(
        self, async_w3, endpoint_uri
    ) -> None:
        w3_1 = async_w3

        w3_2 = AsyncWeb3(AsyncHTTPProvider(endpoint_uri))
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
