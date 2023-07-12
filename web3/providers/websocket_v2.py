import asyncio
import logging
import os
from typing import (
    Any,
    AsyncIterator,
    Optional,
    Union,
)


from eth_typing import (
    URI,
)
import websockets
from websockets.legacy.client import (
    WebSocketClientProtocol,
)

from web3.exceptions import (
    Web3ValidationError,
)
from web3.providers.persistent import PersistentConnectionProvider

RESTRICTED_WEBSOCKET_KWARGS = {"uri", "loop"}
DEFAULT_WEBSOCKET_TIMEOUT = 10


def get_default_endpoint() -> URI:
    return URI(os.environ.get("WEB3_WS_PROVIDER_URI", "ws://127.0.0.1:8546"))


class PersistentWebsocketConnection(WebSocketClientProtocol):
    logger = logging.getLogger(
        "web3.providers.websocket_v2.PersistentWebsocketConnection"
    )

    def __init__(self, endpoint_uri: URI, websocket_kwargs: Any) -> None:
        super().__init__(**websocket_kwargs)
        self.endpoint_uri = endpoint_uri

    async def __aiter__(self) -> AsyncIterator["PersistentWebsocketConnection"]:
        try:
            while True:
                yield await self.recv()
        except websockets.ConnectionClosedOK:
            return


class WebsocketProviderV2(PersistentConnectionProvider):
    logger = logging.getLogger("web3.providers.WebsocketProviderV2")
    is_async = True
    ws: Optional[WebSocketClientProtocol] = None

    def __init__(
        self,
        endpoint_uri: Optional[Union[URI, str]] = None,
        websocket_kwargs: Optional[Any] = None,
        websocket_timeout: int = DEFAULT_WEBSOCKET_TIMEOUT,
    ) -> None:
        self.endpoint_uri = URI(endpoint_uri)
        if self.endpoint_uri is None:
            self.endpoint_uri = get_default_endpoint()

        self.websocket_timeout = websocket_timeout

        if websocket_kwargs is None:
            websocket_kwargs = {}
        else:
            found_restricted_keys = set(websocket_kwargs).intersection(
                RESTRICTED_WEBSOCKET_KWARGS
            )
            if found_restricted_keys:
                raise Web3ValidationError(
                    f"{RESTRICTED_WEBSOCKET_KWARGS} are not allowed "
                    f"in websocket_kwargs, found: {found_restricted_keys}"
                )
        self.websocket_kwargs = websocket_kwargs
        super().__init__()

    async def is_connected(self, **kwargs) -> bool:
        return await self.ws.ping() is not None

    async def connect(self) -> WebSocketClientProtocol:
        self.ws = await websockets.connect(self.endpoint_uri, **self.websocket_kwargs)
        return self.ws

    async def disconnect(self) -> None:
        await self.ws.close()

    async def make_request(self, method, params) -> None:
        request_data = self.encode_rpc_request(method, params)
        await asyncio.wait_for(
            self.ws.send(request_data), timeout=self.websocket_timeout
        )
