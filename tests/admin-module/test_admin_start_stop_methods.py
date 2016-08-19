import pytest

from gevent import socket

from flaky import flaky


def get_open_port():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(("", 0))
    s.listen(1)
    port = s.getsockname()[1]
    s.close()
    return port


@flaky(max_runs=3)
def test_admin_startRPC(web3_ipc_empty, skip_if_testrpc):
    web3 = web3_ipc_empty
    skip_if_testrpc(web3)

    with pytest.raises(ValueError):
        web3.admin.startRPC()
    assert web3.admin.stopRPC()
    assert web3.admin.startRPC(port=get_open_port())


@flaky(max_runs=3)
def test_admin_stopRPC(web3_ipc_empty, skip_if_testrpc):
    web3 = web3_ipc_empty
    skip_if_testrpc(web3)

    assert web3.admin.stopRPC()
    with pytest.raises(ValueError):
        web3.admin.stopRPC()


@flaky(max_runs=3)
def test_admin_startWS(web3_ipc_empty, skip_if_testrpc):
    web3 = web3_ipc_empty
    skip_if_testrpc(web3)

    with pytest.raises(ValueError):
        web3.admin.startWS()
    assert web3.admin.stopWS()
    assert web3.admin.startWS(port=get_open_port())


@flaky(max_runs=3)
def test_admin_stopWS(web3_ipc_empty, skip_if_testrpc):
    web3 = web3_ipc_empty
    skip_if_testrpc(web3)

    assert web3.admin.stopWS()
    with pytest.raises(ValueError):
        web3.admin.stopWS()
