import os
import pytest
import tempfile

from tests.integration.parity.utils import (
    wait_for_socket,
)
from web3 import Web3
from web3.utils.module_testing import (
    NetModuleTest,
    VersionModuleTest,
)

from .common import (
    ParityEthModuleTest,
    ParityPersonalModuleTest,
    ParityTraceModuleTest,
    ParityWeb3ModuleTest,
)


@pytest.fixture(scope='module')
def ipc_path(datadir):
    ipc_dir_path = tempfile.mkdtemp()
    _ipc_path = os.path.join(ipc_dir_path, 'jsonrpc.ipc')
    yield _ipc_path

    if os.path.exists(_ipc_path):
        os.remove(_ipc_path)


@pytest.fixture(scope="module")
def parity_command_arguments(
    parity_import_blocks_process,
    parity_binary,
    ipc_path,
    datadir,
    passwordfile,
    author
):
    return (
        parity_binary,
        '--chain', os.path.join(datadir, 'chain_config.json'),
        '--ipc-path', ipc_path,
        '--base-path', datadir,
        '--unlock', author,
        '--password', passwordfile,
        '--no-jsonrpc',
        '--no-ws',
    )


@pytest.fixture(scope="module")
def parity_import_blocks_command(parity_binary, ipc_path, datadir, passwordfile):
    return (
        parity_binary,
        'import', os.path.join(datadir, 'blocks_export.rlp'),
        '--chain', os.path.join(datadir, 'chain_config.json'),
        '--ipc-path', ipc_path,
        '--base-path', datadir,
        '--password', passwordfile,
        '--no-jsonrpc',
        '--no-ws',
        '--tracing', 'on',
    )


@pytest.fixture(scope="module")  # noqa: F811
def web3(parity_process, ipc_path):
    wait_for_socket(ipc_path)
    _web3 = Web3(Web3.IPCProvider(ipc_path))
    return _web3


class TestParityWeb3ModuleTest(ParityWeb3ModuleTest):
    pass


class TestParityEthModuleTest(ParityEthModuleTest):
    pass


class TestParityVersionModule(VersionModuleTest):
    pass


class TestParityNetModule(NetModuleTest):
    pass


class TestParityPersonalModuleTest(ParityPersonalModuleTest):
    pass


class TestParityTraceModuleTest(ParityTraceModuleTest):
    pass
