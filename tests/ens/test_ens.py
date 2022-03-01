from ens import ENS
from web3.middleware import (
    pythonic_middleware,
)


def test_fromWeb3_inherits_web3_middlewares(w3):
    test_middleware = pythonic_middleware
    w3.middleware_onion.add(test_middleware, 'test_middleware')

    ns = ENS.fromWeb3(w3)
    assert ns.w3.middleware_onion.get('test_middleware') == test_middleware
