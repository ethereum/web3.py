from web3._utils.toolz import (
    assoc,
    curry,
    merge,
)


def construct_formatting_middleware(
        request_formatters=None,
        result_formatters=None,
        error_formatters=None):
    def ignore_web3_in_standard_formatters(w3):
        return dict(
            request_formatters=request_formatters or {},
            result_formatters=result_formatters or {},
            error_formatters=error_formatters or {},
        )

    return construct_web3_formatting_middleware(ignore_web3_in_standard_formatters)


def construct_web3_formatting_middleware(web3_formatters_builder):
    def formatter_middleware(make_request, w3):
        formatters = merge(
            {
                'request_formatters': {},
                'result_formatters': {},
                'error_formatters': {},
            },
            web3_formatters_builder(w3),
        )
        return apply_formatters(make_request=make_request, **formatters)

    return formatter_middleware


@curry
def apply_formatters(
        method,
        params,
        make_request,
        request_formatters,
        result_formatters,
        error_formatters):
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
