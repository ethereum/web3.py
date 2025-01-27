from asyncio.exceptions import (
    TimeoutError,
)
import pytest

import pytest_asyncio
import websockets

from web3 import (
    Web3,
)
from web3.exceptions import (
    ProviderConnectionError,
    Web3ValidationError,
)
from web3.providers.legacy_websocket import (
    LegacyWebSocketProvider,
)


@pytest_asyncio.fixture
async def start_websocket_server(open_port):
    async def _serve(websocket, path):
        await websocket.send(b'{"jsonrpc":"2.0","id":1,"result":1}')

    server = await websockets.serve(_serve, "127.0.0.1", open_port)

    yield

    server.close()
    await server.wait_closed()


@pytest.fixture
def w3(open_port, start_websocket_server):
    endpoint_uri = f"ws://127.0.0.1:{open_port}"
    provider = LegacyWebSocketProvider(endpoint_uri, websocket_timeout=0.001)
    return Web3(provider)


def test_no_args():
    provider = LegacyWebSocketProvider()
    w3 = Web3(provider)
    assert w3.manager.provider == provider
    assert not w3.manager.provider.is_async
    assert not w3.is_connected()
    with pytest.raises(ProviderConnectionError):
        w3.is_connected(show_traceback=True)


def test_websocket_provider_timeout(w3):
    with pytest.raises(TimeoutError):
        w3.eth.accounts


def test_restricted_websocket_kwargs():
    invalid_kwargs = {"uri": "ws://127.0.0.1:8546"}
    re_exc_message = f".*found: {set(invalid_kwargs)!r}*"
    with pytest.raises(Web3ValidationError, match=re_exc_message):
        LegacyWebSocketProvider(websocket_kwargs=invalid_kwargs)
