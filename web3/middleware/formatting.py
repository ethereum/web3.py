from cytoolz.dicttoolz import (
    assoc,
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

    def formatter_middleware(make_request, web3):
        def middleware(method, params):
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
