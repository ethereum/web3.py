import pytest

from ens.utils import (
    init_web3,
    is_valid_domain,
)


def test_init_adds_middlewares():
    w3 = init_web3()
    middlewares = map(str, w3.manager.middleware_onion)
    assert 'stalecheck_middleware' in next(middlewares)


@pytest.mark.parametrize('domain,expected', [
    ('thedao.eth', True),
    ('thedao', False),
    ('blog.ethereum.org', True)
])
def test_is_valid_domain(domain, expected):
    actual = is_valid_domain(domain)
    assert actual == expected
