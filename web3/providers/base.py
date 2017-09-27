from __future__ import absolute_import

import json
import itertools

from eth_utils import (
    force_bytes,
    force_obj_to_text,
    force_text,
)


class BaseProvider(object):
    _middlewares = ()
    _middleware_locked = False

    @property
    def middlewares(self):
        if not self._middleware_locked:
            self._middleware_locked = True
        return tuple(self._middlewares)

    @middlewares.setter
    def middlewares(self, values):
        if self._middleware_locked:
            raise RuntimeError(
                "The request manager will not notice changes in provider middleware, "
                "so you cannot modify middleware after it has been read."
            )
        self._middlewares = tuple(values)

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
