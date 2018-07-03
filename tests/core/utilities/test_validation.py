import pytest

from eth_utils import (
    to_bytes,
)

from web3.exceptions import (
    InvalidAddress,
)
from web3.utils.validation import (
    validate_abi,
    validate_abi_type,
    validate_abi_value,
    validate_address,
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
MALFORMED_SELECTOR_COLLISION_ABI = [
    {
        'constant': False,
        'inputs': [{'name': 'input', 'type': 'uint256'}],
        'name': 'blockHashAmphithyronVersify',
        'outputs': [{'name': '', 'type': 'uint256'}],
        'payable': False,
        'stateMutability': 'nonpayable',
        'type': 'function'
    },
    {
        'constant': False,
        'inputs': [{'name': 'input', 'type': 'uint256'}],
        'name': 'blockHashAskewLimitary',
        'outputs': [{'name': '', 'type': 'uint256'}],
        'payable': False,
        'stateMutability': 'nonpayable',
        'type': 'function'
    }
]
MALFORMED_SIGNATURE_COLLISION_ABI = [
    {
        'constant': False,
        'inputs': [{'name': 'input', 'type': 'uint256'}],
        'name': 'blockHashAmphithyronVersify',
        'outputs': [{'name': '', 'type': 'uint256'}],
        'payable': False,
        'stateMutability': 'nonpayable',
        'type': 'function'
    },
    {
        'constant': False,
        'inputs': [{'name': 'input', 'type': 'uint256'}],
        'name': 'blockHashAmphithyronVersify',
        'outputs': [{'name': '', 'type': 'uint256'}],
        'payable': False,
        'stateMutability': 'nonpayable',
        'type': 'function'
    }
]

ADDRESS = '0xd3CdA913deB6f67967B99D67aCDFa1712C293601'
BYTES_ADDRESS = to_bytes(hexstr=ADDRESS)
PADDED_ADDRESS = '0x000000000000000000000000d3cda913deb6f67967b99d67acdfa1712c293601'
INVALID_CHECKSUM_ADDRESS = '0xd3CDA913deB6f67967B99D67aCDFa1712C293601'
NON_CHECKSUM_ADDRESS = '0xd3cda913deb6f67967b99d67acdfa1712c293601'
BYTES_ADDRESS_LEN_LT_20 = bytes(1) * 19
BYTES_ADDRESS_LEN_GT_20 = bytes(1) * 21


@pytest.mark.parametrize(
    'param,validation,expected',
    (
        (ABI, validate_abi, None),
        (MALFORMED_ABI_1, validate_abi, ValueError),
        (MALFORMED_ABI_2, validate_abi, ValueError),
        (MALFORMED_SELECTOR_COLLISION_ABI, validate_abi, ValueError),
        (MALFORMED_SIGNATURE_COLLISION_ABI, validate_abi, ValueError),
        (ADDRESS, validate_address, None),
        (BYTES_ADDRESS, validate_address, None),
        (PADDED_ADDRESS, validate_address, InvalidAddress),
        (INVALID_CHECKSUM_ADDRESS, validate_address, InvalidAddress),
        (NON_CHECKSUM_ADDRESS, validate_address, InvalidAddress),
        (BYTES_ADDRESS_LEN_LT_20, validate_address, InvalidAddress),
        (BYTES_ADDRESS_LEN_GT_20, validate_address, InvalidAddress),
        ("NotAddress", validate_address, InvalidAddress),
        (b'not string', validate_address, InvalidAddress),
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
        ('bool[][2]', [[True, False], [True, False, True]], None),
        ('bool[][2]', [[True, False], [True], [False]], TypeError),
        ('bool[3][]', [[True, False, False]], None),
        ('bool[3][]', [[True, False]], TypeError),
        ('bool[0]', [], TypeError),
        ('bool[0][1]', [[]], TypeError),
        ('uint8', -5, TypeError),
        ('int8', -5, None),
        ('address', "just a string", InvalidAddress),
        ('address', b'not even a string', InvalidAddress),
        ('address[][]', [[4, 5], [True]], TypeError),
        ('address[][]', [[ADDRESS]], None),
        ('address[2][]', [[ADDRESS], [ADDRESS, ADDRESS]], TypeError),
        ('address[2][1]', [[ADDRESS, ADDRESS]], None),
        ('address[2][1]', [[ADDRESS], [ADDRESS, ADDRESS]], TypeError),
        ('bytes', True, TypeError),
        ('bytes', "0x5402", None),
        ('bytes', "5402", TypeError),
        ('bytes', b'T\x02', None),
    )
)
def test_validate_abi_value(abi_type, value, expected):

    if isinstance(expected, type) and issubclass(expected, Exception):
        with pytest.raises(expected):
            validate_abi_value(abi_type, value)
        return

    validate_abi_value(abi_type, value)
