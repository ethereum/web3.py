
import pytest
from web3 import Web3

from ens.exceptions import BidTooLow, InvalidLabel, UnderfundedBid


@pytest.fixture
def reg_bid(registrar, mocker):
    mocker.patch.object(registrar.core, 'shaBid')
    mocker.patch.object(registrar.core, 'newBid')
    return registrar


def test_bid_requires_from(reg_bid, label1, secret1):
    with pytest.raises(TypeError):
        reg_bid.bid(label1, 1, secret1)


@pytest.mark.parametrize(
    'label, expected_labelhash',
    [
        (
            'peasant',
            '0xd36dfa290c53bbaeca00bddd830089c4dd18108122b34218c68dfe08c3ad1807',
        ),
        (
            # bid should switch to label
            'peasant.eth',
            '0xd36dfa290c53bbaeca00bddd830089c4dd18108122b34218c68dfe08c3ad1807',
        ),
        (
            'ööööööö',
            '0x03691b4346cc320858bcc2e5f93a089a2b657e623800507801721a12ffab2e33',
        ),
        (
            # bid should use nameprep, pushing to lower-case
            'ÖÖÖÖÖÖÖ',
            '0x03691b4346cc320858bcc2e5f93a089a2b657e623800507801721a12ffab2e33',
        ),
    ]
)
def test_bid_hash(reg_bid, value1, secret1, addr1, label, expected_labelhash):
    reg_bid.bid(label, value1, secret1, transact={'from': addr1})
    assert reg_bid.core.shaBid.call_count == 1
    actual_label_hash, addr, value, secret = reg_bid.core.shaBid.call_args_list[0][0]
    assert Web3.toHex(actual_label_hash) == expected_labelhash
    assert addr == addr1
    assert value == value1
    assert secret == '0xb40cb7b9d4e4b922db0c6f19ba9752ce39b87a4471ac97e553071ed4db9f1924'


def test_new_bid(reg_bid, mocker, hashbytes1, label1, value1, addr1):
    mocker.patch.object(reg_bid.core, 'shaBid', return_value=hashbytes1)
    reg_bid.bid(label1, value1, '', transact={'from': addr1})
    reg_bid.core.newBid.assert_called_once_with(
        hashbytes1,
        transact={'from': addr1, 'value': value1})

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
        transact={'from': addr1, 'value': value1})


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
