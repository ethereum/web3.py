import pytest

from eth_utils import (
    is_dict,
)

from web3.middleware import (
    construct_fixture_middleware,
)


FIXTURES = {
    'eth_protocolVersion': 'test-protocol',
}


def _make_request(method, params):
    return {'result': 'default'}


@pytest.mark.parametrize(
    'method,params,expected',
    (
        ('eth_mining', [], 'default'),
        ('eth_protocolVersion', [], 'test-protocol'),
    )
)
def test_fixture_middleware(method, params, expected):
    middleware = construct_fixture_middleware(FIXTURES)(_make_request, None)

    actual = middleware(method, params)
    assert is_dict(actual)
    assert 'result' in actual
    assert actual['result'] == expected
