import logging
import os
from typing import (
    Any,
    Dict,
    Iterable,
    Optional,
    Tuple,
    Union,
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
    cache_session,
    make_post_request,
)
from web3.datastructures import (
    NamedElementOnion,
)
from web3.middleware import (
    http_retry_request_middleware,
)
from web3.types import (
    Middleware,
    RPCEndpoint,
    RPCResponse,
)

from .base import (
    JSONBaseProvider,
)


def get_default_endpoint() -> URI:
    return URI(os.environ.get('WEB3_HTTP_PROVIDER_URI', 'http://localhost:8545'))


class HTTPProvider(JSONBaseProvider):
    logger = logging.getLogger("web3.providers.HTTPProvider")
    endpoint_uri = None
    _request_args = None
    _request_kwargs = None
    # type ignored b/c conflict with _middlewares attr on BaseProvider
    _middlewares: Tuple[Middleware, ...] = NamedElementOnion([(http_retry_request_middleware, 'http_retry_request')])  # type: ignore # noqa: E501

    def __init__(
        self, endpoint_uri: Optional[Union[URI, str]] = None,
            request_kwargs: Optional[Any] = None,
            session: Optional[Any] = None
    ) -> None:
        if endpoint_uri is None:
            self.endpoint_uri = get_default_endpoint()
        else:
            self.endpoint_uri = URI(endpoint_uri)

        self._request_kwargs = request_kwargs or {}

        if session:
            cache_session(self.endpoint_uri, session)

        super().__init__()

    def __str__(self) -> str:
        return "RPC connection {0}".format(self.endpoint_uri)

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

    def make_request(self, method: RPCEndpoint, params: Any) -> RPCResponse:
        self.logger.debug("Making request HTTP. URI: %s, Method: %s",
                          self.endpoint_uri, method)
        request_data = self.encode_rpc_request(method, params)
        raw_response = make_post_request(
            self.endpoint_uri,
            request_data,
            **self.get_request_kwargs()
        )
        response = self.decode_rpc_response(raw_response)
        self.logger.debug("Getting response HTTP. URI: %s, "
                          "Method: %s, Response: %s",
                          self.endpoint_uri, method, response)
        return response
