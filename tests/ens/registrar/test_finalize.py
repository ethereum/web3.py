

def test_finalize_name_to_label(registrar, mocker, fake_hash_hexout):
    mocker.patch('web3.Web3.sha3', side_effect=fake_hash_hexout)
    mocker.patch.object(registrar.core, 'finalizeAuction')
    registrar.finalize('theycallmetim.eth')
    registrar.core.finalizeAuction.assert_called_once_with(b'HASH(btheycallmetim)',
                                                           transact={'gas': 120000})
