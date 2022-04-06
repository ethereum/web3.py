import logging
from typing import (
    Any,
    Dict,
    Iterable,
    Optional,
    Tuple,
    Union,
)
from dataclasses import (
    dataclass,
)

from eth_typing import (
    URI,
)
from eth_utils import (
    to_dict,
)
from requests.models import HTTPError

from web3._utils.http import (
    construct_user_agent,
)
from web3._utils.request import (
    async_make_post_request,
    cache_async_session as _cache_async_session,
    make_post_request,
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
from aiohttp.client_exceptions import (
    ClientResponseError,
)


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

    async def cache_async_session(self, session) -> None:
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


@dataclass(frozen=False)
class QueueItem:
    idx: int
    request_data: bytes  # encoded rpc request.
    response_ready_event: asyncio.Event


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
        self.responses_ready = asyncio.Event()

        self.waiting_request_count = 0

        self.request_queue = asyncio.Queue()

        self.response_dict = {}

        # Start the request loop
        asyncio.get_running_loop().create_task(self.start_request_loop())

    async def start_request_loop(self):
        self.logger.debug("Starting request loop...")
        while True:
            await asyncio.sleep(self.sleep_time)
            await self.dispatch_requests()

    async def _build_request_batch(self):
        request_batch = []
        num_requests = min(self.batch_size, self.request_queue.qsize())
        self.logger.debug(f"{self.request_queue.qsize()} requests in queue.")
        for _ in range(num_requests):
            item: QueueItem = await self.request_queue.get()
            request_batch.append(item)

        return request_batch

    async def _make_batch_request(self, request_batch:Iterable[QueueItem]):
        request_data = (
            b"[" + b",".join(item.request_data for item in request_batch) + b"]"
        )

        try:
            raw_response = make_post_request(
                self.endpoint_uri, request_data, **self.get_request_kwargs()
            )

            response_batch = self.decode_rpc_response(raw_response)

            for item, response in zip(request_batch, response_batch):
                self.response_dict[item.idx] = response
                item.response_ready_event.set()
        except HTTPError as e:
            self.logger.exception("Batch request failed. Trying again...")
            for item in request_batch:
                await self.request_queue.put(item)

    async def dispatch_requests(self) -> None:

        if self.request_queue.qsize() < 1:
            return

        request_batch = await self._build_request_batch()
        self.logger.debug(f"Making {len(request_batch)} requests.")

        await self._make_batch_request(request_batch)

    async def make_request(self, method: RPCEndpoint, params: Any) -> RPCResponse:

        self.logger.debug(
            "Queueing request Async HTTP. URI: %s, Method: %s"
            % (self.endpoint_uri, method),
        )

        request_data = self.encode_rpc_request(method, params)
        request_idx = self.request_queue.qsize()
        response_ready_event = asyncio.Event()

        await self.request_queue.put(
            QueueItem(
                idx=request_idx,
                request_data=request_data,
                response_ready_event=response_ready_event,
            )
        )

        response = None

        await response_ready_event.wait()

        response = self.response_dict[request_idx]

        if response is None:
            raise RuntimeError("Something went terribly wrong.")

        self.logger.debug(
            "Getting batched response HTTP. URI: %s, " "Method: %s, Response: %s",
            self.endpoint_uri,
            method,
            response,
        )

        return response


class BatchedAsyncHTTPMulticallProvider(BatchedAsyncHTTPProvider):
    def __init__(*args, multicall_contract, **kwargs):
        super().__init__(*args, **kwargs)
        self.multicall_contract = multicall_contract

    def dispatch_requests(self) -> None:
        raise NotImplementedError
