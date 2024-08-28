import pytest

from web3 import (
    Web3,
)
from web3.exceptions import (
    Web3ValueError,
)
from web3.middleware import (
    FormattingMiddlewareBuilder,
    Web3Middleware,
)


class TestMiddleware(Web3Middleware):
    def response_processor(self, method, response):
        if method == "eth_blockNumber":
            response["result"] = 1234

        return response


class TestMiddleware2(Web3Middleware):
    def response_processor(self, method, response):
        if method == "eth_blockNumber":
            response["result"] = 4321

        return response


def test_middleware_class_eq_magic_method():
    w3_a = Web3()
    w3_b = Web3()

    mw1w3_a = TestMiddleware(w3_a)
    assert mw1w3_a is not None
    assert mw1w3_a != ""

    mw1w3_a_equal = TestMiddleware(w3_a)
    assert mw1w3_a == mw1w3_a_equal

    mw2w3_a = TestMiddleware2(w3_a)
    mw1w3_b = TestMiddleware(w3_b)
    assert mw1w3_a != mw2w3_a
    assert mw1w3_a != mw1w3_b


def test_unnamed_middleware_are_given_unique_keys(w3):
    request_formatting_middleware = FormattingMiddlewareBuilder.build(
        request_formatters={lambda x: x}
    )
    request_formatting_middleware2 = FormattingMiddlewareBuilder.build(
        request_formatters={lambda x: x if x else None}
    )
    result_formatting_middleware = FormattingMiddlewareBuilder.build(
        result_formatters={lambda x: x}
    )
    error_formatting_middleware = FormattingMiddlewareBuilder.build(
        error_formatters={lambda x: x}
    )

    # adding different middleware should not cause an error
    w3.middleware_onion.add(request_formatting_middleware)
    w3.middleware_onion.add(request_formatting_middleware2)
    w3.middleware_onion.add(result_formatting_middleware)
    w3.middleware_onion.add(error_formatting_middleware)
    assert isinstance(w3.eth.block_number, int)

    with pytest.raises(Web3ValueError):
        # adding the same middleware again should cause an error
        w3.middleware_onion.add(request_formatting_middleware)


def test_unnamed_class_middleware_are_given_unique_keys(w3):
    w3.middleware_onion.add(TestMiddleware)
    w3.middleware_onion.add(TestMiddleware2)
    assert isinstance(w3.eth.block_number, int)

    with pytest.raises(Web3ValueError):
        # adding the same middleware again should cause an error
        w3.middleware_onion.add(TestMiddleware)
