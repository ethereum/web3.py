import json
import itertools


class BaseProvider(object):
    def __init__(self):
        self.request_counter = itertools.count()

    def make_request(self, method, params):
        raise NotImplementedError("Providers must implement this method")

    def encode_rpc_request(self, method, params):
        return json.dumps({
            "jsonrpc": "2.0",
            "method": method,
            "params": params or [],
            "id": next(self.request_counter),
        })
