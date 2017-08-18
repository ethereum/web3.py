import pytest

from web3.utils.validation import (
    validate_abi,
    validate_abi_type,
    validate_abi_value,
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
        (MALFORMED_ABI_1, validate_abi, ValueError),
        (MALFORMED_ABI_2, validate_abi, ValueError),
        (ADDRESS, validate_address, None),
        (PADDED_ADDRESS, validate_address, None),
        (INVALID_CHECKSUM_ADDRESS, validate_address, ValueError),
        ("NotAddress", validate_address, ValueError),
        (ADDRESS, validate_address_checksum, None),
        (PADDED_ADDRESS, validate_address_checksum, None),
        (INVALID_CHECKSUM_ADDRESS, validate_address_checksum, ValueError),
        ('bool', validate_abi_type, None),
        ('bool[', validate_abi_type, ValueError),
        ('sbool', validate_abi_type, ValueError),
        ('stringx', validate_abi_type, ValueError),
        ('address', validate_abi_type, None),
    )
)
def test_validation(param, validation, expected):

    if isinstance(expected, type) and issubclass(expected, Exception):
        with pytest.raises(expected):
            validation(param)
        return

    validation(param)


@pytest.mark.parametrize(
    'abi_type,value,expected',
    (
        ('string', True, TypeError),
        ('bool[]', [1, 3], TypeError),
        ('bool[]', [True, False], None),
        ('uint8', -5, TypeError),
        ('int8', -5, None),
        ('address', "just a string", TypeError),
        ('address[][]', [[4, 5], [True]], TypeError),
        ('address[][]', [[ADDRESS]], None),
        ('bytes', True, TypeError),

    )
)
def test_validate_abi_value(abi_type, value, expected):

    if isinstance(expected, type) and issubclass(expected, Exception):
        with pytest.raises(expected):
            validate_abi_value(abi_type, value)
        return

    validate_abi_value(abi_type, value)
