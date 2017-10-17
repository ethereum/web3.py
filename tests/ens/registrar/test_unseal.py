
import pytest

from web3 import Web3

from ens.registrar import InvalidBidHash


@pytest.fixture
def unseal_registrar(registrar, mocker, hashbytes9, addr9):
    mocker.patch.object(registrar.core, 'shaBid', return_value=hashbytes9)
    mocker.patch.object(registrar.core, 'sealedBids', return_value=addr9)
    mocker.patch.object(registrar.core, 'unsealBid')
    return registrar


def test_alias_reveal(unseal_registrar):
    assert unseal_registrar.unseal == unseal_registrar.reveal


def test_reveal_requires_from(unseal_registrar, label1, value1, secret1):
    with pytest.raises(TypeError):
        unseal_registrar.reveal(label1, value1, secret1)


def test_reveal_confirms_sealed_bid(unseal_registrar, mocker, label1, hashbytes9, value1, addr1):
    unseal_registrar.reveal(label1, value1, '', transact={'from': addr1})
    unseal_registrar.core.sealedBids.assert_called_once_with(addr1, hashbytes9)


def test_reveal_fails_on_seal_mismatch(unseal_registrar, mocker, label1, value1, addr1):
    mocker.patch.object(unseal_registrar.core, 'sealedBids', return_value=None)
    with pytest.raises(InvalidBidHash):
        unseal_registrar.reveal(label1, value1, '', transact={'from': addr1})


@pytest.mark.parametrize(
    'label, expected_labelhash',
    [
        (
            'peasant',
            '0xd36dfa290c53bbaeca00bddd830089c4dd18108122b34218c68dfe08c3ad1807',
        ),
        (
            # reveal should switch to label
            'peasant.eth',
            '0xd36dfa290c53bbaeca00bddd830089c4dd18108122b34218c68dfe08c3ad1807',
        ),
        (
            'ööööööö',
            '0x03691b4346cc320858bcc2e5f93a089a2b657e623800507801721a12ffab2e33',
        ),
        (
            # reveal should use nameprep, pushing to lower-case
            'ÖÖÖÖÖÖÖ',
            '0x03691b4346cc320858bcc2e5f93a089a2b657e623800507801721a12ffab2e33',
        ),
    ]
)
def test_reveal_nameprep(unseal_registrar, value1, secret1, addr1, label, expected_labelhash):
    '''
    Must convert unicode letters to lowercase, and convert from full name to label
    '''
    unseal_registrar.reveal(label, value1, secret1, transact={'from': addr1})
    assert unseal_registrar.core.shaBid.call_count == 1
    actual_label_hash, addr, value, secret = unseal_registrar.core.shaBid.call_args_list[0][0]
    assert Web3.toHex(actual_label_hash) == expected_labelhash
    assert addr == addr1
    assert value == value1
    assert secret == '0xb40cb7b9d4e4b922db0c6f19ba9752ce39b87a4471ac97e553071ed4db9f1924'
