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


def validate_address(address):
    """
    Helper function for validating an address
    """
    if not is_address(address):
        raise TypeError("'address' is not an address")
    validate_address_checksum(address)


def validate_address_checksum(address):
    """
    Helper function for validating an address EIP55 checksum
    """
    if is_checksum_formatted_address(address):
        if not is_checksum_address(address):
            raise ValueError("'address' has an invalid EIP55 checksum")
