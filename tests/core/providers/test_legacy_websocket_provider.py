import asyncio
from asyncio.exceptions import (
    TimeoutError,
)
import pytest
from threading import (
    Thread,
)

import websockets

from tests.utils import (
    wait_for_ws,
)
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


@pytest.fixture
def start_websocket_server(open_port):
    event_loop = asyncio.new_event_loop()

    def run_server():
        async def empty_server(websocket, path):
            data = await websocket.recv()
            await asyncio.sleep(0.02)
            await websocket.send(data)

        asyncio.set_event_loop(event_loop)
        server = websockets.serve(empty_server, "127.0.0.1", open_port)
        event_loop.run_until_complete(server)
        event_loop.run_forever()

    thd = Thread(target=run_server)
    thd.start()
    try:
        yield
    finally:
        event_loop.call_soon_threadsafe(event_loop.stop)


@pytest.fixture
def w3(open_port, start_websocket_server):
    # need new event loop as the one used by server is already running
    event_loop = asyncio.new_event_loop()
    endpoint_uri = f"ws://127.0.0.1:{open_port}"
    event_loop.run_until_complete(wait_for_ws(endpoint_uri))
    provider = LegacyWebSocketProvider(endpoint_uri, websocket_timeout=0.01)
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
