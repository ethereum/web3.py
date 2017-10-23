from __future__ import absolute_import

import json
import itertools

from eth_utils import (
    force_bytes,
    force_obj_to_text,
    force_text,
)

from web3.middleware import (
    combine_middlewares,
)


class BaseProvider(object):
    _middlewares = ()
    _request_func_cache = (None, None)  # a tuple of (all_middlewares, request_func)

    @property
    def middlewares(self):
        return self._middlewares

    @middlewares.setter
    def middlewares(self, values):
        self._middlewares = tuple(values)

    def request_func(self, web3, outer_middlewares):
        '''
        @param outer_middlewares is an iterable of middlewares, ordered by first to execute
        @returns a function that calls all the middleware and eventually self.make_request()
        '''
        all_middlewares = tuple(outer_middlewares) + tuple(self.middlewares)

        cache_key = self._request_func_cache[0]
        if cache_key is None or cache_key != all_middlewares:
            self._request_func_cache = (
                all_middlewares,
                self._generate_request_func(web3, all_middlewares)
            )
        return self._request_func_cache[-1]

    def _generate_request_func(self, web3, middlewares):
        return combine_middlewares(
            middlewares=middlewares,
            web3=web3,
            provider_request_fn=self.make_request,
        )

    def make_request(self, method, params):
        raise NotImplementedError("Providers must implement this method")

    def isConnected(self):
        raise NotImplementedError("Providers must implement this method")


class JSONBaseProvider(BaseProvider):
    def __init__(self):
        self.request_counter = itertools.count()

    def decode_rpc_response(self, response):
        return json.loads(force_text(response))

    def encode_rpc_request(self, method, params):
        return force_bytes(json.dumps(force_obj_to_text({
            "jsonrpc": "2.0",
            "method": method,
            "params": params or [],
            "id": next(self.request_counter),
        })))

    def isConnected(self):
        try:
            response = self.make_request('web3_clientVersion', [])
        except IOError:
            return False
        else:
            assert response['jsonrpc'] == '2.0'
            assert 'error' not in response
            return True
        assert False
