
from ens.utils import (
    init_web3,
)


def test_init_adds_middlewares():
    w3 = init_web3()
    middlewares = map(str, w3.manager.middleware_onion)
    assert 'stalecheck_middleware' in next(middlewares)
