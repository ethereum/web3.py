from web3.manager import (
    RequestManager,
)
from web3.providers import (
    BaseProvider,
)


def test_provider_property_setter_and_getter():
    provider_a = BaseProvider()
    provider_b = BaseProvider()

    assert provider_a is not provider_b

    manager = RequestManager(None, provider_a)
    assert manager.provider is provider_a

    manager.provider = provider_b

    assert manager.provider is provider_b
