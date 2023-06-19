import pytest
from unittest.mock import (
    Mock,
)

from web3 import (
    Web3,
)
from web3.middleware import (
    construct_error_generator_middleware,
    construct_formatting_middleware,
    construct_result_generator_middleware,
)
from web3.providers.base import (
    BaseProvider,
)
from web3.types import (
    RPCEndpoint,
)


class DummyProvider(BaseProvider):
    def make_request(self, method, params):
        raise NotImplementedError(f"Cannot make request for {method}:{params}")


@pytest.fixture
def w3():
    return Web3(provider=DummyProvider(), middlewares=[])


def test_formatting_middleware(w3):
    # No formatters by default
    w3.middleware_onion.add(construct_formatting_middleware())
    w3.middleware_onion.add(
        construct_result_generator_middleware(
            {
                "test_endpoint": lambda method, params: "done",
            }
        )
    )

    expected = "done"
    actual = w3.manager.request_blocking("test_endpoint", [])
    assert actual == expected


def test_formatting_middleware_no_method(w3):
    w3.middleware_onion.add(construct_formatting_middleware())

    # Formatting middleware requires an endpoint
    with pytest.raises(NotImplementedError):
        w3.manager.request_blocking("test_endpoint", [])


def test_formatting_middleware_request_formatters(w3):
    callable_mock = Mock()
    w3.middleware_onion.add(
        construct_result_generator_middleware(
            {RPCEndpoint("test_endpoint"): lambda method, params: "done"}
        )
    )

    w3.middleware_onion.add(
        construct_formatting_middleware(
            request_formatters={RPCEndpoint("test_endpoint"): callable_mock}
        )
    )

    expected = "done"
    actual = w3.manager.request_blocking("test_endpoint", ["param1"])

    callable_mock.assert_called_once_with(["param1"])
    assert actual == expected


def test_formatting_middleware_result_formatters(w3):
    w3.middleware_onion.add(
        construct_result_generator_middleware(
            {RPCEndpoint("test_endpoint"): lambda method, params: "done"}
        )
    )
    w3.middleware_onion.add(
        construct_formatting_middleware(
            result_formatters={RPCEndpoint("test_endpoint"): lambda x: f"STATUS:{x}"}
        )
    )

    expected = "STATUS:done"
    actual = w3.manager.request_blocking("test_endpoint", [])
    assert actual == expected


def test_formatting_middleware_result_formatters_for_none(w3):
    w3.middleware_onion.add(
        construct_result_generator_middleware(
            {RPCEndpoint("test_endpoint"): lambda method, params: None}
        )
    )
    w3.middleware_onion.add(
        construct_formatting_middleware(
            result_formatters={RPCEndpoint("test_endpoint"): lambda x: hex(x)}
        )
    )

    expected = None
    actual = w3.manager.request_blocking("test_endpoint", [])
    assert actual == expected


def test_formatting_middleware_error_formatters(w3):
    w3.middleware_onion.add(
        construct_error_generator_middleware(
            {RPCEndpoint("test_endpoint"): lambda method, params: "error"}
        )
    )
    w3.middleware_onion.add(
        construct_formatting_middleware(
            result_formatters={RPCEndpoint("test_endpoint"): lambda x: f"STATUS:{x}"}
        )
    )

    expected = "error"
    with pytest.raises(ValueError) as err:
        w3.manager.request_blocking("test_endpoint", [])
    assert str(err.value) == expected
