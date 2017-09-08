def construct_fixture_middleware(fixtures):
    """
    Constructs a middleware which returns a static response for any method
    which is found in the provided fixtures.
    """
    def fixture_middleware(make_request, web3):
        def middleware(method, params):
            if method in fixtures:
                return {
                    'result': fixtures[method],
                }
            else:
                return make_request(method, params)
        return middleware
    return fixture_middleware
