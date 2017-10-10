
import pytest

from web3.exceptions import StaleBlockchain

from ens.registrar import Status


def test_entries_passthrough(registrar, mocker, hash1, label1):
    result = object()
    mocker.patch.object(registrar, 'entries_by_hash', return_value=result)
    mocker.patch.object(registrar.ens, 'labelhash', return_value=hash1)
    assert registrar.entries(label1) is result
    registrar.ens.labelhash.assert_called_once_with(label1)
    registrar.entries_by_hash.assert_called_once_with(hash1)


@pytest.mark.parametrize("dot", ['.', '．', '。', '｡'])
def test_entries_use_label_with_dots(registrar, mocker, addr1, hash1, dot):
    mocker.patch.object(registrar.ens, 'labelhash')
    mocker.patch.object(registrar, 'entries_by_hash')
    registrar.entries('holygrail%seth' % dot)
    registrar.ens.labelhash.assert_called_once_with('holygrail')


def test_entries_subdomain_meaningless(registrar, mocker, addr1, hash1):
    mocker.patch.object(registrar.web3, 'sha3')
    mocker.patch.object(registrar, 'entries_by_hash')
    with pytest.raises(ValueError):
        registrar.entries('montypythonandthe.holygrail.eth')


def test_entries_status(registrar, mocker):
    NUM_ENTRIES_STATUSES = 6
    core_results = [[idx, None, 0, 0, 0] for idx in range(NUM_ENTRIES_STATUSES)]
    mocker.patch.object(registrar.core, 'entries', side_effect=core_results)
    for idx in range(NUM_ENTRIES_STATUSES):
        entries = registrar.entries_by_hash(b'')
        assert entries[0] == Status(idx)
        assert entries[0] == idx


def test_entries_deed_contract(registrar, mocker, addr1):
    mocker.patch.object(registrar.core, 'entries', return_value=[0, addr1, 2, 3, 4])
    entries = registrar.entries_by_hash(b'')
    assert entries[1]._classic_contract.address == addr1


def test_entries_empty_deed(registrar, mocker):
    mocker.patch.object(registrar.core, 'entries', return_value=[0, None, 0, 0, 0])
    entries = registrar.entries_by_hash(b'')
    assert entries[1] is None


def test_entries_registration_time(registrar, mocker):
    mocker.patch.object(registrar.core, 'entries', return_value=[0, None, 2 * 3600, 0, 0])
    entries = registrar.entries_by_hash(b'')
    assert str(entries[2]) == '1970-01-01 02:00:00+00:00'


def test_entries_registration_empty(registrar, mocker):
    mocker.patch.object(registrar.core, 'entries', return_value=[0, None, 0, 0, 0])
    entries = registrar.entries_by_hash(b'')
    assert entries[2] is None


def test_entries_value_passthrough(registrar, mocker):
    mocker.patch.object(registrar.core, 'entries', return_value=[0, None, 0, 1, 2])
    entries = registrar.entries_by_hash(b'')
    assert entries[-2:] == (1, 2)


def test_entries_named_access(registrar, mocker, addr1):
    mocker.patch.object(registrar.core, 'entries', return_value=[0, addr1, 2, 3, 4])
    entries = registrar.entries_by_hash(b'')
    assert entries[0] is entries.status
    assert entries[1] is entries.deed
    assert entries[2] is entries.close_at
    assert entries[3] is entries.deposit
    assert entries[4] is entries.top_bid


@pytest.mark.parametrize(
    'entry_attr, entry_idx',
    [
        ('status', 0),
        ('close_at', 2),
        ('deposit', 3),
        ('top_bid', 4),
    ]
)
def test_entries_method_access(registrar, mocker, entry_attr, entry_idx, label1):
    mocker.patch.object(registrar.core, 'entries', return_value=[0, None, 2, 3, 4])
    mocker.patch.object(registrar, 'entries_by_hash', wraps=registrar.entries_by_hash)
    entries = registrar.entries_by_hash(b'')
    lookup = getattr(registrar, entry_attr)
    assert lookup(label1) == entries[entry_idx]


def test_entries_method_access_for_deed(registrar, mocker, addr1):
    mocker.patch.object(registrar.core, 'entries', return_value=[0, addr1, 2, 3, 4])
    entries = registrar.entries_by_hash(b'')
    assert entries.deed._classic_contract.address == addr1


def test_entries_stale(registrar, mocker, hash1):
    mocker.patch('web3.middleware.stalecheck._isfresh', return_value=False)
    with pytest.raises(StaleBlockchain):
        registrar.entries(hash1)


def test_status_stale(registrar, mocker, label1):
    mocker.patch('web3.middleware.stalecheck._isfresh', return_value=False)
    with pytest.raises(StaleBlockchain):
        registrar.status(label1)
