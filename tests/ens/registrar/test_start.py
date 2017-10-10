
import pytest


def test_start_skips_empty(registrar, mocker):
    mocker.patch.object(registrar.core, 'startAuctions', side_effect=Exception('started with []'))
    registrar.start([])


def test_start_converts_names_to_labels(registrar, mocker):
    mocker.patch.object(registrar.core, 'startAuctions')
    mocker.patch.object(registrar, '_estimate_start_gas', return_value=0)
    mocker.patch.object(registrar.ens, 'labelhash', side_effect=lambda x: x)
    registrar.start(['anarcho.eth', 'syndicalist.eth', 'commune.eth'])
    registrar.core.startAuctions.assert_called_once_with(
        ['anarcho', 'syndicalist', 'commune'],
        transact={'gas': 0}
    )


def test_start_calculates_gas_needed(registrar, mocker, label1, label2):
    mocker.patch.object(registrar.core, 'startAuctions')
    mocker.patch.object(registrar.ens, 'labelhash', side_effect=lambda x: x)
    registrar.start([label1, label2])
    registrar.core.startAuctions.assert_called_once_with(
        [label1, label2],
        transact={'gas': 103000}
    )


def test_start_hashes_labels(registrar, mocker, fake_hash_utf8):
    mocker.patch.object(registrar.core, 'startAuctions')
    mocker.patch.object(registrar, '_estimate_start_gas', return_value=0)
    mocker.patch.object(registrar.ens, 'labelhash', side_effect=fake_hash_utf8)
    registrar.start(['racketing', 'roadsides'])
    registrar.core.startAuctions.assert_called_once_with(
        [b'HASH(bracketing)', b'HASH(broadsides)'],
        transact={'gas': 0}
    )


def test_start_accepts_one_label(registrar, mocker, label1):
    mocker.patch.object(registrar.core, 'startAuctions')
    mocker.patch.object(registrar, '_estimate_start_gas', return_value=0)
    mocker.patch.object(registrar.ens, 'labelhash', side_effect=lambda x: x)
    registrar.start(label1)
    registrar.core.startAuctions.assert_called_once_with(
        [label1],
        transact={'gas': 0}
    )


def test_start_accepts_one_label_as_bytes(registrar, mocker, label1):
    mocker.patch.object(registrar.core, 'startAuctions')
    mocker.patch.object(registrar, '_estimate_start_gas', return_value=0)
    mocker.patch.object(registrar.ens, 'labelhash', side_effect=lambda x: x)
    registrar.start(bytes(label1, encoding='utf-8'))
    registrar.core.startAuctions.assert_called_once_with(
        [label1],
        transact={'gas': 0}
    )


def test_start_maximum_gas(registrar, mocker, label1):
    mocker.patch.object(registrar.core, 'startAuctions')
    mocker.patch.object(registrar, '_estimate_start_gas', return_value=4)
    mocker.patch.object(registrar, '_last_gaslimit', return_value=3)
    with pytest.raises(ValueError):
        registrar.start([label1])
