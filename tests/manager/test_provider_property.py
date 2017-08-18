from web3.manager import (
    RequestManager,
)
from web3.providers import (
    BaseProvider,
)
from web3.middleware import (
    BaseMiddleware,
)


class DummyMiddleware(BaseMiddleware):
    pass


class DummyProvider(BaseProvider):
    middleware_classes = [DummyMiddleware]


def test_provider_property_setter_and_getter():
    provider_a = DummyProvider()
    provider_b = DummyProvider()

    assert provider_a is not provider_b

    manager = RequestManager(provider_a)
    assert manager.providers[0] is provider_a

    manager.providers = provider_b

    assert manager.providers[0] is provider_b
