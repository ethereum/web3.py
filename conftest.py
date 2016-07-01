import pytest
import contextlib
import tempfile
import shutil

# This has to go here so that the `gevent.monkey.patch_all()` happens in the
# main thread.
from pygeth.geth import (
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


def wait_for_ipc_connection(ipc_path, timeout=30):
    import os
    import gevent

    with gevent.Timeout(timeout):
        while True:
            if os.path.exists(ipc_path):
                break
            gevent.sleep(0.1)
        else:
            raise ValueError("Unable to establish HTTP connection")


@pytest.fixture()
def wait_for_block():
    import gevent

    def _wait_for_block(web3, block_number=1, timeout=60):
        with gevent.Timeout(timeout):
            while True:
                if web3.eth.blockNumber >= block_number:
                    break
                gevent.sleep(1)
    return _wait_for_block


@pytest.fixture()
def wait_for_transaction(web3):
    import gevent

    def _wait_for_transaction(txn_hash, timeout=120):
        with gevent.Timeout(timeout):
            while True:
                txn_receipt = web3.eth.getTransactionReciept(txn_hash)
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


@contextlib.contextmanager
def setup_tester_rpc_provider():
    from testrpc import testrpc

    from web3.web3.rpcprovider import TestRPCProvider
    port = get_open_port()
    provider = TestRPCProvider(port=port)

    testrpc.full_reset()
    testrpc.rpc_configure('eth_mining', False)
    testrpc.rpc_configure('eth_protocolVersion', '0x3f')
    testrpc.rpc_configure('net_version', 1)
    testrpc.evm_mine()

    wait_for_http_connection(port)
    yield provider
    provider.server.shutdown()
    provider.server.server_close()


@contextlib.contextmanager
def setup_rpc_provider():
    from web3.web3.rpcprovider import RPCProvider

    with tempdir() as base_dir:
        geth = GethProcess('testing', base_dir=base_dir)
        geth.start()
        wait_for_http_connection(geth.rpc_port)
        provider = RPCProvider(port=geth.rpc_port)
        provider._geth = geth
        yield provider
        geth.stop()


@contextlib.contextmanager
def setup_ipc_provider():
    from web3.web3.ipcprovider import IPCProvider

    with tempdir() as base_dir:
        geth = GethProcess('testing', base_dir=base_dir)
        geth.start()
        wait_for_ipc_connection(geth.ipc_path)
        provider = IPCProvider(geth.ipc_path)
        provider._geth = geth
        yield provider
        geth.stop()


@pytest.yield_fixture(params=['tester', 'rpc', 'ipc'])
def web3(request):
    from web3 import Web3

    if request.param == "tester":
        setup_fn = setup_tester_rpc_provider
    elif request.param == "rpc":
        setup_fn = setup_rpc_provider
    elif request.param == "ipc":
        setup_fn = setup_ipc_provider
    else:
        raise ValueError("Unknown param")

    with setup_fn() as provider:
        _web3 = Web3(provider)
        yield _web3
