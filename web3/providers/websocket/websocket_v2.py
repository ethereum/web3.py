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
        silence_listener_task_exceptions: bool = False,
        # `PersistentConnectionProvider` kwargs can be passed through
        **kwargs: Any,
    ) -> None:
        self.endpoint_uri = URI(endpoint_uri)
        if self.endpoint_uri is None:
            self.endpoint_uri = get_default_endpoint()

        if not any(
            self.endpoint_uri.startswith(prefix)
            for prefix in VALID_WEBSOCKET_URI_PREFIXES
        ):
            raise Web3ValidationError(
                "Websocket endpoint uri must begin with 'ws://' or 'wss://': "
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
        self.silence_listener_task_exceptions = silence_listener_task_exceptions

        super().__init__(**kwargs)

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
                self._message_listener_task = asyncio.create_task(
                    self._ws_message_listener()
                )
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

        try:
            self._message_listener_task.cancel()
            await self._message_listener_task
        except (asyncio.CancelledError, StopAsyncIteration):
            pass
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
        response = await self._get_response_for_request_id(current_request_id)

        return response

    async def _get_response_for_request_id(self, request_id: RPCId) -> RPCResponse:
        async def _match_response_id_to_request_id() -> RPCResponse:
            request_cache_key = generate_cache_key(request_id)

            while True:
                # sleep(0) here seems to be the most efficient way to yield control
                # back to the event loop while waiting for the response to be in the
                # queue.
                await asyncio.sleep(0)

                if request_cache_key in self._request_processor._request_response_cache:
                    self.logger.debug(
                        f"Popping response for id {request_id} from cache."
                    )
                    popped_response = self._request_processor.pop_raw_response(
                        cache_key=request_cache_key,
                    )
                    return popped_response

        try:
            # Add the request timeout around the while loop that checks the request
            # cache and tried to recv(). If the request is neither in the cache, nor
            # received within the request_timeout, raise ``TimeExhausted``.
            return await asyncio.wait_for(
                _match_response_id_to_request_id(), self.request_timeout
            )
        except asyncio.TimeoutError:
            raise TimeExhausted(
                f"Timed out waiting for response with request id `{request_id}` after "
                f"{self.request_timeout} second(s). This may be due to the provider "
                "not returning a response with the same id that was sent in the "
                "request or an exception raised during the request was caught and "
                "allowed to continue."
            )

    async def _ws_message_listener(self) -> None:
        self.logger.info(
            "Websocket listener background task started. Storing all messages in "
            "appropriate request processor queues / caches to be processed."
        )
        while True:
            # the use of sleep(0) seems to be the most efficient way to yield control
            # back to the event loop to share the loop with other tasks.
            await asyncio.sleep(0)

            try:
                async for raw_message in self._ws:
                    await asyncio.sleep(0)

                    response = json.loads(raw_message)
                    subscription = response.get("method") == "eth_subscription"
                    await self._request_processor.cache_raw_response(
                        response, subscription=subscription
                    )
            except Exception as e:
                if not self.silence_listener_task_exceptions:
                    loop = asyncio.get_event_loop()
                    for task in asyncio.all_tasks(loop=loop):
                        task.cancel()
                    raise e

                self.logger.error(
                    "Exception caught in listener, error logging and keeping "
                    "listener background task alive."
                    f"\n    error={e.__class__.__name__}: {e}"
                )
