import pytest

from eth_utils import (
    is_dict,
)

from web3.middleware import (
    construct_transaction_signing_middleware,
)

test_transaction = {'from': 'acct_local', 'to': 'acct_testrpc'}

FIXTURES = {
    'eth_sendTransaction': 'something',
}


def _make_request(method, params):
    return {'result': 'default'}


@pytest.mark.parametrize(
    'method,params,expected',
    (
        ('eth_mining', [], 'default'),
        ('eth_sendTransaction', [], 'something'),
    )
)
def test_transaction_signing_middleware(method, params, expected):
    middleware = construct_transaction_signing_middleware(FIXTURES)(_make_request, None)

    actual = middleware(method, params)
    assert is_dict(actual)
    assert 'result' in actual
    assert actual['result'] == expected
