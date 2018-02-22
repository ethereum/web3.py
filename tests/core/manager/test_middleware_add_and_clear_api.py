import pytest

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

    manager = RequestManager(None, provider, middlewares=[])

    assert tuple(manager.middleware_stack) == tuple()

    manager.middleware_stack.add(middleware_a)
    manager.middleware_stack.add(middleware_b)

    manager.middleware_stack.clear()

    assert tuple(manager.middleware_stack) == tuple()

    manager.middleware_stack.add(middleware_c)
    manager.middleware_stack.add(middleware_b)
    manager.middleware_stack.add(middleware_a)

    with pytest.raises(ValueError):
        manager.middleware_stack.add(middleware_b)

    assert tuple(manager.middleware_stack) == (
        middleware_a,
        middleware_b,
        middleware_c,
    )


def test_add_named_middleware(middleware_factory):
    mw = middleware_factory()
    manager = RequestManager(None, BaseProvider(), middlewares=[(mw, 'the-name')])
    assert len(manager.middleware_stack) == 1

    assert tuple(manager.middleware_stack) == (mw, )


def test_add_named_duplicate_middleware(middleware_factory):
    mw = middleware_factory()
    manager = RequestManager(None, BaseProvider(), middlewares=[(mw, 'the-name'), (mw, 'name2')])
    assert tuple(manager.middleware_stack) == (mw, mw)

    manager.middleware_stack.clear()
    assert len(manager.middleware_stack) == 0

    manager.middleware_stack.add(mw, 'name1')
    manager.middleware_stack.add(mw, 'name2')
    assert tuple(manager.middleware_stack) == (mw, mw)


def test_add_duplicate_middleware(middleware_factory):
    mw = middleware_factory()
    with pytest.raises(ValueError):
        manager = RequestManager(None, BaseProvider(), middlewares=[mw, mw])

    manager = RequestManager(None, BaseProvider(), middlewares=[])
    manager.middleware_stack.add(mw)

    with pytest.raises(ValueError):
        manager.middleware_stack.add(mw)
    assert tuple(manager.middleware_stack) == (mw, )


def test_replace_middleware(middleware_factory):
    mw1 = middleware_factory()
    mw2 = middleware_factory()
    mw3 = middleware_factory()

    manager = RequestManager(None, BaseProvider(), middlewares=[mw1, (mw2, '2nd'), mw3])

    assert tuple(manager.middleware_stack) == (mw1, mw2, mw3)

    mw_replacement = middleware_factory()
    manager.middleware_stack.replace('2nd', mw_replacement)

    assert tuple(manager.middleware_stack) == (mw1, mw_replacement, mw3)

    manager.middleware_stack.remove('2nd')

    assert tuple(manager.middleware_stack) == (mw1, mw3)


def test_replace_middleware_without_name(middleware_factory):
    mw1 = middleware_factory()
    mw2 = middleware_factory()
    mw3 = middleware_factory()

    manager = RequestManager(None, BaseProvider(), middlewares=[mw1, mw2, mw3])

    assert tuple(manager.middleware_stack) == (mw1, mw2, mw3)

    mw_replacement = middleware_factory()
    manager.middleware_stack.replace(mw2, mw_replacement)

    assert tuple(manager.middleware_stack) == (mw1, mw_replacement, mw3)

    manager.middleware_stack.remove(mw_replacement)

    assert tuple(manager.middleware_stack) == (mw1, mw3)


def test_add_middleware(middleware_factory):
    mw1 = middleware_factory()
    mw2 = middleware_factory()
    mw3 = middleware_factory()

    manager = RequestManager(None, BaseProvider(), middlewares=[mw1, mw2])

    manager.middleware_stack.add(mw3)

    assert tuple(manager.middleware_stack) == (mw3, mw1, mw2)


def test_bury_middleware(middleware_factory):
    mw1 = middleware_factory()
    mw2 = middleware_factory()
    mw3 = middleware_factory()

    manager = RequestManager(None, BaseProvider(), middlewares=[mw1, mw2])

    manager.middleware_stack.inject(mw3, layer=0)

    assert tuple(manager.middleware_stack) == (mw1, mw2, mw3)


def test_bury_named_middleware(middleware_factory):
    mw1 = middleware_factory()
    mw2 = middleware_factory()
    mw3 = middleware_factory()

    manager = RequestManager(None, BaseProvider(), middlewares=[mw1, mw2])

    manager.middleware_stack.inject(mw3, name='middleware3', layer=0)

    assert tuple(manager.middleware_stack) == (mw1, mw2, mw3)

    # make sure middleware was injected with correct name, by trying to remove
    # it by name.
    manager.middleware_stack.remove('middleware3')

    assert tuple(manager.middleware_stack) == (mw1, mw2)


def test_remove_middleware(middleware_factory):
    mw1 = middleware_factory()
    mw2 = middleware_factory()
    mw3 = middleware_factory()

    manager = RequestManager(None, BaseProvider(), middlewares=[mw1, mw2, mw3])

    assert tuple(manager.middleware_stack) == (mw1, mw2, mw3)

    manager.middleware_stack.remove(mw2)

    assert tuple(manager.middleware_stack) == (mw1, mw3)
