from cytoolz.dicttoolz import (
    assoc,
)


class BaseMiddleware(object):
    """
    The Middleware API provides hooks to allow arbitrary modification to the
    RPC requests and responses made to providers.
    """
    provider = None

    def __init__(self, provider):
        self.provider = provider

    def _process_request(self, request, request_id):
        """
        Proxy so that the actual API method can take two parameters rather than
        the single combined `request` parameter.
        """
        method, params = request
        return self.process_request(method, params, request_id)

    def process_request(self, method, params, request_id):
        return method, params

    def _process_response(self, response, request_id):
        if 'result' in response:
            return assoc(
                response,
                'result',
                self.process_result(response['result'], request_id),
            )
        elif 'error' in response:
            return assoc(
                response,
                'error',
                self.process_result(response['error'], request_id),
            )
        else:
            raise KeyError(
                "Expected response to have either a `result` or `error` key. "
                "Only found: {0}".format(sorted(response.keys()))
            )

    def process_result(self, result, request_id):
        return result

    def process_error(self, error, request_id):
        return error
