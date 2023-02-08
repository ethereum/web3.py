import pytest

import pytest_asyncio

from tests.utils import (
    get_open_port,
)
from web3 import (
    Web3,
)
from web3._utils.module_testing.go_ethereum_admin_module import (
    GoEthereumAsyncAdminModuleTest,
)
from web3._utils.module_testing.go_ethereum_personal_module import (
    GoEthereumAsyncPersonalModuleTest,
)
from web3.providers.async_rpc import (
    AsyncHTTPProvider,
)

from .common import (
    GoEthereumAdminModuleTest,
    GoEthereumAsyncEthModuleTest,
    GoEthereumAsyncNetModuleTest,
    GoEthereumAsyncTxPoolModuleTest,
    GoEthereumEthModuleTest,
    GoEthereumNetModuleTest,
    GoEthereumPersonalModuleTest,
    GoEthereumTest,
    GoEthereumTxPoolModuleTest,
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
            "admin,eth,net,web3,personal,miner,txpool",
            "--ipcdisable",
            "--allow-insecure-unlock",
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
    _w3 = Web3(Web3.HTTPProvider(endpoint_uri))
    return _w3


class TestGoEthereumTest(GoEthereumTest):
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


class TestGoEthereumEthModuleTest(GoEthereumEthModuleTest):
    pass


class TestGoEthereumNetModuleTest(GoEthereumNetModuleTest):
    pass


class TestGoEthereumPersonalModuleTest(GoEthereumPersonalModuleTest):
    pass


class TestGoEthereumTxPoolModuleTest(GoEthereumTxPoolModuleTest):
    pass


# -- async -- #


@pytest_asyncio.fixture(scope="module")
async def async_w3(geth_process, endpoint_uri):
    await wait_for_aiohttp(endpoint_uri)
    _w3 = Web3(AsyncHTTPProvider(endpoint_uri))
    return _w3


def async_w3_eth(async_w3):
    return async_w3.eth


class TestGoEthereumAsyncAdminModuleTest(GoEthereumAsyncAdminModuleTest):
    @pytest.mark.asyncio
    @pytest.mark.xfail(
        reason="running geth with the --nodiscover flag doesn't allow peer addition"
    )
    async def test_admin_peers(self, async_w3: "Web3") -> None:
        await super().test_admin_peers(async_w3)

    @pytest.mark.asyncio
    async def test_admin_start_stop_http(self, async_w3: "Web3") -> None:
        # This test causes all tests after it to fail on CI if it's allowed to run
        pytest.xfail(
            reason="Only one HTTP endpoint is allowed to be active at any time"
        )
        await super().test_admin_start_stop_http(async_w3)

    @pytest.mark.asyncio
    async def test_admin_start_stop_ws(self, async_w3: "Web3") -> None:
        # This test causes all tests after it to fail on CI if it's allowed to run
        pytest.xfail(reason="Only one WS endpoint is allowed to be active at any time")
        await super().test_admin_start_stop_ws(async_w3)


class TestGoEthereumAsyncNetModuleTest(GoEthereumAsyncNetModuleTest):
    pass


class TestGoEthereumAsyncPersonalModuleTest(GoEthereumAsyncPersonalModuleTest):
    pass


class TestGoEthereumAsyncEthModuleTest(GoEthereumAsyncEthModuleTest):
    pass


class TestGoEthereumAsyncTxPoolModuleTest(GoEthereumAsyncTxPoolModuleTest):
    pass
