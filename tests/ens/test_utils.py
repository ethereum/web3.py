
from ens.utils import (
    init_w3,
)


def test_init_adds_middlewares():
    w3 = init_w3()
    middlewares = map(str, w3.manager.middleware_onion)
    assert 'stalecheck_middleware' in next(middlewares)
