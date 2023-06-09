import os
import pathlib
import pytest
import socket
import tempfile
from threading import (
    Thread,
)
import time
import uuid

from web3.auto.gethdev import (
    async_w3,
)
from web3.exceptions import (
    ProviderConnectionError,
)
from web3.middleware import (
    async_construct_fixture_middleware,
)
from web3.providers.async_ipc import (
    AsyncIPCProvider,
)


@pytest.fixture
def jsonrpc_ipc_pipe_path():
    with tempfile.TemporaryDirectory() as temp_dir:
        ipc_path = os.path.join(temp_dir, f"{uuid.uuid4()}.ipc")
        try:
            yield ipc_path
        finally:
            if os.path.exists(ipc_path):
                os.remove(ipc_path)


@pytest.mark.asyncio
async def test_ipc_no_path():
    """
    AsyncIPCProvider.is_connected() returns False when no path is supplied
    """
    ipc = AsyncIPCProvider(None)
    assert await ipc.is_connected() is False
    with pytest.raises(ProviderConnectionError):
        await ipc.is_connected(show_traceback=True)


def test_ipc_tilda_in_path():
    expected_path = str(pathlib.Path.home()) + "/foo"
    assert AsyncIPCProvider("~/foo").ipc_path == expected_path
    assert AsyncIPCProvider(pathlib.Path("~/foo")).ipc_path == expected_path


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
            connection.sendall(b"}")
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


@pytest.mark.asyncio
async def test_async_waits_for_full_result(jsonrpc_ipc_pipe_path, serve_empty_result):
    provider = AsyncIPCProvider(pathlib.Path(jsonrpc_ipc_pipe_path), timeout=3)
    result = await provider.make_request("method", [])
    assert result == {"id": 1, "result": {}}
    sock = provider._socket.sock
    reader, writer = sock
    writer.close()
    await writer.wait_closed()


@pytest.mark.asyncio
async def test_web3_auto_gethdev():
    assert isinstance(async_w3.provider, AsyncIPCProvider)
    return_block_with_long_extra_data = await async_construct_fixture_middleware(
        {
            "eth_getBlockByNumber": {"extraData": "0x" + "ff" * 33},
        }
    )
    async_w3.middleware_onion.inject(return_block_with_long_extra_data, layer=0)
    block = await async_w3.eth.get_block("latest")
    assert "extraData" not in block
    assert block.proofOfAuthorityData == b"\xff" * 33
