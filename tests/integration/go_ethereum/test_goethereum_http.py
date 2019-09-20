import pytest

from tests.utils import (
    get_open_port,
)
from web3 import Web3

from .common import (
    CommonGoEthereumShhModuleTest,
    GoEthereumAdminModuleTest,
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
    return get_open_port()


@pytest.fixture(scope="module")
def endpoint_uri(rpc_port):
    return 'http://localhost:{0}'.format(rpc_port)


@pytest.fixture(scope='module')
def geth_command_arguments(geth_binary, datadir, rpc_port):
    return (
        geth_binary,
        '--datadir', str(datadir),
        '--shh',
        '--nodiscover',
        '--fakepow',
        '--rpc',
        '--rpcport', rpc_port,
        '--rpcapi', 'admin,db,eth,net,web3,personal,shh,web3',
        '--ipcdisable',
        '--allow-insecure-unlock',
    )


@pytest.fixture(scope="module")
def web3(geth_process, endpoint_uri):
    wait_for_http(endpoint_uri)
    _web3 = Web3(Web3.HTTPProvider(endpoint_uri))
    return _web3


class TestGoEthereumTest(GoEthereumTest):
    pass


class TestGoEthereumAdminModuleTest(GoEthereumAdminModuleTest):
    @pytest.mark.xfail(reason="running geth with the --nodiscover flag doesn't allow peer addition")
    def test_admin_peers(web3):
        super().test_admin_peers(web3)

    @pytest.mark.xfail(reason='Only one RPC endpoint is allowed to be active at any time')
    def test_admin_start_stop_rpc(web3):
        super().test_admin_start_stop_rpc(web3)

    @pytest.mark.xfail(reason='Only one RPC endpoint is allowed to be active at any time')
    def test_admin_startRPC(web3):
        super().test_admin_stopRPC(web3)

    @pytest.mark.xfail(reason='Only one RPC endpoint is allowed to be active at any time')
    def test_admin_stopRPC(web3):
        super().test_admin_stopRPC(web3)


class TestGoEthereumEthModuleTest(GoEthereumEthModuleTest):
    pass


class TestGoEthereumVersionModuleTest(GoEthereumVersionModuleTest):
    pass


class TestGoEthereumNetModuleTest(GoEthereumNetModuleTest):
    pass


class TestGoEthereumPersonalModuleTest(GoEthereumPersonalModuleTest):
    pass


class TestGoEthereumShhModuleTest(CommonGoEthereumShhModuleTest):
    pass
