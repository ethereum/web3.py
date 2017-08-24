from web3.manager import (
    RequestManager,
)
from web3.providers import (
    BaseProvider,
)


def stateful_middleware(make_request, web3):
    state = []

    def middleware(method, params):
        state.append((method, params))
        return {'result': state}

    middleware.state = state
    return middleware


def test_middleware_holds_state_across_requests():
    provider = BaseProvider()

    manager = RequestManager(None, provider, middlewares=[stateful_middleware])
    state_a = manager.request_blocking('test_statefulness', [])
    assert len(state_a) == 1

    state_b = manager.request_blocking('test_statefulness', [])

    assert id(state_a) == id(state_b)
    assert len(state_b) == 2
