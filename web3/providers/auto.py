import os
from urllib.parse import (
    urlparse,
)

from web3.exceptions import (
    CannotHandleRequest,
)
from web3.providers import (
    BaseProvider,
    HTTPProvider,
    IPCProvider,
    WebsocketProvider,
)


def load_provider_from_environment():
    uri_string = os.environ.get('WEB3_PROVIDER_URI', '')
    if not uri_string:
        return None

    uri = urlparse(uri_string)
    if uri.scheme == 'file':
        return IPCProvider(uri.path)
    elif uri.scheme == 'http':
        return HTTPProvider(uri_string)
    elif uri.scheme == 'ws':
        return WebsocketProvider(uri_string)
    else:
        raise NotImplementedError(
            'Web3 does not know how to connect to scheme %r in %r' % (
                uri.scheme,
                uri_string,
            )
        )


class AutoProvider(BaseProvider):

    default_providers = (
        load_provider_from_environment,
        IPCProvider,
        HTTPProvider,
        WebsocketProvider,
    )
    _active_provider = None

    def __init__(self, potential_providers=None):
        '''
        :param iterable potential_providers: ordered series of provider classes to attempt with

        AutoProvider will initialize each potential provider (without arguments),
        in an attempt to find an active node. The list will default to
        :attribute:`default_providers`.
        '''
        if potential_providers:
            self._potential_providers = potential_providers
        else:
            self._potential_providers = self.default_providers

    def make_request(self, method, params):
        try:
            return self._proxy_request(method, params)
        except IOError as exc:
            return self._proxy_request(method, params, use_cache=False)

    def isConnected(self):
        provider = self._get_active_provider(use_cache=True)
        return provider is not None and provider.isConnected()

    def _proxy_request(self, method, params, use_cache=True):
        provider = self._get_active_provider(use_cache)
        if provider is None:
            raise CannotHandleRequest("Could not discover provider")

        return provider.make_request(method, params)

    def _get_active_provider(self, use_cache):
        if use_cache and self._active_provider is not None:
            return self._active_provider

        for Provider in self._potential_providers:
            provider = Provider()
            if provider is not None and provider.isConnected():
                self._active_provider = provider
                return provider

        return None
