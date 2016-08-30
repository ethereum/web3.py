import contextlib
import tempfile
import shutil
import random

import pytest

import gevent
from gevent import socket

from geth import (  # noqa: E402
    LoggingMixin,
    DevGethProcess,
)


class GethProcess(LoggingMixin, DevGethProcess):
    pass


def get_open_port():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(("", 0))
    s.listen(1)
    port = s.getsockname()[1]
    s.close()
    return port


def wait_for_http_connection(port, timeout=60):
    with gevent.Timeout(timeout):
        while True:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.timeout = 1
            try:
                s.connect(('127.0.0.1', port))
            except (socket.timeout, ConnectionRefusedError):
                gevent.sleep(random.random())
                continue
            else:
                break
        else:
            raise ValueError("Unable to establish HTTP connection")


@pytest.fixture()
def skip_if_testrpc():
    from web3.providers.rpc import TestRPCProvider

    def _skip_if_testrpc(web3):
        if isinstance(web3.currentProvider, TestRPCProvider):
            pytest.skip()
    return _skip_if_testrpc


@pytest.fixture()
def wait_for_miner_start():
    def _wait_for_miner_start(web3, timeout=60):
        with gevent.Timeout(timeout):
            while not web3.eth.mining or not web3.eth.hashrate:
                gevent.sleep(random.random())
    return _wait_for_miner_start


@pytest.fixture()
def wait_for_block():
    from web3.providers.rpc import TestRPCProvider

    def _wait_for_block(web3, block_number=1, timeout=60 * 10):
        with gevent.Timeout(timeout):
            while True:
                if web3.eth.blockNumber >= block_number:
                    break
                if isinstance(web3.currentProvider, TestRPCProvider):
                    web3._requestManager.request_blocking("evm_mine", [])
                gevent.sleep(1)
    return _wait_for_block


@pytest.fixture()
def wait_for_transaction():
    def _wait_for_transaction(web3, txn_hash, timeout=120):
        with gevent.Timeout(timeout):
            while True:
                txn_receipt = web3.eth.getTransactionReceipt(txn_hash)
                if txn_receipt is not None:
                    break
                gevent.sleep(1)

        return txn_receipt
    return _wait_for_transaction


@contextlib.contextmanager
def tempdir():
    directory = tempfile.mkdtemp()

    try:
        yield directory
    finally:
        shutil.rmtree(directory)


@pytest.yield_fixture(scope="session")
def web3_tester_provider():
    from testrpc import testrpc

    from web3.providers.rpc import TestRPCProvider
    port = get_open_port()
    provider = TestRPCProvider(port=port)

    testrpc.full_reset()
    testrpc.rpc_configure('eth_mining', False)
    testrpc.rpc_configure('eth_protocolVersion', '0x3f')
    testrpc.rpc_configure('net_version', 1)
    testrpc.evm_mine()

    provider.testrpc = testrpc
    wait_for_http_connection(port)

    yield provider

    provider.server.stop()
    provider.server.close()
    provider.thread.kill()


@pytest.fixture()
def web3_tester_empty(request, web3_tester_provider):
    from web3 import Web3

    if getattr(request, 'reset_chain', True):
        web3_tester_provider.testrpc.full_reset()

    web3 = Web3(web3_tester_provider)
    return web3


@pytest.fixture()
def web3_tester_persistent(request, web3_tester_provider):
    from web3 import Web3

    web3 = Web3(web3_tester_provider)
    return web3


@pytest.fixture()
def web3_tester(web3_tester_persistent):
    # alias
    return web3_tester_persistent


@contextlib.contextmanager
def setup_testing_geth():
    with tempdir() as base_dir:
        geth_process = GethProcess(
            'testing',
            base_dir=base_dir,
            overrides={'verbosity': '3'},
        )
        with geth_process as running_geth_process:
            running_geth_process.wait_for_ipc(60)
            running_geth_process.wait_for_rpc(60)
            running_geth_process.wait_for_dag(600)
            yield running_geth_process


@pytest.yield_fixture(scope="session")
def geth_persistent():
    with setup_testing_geth() as geth:
        yield geth


@pytest.fixture(scope="session")
def web3_rpc_persistent(geth_persistent):
    from web3 import (
        Web3, RPCProvider,
    )

    provider = RPCProvider(port=geth_persistent.rpc_port)
    provider._geth = geth_persistent
    web3 = Web3(provider)
    return web3


@pytest.yield_fixture()
def web3_rpc_empty():
    from web3 import (
        Web3, RPCProvider,
    )

    with setup_testing_geth() as geth:
        provider = RPCProvider(port=geth.rpc_port)
        provider._geth = geth
        web3 = Web3(provider)
        yield web3


@pytest.fixture(scope="session")
def web3_ipc_persistent(geth_persistent):
    from web3 import (
        Web3, IPCProvider,
    )

    provider = IPCProvider(ipc_path=geth_persistent.ipc_path)
    provider._geth = geth_persistent
    web3 = Web3(provider)
    return web3


@pytest.yield_fixture()
def web3_ipc_empty():
    from web3 import (
        Web3, IPCProvider,
    )

    with setup_testing_geth() as geth:
        provider = IPCProvider(ipc_path=geth.ipc_path)
        provider._geth = geth
        web3 = Web3(provider)
        yield web3


@pytest.fixture(params=[
    'tester',
    pytest.mark.slow('rpc'),
    pytest.mark.slow('ipc'),
])
def web3(request):
    if request.param == "tester":
        return request.getfuncargvalue('web3_tester_persistent')
    elif request.param == "rpc":
        return request.getfuncargvalue('web3_rpc_persistent')
    elif request.param == "ipc":
        return request.getfuncargvalue('web3_ipc_persistent')
    else:
        raise ValueError("Unknown param")


@pytest.fixture(params=[
    'tester',
    pytest.mark.slow('rpc'),
    pytest.mark.slow('ipc'),
])
def web3_empty(request):
    if request.param == "tester":
        return request.getfuncargvalue('web3_tester_empty')
    elif request.param == "rpc":
        return request.getfuncargvalue('web3_rpc_empty')
    elif request.param == "ipc":
        return request.getfuncargvalue('web3_ipc_empty')
    else:
        raise ValueError("Unknown param")
