import pytest

from tests.integration.common import (
    MiscWebsocketTest,
)
from tests.utils import (
    get_open_port,
    wait_for_ws,
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


@pytest.fixture(scope="module")
def ws_port():
    return get_open_port()


@pytest.fixture(scope="module")
def endpoint_uri(ws_port):
    return 'ws://localhost:{0}'.format(ws_port)


@pytest.fixture(scope='module')
def geth_command_arguments(geth_binary,
                           get_geth_version,
                           datadir,
                           ws_port,
                           base_geth_command_arguments):

    if get_geth_version.major == 1:
        if get_geth_version.minor == 9:
            return (
                base_geth_command_arguments +
                (
                    '--ws',
                    '--wsport', ws_port,
                    '--wsapi', 'admin,db,eth,net,shh,web3,personal,web3',
                    '--wsorigins', '*',
                    '--ipcdisable',
                    '--allow-insecure-unlock',
                )
            )
        elif get_geth_version.minor == 8 or get_geth_version.minor == 7:
            return (
                base_geth_command_arguments +
                (
                    '--ws',
                    '--wsport', ws_port,
                    '--wsapi', 'admin,db,eth,net,shh,web3,personal,web3',
                    '--wsorigins', '*',
                    '--ipcdisable',
                )
            )
        else:
            assert False, "Unsupported geth version"
    else:
        assert False, "Unsupported geth version"


@pytest.fixture(scope="module")
def web3(geth_process, endpoint_uri, event_loop):
    event_loop.run_until_complete(wait_for_ws(endpoint_uri, event_loop))
    _web3 = Web3(Web3.WebsocketProvider(endpoint_uri))
    return _web3


class TestGoEthereumTest(GoEthereumTest):
    pass


class TestGoEthereumAdminModuleTest(GoEthereumAdminModuleTest):
    @pytest.mark.xfail(reason="running geth with the --nodiscover flag doesn't allow peer addition")
    def test_admin_peers(web3):
        super().test_admin_peers(web3)

    @pytest.mark.xfail(reason='Only one WebSocket endpoint is allowed to be active at any time')
    def test_admin_start_stop_ws(web3):
        super().test_admin_start_stop_ws(web3)

    @pytest.mark.xfail(reason='Only one WebSocket endpoint is allowed to be active at any time')
    def test_admin_startWS(self, web3):
        super().test_admin_startWS(web3)

    @pytest.mark.xfail(reason='Only one WebSocket endpoint is allowed to be active at any time')
    def test_admin_stopWS(self, web3):
        super().test_admin_stopWS(web3)


class TestGoEthereumEthModuleTest(GoEthereumEthModuleTest):
    pass


class TestGoEthereumVersionModuleTest(GoEthereumVersionModuleTest):
    pass


class TestGoEthereumNetModuleTest(GoEthereumNetModuleTest):
    pass


class TestGoEthereumPersonalModuleTest(GoEthereumPersonalModuleTest):
    pass


class TestMiscWebsocketTest(MiscWebsocketTest):
    pass


class TestGoEthereumShhModuleTest(CommonGoEthereumShhModuleTest):
    def test_shh_async_filter(self, web3):
        pytest.xfail("async filter bug in geth ws version")
        super().test_shh_async_filter(web3)

    def test_shh_async_filter_deprecated(self, web3):
        pytest.xfail("async filter bug in geth ws version")
        super().test_shh_async_filter(web3)
