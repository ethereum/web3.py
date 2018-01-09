import logging
import os

from .base import JSONBaseProvider  # noqa: E402

from eth_utils import (
    to_dict,
)

from web3.utils.request import (
    make_post_request,
)
from web3.utils.http import construct_user_agent

from web3.utils.datastructures import (
    NamedElementStack,
)

from web3.middleware import http_retry_request_middleware

logger = logging.getLogger(__name__)


def get_default_endpoint():
    return os.environ.get('WEB3_HTTP_PROVIDER_URI', 'http://localhost:8545')


class HTTPProvider(JSONBaseProvider):
    endpoint_uri = None
    _request_args = None
    _request_kwargs = None
    _middlewares = NamedElementStack([(http_retry_request_middleware, 'http_retry_request')])

    def __init__(self, endpoint_uri=None, request_kwargs=None):
        if endpoint_uri is None:
            self.endpoint_uri = get_default_endpoint()
        else:
            self.endpoint_uri = endpoint_uri
        self._request_kwargs = request_kwargs or {}
        super(HTTPProvider, self).__init__()

    def __str__(self):
        return "RPC connection {0}".format(self.endpoint_uri)

    @to_dict
    def get_request_kwargs(self):
        if 'headers' not in self._request_kwargs:
            yield 'headers', self.get_request_headers()
        for key, value in self._request_kwargs.items():
            yield key, value

    def get_request_headers(self):
        return {
            'Content-Type': 'application/json',
            'User-Agent': construct_user_agent(str(type(self))),
        }

    def make_request(self, method, params):
        request_data = self.encode_rpc_request(method, params)
        raw_response = make_post_request(
            self.endpoint_uri,
            request_data,
            **self.get_request_kwargs()
        )
        response = self.decode_rpc_response(raw_response)
        return response
