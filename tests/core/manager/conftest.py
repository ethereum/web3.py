import itertools
import pytest

from web3.middleware.base import (
    Web3Middleware,
)


@pytest.fixture
def middleware_factory():
    unique_ids = itertools.count()

    def factory(key=None):
        if key is None:
            key = next(unique_ids)
        key = str(key)

        class Wrapper:
            def __repr__(self):
                return "middleware-" + key

            def __call__(self, web3):
                class Middleware(Web3Middleware):
                    def wrap_make_request(self, make_request):
                        def middleware_fn(method, params):
                            params.append(key)
                            method = "|".join((method, key))
                            response = make_request(method, params)
                            response["result"]["middleware"].append(key)
                            return response

                        return middleware_fn

                return Middleware(web3)

        return Wrapper()

    return factory
