from eth_typing import (
    HexAddress,
    HexStr,
)
from hexbytes import (
    HexBytes,
)

ACCEPTABLE_STALE_HOURS = 48

AUCTION_START_GAS_CONSTANT = 25000
AUCTION_START_GAS_MARGINAL = 39000

EMPTY_SHA3_BYTES = HexBytes(b'\0' * 32)
EMPTY_ADDR_HEX = HexAddress(HexStr('0x' + '00' * 20))

REVERSE_REGISTRAR_DOMAIN = 'addr.reverse'
