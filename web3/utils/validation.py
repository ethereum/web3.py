from functools import reduce
import sys

from eth_utils import (
    is_0x_prefixed,
    is_address,
    is_boolean,
    is_bytes,
    is_checksum_address,
    is_checksum_formatted_address,
    is_dict,
    is_integer,
    is_list_like,
    is_string,
)

from web3.utils.abi import (
    is_address_type,
    is_array_type,
    is_bool_type,
    is_bytes_type,
    is_int_type,
    is_uint_type,
    is_recognized_type,
    is_string_type,
    sub_type_of_array_type,
)


def validate_abi(abi):
    """
    Helper function for validating an ABI
    """
    if not is_list_like(abi):
        raise ValueError("'abi' is not a list")
    for e in abi:
        if not is_dict(e):
            raise ValueError("The elements of 'abi' are not all dictionaries")


def validate_abi_type(abi_type):
    """
    Helper function for validating an abi_type
    """
    if not is_recognized_type(abi_type):
        raise ValueError("Unrecognized abi_type: {abi_type}".format(abi_type=abi_type))


def validate_abi_value(abi_type, value):
    """
    Helper function for validating a value against the expected abi_type
    Note: abi_type 'bytes' must either be python3 'bytes' object or '0x'
    prefixed string
    """
    correct = True
    if is_array_type(abi_type):
        correct = is_list_like(value)
        sub_type = sub_type_of_array_type(abi_type)
        sub_validations = [validate_abi_value(sub_type, v) for v in value]
        correct = correct and reduce((lambda x, y: x and y), sub_validations)
    elif is_bool_type(abi_type):
        correct = is_boolean(value)
    elif is_uint_type(abi_type):
        correct = is_integer(value) and value >= 0
    elif is_int_type(abi_type):
        correct = is_integer(value)
    elif is_address_type(abi_type):
        correct = is_address(value)
    elif is_bytes_type(abi_type):
        if sys.version_info[0] >= 3 and is_bytes(value):
            correct = True
        elif is_string(value):
            if is_0x_prefixed(value):
                correct = True
            else:
                raise TypeError(
                    "ABI values of abi-type 'bytes' must be either"
                    "a python3 'bytes' object or an '0x' prefixed string."
                )
        else:
            correct = False
    elif is_string_type(abi_type):
        correct = is_string(value)

    if correct:
        return True
    else:
        raise TypeError(
            "The following abi value is not a '{abi_type}'': {value}"
            .format(abi_type=abi_type, value=value)
        )


def validate_address(value):
    """
    Helper function for validating an address
    """
    if not is_address(value):
        raise ValueError("'{0}' is not an address".format(value))
    validate_address_checksum(value)


def validate_address_checksum(value):
    """
    Helper function for validating an address EIP55 checksum
    """
    if is_checksum_formatted_address(value):
        if not is_checksum_address(value):
            raise ValueError("'{0}' has an invalid EIP55 checksum".format(value))
