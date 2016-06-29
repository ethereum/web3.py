import pytest


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


@pytest.yield_fixture(params=['tester', 'rpc', 'ipc'])
def web3(request, tmpdir):
    from web3 import Web3
    from pygeth.geth import DevGethProcess

    if request.param == "tester":
        from web3.web3.rpcprovider import TestRPCProvider
        provider = TestRPCProvider(port=get_open_port())
    elif request.param == "rpc":
        from web3.web3.rpcprovider import RPCProvider
        geth = DevGethProcess('testing', base_dir=str(tmpdir.mkdir("data-dir")))
        geth.start()
        wait_for_http_connection(geth.rpc_port)
        provider = RPCProvider(port=geth.rpc_port)
    elif request.param == "ipc":
        from web3.web3.ipcprovider import IPCProvider
        geth = DevGethProcess('testing', base_dir=str(tmpdir.mkdir("data-dir")))
        geth.start()
        wait_for_ipc_connection(geth.ipc_path)
        provider = IPCProvider(geth.ipc_path)
    else:
        raise ValueError("Unknown param")

    _web3 = Web3(provider)

    yield _web3

    if request.param == "tester":
        _web3.currentProvider.server.shutdown()
        _web3.currentProvider.server.server_close()
    elif request.param in {"rpc", "ipc"}:
        geth.stop()
    else:
        raise ValueError("Unknown param")
