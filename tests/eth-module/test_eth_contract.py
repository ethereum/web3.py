import pytest


def test_contract_address_validation(web3):
    with pytest.raises(ValueError):
        web3.eth.contract('0xd3CDA913deB6f67967B99D67aCDFa1712C293601')
