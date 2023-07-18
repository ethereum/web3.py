import pytest

import pytest_asyncio

from tests.integration.common import (
    COINBASE,
)
from tests.utils import (
    get_open_port,
)
from web3 import (
    AsyncWeb3,
    WebsocketProviderV2,
)
from web3._utils.module_testing.go_ethereum_admin_module import (
    GoEthereumAsyncAdminModuleTest,
)
from web3._utils.module_testing.go_ethereum_personal_module import (
    GoEthereumAsyncPersonalModuleTest,
)

from .common import (
    GoEthereumAsyncEthModuleTest,
    GoEthereumAsyncNetModuleTest,
)
from .utils import (
    wait_for_aiohttp,
)


@pytest.fixture(scope="module")
def ws_port():
    return get_open_port()


@pytest.fixture(scope="module")
def endpoint_uri(ws_port):
    return f"ws://localhost:{ws_port}"


def _geth_command_arguments(ws_port, base_geth_command_arguments, geth_version):
    yield from base_geth_command_arguments
    if geth_version.major == 1:
        yield from (
            "--miner.etherbase",
            COINBASE[2:],
            "--ws",
            "--ws.port",
            ws_port,
            "--ws.api",
            "admin,eth,net,web3,personal,miner",
            "--ws.origins",
            "*",
            "--ipcdisable",
            "--allow-insecure-unlock",
        )
        if geth_version.minor not in [10, 11]:
            raise AssertionError("Unsupported Geth version")
    else:
        raise AssertionError("Unsupported Geth version")


@pytest.fixture(scope="module")
def geth_command_arguments(
    geth_binary, get_geth_version, datadir, ws_port, base_geth_command_arguments
):
    return _geth_command_arguments(
        ws_port, base_geth_command_arguments, get_geth_version
    )


@pytest_asyncio.fixture(scope="module")
async def async_w3(geth_process, endpoint_uri):
    await wait_for_aiohttp(endpoint_uri)
    async with AsyncWeb3.persistent_websocket(
        WebsocketProviderV2(endpoint_uri, call_timeout=30)
    ) as w3:
        yield w3


class TestGoEthereumAsyncAdminModuleTest(GoEthereumAsyncAdminModuleTest):
    @pytest.mark.xfail(
        reason="running geth with the --nodiscover flag doesn't allow peer addition"
    )
    async def test_admin_peers(self, async_w3: "AsyncWeb3") -> None:
        await super().test_admin_peers(async_w3)

    async def test_admin_start_stop_http(self, async_w3: "AsyncWeb3") -> None:
        # This test causes all tests after it to fail on CI if it's allowed to run
        pytest.xfail(
            reason="Only one HTTP endpoint is allowed to be active at any time"
        )
        await super().test_admin_start_stop_http(async_w3)

    async def test_admin_start_stop_ws(self, async_w3: "AsyncWeb3") -> None:
        # This test inconsistently causes all tests after it to
        # fail on CI if it's allowed to run
        pytest.xfail(
            reason="Only one WebSocket endpoint is allowed to be active at any time"
        )
        await super().test_admin_start_stop_ws(async_w3)


class TestGoEthereumAsyncEthModuleTest(GoEthereumAsyncEthModuleTest):
    pass


class TestGoEthereumAsyncNetModuleTest(GoEthereumAsyncNetModuleTest):
    pass


class TestGoEthereumAsyncPersonalModuleTest(GoEthereumAsyncPersonalModuleTest):
    pass
