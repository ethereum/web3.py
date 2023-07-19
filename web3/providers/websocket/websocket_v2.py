import asyncio
import logging
import os
from typing import (
    Any,
    Dict,
    Optional,
    Union,
)

from eth_typing import (
    URI,
)
from toolz import (
    merge,
)
from websockets.client import (
    connect,
)
from websockets.exceptions import (
    WebSocketException,
)

from web3.exceptions import (
    ProviderConnectionError,
    Web3ValidationError,
)
from web3.providers.persistent import (
    PersistentConnectionProvider,
)
from web3.types import (
    RPCEndpoint,
)

DEFAULT_PING_INTERVAL = 30  # 30 seconds
DEFAULT_PING_TIMEOUT = 300  # 5 minutes

VALID_WEBSOCKET_URI_PREFIXES = {"ws://", "wss://"}
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
        websocket_kwargs: Optional[Dict[str, Any]] = None,
        call_timeout: Optional[int] = None,
    ) -> None:
        self.endpoint_uri = URI(endpoint_uri)
        if self.endpoint_uri is None:
            self.endpoint_uri = get_default_endpoint()

        if not any(
            self.endpoint_uri.startswith(prefix)
            for prefix in VALID_WEBSOCKET_URI_PREFIXES
        ):
            raise Web3ValidationError(
                f"Websocket endpoint uri must begin with 'ws://' or 'wss://': "
                f"{self.endpoint_uri}"
            )

        if websocket_kwargs is not None:
            found_restricted_keys = set(websocket_kwargs).intersection(
                RESTRICTED_WEBSOCKET_KWARGS
            )
            if found_restricted_keys:
                raise Web3ValidationError(
                    f"Found restricted keys for websocket_kwargs: "
                    f"{found_restricted_keys}."
                )

        self.websocket_kwargs = merge(DEFAULT_WEBSOCKET_KWARGS, websocket_kwargs or {})

        super().__init__(endpoint_uri, call_timeout=call_timeout)

    def __str__(self) -> str:
        return f"Websocket connection: {self.endpoint_uri}"

    async def is_connected(self, show_traceback: bool = False) -> bool:
        if not self.ws:
            return False

        try:
            pong_waiter = await self.ws.ping()
            await asyncio.wait_for(pong_waiter, timeout=self.call_timeout)
            return True

        except (WebSocketException, asyncio.TimeoutError) as e:
            if show_traceback:
                raise ProviderConnectionError(
                    f"Error connecting to endpoint: '{self.endpoint_uri}'"
                ) from e
            return False

    async def connect(self) -> None:
        try:
            self.ws = await connect(self.endpoint_uri, **self.websocket_kwargs)
        except Exception as e:
            raise ProviderConnectionError(
                f"Could not connect to endpoint: {self.endpoint_uri}"
            ) from e

    async def disconnect(self) -> None:
        await self.ws.close()

        # clear the provider request cache after disconnecting
        self._async_response_processing_cache.clear()

    async def make_request(self, method: RPCEndpoint, params: Any) -> None:
        request_data = self.encode_rpc_request(method, params)

        if self.ws is None:
            await self.connect()

        await asyncio.wait_for(self.ws.send(request_data), timeout=self.call_timeout)
