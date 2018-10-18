import asyncio
import json
import logging
import os
from threading import (
    Thread,
)

import websockets

from web3.exceptions import (
    ValidationError,
)
from web3.providers.base import (
    JSONBaseProvider,
)

RESTRICTED_WEBSOCKET_KWARGS = {'uri', 'loop'}
DEFAULT_WEBSOCKET_TIMEOUT = 10


def _start_event_loop(loop):
    asyncio.set_event_loop(loop)
    loop.run_forever()
    loop.close()


def _get_threaded_loop():
    new_loop = asyncio.new_event_loop()
    thread_loop = Thread(target=_start_event_loop, args=(new_loop,), daemon=True)
    thread_loop.start()
    return new_loop


def get_default_endpoint():
    return os.environ.get('WEB3_WS_PROVIDER_URI', 'ws://127.0.0.1:8546')


class PersistentWebSocket:

    def __init__(self, endpoint_uri, loop, websocket_kwargs):
        self.ws = None
        self.endpoint_uri = endpoint_uri
        self.loop = loop
        self.websocket_kwargs = websocket_kwargs

    async def __aenter__(self):
        if self.ws is None:
            self.ws = await websockets.connect(
                uri=self.endpoint_uri, loop=self.loop, **self.websocket_kwargs
            )
        return self.ws

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        if exc_val is not None:
            try:
                await self.ws.close()
            except Exception:
                pass
            self.ws = None


class WebsocketProvider(JSONBaseProvider):
    logger = logging.getLogger("web3.providers.WebsocketProvider")
    _loop = None

    def __init__(
            self,
            endpoint_uri=None,
            websocket_kwargs=None,
            websocket_timeout=DEFAULT_WEBSOCKET_TIMEOUT
    ):
        self.endpoint_uri = endpoint_uri
        self.websocket_timeout = websocket_timeout
        if self.endpoint_uri is None:
            self.endpoint_uri = get_default_endpoint()
        if WebsocketProvider._loop is None:
            WebsocketProvider._loop = _get_threaded_loop()
        if websocket_kwargs is None:
            websocket_kwargs = {}
        else:
            found_restricted_keys = set(websocket_kwargs.keys()).intersection(
                RESTRICTED_WEBSOCKET_KWARGS
            )
            if found_restricted_keys:
                raise ValidationError(
                    '{0} are not allowed in websocket_kwargs, '
                    'found: {1}'.format(RESTRICTED_WEBSOCKET_KWARGS, found_restricted_keys)
                )
        self.conn = PersistentWebSocket(
            self.endpoint_uri, WebsocketProvider._loop, websocket_kwargs
        )
        super().__init__()

    def __str__(self):
        return "WS connection {0}".format(self.endpoint_uri)

    async def coro_make_request(self, request_data):
        async with self.conn as conn:
            await asyncio.wait_for(
                conn.send(request_data),
                timeout=self.websocket_timeout
            )
            return json.loads(
                await asyncio.wait_for(
                    conn.recv(),
                    timeout=self.websocket_timeout
                )
            )

    def make_request(self, method, params):
        self.logger.debug("Making request WebSocket. URI: %s, "
                          "Method: %s", self.endpoint_uri, method)
        request_data = self.encode_rpc_request(method, params)
        future = asyncio.run_coroutine_threadsafe(
            self.coro_make_request(request_data),
            WebsocketProvider._loop
        )
        return future.result()
