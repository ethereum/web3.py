import pytest

from tests.integration.common import (
    MiscWebsocketTest,
)
from tests.integration.utils import (
    wait_for_ws,
)
from web3 import Web3

from .common import (
    GoEthereumEthModuleTest,
    GoEthereumNetModuleTest,
    GoEthereumPersonalModuleTest,
    GoEthereumTest,
    GoEthereumVersionModuleTest,
    get_open_port,
)


@pytest.fixture(scope="module")
def ws_port():
    return get_open_port()


@pytest.fixture(scope="module")
def endpoint_uri(ws_port):
    return 'ws://localhost:{0}'.format(ws_port)


@pytest.fixture(scope='module')
def geth_command_arguments(geth_binary, datadir, ws_port):
    return (
        geth_binary,
        '--datadir', str(datadir),
        '--nodiscover',
        '--fakepow',
        '--ws',
        '--wsport', ws_port,
        '--wsapi', 'db,eth,net,web3,personal,web3',
        '--wsorigins', '*',
        '--ipcdisable',
    )


@pytest.fixture(scope="module")
def web3(geth_process, endpoint_uri, event_loop):
    event_loop.run_until_complete(wait_for_ws(endpoint_uri, event_loop))
    _web3 = Web3(Web3.WebsocketProvider(endpoint_uri))
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


class TestMiscWebsocketTest(MiscWebsocketTest):
    pass
