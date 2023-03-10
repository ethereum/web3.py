import pytest
from unittest.mock import (
    patch,
)

from ens import ENS
from web3.middleware import (
    pythonic_middleware,
)


def test_from_web3_inherits_web3_middlewares(web3):
    test_middleware = pythonic_middleware
    web3.middleware_onion.add(test_middleware, 'test_middleware')

    ns = ENS.from_web3(web3)
    assert ns.web3.middleware_onion.get('test_middleware') == test_middleware


@patch('ens.ENS.from_web3', lambda *args, **kwargs: (args, kwargs))
def test_fromWeb3_delegates_to_from_web3_and_issues_deprecation_warning(web3):
    with pytest.warns(
        DeprecationWarning,
        match="ENS.fromWeb3 is deprecated in favor of ENS.from_web3",
    ):
        passed_on_args, _ = ENS.fromWeb3(web3)
        assert passed_on_args == (web3,)
