from __future__ import absolute_import

import json
import itertools

from web3.utils.string import (
    force_bytes,
    force_obj_to_text,
    force_text,
)


class BaseProvider(object):
    def make_request(self, method, params):
        raise NotImplementedError("Providers must implement this method")

    def isConnected(self):
        raise NotImplementedError("Providers must implement this method")


class JSONBaseProvider(BaseProvider):
    def __init__(self):
        self.request_counter = itertools.count()

    def encode_rpc_request(self, method, params):
        return force_bytes(json.dumps(force_obj_to_text({
            "jsonrpc": "2.0",
            "method": method,
            "params": params or [],
            "id": next(self.request_counter),
        })))

    def isConnected(self):
        try:
            response_raw = self.make_request('web3_clientVersion', [])
            response = json.loads(force_text(response_raw))
        except IOError:
            return False
        else:
            assert response['jsonrpc'] == '2.0'
            assert 'error' not in response
            return True
        assert False
