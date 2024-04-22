from web3.manager import (
    RequestManager,
)
from web3.providers import (
    BaseProvider,
)


class DummyProvider(BaseProvider):
    def make_request(self, method, params):
        return {
            "jsonrpc": "2.0",
            "id": 1,
            "result": {
                "method": method,
                "params": params,
                "middleware": [],
            },
        }


def test_provider_property_setter_and_getter(middleware_factory):
    middleware_a = middleware_factory("middleware-A")
    middleware_b = middleware_factory("middleware-B")

    provider = DummyProvider()

    manager = RequestManager(None, provider, middleware=[middleware_a, middleware_b])
    response = manager.request_blocking("init", ["init"])

    assert response["method"] == "init|middleware-A|middleware-B"
    assert response["params"] == ["init", "middleware-A", "middleware-B"]
    assert response["middleware"] == ["middleware-B", "middleware-A"]
