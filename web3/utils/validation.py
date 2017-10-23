import itertools
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
    length_of_array_type,
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
    Note: abi_type 'bytes' must either be python3 'bytes' object or ''
    """
    if is_array_type(abi_type) and is_list_like(value):
        # validate length
        specified_length = length_of_array_type(abi_type)
        if specified_length is not None:
            if specified_length < 1:
                raise TypeError(
                    "Invalid abi-type: {abi_type}. Length of fixed sized arrays"
                    "must be greater than 0."
                    .format(abi_type=abi_type)
                )
            if specified_length != len(value):
                raise TypeError(
                    "The following array length does not the length specified"
                    "by the abi-type, {abi_type}: {value}"
                    .format(abi_type=abi_type, value=value)
                )

        # validate sub_types
        sub_type = sub_type_of_array_type(abi_type)
        for v in value:
            validate_abi_value(sub_type, v)
        return
    elif is_bool_type(abi_type) and is_boolean(value):
        return
    elif is_uint_type(abi_type) and is_integer(value) and value >= 0:
        return
    elif is_int_type(abi_type) and is_integer(value):
        return
    elif is_address_type(abi_type) and is_address(value):
        return
    elif is_bytes_type(abi_type):
        if sys.version_info.major >= 3 and is_bytes(value):
            return
        elif is_string(value):
            if is_0x_prefixed(value):
                return
            else:
                raise TypeError(
                    "ABI values of abi-type 'bytes' must be either"
                    "a python3 'bytes' object or an '0x' prefixed string."
                )
    elif is_string_type(abi_type) and is_string(value):
        return

    raise TypeError(
        "The following abi value is not a '{abi_type}'': {value}"
        .format(abi_type=abi_type, value=value)
    )


def validate_address(value):
    """
    Helper function for validating an address
    """
    validate_address_checksum(value)
    if not is_address(value):
        raise ValueError("'{0}' is not an address".format(value))


def validate_address_checksum(value):
    """
    Helper function for validating an address EIP55 checksum
    """
    if is_checksum_formatted_address(value):
        if not is_checksum_address(value):
            raise ValueError("'{0}' has an invalid EIP55 checksum".format(value))


def has_one_val(*args, **kwargs):
    vals = itertools.chain(args, kwargs.values())
    not_nones = list(filter(lambda val: val is not None, vals))
    return len(not_nones) == 1


def assert_one_val(*args, **kwargs):
    if not has_one_val(*args, **kwargs):
        raise TypeError(
            "Exactly one of the passed values can be specified. "
            "Instead, values were: %r, %r" % (args, kwargs)
        )
