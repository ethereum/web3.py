from ens import ENS
from web3.middleware import (
    pythonic_middleware,
)


def test_fromWeb3_inherits_web3_middlewares(web3):
    test_middleware = pythonic_middleware
    web3.middleware_onion.add(test_middleware, 'test_middleware')

    ns = ENS.fromWeb3(web3)
    assert ns.web3.middleware_onion.get('test_middleware') == test_middleware
