import asyncio
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
    ClientError,
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
    async_cache_and_return_session as _async_cache_and_return_session,
    async_make_post_request,
    get_default_http_endpoint,
)
from web3.types import (
    RPCEndpoint,
    RPCResponse,
)

from ..._utils.caching import (
    async_handle_request_caching,
)
from ..async_base import (
    AsyncJSONBaseProvider,
)
from .utils import (
    ExceptionRetryConfiguration,
    check_if_retry_on_failure,
)


class AsyncHTTPProvider(AsyncJSONBaseProvider):
    logger = logging.getLogger("web3.providers.AsyncHTTPProvider")
    endpoint_uri = None
    _request_kwargs = None

    def __init__(
        self,
        endpoint_uri: Optional[Union[URI, str]] = None,
        request_kwargs: Optional[Any] = None,
        exception_retry_configuration: Optional[
            ExceptionRetryConfiguration
        ] = ExceptionRetryConfiguration(errors=(ClientError, TimeoutError)),
    ) -> None:
        if endpoint_uri is None:
            self.endpoint_uri = get_default_http_endpoint()
        else:
            self.endpoint_uri = URI(endpoint_uri)

        self._request_kwargs = request_kwargs or {}
        self.exception_retry_configuration = exception_retry_configuration

        super().__init__()

    async def cache_async_session(self, session: ClientSession) -> ClientSession:
        return await _async_cache_and_return_session(self.endpoint_uri, session)

    def __str__(self) -> str:
        return f"RPC connection {self.endpoint_uri}"

    @to_dict
    def get_request_kwargs(self) -> Iterable[Tuple[str, Any]]:
        if "headers" not in self._request_kwargs:
            yield "headers", self.get_request_headers()
        for key, value in self._request_kwargs.items():
            yield key, value

    def get_request_headers(self) -> Dict[str, str]:
        return {
            "Content-Type": "application/json",
            "User-Agent": construct_user_agent(type(self)),
        }

    async def _make_request(self, method: RPCEndpoint, request_data: bytes) -> bytes:
        """
        If exception_retry_configuration is set, retry on failure; otherwise, make
        the request without retrying.
        """
        if (
            self.exception_retry_configuration is not None
            and check_if_retry_on_failure(
                method, self.exception_retry_configuration.method_allowlist
            )
        ):
            for i in range(self.exception_retry_configuration.retries):
                try:
                    return await async_make_post_request(
                        self.endpoint_uri, request_data, **self.get_request_kwargs()
                    )
                except tuple(self.exception_retry_configuration.errors):
                    if i < self.exception_retry_configuration.retries - 1:
                        await asyncio.sleep(
                            self.exception_retry_configuration.backoff_factor
                        )
                        continue
                    else:
                        raise
            return None
        else:
            return await async_make_post_request(
                self.endpoint_uri, request_data, **self.get_request_kwargs()
            )

    @async_handle_request_caching
    async def make_request(self, method: RPCEndpoint, params: Any) -> RPCResponse:
        self.logger.debug(
            f"Making request HTTP. URI: {self.endpoint_uri}, Method: {method}"
        )
        request_data = self.encode_rpc_request(method, params)
        raw_response = await self._make_request(method, request_data)
        response = self.decode_rpc_response(raw_response)
        self.logger.debug(
            f"Getting response HTTP. URI: {self.endpoint_uri}, "
            f"Method: {method}, Response: {response}"
        )
        return response
