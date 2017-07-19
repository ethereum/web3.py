import pytest

from web3.utils.validation import (
    validate_abi,
    validate_address,
    validate_address_checksum,
)
ABI = [
    {
        "constant": False,
        "inputs": [],
        "name": "func_1",
        "outputs": [],
        "type": "function",
    },
]

MALFORMED_ABI_1 = "NON-LIST ABI"
MALFORMED_ABI_2 = [5, {"test": "value"}, True]

ADDRESS = '0xd3cda913deb6f67967b99d67acdfa1712c293601'
PADDED_ADDRESS = '0x000000000000000000000000d3cda913deb6f67967b99d67acdfa1712c293601'
INVALID_CHECKSUM_ADDRESS = '0xd3CDA913deB6f67967B99D67aCDFa1712C293601'


@pytest.mark.parametrize(
    'param,validation,expected',
    (
        (ABI, validate_abi, None),
        (MALFORMED_ABI_1, validate_abi, TypeError),
        (MALFORMED_ABI_2, validate_abi, TypeError),
        (ADDRESS, validate_address, None),
        (PADDED_ADDRESS, validate_address, None),
        (INVALID_CHECKSUM_ADDRESS, validate_address, ValueError),
        ("NotAddress", validate_address, TypeError),
        (ADDRESS, validate_address_checksum, None),
        (PADDED_ADDRESS, validate_address_checksum, None),
        (INVALID_CHECKSUM_ADDRESS, validate_address_checksum, ValueError),
    )
)
def test_validation(param, validation, expected):

    if isinstance(expected, type) and issubclass(expected, Exception):
        with pytest.raises(expected):
            validation(param)
        return

    validation(param)
