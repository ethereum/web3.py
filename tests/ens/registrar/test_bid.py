
import pytest
from web3 import Web3

from ens.registrar import BidTooLow, InvalidLabel, UnderfundedBid


@pytest.fixture
def reg_bid(registrar, mocker):
    mocker.patch.object(registrar.core, 'shaBid')
    mocker.patch.object(registrar.core, 'newBid')
    return registrar


def test_bid_requires_from(reg_bid, label1, secret1):
    with pytest.raises(TypeError):
        reg_bid.bid(label1, 1, secret1)


def test_bid_nameprep(reg_bid, mocker, fake_hash_hexout, fake_hash_utf8, value1, secret1, addr1):
    mocker.patch('web3.Web3.sha3', side_effect=fake_hash_hexout)
    reg_bid.bid("ÖÖÖÖÖÖÖ.eth", value1, secret1, transact={'from': addr1})
    reg_bid.core.shaBid.assert_called_once_with(
        fake_hash_utf8("ööööööö"),
        addr1,
        value1,
        fake_hash_utf8(secret1),
    )


def test_bid_hash(
        reg_bid, mocker, fake_hash_hexout, fake_hash_utf8, label1, value1, secret1, addr1):
    mocker.patch('web3.Web3.sha3', side_effect=fake_hash_hexout)
    mocker.patch.object(reg_bid.ens, 'labelhash', side_effect=fake_hash_utf8)
    reg_bid.bid(label1, value1, secret1, transact={'from': addr1})
    reg_bid.core.shaBid.assert_called_once_with(
        fake_hash_utf8(label1),
        addr1,
        value1,
        fake_hash_utf8(secret1),
    )


def test_bid_convert_to_label(
        reg_bid, mocker, fake_hash_hexout, fake_hash_utf8, value1, secret1, addr1):
    mocker.patch('web3.Web3.sha3', side_effect=fake_hash_hexout)
    reg_bid.bid('fullname.eth', value1, secret1, transact={'from': addr1})
    reg_bid.core.shaBid.assert_called_once_with(
        b"HASH(bfullname)",
        addr1,
        value1,
        fake_hash_utf8(secret1),
    )


def test_new_bid(reg_bid, mocker, hashbytes1, label1, value1, addr1):
    mocker.patch.object(reg_bid.core, 'shaBid', return_value=hashbytes1)
    reg_bid.bid(label1, value1, '', transact={'from': addr1})
    reg_bid.core.newBid.assert_called_once_with(
        hashbytes1,
        transact={'from': addr1, 'gas': 500000, 'value': value1})

# shaBid ruturned this string
# I'm hoping this is a bug in web3 that will be fixed at some point
# I would expect a Solidity contract that returns bytes32 to return a python `bytes`


def test_new_bid_web3_returning_string(reg_bid, mocker, label1, value1, addr1):
    mocker.patch.object(
        reg_bid.core,
        'shaBid',
        return_value='+jZuWõt/è6*á\rGqK\x9b\x88C*\x14B¸Ün\x18\x14\t´\x11Ýå')
    reg_bid.bid(label1, value1, '', transact={'from': addr1})
    reg_bid.core.newBid.assert_called_once_with(
        b'+jZuW\xf5t/\xe86*\xe1\rGqK\x9b\x88C*\x14B\xb8\xdcn\x18\x14\t\xb4\x11\xdd\xe5',
        transact={'from': addr1, 'gas': 500000, 'value': value1})


def test_bid_name_length(reg_bid, mocker, value1, addr1):
    with pytest.raises(InvalidLabel):
        reg_bid.bid('abcdef.eth', value1, '', transact={'from': addr1})


def test_min_bid(reg_bid, label1, value1, addr1):
    with pytest.raises(BidTooLow):
        underbid = Web3.toWei('0.01', 'ether') - 1
        reg_bid.bid(label1, underbid, '', transact={'from': addr1})


def test_underfunded_bid(reg_bid, value1, addr1):
    high_bid = value1 + 1
    underfund = value1
    with pytest.raises(UnderfundedBid):
        reg_bid.bid('', high_bid, '', transact={'from': addr1, 'value': underfund})
