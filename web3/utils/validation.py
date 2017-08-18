from eth_utils import (
    is_address,
    is_checksum_address,
    is_checksum_formatted_address,
    is_dict,
    is_list_like,
)


def validate_abi(abi):
    """
    Helper function for validating an ABI
    """
    if not is_list_like(abi):
        raise TypeError("'abi' is not a list")
    for e in abi:
        if not is_dict(e):
            raise TypeError("The elements of 'abi' are not all dictionaries")


def validate_address(value):
    """
    Helper function for validating an address
    """
    if not is_address(value):
        raise TypeError("'{0}' is not an address".format(value))
    validate_address_checksum(value)


def validate_address_checksum(value):
    """
    Helper function for validating an address EIP55 checksum
    """
    if is_checksum_formatted_address(value):
        if not is_checksum_address(value):
            raise ValueError("'{0}' has an invalid EIP55 checksum".format(value))
