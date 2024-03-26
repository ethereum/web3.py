import asyncio
import pytest

from tests.integration.common import (
    COINBASE,
    MiscWebSocketTest,
)
from tests.utils import (
    get_open_port,
    wait_for_ws,
)
from web3 import (
    Web3,
)

from .common import (
    GoEthereumAdminModuleTest,
    GoEthereumEthModuleTest,
    GoEthereumNetModuleTest,
    GoEthereumWeb3ModuleTest,
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
            "admin,eth,net,web3",
            "--ws.origins",
            "*",
            "--ipcdisable",
            "--allow-insecure-unlock",
        )
        if geth_version.minor not in [13, 14]:
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


@pytest.fixture(scope="module")
def w3(geth_process, endpoint_uri):
    event_loop = asyncio.new_event_loop()
    event_loop.run_until_complete(wait_for_ws(endpoint_uri))
    _w3 = Web3(Web3.LegacyWebSocketProvider(endpoint_uri, websocket_timeout=30))
    return _w3


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
        # This test inconsistently causes all tests after it to
        # fail on CI if it's allowed to run
        pytest.xfail(
            reason="Only one WebSocket endpoint is allowed to be active at any time"
        )
        super().test_admin_start_stop_ws(w3)


class TestGoEthereumEthModuleTest(GoEthereumEthModuleTest):
    pass


class TestGoEthereumNetModuleTest(GoEthereumNetModuleTest):
    pass


class TestMiscWebSocketTest(MiscWebSocketTest):
    pass
