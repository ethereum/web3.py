from __future__ import absolute_import

import json
import itertools

from web3.utils.encoding import (
    force_bytes,
    force_obj_to_text,
)


class BaseProvider(object):
    def __init__(self):
        self.request_counter = itertools.count()

    def make_request(self, method, params):
        raise NotImplementedError("Providers must implement this method")

    def encode_rpc_request(self, method, params):
        return force_bytes(json.dumps(force_obj_to_text({
            "jsonrpc": "2.0",
            "method": method,
            "params": params or [],
            "id": next(self.request_counter),
        })))
