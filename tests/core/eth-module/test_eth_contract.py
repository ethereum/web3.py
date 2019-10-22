import pytest
from unittest.mock import (
    Mock,
)

from eth_utils import (
    to_bytes,
)

from web3.exceptions import (
    InvalidAddress,
)

ABI = [{}]
ADDRESS = "0xd3CdA913deB6f67967B99D67aCDFa1712C293601"
BYTES_ADDRESS = to_bytes(hexstr=ADDRESS)
NON_CHECKSUM_ADDRESS = "0xd3cda913deb6f67967b99d67acdfa1712c293601"
INVALID_CHECKSUM_ADDRESS = "0xd3CDA913deB6f67967B99D67aCDFa1712C293601"


@pytest.mark.parametrize(
    "args,kwargs,expected",
    (
        ((ADDRESS,), {}, None),
        ((BYTES_ADDRESS,), {}, None),
        ((INVALID_CHECKSUM_ADDRESS,), {}, InvalidAddress),
        ((NON_CHECKSUM_ADDRESS,), {}, InvalidAddress),
        ((), {"address": ADDRESS}, None),
        ((), {"address": INVALID_CHECKSUM_ADDRESS}, InvalidAddress),
        ((), {"address": NON_CHECKSUM_ADDRESS}, InvalidAddress),
    ),
)
def test_contract_address_validation(w3, args, kwargs, expected):
    if isinstance(expected, type) and issubclass(expected, Exception):
        with pytest.raises(expected):
            w3.eth.contract(*args, **kwargs)
        return

    # run without errors
    w3.eth.contract(*args, **kwargs)


def test_set_contract_factory(w3):
    factoryClass = Mock()
    w3.eth.set_contract_factory(factoryClass)
    w3.eth.contract(contract_name="myname")
    factoryClass.factory.assert_called_once_with(w3, contract_name="myname")
