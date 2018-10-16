import asyncio
import json
import logging
import os
import threading

import websockets

from web3.exceptions import (
    ValidationError,
)
from web3.providers.base import (
    JSONBaseProvider,
)

RESTRICTED_WEBSOCKET_KWARGS = {'uri', 'loop'}
DEFAULT_WEBSOCKET_TIMEOUT = 10


def get_default_endpoint():
    return os.environ.get('WEB3_WS_PROVIDER_URI', 'ws://127.0.0.1:8546')


class InitLocal(threading.local):
    def __init__(self):
        self.ws = None
        self.loop = None


class PersistentWebSocket:
    local = InitLocal()

    def __init__(self, endpoint_uri, websocket_kwargs):
        self.endpoint_uri = endpoint_uri
        self.websocket_kwargs = websocket_kwargs

    async def __aenter__(self):
        loop = asyncio.get_event_loop()
        if self.local.ws is None or self.local.loop != loop:
            self.local.loop = loop
            self.local.ws = await websockets.connect(
                uri=self.endpoint_uri, loop=loop, **self.websocket_kwargs
            )
        return self.local.ws

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        thread_id = threading.get_ident()
        if exc_val is not None:
            try:
                await self.local.ws.close()
            except Exception:
                pass
            self.local.ws = None


class WebsocketProvider(JSONBaseProvider):
    logger = logging.getLogger("web3.providers.WebsocketProvider")

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
        self.conn = WebSocketConnection(
            self.endpoint_uri, websocket_kwargs
        )
        super().__init__()

    def __str__(self):
        return "WS connection {0}".format(self.endpoint_uri)

    async def make_request(self, method, params):
        self.logger.debug("Making request WebSocket. URI: %s, "
                          "Method: %s", self.endpoint_uri, method)
        request_data = self.encode_rpc_request(method, params)
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
