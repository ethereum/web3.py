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


def test_provider_property_triggers_regeneration_of_wrapped_middleware():
    provider = BaseProvider()

    manager = RequestManager(None, provider)

    prev_id = id(manager._wrapped_provider_request_functions)

    manager.providers = provider

    after_id = id(manager._wrapped_provider_request_functions)

    assert prev_id != after_id
