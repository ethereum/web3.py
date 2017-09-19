import sys

import pytest

if sys.version_info >= (3, 3):
    from unittest.mock import Mock


ABI = [{}]
ADDRESS = '0xd3cda913deb6f67967b99d67acdfa1712c293601'
INVALID_CHECKSUM_ADDRESS = '0xd3CDA913deB6f67967B99D67aCDFa1712C293601'


@pytest.mark.parametrize(
    'args,kwargs,expected',
    (
        ((ADDRESS,), {}, None),
        ((INVALID_CHECKSUM_ADDRESS,), {}, ValueError),
        ((), {'address': INVALID_CHECKSUM_ADDRESS}, ValueError),
        ((), {'address': INVALID_CHECKSUM_ADDRESS}, ValueError),
    )
)
def test_contract_address_validation(web3, args, kwargs, expected):
    if isinstance(expected, type) and issubclass(expected, Exception):
        with pytest.raises(expected):
            web3.eth.contract(*args, **kwargs)
        return

    # run without errors
    web3.eth.contract(*args, **kwargs)


@pytest.mark.skipif(sys.version_info < (3, 3), reason="needs Mock library from 3.3")
def test_set_contract_factory(web3):
    factoryClass = Mock()
    web3.eth.setContractFactory(factoryClass)
    web3.eth.contract(contract_name='myname')
    factoryClass.factory.assert_called_once_with(web3, contract_name='myname')
