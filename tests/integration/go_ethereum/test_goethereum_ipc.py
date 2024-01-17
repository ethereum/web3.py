import os
import pytest
import tempfile

from tests.integration.common import (
    COINBASE,
)
from web3 import (
    Web3,
)

from .common import (
    GoEthereumAdminModuleTest,
    GoEthereumEthModuleTest,
    GoEthereumNetModuleTest,
    GoEthereumPersonalModuleTest,
    GoEthereumTest,
)
from .utils import (
    wait_for_socket,
)


def _geth_command_arguments(geth_ipc_path, base_geth_command_arguments):
    yield from base_geth_command_arguments
    yield from (
        "--ipcpath",
        geth_ipc_path,
        "--miner.etherbase",
        COINBASE[2:],
        "--rpc.enabledeprecatedpersonal",
    )


@pytest.fixture(scope="module")
def geth_command_arguments(geth_ipc_path, base_geth_command_arguments):
    return _geth_command_arguments(geth_ipc_path, base_geth_command_arguments)


@pytest.fixture(scope="module")
def geth_ipc_path(datadir):
    geth_ipc_dir_path = tempfile.mkdtemp()
    _geth_ipc_path = os.path.join(geth_ipc_dir_path, "geth.ipc")
    yield _geth_ipc_path

    if os.path.exists(_geth_ipc_path):
        os.remove(_geth_ipc_path)


@pytest.fixture(scope="module")
def w3(geth_process, geth_ipc_path):
    wait_for_socket(geth_ipc_path)
    _w3 = Web3(Web3.IPCProvider(geth_ipc_path, timeout=30))
    return _w3


class TestGoEthereumTest(GoEthereumTest):
    pass


class TestGoEthereumAdminModuleTest(GoEthereumAdminModuleTest):
    @pytest.mark.xfail(
        reason="running geth with the --nodiscover flag doesn't allow peer addition"
    )
    def test_admin_peers(w3):
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
