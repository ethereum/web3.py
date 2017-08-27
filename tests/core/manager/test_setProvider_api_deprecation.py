import pytest

from web3.providers import (
    BaseProvider,
)
from web3.manager import (
    RequestManager,
)


def test_setProvider_api_deprecation():
    manager = RequestManager(None, BaseProvider())

    with pytest.warns(DeprecationWarning):
        manager.setProvider(BaseProvider())
