from web3.manager import (
    RequestManager,
)
from web3.providers import (
    BaseProvider,
)


def middleware_factory():
    def generated_middleware(*args, **kwargs):
        def middleware(*args, **kwargs):
            pass
        return middleware
    return generated_middleware


def test_provider_property_setter_and_getter():
    provider = BaseProvider()

    middleware_a = middleware_factory()
    middleware_b = middleware_factory()
    assert middleware_a is not middleware_b

    manager = RequestManager(None, provider, middlewares=[])

    assert manager.middlewares == tuple()

    manager.add_middleware(middleware_a)
    manager.add_middleware(middleware_b)

    manager.clear_middlewares()

    assert manager.middlewares == tuple()

    manager.add_middleware(middleware_b)
    manager.add_middleware(middleware_a)
    manager.add_middleware(middleware_b)
    manager.add_middleware(middleware_b)
    manager.add_middleware(middleware_a)

    assert manager.middlewares == (
        middleware_a,
        middleware_b,
        middleware_b,
        middleware_a,
        middleware_b,
    )
