import os
import pytest
import tempfile

from web3 import Web3

from .common import (
    GoEthereumEthModuleTest,
    GoEthereumNetModuleTest,
    GoEthereumPersonalModuleTest,
    GoEthereumTest,
    GoEthereumVersionModuleTest,
)
from .utils import (
    get_open_port,
    wait_for_socket,
)


@pytest.fixture(scope='module')
def geth_command_arguments(geth_binary, datadir, geth_ipc_path):
    geth_port = get_open_port()
    return (
        geth_binary,
        '--datadir', str(datadir),
        '--ipcpath', geth_ipc_path,
        '--nodiscover',
        '--fakepow',
        '--port', geth_port,
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


class TestGoEthereumEthModuleTest(GoEthereumEthModuleTest):
    pass


class TestGoEthereumVersionModuleTest(GoEthereumVersionModuleTest):
    pass


class TestGoEthereumNetModuleTest(GoEthereumNetModuleTest):
    pass


class TestGoEthereumPersonalModuleTest(GoEthereumPersonalModuleTest):
    pass
