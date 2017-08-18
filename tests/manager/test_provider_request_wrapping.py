from web3.manager import (
    RequestManager,
)
from web3.providers import (
    BaseProvider,
)


def middleware_factory(key):
    def middleware_wrapper(provider, make_request):
        def middleware_fn(method, params, request_id):
            params.append(key)
            method = "|".join((method, key))
            response = make_request(method, params)
            response['result']['middlewares'].append(key)
            return response
        return middleware_fn
    return middleware_wrapper


middleware_a = middleware_factory('middleware-A')
middleware_b = middleware_factory('middleware-B')


class DummyProvider(BaseProvider):
    def make_request(self, method, params):
        return {
            'result': {
                'method': method,
                'params': params,
                'middlewares': [],
            },
        }


def test_provider_property_setter_and_getter():
    provider = DummyProvider()

    manager = RequestManager(provider, middlewares=[middleware_a, middleware_b])
    response = manager.request_blocking('init', ['init'], 'id-12345')

    assert response['method'] == 'init|middleware-A|middleware-B'
    assert response['params'] == ['init', 'middleware-A', 'middleware-B']
    assert response['middlewares'] == ['middleware-B', 'middleware-A']
