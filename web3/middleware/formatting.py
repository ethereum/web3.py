from __future__ import absolute_import

import pylru

from cytoolz.dicttoolz import (
    assoc,
)
from cytoolz.functoolz import (
    identity,
)

from .base import (
    BaseMiddleware,
)


def construct_formatting_middleware(request_formatters=None,
                                    result_formatters=None,
                                    error_formatters=None):
    if request_formatters is None:
        request_formatters = {}
    if result_formatters is None:
        result_formatters = {}
    if error_formatters is None:
        error_formatters = {}

    def formatter_middleware(provider, make_request):
        def middleware(method, params, request_id):
            if method in request_formatters:
                formatter = request_formatters[method]
                formatted_params = formatter(params)
                response = make_request(method, formatted_params)
            else:
                response = make_request(method, params)

            if 'result' in response and method in result_formatters:
                formatter = result_formatters[method]
                formatted_response = assoc(
                    response,
                    'result',
                    formatter(response['result']),
                )
                return formatted_response
            elif 'error' in response and method in error_formatters:
                formatter = error_formatters[method]
                formatted_response = assoc(
                    response,
                    'error',
                    formatter(response['error']),
                )
                return formatted_response
            else:
                return response
        return middleware
    return formatter_middleware


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
