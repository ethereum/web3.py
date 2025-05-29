import pytest
import os
import tempfile

import pytest_asyncio

from web3 import (
    AsyncIPCProvider,
    AsyncWeb3,
    AutoProvider,
    Web3,
)
from web3._utils.module_testing.persistent_connection_provider import (
    PersistentConnectionProviderTest,
)

from .common import (
    GoEthereumAdminModuleTest,
    GoEthereumAsyncDebugModuleTest,
    GoEthereumAsyncEthModuleTest,
    GoEthereumAsyncNetModuleTest,
    GoEthereumAsyncWeb3ModuleTest,
    GoEthereumDebugModuleTest,
    GoEthereumEthModuleTest,
    GoEthereumNetModuleTest,
    GoEthereumWeb3ModuleTest,
)
from .utils import (
    wait_for_async_socket,
    wait_for_socket,
)


def _geth_command_arguments(geth_ipc_path, base_geth_command_arguments):
    yield from base_geth_command_arguments
    yield from (
        "--ipcpath",
        geth_ipc_path,
    )


@pytest.fixture
def geth_command_arguments(geth_ipc_path, base_geth_command_arguments):
    return _geth_command_arguments(geth_ipc_path, base_geth_command_arguments)


@pytest.fixture
def geth_ipc_path(datadir):
    geth_ipc_dir_path = tempfile.mkdtemp()
    _geth_ipc_path = os.path.join(geth_ipc_dir_path, "geth.ipc")
    yield _geth_ipc_path

    if os.path.exists(_geth_ipc_path):
        os.remove(_geth_ipc_path)


@pytest.fixture
def auto_w3(start_geth_process_and_yield_port, geth_ipc_path, monkeypatch):
    from web3.auto import (
        w3,
    )

    wait_for_socket(geth_ipc_path)
    monkeypatch.setenv("WEB3_PROVIDER_URI", f"file:///{geth_ipc_path}")

    return w3


@pytest.fixture
def w3(start_geth_process_and_yield_port, geth_ipc_path):
    wait_for_socket(geth_ipc_path)
    return Web3(Web3.IPCProvider(geth_ipc_path, timeout=10))


class TestGoEthereumWeb3ModuleTest(GoEthereumWeb3ModuleTest):
    pass


class TestGoEthereumDebugModuleTest(GoEthereumDebugModuleTest):
    pass


class TestGoEthereumEthModuleTest(GoEthereumEthModuleTest):
    def test_auto_provider_batching(self, auto_w3: "Web3") -> None:
        with auto_w3.batch_requests() as batch:
            assert isinstance(auto_w3.provider, AutoProvider)
            assert auto_w3.provider._is_batching
            assert auto_w3.provider._batching_context is not None
            batch.add(auto_w3.eth.get_block("latest"))
            batch.add(auto_w3.eth.get_block("earliest"))
            batch.add(auto_w3.eth.get_block("pending"))
            results = batch.execute()

        assert not auto_w3.provider._is_batching
        assert len(results) == 3


class TestGoEthereumNetModuleTest(GoEthereumNetModuleTest):
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


# -- async -- #


@pytest_asyncio.fixture
async def async_w3(start_geth_process_and_yield_port, geth_ipc_path):
    await wait_for_async_socket(geth_ipc_path)
    async with AsyncWeb3(AsyncIPCProvider(geth_ipc_path, request_timeout=10)) as _aw3:
        yield _aw3


class TestGoEthereumAsyncWeb3ModuleTest(GoEthereumAsyncWeb3ModuleTest):
    pass


class TestGoEthereumAsyncDebugModuleTest(GoEthereumAsyncDebugModuleTest):
    pass


class TestGoEthereumAsyncEthModuleTest(GoEthereumAsyncEthModuleTest):
    pass


class TestGoEthereumAsyncNetModuleTest(GoEthereumAsyncNetModuleTest):
    pass


class TestPersistentConnectionProviderTest(PersistentConnectionProviderTest):
    pass
