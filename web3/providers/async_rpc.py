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
    async_cache_and_return_session as _async_cache_and_return_session,
    async_make_post_request,
    get_default_http_endpoint,
)
from web3.types import (
    RPCEndpoint,
    RPCResponse,
)

from .async_base import (
    AsyncJSONBaseProvider,
)


class AsyncHTTPProvider(AsyncJSONBaseProvider):
    logger = logging.getLogger("web3.providers.HTTPProvider")
    endpoint_uri = None
    _request_kwargs = None

    def __init__(
        self,
        endpoint_uri: Optional[Union[URI, str]] = None,
        request_kwargs: Optional[Any] = None,
    ) -> None:
        if endpoint_uri is None:
            self.endpoint_uri = get_default_http_endpoint()
        else:
            self.endpoint_uri = URI(endpoint_uri)

        self._request_kwargs = request_kwargs or {}

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
            "User-Agent": construct_user_agent(str(type(self))),
        }

    async def make_request(self, method: RPCEndpoint, params: Any) -> RPCResponse:
        self.logger.debug(
            f"Making request HTTP. URI: {self.endpoint_uri}, Method: {method}"
        )
        request_data = self.encode_rpc_request(method, params)
        raw_response = await async_make_post_request(
            self.endpoint_uri, request_data, **self.get_request_kwargs()
        )
        response = self.decode_rpc_response(raw_response)
        self.logger.debug(
            f"Getting response HTTP. URI: {self.endpoint_uri}, "
            f"Method: {method}, Response: {response}"
        )
        return response
