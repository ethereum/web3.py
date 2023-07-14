import asyncio
import logging
import os
from typing import (
    Any,
    Optional,
    Union,
)

from eth_typing import (
    URI,
)
from websockets import (
    connect as websockets_connect,
    ConnectionClosed,
)

from web3.exceptions import (
    Web3ValidationError,
)
from web3.providers.persistent import (
    PersistentConnectionProvider,
)

DEFAULT_PING_TIMEOUT = 300  # 5 minutes
DEFAULT_PING_INTERVAL = 60  # 1 minute

RESTRICTED_WEBSOCKET_KWARGS = {"uri", "loop"}
DEFAULT_WEBSOCKET_KWARGS = {
    # set how long to wait between pings from the server
    "ping_interval": DEFAULT_PING_INTERVAL,
    # set how long to wait without a pong response before closing the connection
    "ping_timeout": DEFAULT_PING_TIMEOUT,
}


def get_default_endpoint() -> URI:
    return URI(os.environ.get("WEB3_WS_PROVIDER_URI", "ws://127.0.0.1:8546"))


class WebsocketProviderV2(PersistentConnectionProvider):
    logger = logging.getLogger("web3.providers.WebsocketProviderV2")
    is_async: bool = True

    def __init__(
        self,
        endpoint_uri: Optional[Union[URI, str]] = None,
        websocket_kwargs: Optional[Any] = None,
        call_timeout: Optional[int] = None,
    ) -> None:
        self.endpoint_uri = URI(endpoint_uri)
        if self.endpoint_uri is None:
            self.endpoint_uri = get_default_endpoint()

        if websocket_kwargs is None:
            websocket_kwargs = DEFAULT_WEBSOCKET_KWARGS
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
        super().__init__(call_timeout=call_timeout)

    def __str__(self) -> str:
        return f"Websocket connection: {self.endpoint_uri}"

    async def is_connected(self, **kwargs) -> bool:
        try:
            return await self.ws.ping() if self.ws else False
        except ConnectionClosed:
            return False

    async def connect(self) -> None:
        self.ws = await websockets_connect(self.endpoint_uri, **self.websocket_kwargs)

    async def disconnect(self) -> None:
        await self.ws.close()

    async def make_request(self, method, params) -> None:
        request_data = self.encode_rpc_request(method, params)

        if self.ws is None:
            await self.connect()

        await asyncio.wait_for(
            self.ws.send(request_data), timeout=self.call_timeout
        )
