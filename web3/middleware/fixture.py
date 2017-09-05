def construct_fixture_middleware(fixtures):
    def fixture_middleware(make_request, web3):
        def middleware(method, params):
            if method in fixtures:
                fixture = fixtures[method]
                if callable(fixture):
                    return fixture(params)
                else:
                    return fixture
            else:
                return make_request(method, params)
        return middleware
    return fixture_middleware
