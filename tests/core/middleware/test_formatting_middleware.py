import pytest
from unittest.mock import (
    Mock,
)

from web3 import (
    Web3,
)
from web3.exceptions import (
    Web3RPCError,
)
from web3.middleware import (
    FormattingMiddlewareBuilder,
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
    return Web3(provider=DummyProvider(), middleware=[])


def test_formatting_middleware(w3, request_mocker):
    # No formatters by default
    expected = "done"
    with request_mocker(w3, mock_results={"test_endpoint": "done"}):
        actual = w3.manager.request_blocking(RPCEndpoint("test_endpoint"), [])
        assert actual == expected


def test_formatting_middleware_no_method(w3):
    w3.middleware_onion.add(FormattingMiddlewareBuilder.build())

    # Formatting middleware requires an endpoint
    with pytest.raises(NotImplementedError):
        w3.manager.request_blocking("test_endpoint", [])


def test_formatting_middleware_request_formatters(w3, request_mocker):
    callable_mock = Mock()
    w3.middleware_onion.add(
        FormattingMiddlewareBuilder.build(
            request_formatters={"test_endpoint": callable_mock}
        )
    )

    expected = "done"
    with request_mocker(w3, mock_results={"test_endpoint": "done"}):
        actual = w3.manager.request_blocking("test_endpoint", ["param1"])

    callable_mock.assert_called_once_with(["param1"])
    assert actual == expected


def test_formatting_middleware_result_formatters(w3, request_mocker):
    w3.middleware_onion.add(
        FormattingMiddlewareBuilder.build(
            result_formatters={"test_endpoint": lambda x: f"STATUS: {x}"}
        )
    )

    expected = "STATUS: done"
    with request_mocker(w3, mock_results={"test_endpoint": "done"}):
        actual = w3.manager.request_blocking("test_endpoint", [])

    assert actual == expected


def test_formatting_middleware_result_formatters_for_none(w3, request_mocker):
    w3.middleware_onion.add(
        FormattingMiddlewareBuilder.build(
            result_formatters={"test_endpoint": lambda x: hex(x)}
        )
    )

    expected = None
    with request_mocker(w3, mock_results={"test_endpoint": expected}):
        actual = w3.manager.request_blocking("test_endpoint", [])
    assert actual == expected


def test_formatting_middleware_error_formatters(w3, request_mocker):
    w3.middleware_onion.add(
        FormattingMiddlewareBuilder.build(
            result_formatters={"test_endpoint": lambda x: f"STATUS: {x}"}
        )
    )

    expected = "error"
    with request_mocker(w3, mock_errors={"test_endpoint": {"message": "error"}}):
        with pytest.raises(Web3RPCError) as err:
            w3.manager.request_blocking("test_endpoint", [])
            assert str(err.value) == expected
