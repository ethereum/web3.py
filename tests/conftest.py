import pytest

from eth_utils import (
    to_bytes,
)

from web3.utils.toolz import (
    identity,
)


@pytest.fixture(scope="module", params=[lambda x: to_bytes(hexstr=x), identity])
def address_conversion_func(request):
    return request.param
