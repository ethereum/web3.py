import logging

from .base import JSONBaseProvider  # noqa: E402

from eth_utils import (
    to_dict,
)

from web3.utils.six import (
    urlunparse,
)
from web3.utils.compat import (
    make_post_request,
)
from web3.utils.http import construct_user_agent


logger = logging.getLogger(__name__)


class HTTPProvider(JSONBaseProvider):
    endpoint_uri = None
    _request_args = None
    _request_kwargs = None

    def __init__(self, endpoint_uri, request_kwargs=None):
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
        response = make_post_request(
            self.endpoint_uri,
            request_data,
            **self.get_request_kwargs()
        )
        return response


class RPCProvider(HTTPProvider):
    """
    Deprecated:  Use HTTPProvider instead.
    """
    def __init__(self,
                 host="127.0.0.1",
                 port=8545,
                 path="/",
                 ssl=False,
                 **kwargs):
        netloc = "{0}:{1}".format(host, port)
        endpoint_uri = urlunparse((
            'https' if ssl else 'http',
            netloc,
            path,
            '',
            '',
            ''
        ))

        super(RPCProvider, self).__init__(endpoint_uri, kwargs)


class KeepAliveRPCProvider(RPCProvider):
    """
    Deprecated:  Use HTTPProvider instead.
    """
    def __init__(self,
                 host="127.0.0.1",
                 port=8545,
                 path="/",
                 **kwargs):
        super(KeepAliveRPCProvider, self).__init__(
            host,
            port,
            path,
            **kwargs
        )
