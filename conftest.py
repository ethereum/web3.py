import pytest
import contextlib
import tempfile
import shutil
import random

import gevent

# This has to go here so that the `gevent.monkey.patch_all()` happens in the
# main thread.
from geth import (
    LoggingMixin,
    DevGethProcess,
)


class GethProcess(LoggingMixin, DevGethProcess):
    pass


def get_open_port():
    import socket
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(("", 0))
    s.listen(1)
    port = s.getsockname()[1]
    s.close()
    return port


def wait_for_http_connection(port, timeout=30):
    import gevent
    import requests

    with gevent.Timeout(timeout):
        while True:
            try:
                requests.post("http://127.0.0.1:{0}".format(port))
            except requests.ConnectionError:
                gevent.sleep(0.1)
                continue
            else:
                break
        else:
            raise ValueError("Unable to establish HTTP connection")


@pytest.fixture()
def wait_for_miner_start():
    def _wait_for_miner_start(web3, timeout=60):
        with gevent.Timeout(timeout):
            while not web3.eth.mining or not web3.eth.hashrate:
                gevent.sleep(random.random())
    return _wait_for_miner_start


@pytest.fixture()
def wait_for_block():
    import gevent
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
    import gevent

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

    provider.server.shutdown()
    provider.server.server_close()


@pytest.fixture()
def web3_tester(request, web3_tester_provider):
    from web3 import Web3

    if getattr(request, 'reset_chain', True):
        web3_tester_provider.testrpc.full_reset()

    web3 = Web3(web3_tester_provider)
    return web3


def _web3_rpc():
    from web3 import (
        Web3,
        RPCProvider,
    )

    with tempdir() as base_dir:
        with GethProcess('testing', base_dir=base_dir) as geth:
            geth.wait_for_rpc(30)
            geth.wait_for_dag(600)
            provider = RPCProvider(port=geth.rpc_port)
            provider._geth = geth
            web3 = Web3(provider)
            yield web3

web3_rpc_empty = pytest.yield_fixture()(_web3_rpc)
web3_rpc_persistent = pytest.yield_fixture(scope="session")(_web3_rpc)


@pytest.fixture()
def web3_rpc(request):
    if getattr(request, 'reset_chain', False):
        return request.getfuncargvalue('web3_rpc_empty')
    else:
        return request.getfuncargvalue('web3_rpc_persistent')


def _web3_ipc():
    from web3 import (
        Web3,
        IPCProvider,
    )

    with tempdir() as base_dir:
        with GethProcess('testing', base_dir=base_dir) as geth:
            geth.wait_for_ipc(30)
            geth.wait_for_dag(600)
            provider = IPCProvider(geth.ipc_path)
            provider._geth = geth
            web3 = Web3(provider)
            yield web3

web3_ipc_empty = pytest.yield_fixture()(_web3_ipc)
web3_ipc_persistent = pytest.yield_fixture(scope="session")(_web3_ipc)


@pytest.fixture()
def web3_ipc(request):
    if getattr(request, 'reset_chain', False):
        return request.getfuncargvalue('web3_ipc_empty')
    else:
        return request.getfuncargvalue('web3_ipc_persistent')


@pytest.fixture(params=[
    'tester',
    pytest.mark.slow('rpc'),
    pytest.mark.slow('ipc'),
])
def web3(request):
    if request.param == "tester":
        return request.getfuncargvalue('web3_tester')
    elif request.param == "rpc":
        return request.getfuncargvalue('web3_rpc')
    elif request.param == "ipc":
        return request.getfuncargvalue('web3_ipc')
    else:
        raise ValueError("Unknown param")


@pytest.fixture()
def empty_account(web3):
    from eth_tester_client.utils import mk_random_privkey
    address = web3.personal.importRawKey(mk_random_privkey(), "a-password")

    assert web3.eth.getBalance(address) == 0
    return address
