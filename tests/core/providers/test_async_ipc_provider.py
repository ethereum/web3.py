import asyncio
import os
import pathlib
import socket
import uuid

import aiofiles
import pytest

from web3.exceptions import (
    ProviderConnectionError
)
from web3.providers.async_ipc import (
    AsyncIPCProvider
)

from web3.auto.gethdev import (
    w3,
)

from web3.middleware import (
    construct_fixture_middleware,
)


@pytest.fixture
async def jsonrpc_ipc_pipe_path():
    async with aiofiles.tempfile.TemporaryDirectory() as temp_dir:
        ipc_path = os.path.join(temp_dir, f"{uuid.uuid4()}.ipc")
        try:
            yield ipc_path
        finally:
            if os.path.exists(ipc_path):
                os.remove(ipc_path)


async def test_ipc_no_path():
    """
    IPCProvider.is_connected() returns False when no path is supplied
    """
    ipc = AsyncIPCProvider(None)
    assert ipc.is_connected() is False
    with pytest.raises(ProviderConnectionError):
        ipc.is_connected(show_traceback=True)


async def test_ipc_tilda_in_path():
    expected_path = str(pathlib.Path.home()) + "/foo"
    assert AsyncIPCProvider("~/foo").ipc_path == expected_path
    assert AsyncIPCProvider(pathlib.Path("~/foo")).ipc_path == expected_path


@pytest.fixture
async def simple_ipc_server(jsonrpc_ipc_pipe_path):
    serv = socket.socket(socket.AF_UNIX)
    serv.bind(jsonrpc_ipc_pipe_path)
    serv.listen(1)
    try:
        yield serv
    finally:
        serv.close()


@pytest.fixture
async def serve_empty_result(simple_ipc_server):
    async def reply():
        connection, client_address = await asyncio.wait_for(asyncio.create_task(simple_ipc_server.accept()), 1)
        try:
            await asyncio.wait_for(connection.recv(1024), 1)
            connection.sendall(b'{"id":1, "result": {}')
            await asyncio.sleep(0.1)
            connection.sendall(b"}")
        finally:
            # Clean up the connection
            connection.close()
            simple_ipc_server.close()

    task = asyncio.create_task(reply())

    try:
        yield
    finally:
        task.cancel()
        await task


async def test_sync_waits_for_full_result(jsonrpc_ipc_pipe_path, serve_empty_result):
    provider = AsyncIPCProvider(pathlib.Path(jsonrpc_ipc_pipe_path), timeout=3)
    result = await provider.make_request("method", [])
    assert result == {"id": 1, "result": {}}
    provider._socket.sock.close()


def test_web3_auto_gethdev():
    assert isinstance(w3.provider, AsyncIPCProvider)
    return_block_with_long_extra_data = construct_fixture_middleware(
        {
            "eth_getBlockByNumber": {"extraData": "0x" + "ff" * 33},
        }
    )
    w3.middleware_onion.inject(return_block_with_long_extra_data, layer=0)
    block = w3.eth.get_block("latest")
    assert "extraData" not in block
    assert block.proofOfAuthorityData == b"\xff" * 33
