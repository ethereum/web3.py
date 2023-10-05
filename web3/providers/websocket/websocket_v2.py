import asyncio
import json
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

from web3._utils.caching import (
    generate_cache_key,
)
from web3.exceptions import (
    ProviderConnectionError,
    TimeExhausted,
    Web3ValidationError,
)
from web3.providers.persistent import (
    DEFAULT_PERSISTENT_CONNECTION_TIMEOUT,
    PersistentConnectionProvider,
)
from web3.types import (
    RPCEndpoint,
    RPCId,
    RPCResponse,
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
    _max_connection_retries: int = 5

    def __init__(
        self,
        endpoint_uri: Optional[Union[URI, str]] = None,
        websocket_kwargs: Optional[Dict[str, Any]] = None,
        call_timeout: Optional[float] = DEFAULT_PERSISTENT_CONNECTION_TIMEOUT,
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
        if not self._ws:
            return False

        try:
            await self._ws.pong()
            return True

        except WebSocketException as e:
            if show_traceback:
                raise ProviderConnectionError(
                    f"Error connecting to endpoint: '{self.endpoint_uri}'"
                ) from e
            return False

    async def connect(self) -> None:
        _connection_attempts = 0
        _backoff_rate_change = 1.75
        _backoff_time = 1.75

        while _connection_attempts != self._max_connection_retries:
            try:
                _connection_attempts += 1
                self._ws = await connect(self.endpoint_uri, **self.websocket_kwargs)
                break
            except WebSocketException as e:
                if _connection_attempts == self._max_connection_retries:
                    raise ProviderConnectionError(
                        f"Could not connect to endpoint: {self.endpoint_uri}. "
                        f"Retries exceeded max of {self._max_connection_retries}."
                    ) from e
                self.logger.info(
                    f"Could not connect to endpoint: {self.endpoint_uri}. Retrying in "
                    f"{round(_backoff_time, 1)} seconds.",
                    exc_info=True,
                )
                await asyncio.sleep(_backoff_time)
                _backoff_time *= _backoff_rate_change

    async def disconnect(self) -> None:
        await self._ws.close()
        self._ws = None

        # clear the request information cache after disconnecting
        self._request_processor.clear_caches()
        self.logger.debug(
            f'Successfully disconnected from endpoint: "{self.endpoint_uri}" '
            "and the request processor transient caches were cleared."
        )

    async def make_request(self, method: RPCEndpoint, params: Any) -> RPCResponse:
        request_data = self.encode_rpc_request(method, params)

        if self._ws is None:
            await self.connect()

        await asyncio.wait_for(self._ws.send(request_data), timeout=self.call_timeout)

        current_request_id = json.loads(request_data)["id"]
        request_cache_key = generate_cache_key(current_request_id)

        if request_cache_key in self._request_processor._raw_response_cache:
            # if response is already cached, pop it from cache
            response = await self._request_processor.pop_raw_response(request_cache_key)
        else:
            # else, wait for the desired response, caching all others along the way
            response = await self._get_response_for_request_id(current_request_id)

        return response

    async def _get_response_for_request_id(self, request_id: RPCId) -> RPCResponse:
        async def _match_response_id_to_request_id() -> RPCResponse:
            response_id = None
            response = None
            while response_id != request_id:
                response = await self._ws_recv()
                response_id = response.get("id")

                if response_id == request_id:
                    break
                else:
                    # cache all responses that are not the desired response
                    await self._request_processor.cache_raw_response(
                        response,
                    )
                    await asyncio.sleep(0.1)

            return response

        try:
            # Enters a while loop, looking for a response id match to the request id.
            # If the provider does not give responses with matching ids, this will
            # hang forever. The JSON-RPC spec requires that providers respond with
            # the same id that was sent in the request, but we need to handle these
            # "bad" cases somewhat gracefully.
            timeout = (
                self.call_timeout
                if self.call_timeout and self.call_timeout <= 20
                else 20
            )
            return await asyncio.wait_for(_match_response_id_to_request_id(), timeout)
        except asyncio.TimeoutError:
            raise TimeExhausted(
                f"Timed out waiting for response with request id `{request_id}` after "
                f"{self.call_timeout} seconds. This is likely due to the provider not "
                "returning a response with the same id that was sent in the request, "
                "which is required by the JSON-RPC spec."
            )

    async def _ws_recv(self) -> RPCResponse:
        return json.loads(
            await asyncio.wait_for(self._ws.recv(), timeout=self.call_timeout)
        )
