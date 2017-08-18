from web3.manager import (
    RequestManager,
)
from web3.providers import (
    BaseProvider,
)


class DummyProvider(BaseProvider):
    pass


def test_provider_property_setter_and_getter():
    provider_a = DummyProvider()
    provider_b = DummyProvider()

    assert provider_a is not provider_b

    manager = RequestManager(provider_a)
    assert manager.provider is provider_a

    manager.provider = provider_b

    assert manager.provider is provider_b
