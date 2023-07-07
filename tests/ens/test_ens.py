import pytest

from ens import (
    ENS,
    AsyncENS,
)
from web3 import (
    AsyncWeb3,
)
from web3.middleware import (
    async_validation_middleware,
    gas_price_strategy_middleware,
)
from web3.providers.eth_tester import (
    AsyncEthereumTesterProvider,
)


def test_from_web3_inherits_web3_middlewares(w3):
    test_middleware = gas_price_strategy_middleware
    w3.middleware_onion.add(test_middleware, "test_middleware")

    ns = ENS.from_web3(w3)
    assert ns.w3.middleware_onion.get("test_middleware") == test_middleware


def test_from_web3_does_not_set_w3_object_reference(w3):
    assert w3.strict_bytes_type_checking

    ns = ENS.from_web3(w3)
    assert ns.w3.strict_bytes_type_checking

    assert w3 != ns.w3  # assert not the same object

    w3.strict_bytes_type_checking = False
    assert not w3.strict_bytes_type_checking

    assert ns.w3.strict_bytes_type_checking  # assert unchanged instance property


def test_w3_ens_for_empty_ens_sets_w3_object_reference(w3):
    assert w3.strict_bytes_type_checking
    assert w3.ens.w3.strict_bytes_type_checking

    assert w3 == w3.ens.w3  # assert same object

    w3.strict_bytes_type_checking = False
    assert not w3.strict_bytes_type_checking
    assert not w3.ens.w3.strict_bytes_type_checking


def test_w3_ens_setter_sets_w3_object_reference_on_ens(w3):
    ns = ENS.from_web3(w3)
    w3.ens = ns
    assert ns == w3.ens
    assert w3 == w3.ens.w3

    assert w3.strict_bytes_type_checking
    assert w3.ens.strict_bytes_type_checking
    assert w3.ens.w3.strict_bytes_type_checking

    w3.strict_bytes_type_checking = False
    assert not w3.strict_bytes_type_checking
    assert not w3.ens.strict_bytes_type_checking
    assert not w3.ens.w3.strict_bytes_type_checking


def test_ens_strict_bytes_type_checking_is_distinct_from_w3_instance(w3):
    ns = ENS.from_web3(w3)
    assert ns.w3 != w3  # assert unique instance for ns
    assert ns.w3 == ns._resolver_contract.w3  # assert same instance used under the hood

    assert w3.strict_bytes_type_checking
    assert ns.strict_bytes_type_checking

    w3.strict_bytes_type_checking = False
    assert not w3.strict_bytes_type_checking
    assert ns.strict_bytes_type_checking
    assert ns.w3.strict_bytes_type_checking
    assert ns._resolver_contract.w3.strict_bytes_type_checking

    w3.strict_bytes_type_checking = True
    assert w3.strict_bytes_type_checking

    ns.strict_bytes_type_checking = False
    assert not ns.strict_bytes_type_checking
    assert not ns.w3.strict_bytes_type_checking
    assert not ns._resolver_contract.w3.strict_bytes_type_checking


# -- async -- #


@pytest.fixture
def local_async_w3():
    return AsyncWeb3(AsyncEthereumTesterProvider())


def test_async_from_web3_inherits_web3_middlewares(local_async_w3):
    test_middleware = async_validation_middleware
    local_async_w3.middleware_onion.add(test_middleware, "test_middleware")

    ns = AsyncENS.from_web3(local_async_w3)
    assert ns.w3.middleware_onion.get("test_middleware") == test_middleware


def test_async_from_web3_does_not_set_w3_object_reference(local_async_w3):
    assert local_async_w3.strict_bytes_type_checking

    ns = AsyncENS.from_web3(local_async_w3)
    assert ns.w3.strict_bytes_type_checking

    assert local_async_w3 != ns.w3  # assert not the same object

    local_async_w3.strict_bytes_type_checking = False
    assert not local_async_w3.strict_bytes_type_checking

    assert ns.w3.strict_bytes_type_checking  # assert unchanged instance property


def test_async_w3_ens_for_empty_ens_sets_w3_object_reference(local_async_w3):
    assert local_async_w3.strict_bytes_type_checking
    assert local_async_w3.ens.w3.strict_bytes_type_checking

    assert local_async_w3 == local_async_w3.ens.w3  # assert same object

    local_async_w3.strict_bytes_type_checking = False
    assert not local_async_w3.strict_bytes_type_checking
    assert not local_async_w3.ens.w3.strict_bytes_type_checking


def test_async_w3_ens_setter_sets_w3_object_reference_on_ens(local_async_w3):
    ns = AsyncENS.from_web3(local_async_w3)
    local_async_w3.ens = ns
    assert ns == local_async_w3.ens
    assert local_async_w3 == local_async_w3.ens.w3

    assert local_async_w3.strict_bytes_type_checking
    assert local_async_w3.ens.w3.strict_bytes_type_checking

    local_async_w3.strict_bytes_type_checking = False
    assert not local_async_w3.strict_bytes_type_checking
    assert not local_async_w3.ens.w3.strict_bytes_type_checking


def test_async_ens_strict_bytes_type_checking_is_distinct_from_w3_instance(
    local_async_w3,
):
    ns = AsyncENS.from_web3(local_async_w3)
    assert ns.w3 != local_async_w3  # assert unique instance for ns
    assert ns.w3 == ns._resolver_contract.w3  # assert same instance used under the hood

    assert local_async_w3.strict_bytes_type_checking
    assert ns.strict_bytes_type_checking

    local_async_w3.strict_bytes_type_checking = False
    assert not local_async_w3.strict_bytes_type_checking
    assert ns.strict_bytes_type_checking
    assert ns.w3.strict_bytes_type_checking
    assert ns._resolver_contract.w3.strict_bytes_type_checking

    local_async_w3.strict_bytes_type_checking = True
    assert local_async_w3.strict_bytes_type_checking

    ns.strict_bytes_type_checking = False
    assert not ns.strict_bytes_type_checking
    assert not ns.w3.strict_bytes_type_checking
    assert not ns._resolver_contract.w3.strict_bytes_type_checking
