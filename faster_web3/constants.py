from typing import Final
from eth_typing import (
    ChecksumAddress,
    HexAddress,
    HexStr,
)

# Constants as Strings
ADDRESS_ZERO: Final = HexAddress(HexStr("0x0000000000000000000000000000000000000000"))
CHECKSUM_ADDRESSS_ZERO: Final = ChecksumAddress(ADDRESS_ZERO)
MAX_INT: Final = HexStr("0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff")
HASH_ZERO: Final = HexStr("0x0000000000000000000000000000000000000000000000000000000000000000")

# Constants as Int
WEI_PER_ETHER: Final = 1000000000000000000

# Grouped constants as Tuples
DYNAMIC_FEE_TXN_PARAMS: Final = ("maxFeePerGas", "maxPriorityFeePerGas")
