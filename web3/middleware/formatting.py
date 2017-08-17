from __future__ import absolute_import

import pylru

from cytoolz.functoolz import (
    identity,
)

from .base import (
    BaseMiddleware,
)


class BaseFormatterMiddleware(BaseMiddleware):
    request_formatters = None
    result_formatters = None

    def __init__(self, *args, **kwargs):
        self._request_id_cache = pylru.lrucache(1024)
        super(BaseFormatterMiddleware, self).__init__(*args, **kwargs)

    def get_request_formatter(self, method):
        if not self.request_formatters:
            return identity
        else:
            return self.request_formatters.get(method, identity)

    def get_result_formatter(self, method):
        if not self.result_formatters:
            return identity
        else:
            return self.result_formatters.get(method, identity)

    def process_request(self, method, params, request_id):
        formatter = self.get_request_formatter(method)
        self._request_id_cache[request_id] = method
        return method, formatter(params)

    def process_result(self, result, request_id):
        method = self._request_id_cache[request_id]
        del self._request_id_cache[request_id]
        formatter = self.get_result_formatter(method)
        return formatter(result)
