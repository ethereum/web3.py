import json
import os
import pathlib
import pytest
import socket
import tempfile
from threading import (
    Thread,
)
import time

from web3 import (
    AsyncWeb3,
)
from web3.datastructures import (
    AttributeDict,
)
from web3.providers import (
    AsyncIPCProvider,
)

ETH_SUBSCRIBE_RESPONSE = {
    "jsonrpc": "2.0",
    "id": 1,
    "method": "eth_subscription",
    "params": {
        "result": {
            "removed": "false",
            "transaction": {
                "hash": "0xa8f2cf69e302da6c8100b80298ed77c37b6e75eed1177ca22acd5772c9fb9876",  # noqa: E501
            },
        },
        "subscription": "0xf13f7073ddef66a8c1b0c9c9f0e543c3",
    },
}


@pytest.fixture
def jsonrpc_ipc_pipe_path():
    with tempfile.TemporaryDirectory() as temp_dir:
        ipc_path = os.path.join(temp_dir, "filename.ipc")
        try:
            yield ipc_path
        finally:
            if os.path.exists(ipc_path):
                os.remove(ipc_path)


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
            connection.sendall(b'{"id": 0, "result": {}')
            time.sleep(0.1)
            connection.sendall(b"}")
        except BrokenPipeError:
            pass
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


@pytest.fixture
def serve_subscription_result(simple_ipc_server):
    def reply():
        connection, client_address = simple_ipc_server.accept()
        try:
            connection.recv(1024)
            connection.sendall(
                b'{"jsonrpc": "2.0", "id": 0, "result": "0xf13f7073ddef66a8c1b0c9c9f0e543c3"}'  # noqa: E501
            )
            connection.sendall(json.dumps(ETH_SUBSCRIBE_RESPONSE).encode("utf-8"))
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


def test_ipc_tilde_in_path():
    expected_path = str(pathlib.Path.home()) + "/foo"
    assert AsyncIPCProvider("~/foo").ipc_path == expected_path
    assert AsyncIPCProvider(pathlib.Path("~/foo")).ipc_path == expected_path


@pytest.mark.asyncio
async def test_provider_is_connected(jsonrpc_ipc_pipe_path, serve_empty_result):
    w3 = await AsyncWeb3(AsyncIPCProvider(pathlib.Path(jsonrpc_ipc_pipe_path)))
    await w3.provider.disconnect()
    assert await w3.is_connected() is False


@pytest.mark.asyncio
async def test_async_waits_for_full_result(jsonrpc_ipc_pipe_path, serve_empty_result):
    async with AsyncWeb3(AsyncIPCProvider(pathlib.Path(jsonrpc_ipc_pipe_path))) as w3:
        result = await w3.provider.make_request("method", [])
        assert result == {"id": 0, "result": {}}
        await w3.provider.disconnect()


@pytest.mark.asyncio
async def test_await_instantiation(jsonrpc_ipc_pipe_path, serve_empty_result):
    w3 = await AsyncWeb3(AsyncIPCProvider(pathlib.Path(jsonrpc_ipc_pipe_path)))
    result = await w3.provider.make_request("method", [])
    assert result == {"id": 0, "result": {}}
    await w3.provider.disconnect()


@pytest.mark.asyncio
async def test_await_connect(jsonrpc_ipc_pipe_path, serve_empty_result):
    w3 = AsyncWeb3(AsyncIPCProvider(pathlib.Path(jsonrpc_ipc_pipe_path)))
    await w3.provider.connect()
    result = await w3.provider.make_request("method", [])
    assert result == {"id": 0, "result": {}}
    await w3.provider.disconnect()


@pytest.mark.asyncio
async def test_eth_subscription(jsonrpc_ipc_pipe_path, serve_subscription_result):
    async with AsyncWeb3(AsyncIPCProvider(pathlib.Path(jsonrpc_ipc_pipe_path))) as w3:
        subscribe_response = await w3.eth.subscribe("newHeads")
        subscription_id = "0xf13f7073ddef66a8c1b0c9c9f0e543c3"
        assert subscribe_response == subscription_id

        subscription_response = {
            "result": AttributeDict(
                {
                    "removed": "false",
                    "transaction": AttributeDict(
                        {
                            "hash": "0xa8f2cf69e302da6c8100b80298ed77c37b6e75eed1177ca22acd5772c9fb9876"  # noqa: E501
                        }
                    ),
                }
            ),
            "subscription": "0xf13f7073ddef66a8c1b0c9c9f0e543c3",
        }
        async for response in w3.socket.process_subscriptions():
            assert response == subscription_response
            break
        await w3.provider.disconnect()


def test_get_endpoint_uri_or_ipc_path_returns_ipc_path():
    provider = AsyncIPCProvider(pathlib.Path("/path/to/file"))
    assert (
        provider.get_endpoint_uri_or_ipc_path() == "/path/to/file" == provider.ipc_path
    )
