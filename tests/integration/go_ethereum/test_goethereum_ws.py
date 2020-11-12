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


def _geth_command_arguments(ws_port,
                            base_geth_command_arguments,
                            geth_version):
    yield from base_geth_command_arguments
    if geth_version.major == 1:
        yield from (
            '--ws',
            '--ws.port', ws_port,
            '--ws.api', 'admin,eth,net,web3,personal,miner',
            '--ws.origins', '*',
            '--ipcdisable',
            '--allow-insecure-unlock',
        )
        if geth_version.minor not in [9]:
            raise AssertionError("Unsupported Geth version")
    else:
        raise AssertionError("Unsupported Geth version")


@pytest.fixture(scope='module')
def geth_command_arguments(geth_binary,
                           get_geth_version,
                           datadir,
                           ws_port,
                           base_geth_command_arguments):

    return _geth_command_arguments(
        ws_port,
        base_geth_command_arguments,
        get_geth_version
    )


@pytest.fixture(scope="module")
def web3(geth_process, endpoint_uri, event_loop):
    event_loop.run_until_complete(wait_for_ws(endpoint_uri, event_loop))
    _web3 = Web3(Web3.WebsocketProvider(endpoint_uri))
    return _web3


class TestGoEthereumTest(GoEthereumTest):
    pass


class TestGoEthereumAdminModuleTest(GoEthereumAdminModuleTest):
    @pytest.mark.xfail(reason="running geth with the --nodiscover flag doesn't allow peer addition")
    def test_admin_peers(self, web3: "Web3") -> None:
        super().test_admin_peers(web3)

    def test_admin_start_stop_ws(self, web3: "Web3") -> None:
        # This test inconsistently causes all tests after it to fail on CI if it's allowed to run
        pytest.xfail(reason='Only one WebSocket endpoint is allowed to be active at any time')
        super().test_admin_start_stop_ws(web3)

    def test_admin_start_stop_rpc(self, web3: "Web3") -> None:
        pytest.xfail(reason="This test inconsistently causes all tests after it on CI to fail if it's allowed to run")  # noqa: E501
        super().test_admin_start_stop_ws(web3)


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
