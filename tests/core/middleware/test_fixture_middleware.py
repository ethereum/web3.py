import pytest

from eth_utils import (
    is_dict,
)

from web3.middleware import (
    construct_fixture_middleware,
)


def _fixture_callback(method, params):
    return {'result': bool(params)}


FIXTURES = {
    'eth_protocolVersion': {'result': 'test-protocol'},
    'test_endpoint': _fixture_callback,
}


def _make_request(method, params):
    return {'result': 'default'}


@pytest.mark.parametrize(
    'method,params,expected',
    (
        ('eth_mining', [], 'default'),
        ('eth_protocolVersion', [], 'test-protocol'),
        ('test_endpoint', [], False),
        ('test_endpoint', [1], True),
    )
)
def test_fixture_middleware(method, params, expected):
    middleware = construct_fixture_middleware(FIXTURES)(_make_request, None)

    actual = middleware(method, params)
    assert is_dict(actual)
    assert 'result' in actual
    assert actual['result'] == expected
