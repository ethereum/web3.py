import pytest


ABI = [{}]
ADDRESS = '0xd3cda913deb6f67967b99d67acdfa1712c293601'
INVALID_CHECKSUM_ADDRESS = '0xd3CDA913deB6f67967B99D67aCDFa1712C293601'


@pytest.mark.parametrize(
    'args,kwargs,expected',
    (
        ((ADDRESS,), {}, None),
        ((ADDRESS, ABI), {}, None),
        ((INVALID_CHECKSUM_ADDRESS,), {}, ValueError),
        ((), {'address': INVALID_CHECKSUM_ADDRESS}, ValueError),
        ((ABI), {'address': INVALID_CHECKSUM_ADDRESS}, ValueError),
    )
)
def test_contract_address_validation(web3, args, kwargs, expected):
    if isinstance(expected, type) and issubclass(expected, Exception):
        with pytest.raises(expected):
            web3.eth.contract(*args, **kwargs)
        return

    # run without errors
    web3.eth.contract(*args, **kwargs)
