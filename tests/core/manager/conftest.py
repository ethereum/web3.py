import itertools
import pytest


@pytest.fixture
def middleware_factory():
    unique_ids = itertools.count()

    def factory(key=None):
        if key is None:
            key = next(unique_ids)
        key = str(key)

        class Wrapper:
            def __repr__(self):
                return 'middleware-' + key

            def __call__(self, make_request, web3):
                def middleware_fn(method, params):
                    params.append(key)
                    method = "|".join((method, key))
                    response = make_request(method, params)
                    response['result']['middlewares'].append(key)
                    return response
                return middleware_fn
        return Wrapper()
    return factory
