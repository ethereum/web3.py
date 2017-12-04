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

        for Provider in (IPCProvider, HTTPProvider):
            provider = Provider()
            if provider.isConnected():
                self._active_provider = provider
                return provider

        return None
