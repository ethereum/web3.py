import os
import pytest
import tempfile

from tests.utils import (
    get_open_port,
)
from web3 import Web3

from .common import (
    GoEthereumAdminModuleTest,
    GoEthereumEthModuleTest,
    GoEthereumNetModuleTest,
    GoEthereumPersonalModuleTest,
    GoEthereumTest,
    GoEthereumVersionModuleTest,
)
from .utils import (
    wait_for_socket,
)


def _geth_command_arguments(geth_ipc_path,
                            base_geth_command_arguments):

    geth_port = get_open_port()
    yield from base_geth_command_arguments
    yield from (
        '--port', geth_port,
        '--ipcpath', geth_ipc_path,
    )


@pytest.fixture(scope='module')
def geth_command_arguments(geth_ipc_path,
                           base_geth_command_arguments):

    return _geth_command_arguments(
        geth_ipc_path,
        base_geth_command_arguments
    )


@pytest.fixture(scope='module')
def geth_ipc_path(datadir):
    geth_ipc_dir_path = tempfile.mkdtemp()
    _geth_ipc_path = os.path.join(geth_ipc_dir_path, 'geth.ipc')
    yield _geth_ipc_path

    if os.path.exists(_geth_ipc_path):
        os.remove(_geth_ipc_path)


@pytest.fixture(scope="module")
def web3(geth_process, geth_ipc_path):
    wait_for_socket(geth_ipc_path)
    _web3 = Web3(Web3.IPCProvider(geth_ipc_path))
    return _web3


class TestGoEthereumTest(GoEthereumTest):
    pass


class TestGoEthereumAdminModuleTest(GoEthereumAdminModuleTest):
    @pytest.mark.xfail(reason="running geth with the --nodiscover flag doesn't allow peer addition")
    def test_admin_peers(web3):
        super().test_admin_peers(web3)

    @pytest.mark.xfail(reason="websockets aren't enabled with our IPC flags")
    def test_admin_start_stop_ws(web3):
        super().test_admin_start_stop_ws(web3)


class TestGoEthereumEthModuleTest(GoEthereumEthModuleTest):
    pass


class TestGoEthereumVersionModuleTest(GoEthereumVersionModuleTest):
    pass


class TestGoEthereumNetModuleTest(GoEthereumNetModuleTest):
    pass


class TestGoEthereumPersonalModuleTest(GoEthereumPersonalModuleTest):
    pass
