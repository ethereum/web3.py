import contextlib
from geventhttpclient import HTTPClient
import logging

import pylru

from .base import JSONBaseProvider  # noqa: E402


logger = logging.getLogger(__name__)


class RPCProvider(JSONBaseProvider):
    """Create a RPC client.

    .. note ::

        You should preferably create only one client per process,
        or otherwise underlying HTTP network connections may leak.

    """
    def __init__(self,
                 host="127.0.0.1",
                 port=8545,
                 path="/",
                 ssl=False,
                 connection_timeout=10,
                 network_timeout=10,
                 *args,
                 **kwargs):
        """Create a new RPC client.

        :param connection_timeout: See :class:`geventhttpclient.HTTPClient`

        :param network_timeout: See :class:`geventhttpclient.HTTPClient`
        """
        self.host = host
        self.port = int(port)
        self.path = path
        self.ssl = ssl
        self.connection_timeout = connection_timeout
        self.network_timeout = network_timeout

        super(RPCProvider, self).__init__(*args, **kwargs)

    def __str__(self):
        return "RPC connection {}:{}".format(self.host, self.port)

    def __repr__(self):
        return self.__str__()

    def make_request(self, method, params):
        from web3 import __version__ as web3_version
        request_data = self.encode_rpc_request(method, params)
        request_user_agent = 'Web3.py/{version}/{class_name}'.format(
            version=web3_version,
            class_name=type(self),
        )
        client = HTTPClient(
            host=self.host,
            port=self.port,
            ssl=self.ssl,
            connection_timeout=self.connection_timeout,
            network_timeout=self.network_timeout,
            headers={
                'Content-Type': 'application/json',
                'User-Agent': request_user_agent,
            },
        )
        with contextlib.closing(client):
            response = client.post(self.path, body=request_data)
            response_body = response.read()

        return response_body


_client_cache = pylru.lrucache(128)


class KeepAliveRPCProvider(JSONBaseProvider):
    """RPC-provider that handles HTTP keep-alive connection correctly.

    HTTP client is recycled across requests. Create only one instance of
    KeepAliveProvider per process.
    """
    def __init__(self,
                 host="127.0.0.1",
                 port=8545,
                 path="/",
                 ssl=False,
                 connection_timeout=10,
                 network_timeout=10,
                 concurrency=10,
                 *args,
                 **kwargs):
        """Create a new RPC client with keep-alive connection pool.

        :param concurrency: See :class:`geventhttpclient.HTTPClient`

        :param connection_timeout: See :class:`geventhttpclient.HTTPClient`

        :param network_timeout: See :class:`geventhttpclient.HTTPClient`
        """
        self.host = host
        self.port = int(port)
        self.path = path
        self.ssl = ssl
        self.connection_timeout = connection_timeout
        self.network_timeout = network_timeout
        self.concurrency = concurrency

        super(KeepAliveRPCProvider, self).__init__(*args, **kwargs)

        self.client = self.get_or_create_client()

    def get_or_create_client(self):
        from web3 import __version__ as web3_version
        global _client_cache

        key = "{}:{}".format(self.host, self.port)

        try:
            # Get in-process client instance for this host
            client = _client_cache[key]
            logger.debug("Re-using HTTP client for RPC connection to %s", key)
        except KeyError:
            request_user_agent = 'Web3.py/{version}/{class_name}'.format(
                version=web3_version,
                class_name=type(self),
            )

            client = HTTPClient(
                host=self.host,
                port=self.port,
                ssl=self.ssl,
                connection_timeout=self.connection_timeout,
                network_timeout=self.network_timeout,
                concurrency=self.concurrency,
                headers={
                    'Content-Type': 'application/json',
                    'User-Agent': request_user_agent,
                },
            )
            _client_cache[key] = client
            logger.debug(
                "Created new keep-alive HTTP client for RPC connection to %s",
                key,
            )

        return client

    def __str__(self):
        return "Keep-alive RPC connection {}:{}".format(self.host, self.port)

    def __repr__(self):
        return self.__str__()

    def make_request(self, method, params):
        request_data = self.encode_rpc_request(method, params)
        response = self.client.post(self.path, body=request_data)
        response_body = response.read()
        return response_body
