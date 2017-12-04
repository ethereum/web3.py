import os
from urllib.parse import urlparse

from web3.exceptions import CannotHandleRequest

from web3.providers.base import BaseProvider
from web3.providers.ipc import IPCProvider
from web3.providers.rpc import HTTPProvider


class AutoProvider(BaseProvider):

    _active_provider = None

    def make_request(self, method, params):
        try:
            return self._proxy_request(method, params)
        except IOError as exc:
            return self._proxy_request(method, params, use_cache=False)

    def _proxy_request(self, method, params, use_cache=True):
        provider = self._get_active_provider(use_cache)
        if provider is None:
            raise CannotHandleRequest("Could not discover provider")

        return provider.make_request(method, params)

    def _get_active_provider(self, use_cache):
        if use_cache and self._active_provider is not None:
            return self._active_provider

        for Provider in (
            load_provider_from_environment,
            IPCProvider,
            HTTPProvider,
        ):
            provider = Provider()
            if provider is not None and provider.isConnected():
                self._active_provider = provider
                return provider

        return None


def load_provider_from_environment():
    uri_string = os.environ.get('WEB3_PROVIDER_URI', '')
    uri = urlparse(uri_string)
    if uri.scheme == 'file':
        return IPCProvider(uri.path)
    elif uri.scheme == 'http':
        return HTTPProvider(uri_string)
    else:
        return None
