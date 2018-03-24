import os
import pytest
import random
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
    wait_for_http,
)


@pytest.fixture(scope="module")
def rpc_port():
    return random.choice(range(8000, 9000))


@pytest.fixture(scope="module")
def endpoint_uri(rpc_port):
    return 'http://localhost:{}'.format(rpc_port)


@pytest.fixture(scope='module')
def geth_command_arguments(geth_binary, datadir, rpc_port):
    return (
        geth_binary,
        '--datadir', str(datadir),
        '--nodiscover',
        '--fakepow',
        '--rpc',
        '--rpcport', str(rpc_port),
        '--rpcapi', 'db,eth,net,web3,personal,web3',
        '--ipcdisable',
    )


@pytest.fixture(scope='module')
def geth_ipc_path(datadir):
    geth_ipc_dir_path = tempfile.mkdtemp()
    _geth_ipc_path = os.path.join(geth_ipc_dir_path, 'geth.ipc')
    yield _geth_ipc_path

    if os.path.exists(_geth_ipc_path):
        os.remove(_geth_ipc_path)


@pytest.fixture(scope="module")
def web3(geth_process, endpoint_uri):
    wait_for_http(endpoint_uri)
    _web3 = Web3(Web3.HTTPProvider(endpoint_uri))
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
