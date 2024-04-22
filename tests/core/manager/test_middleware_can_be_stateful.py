from web3.manager import (
    RequestManager,
)
from web3.middleware.base import (
    Web3Middleware,
)
from web3.providers import (
    BaseProvider,
)


class StatefulMiddleware(Web3Middleware):
    state = []

    def wrap_make_request(self, make_request):
        def middleware(method, params):
            self.state.append((method, params))
            return {"jsonrpc": "2.0", "id": 1, "result": self.state}

        return middleware


stateful_middleware = StatefulMiddleware


def test_middleware_holds_state_across_requests():
    provider = BaseProvider()

    manager = RequestManager(None, provider, middleware=[stateful_middleware])
    state_a = manager.request_blocking("test_statefulness", [])
    assert len(state_a) == 1

    state_b = manager.request_blocking("test_statefulness", [])

    assert id(state_a) == id(state_b)
    assert len(state_b) == 2
