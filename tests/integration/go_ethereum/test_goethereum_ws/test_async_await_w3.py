import pytest

import pytest_asyncio

from web3 import (
    AsyncWeb3,
    WebSocketProvider,
)
from web3._utils.module_testing.go_ethereum_admin_module import (
    GoEthereumAsyncAdminModuleTest,
)
from web3._utils.module_testing.persistent_connection_provider import (
    PersistentConnectionProviderTest,
)

from ..common import (
    GoEthereumAsyncEthModuleTest,
    GoEthereumAsyncNetModuleTest,
    GoEthereumAsyncWeb3ModuleTest,
)
from ..utils import (
    wait_for_aiohttp,
)


@pytest_asyncio.fixture(scope="module")
async def async_w3(geth_process, endpoint_uri):
    await wait_for_aiohttp(endpoint_uri)

    # await the persistent connection itself
    return await AsyncWeb3(WebSocketProvider(endpoint_uri))


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
        # This test inconsistently causes all tests after it to
        # fail on CI if it's allowed to run
        pytest.xfail(
            reason="Only one WebSocket endpoint is allowed to be active at any time"
        )
        await super().test_admin_start_stop_ws(async_w3)


class TestPersistentConnectionProviderTest(PersistentConnectionProviderTest):
    pass


class TestGoEthereumAsyncEthModuleTest(GoEthereumAsyncEthModuleTest):
    pass


class TestGoEthereumAsyncNetModuleTest(GoEthereumAsyncNetModuleTest):
    pass
