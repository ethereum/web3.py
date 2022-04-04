import pytest

from eth_tester.exceptions import (
    TransactionFailed,
)

from ens.exceptions import (
    UnownedName,
)
from web3 import Web3


@pytest.mark.parametrize('key,expected', (
    ('avatar', 'tester.jpeg'),
    ('email', 'user@example.com'),
    ('url', 'http://example.com'),
    ('description', 'a test'),
    ('notice', 'this contract is a test contract'),
),)
def test_set_text_unowned_name(ens, key, expected):
    with pytest.raises(UnownedName):
        ens.set_text('tester.eth', key, expected)


@pytest.mark.parametrize('key,expected', (
    ('avatar', 'tester.jpeg'),
    ('email', 'user@example.com'),
    ('url', 'http://example.com'),
    ('description', 'a test'),
    ('notice', 'this contract is a test contract'),
),)
def test_get_text(ens, key, expected):
    address = ens.w3.eth.accounts[2]
    ens.setup_address('tester.eth', address)
    owner = ens.owner('tester.eth')
    assert address == owner
    ens.set_text('tester.eth', key, expected)
    assert ens.get_text('tester.eth', key) == expected

    # teardown
    ens.setup_address('tester.eth', None)


def test_set_text_fails_with_bad_address(ens):
    address = ens.w3.eth.accounts[2]
    ens.setup_address('tester.eth', address)
    zero_address = '0x' + '00' * 20
    with pytest.raises(TransactionFailed):
        ens.set_text('tester.eth', 'url', 'http://example.com', transact={'from': zero_address})


def test_set_text_pass_in_transaction_dict(ens):
    address = ens.w3.eth.accounts[2]
    ens.setup_address('tester.eth', address)
    ens.set_text('tester.eth', 'url', 'http://example.com', transact={'from': address})
    ens.set_text(
        'tester.eth',
        'avatar',
        'example.jpeg',
        transact={'gasPrice': Web3.toWei(100, 'gwei')}
    )
    assert ens.get_text('tester.eth', 'url') == 'http://example.com'
    assert ens.get_text('tester.eth', 'avatar') == 'example.jpeg'

    # teardown
    ens.setup_address('tester.eth', None)
