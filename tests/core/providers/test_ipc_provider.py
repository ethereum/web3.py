import os
import pytest
import socket
import tempfile
from threading import (
    Thread,
)
import time
import uuid

from web3.providers.ipc import (
    IPCProvider,
)


@pytest.fixture
def jsonrpc_ipc_pipe_path():
    with tempfile.TemporaryDirectory() as temp_dir:
        ipc_path = os.path.join(temp_dir, '{0}.ipc'.format(uuid.uuid4()))
        try:
            yield ipc_path
        finally:
            if os.path.exists(ipc_path):
                os.remove(ipc_path)


def test_ipc_no_path():
    """
    IPCProvider.isConnected() returns False when no path is supplied
    """
    ipc = IPCProvider(None)
    assert ipc.isConnected() is False


@pytest.fixture
def simple_ipc_server(jsonrpc_ipc_pipe_path):
    serv = socket.socket(socket.AF_UNIX)
    serv.bind(jsonrpc_ipc_pipe_path)
    serv.listen(1)
    try:
        yield serv
    finally:
        serv.close()


@pytest.fixture
def serve_empty_result(simple_ipc_server):
    def reply():
        connection, client_address = simple_ipc_server.accept()
        try:
            connection.recv(1024)
            connection.sendall(b'{"id":1, "result": {}')
            time.sleep(0.1)
            connection.sendall(b'}')
        finally:
            # Clean up the connection
            connection.close()
            simple_ipc_server.close()

    thd = Thread(target=reply, daemon=True)
    thd.start()

    try:
        yield
    finally:
        thd.join()


def test_sync_waits_for_full_result(jsonrpc_ipc_pipe_path, serve_empty_result):
    provider = IPCProvider(jsonrpc_ipc_pipe_path, timeout=3)
    result = provider.make_request("method", [])
    assert result == {'id': 1, 'result': {}}
    provider._socket.sock.close()
