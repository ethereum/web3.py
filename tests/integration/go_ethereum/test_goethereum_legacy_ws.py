import pytest

from tests.integration.common import (
    COINBASE,
    MiscWebSocketTest,
)
from web3 import (
    Web3,
)

from .common import (
    GoEthereumAdminModuleTest,
    GoEthereumDebugModuleTest,
    GoEthereumEthModuleTest,
    GoEthereumNetModuleTest,
    GoEthereumWeb3ModuleTest,
)


def _geth_command_arguments(base_geth_command_arguments, geth_version):
    yield from base_geth_command_arguments
    if geth_version.major == 1:
        yield from (
            "--miner.etherbase",
            COINBASE[2:],
            "--ws",
            "--ws.port",
            "0",
            "--ws.api",
            "admin,debug,eth,net,web3",
            "--ws.origins",
            "*",
            "--ipcdisable",
            "--allow-insecure-unlock",
        )
        if geth_version.minor not in [13, 14, 15, 16]:
            # TODO: remove support for 13 + 14 in next major version
            raise AssertionError("Unsupported Geth version")
    else:
        raise AssertionError("Unsupported Geth version")


@pytest.fixture
def geth_command_arguments(
    geth_binary, get_geth_version, datadir, base_geth_command_arguments
):
    return _geth_command_arguments(base_geth_command_arguments, get_geth_version)


@pytest.fixture
def w3(start_geth_process_and_yield_port):
    port = start_geth_process_and_yield_port
    endpoint_uri = f"ws://127.0.0.1:{port}"
    _w3 = Web3(Web3.LegacyWebSocketProvider(endpoint_uri, websocket_timeout=30))
    return _w3


@pytest.mark.skip("LegacyWebSocketProvider does not support concurrent requests")
class TestGoEthereumWeb3ModuleTest(GoEthereumWeb3ModuleTest):
    def test_batch_requests_concurrently_with_regular_requests(
        self, w3: "Web3"
    ) -> None:
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


class TestGoEthereumDebugModuleTest(GoEthereumDebugModuleTest):
    pass


class TestGoEthereumEthModuleTest(GoEthereumEthModuleTest):
    pass


class TestGoEthereumNetModuleTest(GoEthereumNetModuleTest):
    pass


class TestMiscWebSocketTest(MiscWebSocketTest):
    pass
