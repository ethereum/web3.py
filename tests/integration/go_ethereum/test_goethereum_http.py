import pytest

import pytest_asyncio

from tests.utils import (
    get_open_port,
)
from web3 import Web3
from web3._utils.module_testing.go_ethereum_admin_module import (
    GoEthereumAsyncAdminModuleTest,
)
from web3._utils.module_testing.go_ethereum_personal_module import (
    GoEthereumAsyncPersonalModuleTest,
)
from web3.eth import (
    AsyncEth,
)
from web3.geth import (
    AsyncGethAdmin,
    AsyncGethPersonal,
    AsyncGethTxPool,
    Geth,
)
from web3.middleware import (
    async_buffered_gas_estimate_middleware,
    async_gas_price_strategy_middleware,
    async_validation_middleware,
)
from web3.net import (
    AsyncNet,
)
from web3.providers.async_rpc import (
    AsyncHTTPProvider,
)

from .common import (
    GoEthereumAdminModuleTest,
    GoEthereumAsyncEthModuleTest,
    GoEthereumAsyncNetModuleTest,
    GoEthereumAsyncTxPoolModuleTest,
    GoEthereumEthModuleTest,
    GoEthereumNetModuleTest,
    GoEthereumPersonalModuleTest,
    GoEthereumTest,
    GoEthereumTxPoolModuleTest,
    GoEthereumVersionModuleTest,
)
from .utils import (
    wait_for_aiohttp,
    wait_for_http,
)


@pytest.fixture(scope="module")
def rpc_port():
    return get_open_port()


@pytest.fixture(scope="module")
def endpoint_uri(rpc_port):
    return 'http://localhost:{0}'.format(rpc_port)


def _geth_command_arguments(rpc_port,
                            base_geth_command_arguments,
                            geth_version):
    yield from base_geth_command_arguments
    if geth_version.major == 1:
        yield from (
            '--http',
            '--http.port', rpc_port,
            '--http.api', 'admin,eth,net,web3,personal,miner,txpool',
            '--ipcdisable',
            '--allow-insecure-unlock'
        )
    else:
        raise AssertionError("Unsupported Geth version")


@pytest.fixture(scope='module')
def geth_command_arguments(rpc_port,
                           base_geth_command_arguments,
                           get_geth_version):

    return _geth_command_arguments(
        rpc_port,
        base_geth_command_arguments,
        get_geth_version
    )


@pytest.fixture(scope="module")
def web3(geth_process, endpoint_uri):
    wait_for_http(endpoint_uri)
    _web3 = Web3(Web3.HTTPProvider(endpoint_uri))
    return _web3


@pytest_asyncio.fixture(scope="module")
async def async_w3(geth_process, endpoint_uri):
    await wait_for_aiohttp(endpoint_uri)
    _web3 = Web3(
        AsyncHTTPProvider(endpoint_uri),
        middlewares=[
            async_buffered_gas_estimate_middleware,
            async_gas_price_strategy_middleware,
            async_validation_middleware,
        ],
        modules={'eth': AsyncEth,
                 'async_net': AsyncNet,
                 'geth': (Geth,
                          {'txpool': (AsyncGethTxPool,),
                           'personal': (AsyncGethPersonal,),
                           'admin': (AsyncGethAdmin,)}
                          )
                 }
    )
    return _web3


class TestGoEthereumTest(GoEthereumTest):
    pass


class TestGoEthereumAdminModuleTest(GoEthereumAdminModuleTest):
    @pytest.mark.xfail(reason="running geth with the --nodiscover flag doesn't allow peer addition")
    def test_admin_peers(self, web3: "Web3") -> None:
        super().test_admin_peers(web3)

    def test_admin_start_stop_rpc(self, web3: "Web3") -> None:
        # This test causes all tests after it to fail on CI if it's allowed to run
        pytest.xfail(reason='Only one RPC endpoint is allowed to be active at any time')
        super().test_admin_start_stop_rpc(web3)

    def test_admin_start_stop_ws(self, web3: "Web3") -> None:
        # This test causes all tests after it to fail on CI if it's allowed to run
        pytest.xfail(reason='Only one WS endpoint is allowed to be active at any time')
        super().test_admin_start_stop_ws(web3)


class TestGoEthereumAsyncAdminModuleTest(GoEthereumAsyncAdminModuleTest):
    @pytest.mark.asyncio
    @pytest.mark.xfail(reason="running geth with the --nodiscover flag doesn't allow peer addition")
    async def test_admin_peers(self, web3: "Web3") -> None:
        await super().test_admin_peers(web3)

    @pytest.mark.asyncio
    async def test_admin_start_stop_rpc(self, web3: "Web3") -> None:
        # This test causes all tests after it to fail on CI if it's allowed to run
        pytest.xfail(reason='Only one RPC endpoint is allowed to be active at any time')
        await super().test_admin_start_stop_rpc(web3)

    @pytest.mark.asyncio
    async def test_admin_start_stop_ws(self, web3: "Web3") -> None:
        # This test causes all tests after it to fail on CI if it's allowed to run
        pytest.xfail(reason='Only one WS endpoint is allowed to be active at any time')
        await super().test_admin_start_stop_ws(web3)


class TestGoEthereumEthModuleTest(GoEthereumEthModuleTest):
    pass


class TestGoEthereumVersionModuleTest(GoEthereumVersionModuleTest):
    pass


class TestGoEthereumNetModuleTest(GoEthereumNetModuleTest):
    pass


class TestGoEthereumAsyncNetModuleTest(GoEthereumAsyncNetModuleTest):
    pass


class TestGoEthereumPersonalModuleTest(GoEthereumPersonalModuleTest):
    pass


class TestGoEthereumAsyncPersonalModuleTest(GoEthereumAsyncPersonalModuleTest):
    pass


class TestGoEthereumAsyncEthModuleTest(GoEthereumAsyncEthModuleTest):
    pass


class TestGoEthereumTxPoolModuleTest(GoEthereumTxPoolModuleTest):
    pass


class TestGoEthereumAsyncTxPoolModuleTest(GoEthereumAsyncTxPoolModuleTest):
    pass
