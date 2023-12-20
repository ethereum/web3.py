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
        request_timeout: Optional[float] = DEFAULT_PERSISTENT_CONNECTION_TIMEOUT,
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
                    "Found restricted keys for websocket_kwargs: "
                    f"{found_restricted_keys}."
                )

        self.websocket_kwargs = merge(DEFAULT_WEBSOCKET_KWARGS, websocket_kwargs or {})

        super().__init__(endpoint_uri, request_timeout=request_timeout)

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
        if self._ws is not None and not self._ws.closed:
            await self._ws.close()
            self._ws = None
            self.logger.debug(
                f'Successfully disconnected from endpoint: "{self.endpoint_uri}'
            )

        self._request_processor.clear_caches()

    async def make_request(self, method: RPCEndpoint, params: Any) -> RPCResponse:
        request_data = self.encode_rpc_request(method, params)

        if self._ws is None:
            raise ProviderConnectionError(
                "Connection to websocket has not been initiated for the provider."
            )

        await asyncio.wait_for(
            self._ws.send(request_data), timeout=self.request_timeout
        )

        current_request_id = json.loads(request_data)["id"]
        response = await self._get_response_for_request_with_id(current_request_id)

        return response

    async def _get_response_for_request_with_id(self, request_id: RPCId) -> RPCResponse:
        # check cache early to avoid unnecessary websocket recv()
        cache_key = generate_cache_key(request_id)
        cached_response = self._request_processor.pop_raw_response(cache_key)
        if cached_response is not None:
            return cached_response

        # if not in cache, kick off two competing tasks to wait for the desired response
        try:
            completed, pending = await asyncio.wait_for(
                asyncio.wait(
                    [
                        # create a task to wait for response with matching request id
                        # from the websocket
                        asyncio.create_task(
                            self._await_next_ws_response(request_id=request_id)
                        ),
                        # create a task to wait for response with matching request id
                        # from the cache
                        asyncio.create_task(
                            self._request_processor._await_next_cached_response(
                                request_id=request_id
                            )
                        ),
                    ],
                    # return when the first task to find the desired response completes
                    return_when=asyncio.FIRST_COMPLETED,
                ),
                timeout=self.request_timeout,
            )

            for task in pending:
                task.cancel()

            return completed.pop().result()

        except asyncio.TimeoutError:
            raise TimeExhausted(
                f"Timed out waiting for response with request id `{request_id}` after "
                f"{self.request_timeout} second(s). This may be due to the provider "
                "not returning a response with the same id that was sent in the "
                "request or an exception raised during the request was caught and "
                "allowed to continue."
            )

    async def _await_next_ws_response(
        self, request_id: Optional[RPCId] = None, subscription: bool = False
    ) -> RPCResponse:
        """
        Wait for the next response from the websocket connection, by type, while
        caching all other responses.

        - If subscription is True, wait for the next subscription response.
        - If subscription is False, wait for the next response that matches the
            ``request_id``.
        """
        if request_id is None and not subscription:
            raise ValueError("Must provide a request_id when subscription is False.")
        elif subscription and request_id is not None:
            raise ValueError(
                "``request_id`` must be ``None`` when ``subscription`` is True."
            )

        while True:
            await asyncio.sleep(0)

            if not self._ws_lock.locked():
                async with self._ws_lock:
                    response = await self._ws_recv()

                    if subscription and response.get("method") == "eth_subscription":
                        # is a subscription type and is a subscription response
                        self.logger.info(
                            "Received subscription response from websocket, "
                            "subscription_id="
                            f"{response['params']['subscription']!r}"
                        )
                        return response
                    elif not subscription and response.get("id") == request_id:
                        # is not a subscription and response id matches the request id
                        self.logger.info(
                            f"Received response for request id `{request_id}` from "
                            "websocket."
                        )
                        return response
                    else:
                        # cache all other responses
                        self.logger.debug(
                            "Caching undesired response from websocket:\n"
                            f"    request_id={request_id}\n"
                            f"    is_subscription={subscription}"
                        )
                        self._request_processor.cache_raw_response(response)

    async def _ws_recv(self) -> RPCResponse:
        return json.loads(await self._ws.recv())
