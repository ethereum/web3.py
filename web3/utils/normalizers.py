
from eth_utils import (
    to_checksum_address,
)


def addresses_checksummed(abi_type, data):
    if abi_type == 'address':
        return (abi_type, to_checksum_address(data))
    else:
        return (abi_type, data)
