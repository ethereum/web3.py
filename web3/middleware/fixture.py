def construct_fixture_middleware(fixtures):
    """
    Constructs a middleware which returns a static response for any method
    which is found in the provided fixtures.
    """
    def fixture_middleware(make_request, web3):
        def middleware(method, params):
            if method in fixtures:
                result = fixtures[method]
                return {'result': result}
            else:
                return make_request(method, params)
        return middleware
    return fixture_middleware


def construct_result_middleware(result_callbacks):
    """
    Constructs a middleware which intercepts requests for any method found in
    the provided mapping of endpoints to callbacks, returning whatever response
    the callback generates.  Callbacks must be functions with the signature
    `fn(method, params)`.
    """
    def result_callback_middleware(make_request, web3):
        def middleware(method, params):
            if method in result_callbacks:
                result = result_callbacks[method](method, params)
                return {'result': result}
            else:
                return make_request(method, params)
        return middleware
    return result_callback_middleware


def construct_error_middleware(error_callbacks):
    """
    Constructs a middleware which intercepts requests for any method found in
    the provided mapping of endpoints to callbacks, returning whatever response
    the callback generates.  Callbacks must be functions with the signature
    `fn(method, params)`.
    """
    def error_callback_middleware(make_request, web3):
        def middleware(method, params):
            if method in error_callbacks:
                error_msg = error_callbacks[method](method, params)
                return {'error': error_msg}
            else:
                return make_request(method, params)
        return middleware
    return error_callback_middleware
