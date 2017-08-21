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
    assert manager.providers[0] is provider_a

    manager.providers = provider_b

    assert manager.providers[0] is provider_b
