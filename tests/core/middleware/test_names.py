
import pytest
from unittest.mock import Mock, patch

from web3.middleware import name_to_address_middleware


def fake_addr(val):
    letter = str(val)
    assert len(letter) == 1
    return '0x' + letter * 40


@pytest.fixture
def request_middleware():
    make_request, web3 = Mock(), Mock()
    with patch('web3.middleware.names.ENS') as MockENS:
        initialized = name_to_address_middleware(make_request, web3)
        initialized.ens = MockENS.return_value
    # for easier mocking, later:
    initialized.web3 = web3
    initialized.make_request = make_request
    return initialized


@pytest.fixture
def classic_transaction():
    return {
        "from": "13978aee95f38490e9769c39b2773ed763d9cd5f",
        "nonce": 0,
        "gasprice": 1000000000000,
        "startgas": 10000,
        "to": "0x5FfC014343cd971B7eb70732021E26C35B744cc4",
        "value": 10000000000000000,
        "data": "6025515b525b600a37f260003556601b596020356000355760015b525b54602052f260255860005b525b54602052f2",  # noqa: 501
    }


@pytest.fixture
def named_transaction(classic_transaction):
    return dict(classic_transaction, **{'from': 'from.eth', 'to': 'to.eth'})


def test_no_change_to_addresses(request_middleware, classic_transaction):
    method = 'eth_sendTransaction'
    request_middleware(method, [classic_transaction])
    request_middleware.make_request.assert_called_once_with(method, [classic_transaction])


def test_resolve_names_in_send_transaction(
        request_middleware,
        classic_transaction,
        named_transaction):
    def fake_resolver(name):
        if name == 'from.eth':
            return classic_transaction['from']
        elif name == 'to.eth':
            return classic_transaction['to']
    request_middleware.ens.address.side_effect = fake_resolver
    method = 'eth_sendTransaction'
    request_middleware(method, [named_transaction])
    request_middleware.make_request.assert_called_once_with(method, [classic_transaction])


def test_resolve_names_error_on_bad_name(
        request_middleware,
        named_transaction):
    request_middleware.ens.address.return_value = None
    with pytest.raises(ValueError):
        request_middleware('eth_estimateGas', [named_transaction])
