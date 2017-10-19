
import pytest
from unittest.mock import Mock

from web3 import Web3

from ens.exceptions import OversizeTransaction


def assert_equal_start_auction_hashes(startAuctions, expected_hashes):
    if expected_hashes:
        assert startAuctions.call_count == 1
        start_hashes = startAuctions.call_args_list[0][0][0]
        assert list(map(Web3.toHex, start_hashes)) == expected_hashes
    else:
        # do not waste any gas on a transaction with 0 labels
        assert startAuctions.call_count == 0


@pytest.mark.parametrize(
    'labels, expected_hashes',
    [
        (
            ['anarcho.eth', 'syndicalist.eth', 'commune.eth'],
            [
                '0xd7e41683cbd2d80689afca81da0d105b98242cd5edf8b0b3067c3d50b06cbbd5',
                '0x2908cf6845d47a184831d7b3b68de9ecd230f430fbce21ac8a03e461ee362d6b',
                '0xe181468995e4c2f8ef00f4db5940729b03f41f7604d6f2dadee191cf4e067fc3',
            ],
        ),
        (
            ['anarcho', 'syndicalist', 'commune'],
            [
                '0xd7e41683cbd2d80689afca81da0d105b98242cd5edf8b0b3067c3d50b06cbbd5',
                '0x2908cf6845d47a184831d7b3b68de9ecd230f430fbce21ac8a03e461ee362d6b',
                '0xe181468995e4c2f8ef00f4db5940729b03f41f7604d6f2dadee191cf4e067fc3',
            ],
        ),
        (
            ['ANARCHO', 'SYNDICALIST', 'COMMUNE'],
            [
                '0xd7e41683cbd2d80689afca81da0d105b98242cd5edf8b0b3067c3d50b06cbbd5',
                '0x2908cf6845d47a184831d7b3b68de9ecd230f430fbce21ac8a03e461ee362d6b',
                '0xe181468995e4c2f8ef00f4db5940729b03f41f7604d6f2dadee191cf4e067fc3',
            ],
        ),
        (
            [b'anarcho', b'syndicalist', b'commune'],
            [
                '0xd7e41683cbd2d80689afca81da0d105b98242cd5edf8b0b3067c3d50b06cbbd5',
                '0x2908cf6845d47a184831d7b3b68de9ecd230f430fbce21ac8a03e461ee362d6b',
                '0xe181468995e4c2f8ef00f4db5940729b03f41f7604d6f2dadee191cf4e067fc3',
            ],
        ),
        (
            'anarcho',
            [
                '0xd7e41683cbd2d80689afca81da0d105b98242cd5edf8b0b3067c3d50b06cbbd5',
            ],
        ),
        (
            'ANARCHO',
            [
                '0xd7e41683cbd2d80689afca81da0d105b98242cd5edf8b0b3067c3d50b06cbbd5',
            ],
        ),
        (
            b'ANARCHO',
            [
                '0xd7e41683cbd2d80689afca81da0d105b98242cd5edf8b0b3067c3d50b06cbbd5',
            ],
        ),
        (
            [],
            [],
        ),
    ],
)
def test_start_auctions(registrar, mocker, labels, expected_hashes):
    startAuctions = mocker.patch.object(registrar.core, 'startAuctions')
    registrar.start(labels)
    assert_equal_start_auction_hashes(startAuctions, expected_hashes)


# To leave alpha, investigate why this is failing:
'''
def test_start_auctions_integrated(ens, labels, expected_hashes):
    def assert_label_state(_labels, _expected_hashes, state):
        byte_hashes = [Web3.toBytes(hexstr=hexhash) for hexhash in _expected_hashes]
        for label, expected_hash in zip(_labels, byte_hashes):
            assert ens.registrar.status(label) == state
            assert ens.registrar.entries_by_hash(expected_hash).status == state

    assert_label_state(labels, expected_hashes, Status.Open)
    ens.registrar.start(labels)
    assert_label_state(labels, expected_hashes, Status.Auctioning)
'''


def test_start_calculates_gas_needed(registrar, mocker, label1, label2):
    startAuctions = mocker.patch.object(registrar.core, 'startAuctions')
    registrar.start([label1, label2])
    startAuctions.call_args_list[0][1] == {'transact': {'gas': 103000}}


def test_start_maximum_gas(registrar, mocker, label1):
    tinyblock = Mock(gasLimit=0)
    mocker.patch.object(registrar.web3.eth, 'getBlock', return_value=tinyblock)
    with pytest.raises(OversizeTransaction):
        registrar.start([label1])
