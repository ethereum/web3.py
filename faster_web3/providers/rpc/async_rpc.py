import asyncio
import logging
from typing import (
    Any,
    Dict,
    Iterable,
    List,
    Optional,
    Tuple,
    Union,
    cast,
)

from aiohttp import (
    ClientError,
    ClientSession,
)
from eth_typing import (
    URI,
)
from faster_eth_utils import (
    combomethod,
    to_dict,
)

from faster_web3._utils.empty import (
    Empty,
    empty,
)
from faster_web3._utils.http import (
    construct_user_agent,
)
from faster_web3.types import (
    RPCEndpoint,
    RPCResponse,
)

from ..._utils.batching import (
    sort_batch_response_by_response_ids,
)
from ..._utils.caching import (
    async_handle_request_caching,
)
from ..._utils.http_session_manager import (
    HTTPSessionManager,
)
from ..async_base import (
    AsyncJSONBaseProvider,
)
from .utils import (
    ExceptionRetryConfiguration,
    check_if_retry_on_failure,
)


class AsyncHTTPProvider(AsyncJSONBaseProvider):
    logger = logging.getLogger("faster_web3.providers.AsyncHTTPProvider")
    endpoint_uri = None
    _request_kwargs = None

    def __init__(
        self,
        endpoint_uri: Optional[Union[URI, str]] = None,
        request_kwargs: Optional[Any] = None,
        exception_retry_configuration: Optional[
            Union[ExceptionRetryConfiguration, Empty]
        ] = empty,
        **kwargs: Any,
    ) -> None:
        self._request_session_manager = HTTPSessionManager()

        if endpoint_uri is None:
            self.endpoint_uri = (
                self._request_session_manager.get_default_http_endpoint()
            )
        else:
            self.endpoint_uri = URI(endpoint_uri)

        self._request_kwargs = request_kwargs or {}
        self._exception_retry_configuration = exception_retry_configuration

        super().__init__(**kwargs)

    async def cache_async_session(self, session: ClientSession) -> ClientSession:
        return await self._request_session_manager.async_cache_and_return_session(
            self.endpoint_uri, session
        )

    def __str__(self) -> str:
        return f"RPC connection {self.endpoint_uri}"

    @property
    def exception_retry_configuration(self) -> ExceptionRetryConfiguration:
        if isinstance(self._exception_retry_configuration, Empty):
            self._exception_retry_configuration = ExceptionRetryConfiguration(
                errors=(ClientError, TimeoutError)
            )
        return self._exception_retry_configuration

    @exception_retry_configuration.setter
    def exception_retry_configuration(
        self, value: Union[ExceptionRetryConfiguration, Empty]
    ) -> None:
        self._exception_retry_configuration = value

    @to_dict
    def get_request_kwargs(self) -> Iterable[Tuple[str, Any]]:
        if "headers" not in self._request_kwargs:
            yield "headers", self.get_request_headers()
        yield from self._request_kwargs.items()

    @combomethod
    def get_request_headers(cls) -> Dict[str, str]:
        if isinstance(cls, AsyncHTTPProvider):
            cls_name = cls.__class__.__name__
        else:
            cls_name = cls.__name__
        module = cls.__module__

        return {
            "Content-Type": "application/json",
            "User-Agent": construct_user_agent(module, cls_name),
        }

    async def _make_request(self, method: RPCEndpoint, request_data: bytes) -> bytes:
        """
        If exception_retry_configuration is set, retry on failure; otherwise, make
        the request without retrying.
        """
        session_manager = self._request_session_manager
        retry_config = self.exception_retry_configuration
        endpoint = self.endpoint_uri
        if (
            retry_config is None
            or not check_if_retry_on_failure(method, retry_config.method_allowlist)
        ):
            return await session_manager.async_make_post_request(
                endpoint, request_data, **self.get_request_kwargs()
            )
        
        retry_on_errs = tuple(retry_config.errors)
        for i in range(retries := retry_config.retries):
            try:
                return await session_manager.async_make_post_request(
                    endpoint, request_data, **self.get_request_kwargs()
                )
            except retry_on_errs:
                if i < retries - 1:
                    await asyncio.sleep(
                        retry_config.backoff_factor * 2**i
                    )
                else:
                    raise
        return None

    @async_handle_request_caching
    async def make_request(self, method: RPCEndpoint, params: Any) -> RPCResponse:
        self.logger.debug(
            "Making request HTTP. URI: %s, Method: %s", self.endpoint_uri, method
        )
        request_data = self.encode_rpc_request(method, params)
        raw_response = await self._make_request(method, request_data)
        response = self.decode_rpc_response(raw_response)
        self.logger.debug(
            "Getting response HTTP. URI: %s, Method: %s, Response: %s",
            self.endpoint_uri,
            method,
            response,
        )
        return response

    async def make_batch_request(
        self, batch_requests: List[Tuple[RPCEndpoint, Any]]
    ) -> Union[List[RPCResponse], RPCResponse]:
        self.logger.debug("Making batch request HTTP - uri: `%s`", self.endpoint_uri)
        request_data = self.encode_batch_rpc_request(batch_requests)
        raw_response = await self._request_session_manager.async_make_post_request(
            self.endpoint_uri, request_data, **self.get_request_kwargs()
        )
        self.logger.debug("Received batch response HTTP.")
        response = self.decode_rpc_response(raw_response)
        if not isinstance(response, list):
            # RPC errors return only one response with the error object
            return response
        return sort_batch_response_by_response_ids(
            cast(List[RPCResponse], sort_batch_response_by_response_ids(response))
        )

    async def disconnect(self) -> None:
        cache = self._request_session_manager.session_cache
        for _, session in cache.items():
            await session.close()
        cache.clear()

        self.logger.info("Successfully disconnected from: %s", self.endpoint_uri)
