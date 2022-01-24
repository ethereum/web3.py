import logging
from typing import (
    Any,
    Dict,
    Iterable,
    Optional,
    Tuple,
    Union,
)

from aiohttp import (
    ClientSession,
)
from eth_typing import (
    URI,
)
from eth_utils import (
    to_dict,
)

from web3._utils.http import (
    construct_user_agent,
)
from web3._utils.request import (
    async_make_post_request,
    cache_async_session as _cache_async_session,
    get_default_http_endpoint,
)
from web3.types import (
    RPCEndpoint,
    RPCResponse,
)

from .async_base import (
    AsyncJSONBaseProvider,
)

import asyncio


class AsyncHTTPProvider(AsyncJSONBaseProvider):
    logger = logging.getLogger("web3.providers.HTTPProvider")
    endpoint_uri = None
    _request_kwargs = None

    def __init__(
        self, endpoint_uri: Optional[Union[URI, str]] = None,
            request_kwargs: Optional[Any] = None
    ) -> None:
        if endpoint_uri is None:
            self.endpoint_uri = get_default_http_endpoint()
        else:
            self.endpoint_uri = URI(endpoint_uri)

        self._request_kwargs = request_kwargs or {}

        super().__init__()

    async def cache_async_session(self, session: ClientSession) -> None:
        await _cache_async_session(self.endpoint_uri, session)

    def __str__(self) -> str:
        return f"RPC connection {self.endpoint_uri}"

    @to_dict
    def get_request_kwargs(self) -> Iterable[Tuple[str, Any]]:
        if 'headers' not in self._request_kwargs:
            yield 'headers', self.get_request_headers()
        for key, value in self._request_kwargs.items():
            yield key, value

    def get_request_headers(self) -> Dict[str, str]:
        return {
            'Content-Type': 'application/json',
            'User-Agent': construct_user_agent(str(type(self))),
        }

    async def make_request(self, method: RPCEndpoint, params: Any) -> RPCResponse:
        self.logger.debug(f"Making request HTTP. URI: {self.endpoint_uri}, Method: {method}")
        request_data = self.encode_rpc_request(method, params)
        raw_response = await async_make_post_request(
            self.endpoint_uri,
            request_data,
            **self.get_request_kwargs()
        )
        response = self.decode_rpc_response(raw_response)
        self.logger.debug(f"Getting response HTTP. URI: {self.endpoint_uri}, "
                          f"Method: {method}, Response: {response}")
        return response


class BatchedAsyncHTTPProvider(AsyncHTTPProvider):
    def __init__(self, *args, batch_size=1000, sleep_time=1.0, **kwargs):
        super().__init__(*args, **kwargs)
        self.batch_size = batch_size
        self.request_data_batch = []
        self.response_data_batch = []

        self.sleep_time = sleep_time

        self.request_count = 0
        self.batch_update_lock = asyncio.Lock()
        self.batch_response_event = asyncio.Event()

        self.response_lock = asyncio.Lock()
        self.responses_processed_event = asyncio.Event()

        # Start the request loop
        asyncio.get_running_loop().create_task(self.start_request_loop())

    async def start_request_loop(self):
        self.logger.debug("Starting request loop...")
        while True:
            await asyncio.sleep(self.sleep_time)
            self.logger.debug(f"Making {len(self.request_data_batch)} requests.")
            async with self.batch_update_lock:
                await self.dispatch_requests(self.request_data_batch)

            self.batch_response_event.clear()

    async def dispatch_requests(self, request_batch=None) -> None:
        if request_batch is None:
            request_batch = self.request_data_batch

        if len(request_batch) < 1:
            return

        request_data = b",".join(request for request in request_batch)

        request_data = b"[" + request_data + b"]"

        raw_response = await async_make_post_request(
            self.endpoint_uri, request_data, **self.get_request_kwargs()
        )

        async with self.response_lock:
            self.response_data_batch = self.decode_rpc_response(raw_response)

        self.request_data_batch = []

        self.batch_response_event.set()

        await self.responses_processed_event.wait()

    async def make_request(self, method: RPCEndpoint, params: Any) -> RPCResponse:

        self.logger.debug(
            "Making request Async HTTP. URI: %s, Method: %s"
            % (self.endpoint_uri, method),
        )

        if len(self.request_data_batch) >= self.batch_size:
            # batch is too big, wait for response recieval and processing to be done.
                await self.batch_response_event.wait()
                await self.responses_processed_event.wait()

        async with self.batch_update_lock:
            assert len(self.request_data_batch) < self.batch_size

            request_data = self.encode_rpc_request(method, params)

            request_id = self.request_count
            if self.request_count < 1:
                # We've started a new batch
                # Make sure everyone waits until all responses are processed
                self.responses_processed_event.clear()

            self.request_count += 1

            self.request_data_batch.append(request_data)

        await self.batch_response_event.wait()

        response = None

        async with self.response_lock:
            response = self.response_data_batch[request_id]
            self.request_count -= 1

            if self.request_count < 1:
                # We're done processing all the requests.
                # Clear the response batch and tell everyone that we're done.
                self.response_data_batch = []
                self.responses_processed_event.set()

        if response is None:
            raise RuntimeError("Something went terribly wrong.")

        self.logger.debug(
            "Getting batched response HTTP. URI: %s, " "Method: %s, Response: %s",
            self.endpoint_uri,
            method,
            response,
        )

        return response
