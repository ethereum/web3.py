from __future__ import absolute_import

import json
import itertools

from eth_utils import (
    force_bytes,
    force_obj_to_text,
    force_text,
)


class BaseProvider(object):
    _middlewares = None

    @property
    def middlewares(self):
        return self._middlewares or tuple()

    @middlewares.setter
    def middlewares(self, value):
        self._middlewares = tuple(value)

    def add_middleware(self, middleware):
        self.middlewares = tuple(itertools.chain(
            [middleware],
            self.middlewares,
        ))

    def clear_middlewares(self):
        self.middlewares = tuple()

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
