import pytest

from web3.exceptions import (
    Web3ValueError,
)
from web3.manager import (
    RequestManager,
)
from web3.providers import (
    BaseProvider,
)


def test_provider_property_setter_and_getter(middleware_factory):
    provider = BaseProvider()

    middleware_a = middleware_factory()
    middleware_b = middleware_factory()
    middleware_c = middleware_factory()
    assert middleware_a is not middleware_b
    assert middleware_a is not middleware_c

    manager = RequestManager(None, provider, middleware=[])

    assert tuple(manager.middleware_onion) == tuple()

    manager.middleware_onion.add(middleware_a)
    manager.middleware_onion.add(middleware_b)

    manager.middleware_onion.clear()

    assert tuple(manager.middleware_onion) == tuple()

    manager.middleware_onion.add(middleware_c)
    manager.middleware_onion.add(middleware_b)
    manager.middleware_onion.add(middleware_a)

    with pytest.raises(Web3ValueError):
        manager.middleware_onion.add(middleware_b)

    assert tuple(manager.middleware_onion) == (
        middleware_a,
        middleware_b,
        middleware_c,
    )


def test_add_named_middleware(middleware_factory):
    mw = middleware_factory()
    manager = RequestManager(None, BaseProvider(), middleware=[(mw, "the-name")])
    assert len(manager.middleware_onion) == 1

    assert tuple(manager.middleware_onion) == (mw,)


def test_add_named_duplicate_middleware(middleware_factory):
    mw = middleware_factory()
    manager = RequestManager(
        None, BaseProvider(), middleware=[(mw, "the-name"), (mw, "name2")]
    )
    assert tuple(manager.middleware_onion) == (mw, mw)

    manager.middleware_onion.clear()
    assert len(manager.middleware_onion) == 0

    manager.middleware_onion.add(mw, "name1")
    manager.middleware_onion.add(mw, "name2")
    assert tuple(manager.middleware_onion) == (mw, mw)


def test_add_duplicate_middleware(middleware_factory):
    mw = middleware_factory()
    with pytest.raises(Web3ValueError):
        RequestManager(None, BaseProvider(), middleware=[mw, mw])

    manager = RequestManager(None, BaseProvider(), middleware=[])
    manager.middleware_onion.add(mw)

    with pytest.raises(Web3ValueError):
        manager.middleware_onion.add(mw)
    assert tuple(manager.middleware_onion) == (mw,)


def test_replace_middleware(middleware_factory):
    mw1 = middleware_factory()
    mw2 = middleware_factory()
    mw3 = middleware_factory()

    manager = RequestManager(None, BaseProvider(), middleware=[mw1, (mw2, "2nd"), mw3])

    assert tuple(manager.middleware_onion) == (mw1, mw2, mw3)

    mw_replacement = middleware_factory()
    manager.middleware_onion.replace("2nd", mw_replacement)

    assert tuple(manager.middleware_onion) == (mw1, mw_replacement, mw3)

    manager.middleware_onion.remove("2nd")

    assert tuple(manager.middleware_onion) == (mw1, mw3)


def test_replace_middleware_without_name(middleware_factory):
    mw1 = middleware_factory()
    mw2 = middleware_factory()
    mw3 = middleware_factory()

    manager = RequestManager(None, BaseProvider(), middleware=[mw1, mw2, mw3])

    assert tuple(manager.middleware_onion) == (mw1, mw2, mw3)

    mw_replacement = middleware_factory()
    manager.middleware_onion.replace(mw2, mw_replacement)

    assert tuple(manager.middleware_onion) == (mw1, mw_replacement, mw3)

    manager.middleware_onion.remove(mw_replacement)

    assert tuple(manager.middleware_onion) == (mw1, mw3)


def test_add_middleware(middleware_factory):
    mw1 = middleware_factory()
    mw2 = middleware_factory()
    mw3 = middleware_factory()

    manager = RequestManager(None, BaseProvider(), middleware=[mw1, mw2])

    manager.middleware_onion.add(mw3)

    assert tuple(manager.middleware_onion) == (mw3, mw1, mw2)


def test_bury_middleware(middleware_factory):
    mw1 = middleware_factory()
    mw2 = middleware_factory()
    mw3 = middleware_factory()

    manager = RequestManager(None, BaseProvider(), middleware=[mw1, mw2])

    manager.middleware_onion.inject(mw3, layer=0)

    assert tuple(manager.middleware_onion) == (mw1, mw2, mw3)


def test_bury_named_middleware(middleware_factory):
    mw1 = middleware_factory()
    mw2 = middleware_factory()
    mw3 = middleware_factory()

    manager = RequestManager(None, BaseProvider(), middleware=[mw1, mw2])

    manager.middleware_onion.inject(mw3, name="middleware3", layer=0)

    assert tuple(manager.middleware_onion) == (mw1, mw2, mw3)

    # make sure middleware was injected with correct name, by trying to remove
    # it by name.
    manager.middleware_onion.remove("middleware3")

    assert tuple(manager.middleware_onion) == (mw1, mw2)


def test_remove_middleware(middleware_factory):
    mw1 = middleware_factory()
    mw2 = middleware_factory()
    mw3 = middleware_factory()

    manager = RequestManager(None, BaseProvider(), middleware=[mw1, mw2, mw3])

    assert tuple(manager.middleware_onion) == (mw1, mw2, mw3)

    manager.middleware_onion.remove(mw2)

    assert tuple(manager.middleware_onion) == (mw1, mw3)


def test_export_middleware(middleware_factory):
    mw1 = middleware_factory()
    mw2 = middleware_factory()
    manager = RequestManager(
        None, BaseProvider(), middleware=[(mw1, "name1"), (mw2, "name2")]
    )
    assert tuple(manager.middleware_onion) == (mw1, mw2)

    middleware = manager.middleware_onion.middleware
    assert middleware == [(mw1, "name1"), (mw2, "name2")]
